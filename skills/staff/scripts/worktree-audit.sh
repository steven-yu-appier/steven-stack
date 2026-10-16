#!/usr/bin/env bash
# Read-only worktree prune audit. Classifies every git worktree by size, merge
# state, local data, and remote/PR state. Session usage remains unknown until
# checked by the caller. Never reads chat contents or deletes user files.
#
# Usage: worktree-audit.sh [--github] [repo-path] (defaults to the current repo)
# --github invokes gh; run the script outside the sandbox with escalated permissions.
# Without it, PR state is unknown. Git refs are local snapshots; no fetch is performed.
set -uo pipefail

for dependency in git du awk sort grep; do
	command -v "$dependency" >/dev/null 2>&1 || { echo "requires $dependency" >&2; exit 1; }
done

github=false
if [ "${1:-}" = --github ]; then github=true; shift; fi
repo="${1:-$(git rev-parse --show-toplevel 2>/dev/null)}"
[ -z "$repo" ] && { echo "not in a git repo; pass a repo path" >&2; exit 1; }
cd "$repo" || exit 1

# Local remote refs drive merge checks; their freshness is reported to the caller.
base=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null)
if [ -n "$base" ] && git rev-parse --verify --quiet "$base^{commit}" >/dev/null; then
	echo "merge checks use local $base; refs were not refreshed" >&2
else
	base=""
	echo "warn: no local remote default ref; merge state is unknown" >&2
fi

# PR state is known only after a successful, parseable GitHub query.
audit_tmp=$(mktemp -d) || exit 1
trap 'rm -rf "$audit_tmp"' EXIT
if ! git worktree list --porcelain -z > "$audit_tmp/worktrees"; then
	echo "cannot enumerate worktrees; audit incomplete" >&2
	exit 1
fi
prs="$audit_tmp/prs.json"
pr_known=false
if [ "$github" = true ]; then
	if command -v gh >/dev/null 2>&1 && command -v jq >/dev/null 2>&1; then
		if gh pr list --author "@me" --state all --limit 1000 \
			--json number,state,headRefName > "$prs" 2> "$audit_tmp/gh-error"; then
			if jq -e 'type == "array"' "$prs" >/dev/null 2> "$audit_tmp/json-error"; then
				pr_known=true
			else
				cat "$audit_tmp/json-error" >&2
				echo "warn: invalid PR response; PR state is unknown" >&2
			fi
		else
			cat "$audit_tmp/gh-error" >&2
			echo "warn: GitHub query failed; PR state is unknown" >&2
		fi
	else
		echo "warn: --github requires gh and jq; PR state is unknown" >&2
	fi
else
	echo "PR state is unknown; rerun with --github outside the sandbox to query GitHub" >&2
fi

now=$(date +%s)

printf "SIZE\tAGE\tMERGED\tDIRTY\tREMOTE\tPR\tUSAGE\tBUCKET\tWORKTREE\n"

main_wt=""
while IFS= read -r -d '' field; do
	case "$field" in 'worktree '*) wt=${field#worktree } ;; *) continue ;; esac
	if [ -z "$main_wt" ]; then main_wt=$wt; continue; fi

	size=$(du -sh "$wt" 2>/dev/null | awk '{print $1}')
	head=$(git -C "$wt" rev-parse HEAD 2>/dev/null)
	head_ts=$(git -C "$wt" log -1 --format='%ct' HEAD 2>/dev/null || echo 0)
	age=$([ "$head_ts" -gt 0 ] 2>/dev/null && echo "$(( (now - head_ts) / 86400 ))d" || echo "?")

	# Squash-merged branches are not ancestors of main, so PR state is the
	# real signal; merge-base only catches fast-forward/rebase merges.
	merged=unknown
	if [ -n "$base" ]; then
		git merge-base --is-ancestor "$head" "$base" 2>/dev/null
		merge_result=$?
		case "$merge_result" in 0) merged=YES ;; 1) merged=no ;; esac
	fi

	if ! porcelain=$(git --no-optional-locks -C "$wt" status --porcelain --untracked-files=all --ignored=matching); then
		dirty=unknown
	elif [ -z "$porcelain" ]; then dirty=clean
	elif printf '%s\n' "$porcelain" | grep -qv -e '^??' -e '^!!'; then
		dirty="wip:$(printf '%s\n' "$porcelain" | grep -cv -e '^??' -e '^!!')"
	elif printf '%s\n' "$porcelain" | grep -q '^??'; then
		dirty="untracked:$(printf '%s\n' "$porcelain" | grep -c '^??')"
	else dirty="ignored:$(printf '%s\n' "$porcelain" | grep -c '^!!')"; fi

	branch=$(git -C "$wt" symbolic-ref --quiet --short HEAD 2>/dev/null || echo "")
	if [ -z "$branch" ]; then remote=detached
	elif git -C "$wt" show-ref --verify --quiet "refs/remotes/origin/$branch"; then
		[ "$(git -C "$wt" rev-parse "origin/$branch" 2>/dev/null)" = "$head" ] \
			&& remote=pushed \
			|| remote="ahead$(git -C "$wt" rev-list --count "origin/$branch..HEAD" 2>/dev/null)"
	else remote=no-remote; fi

	pr=unknown
	if [ "$pr_known" = true ]; then
		pr=$([ -n "$branch" ] && jq -r --arg b "$branch" \
			'.[] | select(.headRefName==$b) | "#\(.number)/\(.state)"' "$prs" 2>/dev/null | head -1)
		[ -z "$pr" ] && pr="-"
	fi

	case "$dirty" in
	unknown) bucket=hold-unknown ;;
	clean)
		if [ "$pr" = unknown ]; then bucket=hold-unknown
		else
		case "$pr" in *OPEN*) bucket=hold-open-pr ;; *)
			if [ "$merged" = YES ] || [[ "$pr" = */MERGED ]]; then bucket=verify-usage
			else bucket=review; fi ;;
		esac
		fi ;;
	*) bucket=hold-local-data ;;
	esac

	printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
		"$size" "$age" "$merged" "$dirty" "$remote" "$pr" unknown "$bucket" "$wt"
done < "$audit_tmp/worktrees" | sort -t$'\t' -k1,1 -rh
