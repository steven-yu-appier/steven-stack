### Opening a PR

Invoked at the end of every other playbook.

## Contents

- Delivery scope, worktree, and commits
- Cleanup, test audit, commit, and push
- PR writing and required body sections
- FE AC evidence and freshness
- Preview synchronization, publication, and readback
- Forge, stacks, readiness, and babysitting

For implementation and fix work, follow Staff's **Automatic delivery** scope in [`../SKILL.md`](../SKILL.md#autonomy). Read-only playbooks and explicitly limited requests perform only their authorized actions. The delivery owner runs this playbook after successful final verification without another user prompt.

**Worktree.** Reuse the task's current branch and worktree for delivery, including follow-up fixes to an existing PR. Create any needed isolated worktree during task setup, before implementation; give concurrent writers separate worktrees or disjoint files. Preserve unrelated work and published history. Delivery does not reset the checkout, reconstruct the change from main, or move it onto a fresh branch.

**Commits.** Keep commits small, ordered, and independently landable. Rebase or amend only unpublished task commits; append follow-up commits to a published branch so delivery remains a normal push. Follow the format in [`/playbooks/writing-a-commit.md`](writing-a-commit.md).

**Delivery addon.** Run `ss-simplify-code` over the settled delivery scope before final verification and publication. Reuse the Staff delivery result when the scoped code and constraints are unchanged, rather than dispatching the addon twice. Every code delivery runs the pass regardless of size; non-code scopes report a no-op. Finish `deslop` and `no-comments` cleanup, refresh the addon only for code changed since its pass, then run the caller's applicable final checks on the resulting source. A pending or failed final verification is not a successful delivery. The addon does not replace `interrogate`, and `ss-code-review` remains standalone.

**Test audit.** When preparing or committing implementation changes, or reviewing task tests, invoke `test-audit` in audit mode. Account for every task-added or modified test using its candidate evidence and value/retention bars. Apply its authoring gate to new or rewritten tests. Remove only task-added tests proven to lack distinct coverage; keep unchanged pre-existing tests intact. Use repository verification and review policy in place of external tooling or landing flows. Run focused checks after audit edits and report test dispositions and failed or unavailable verification in the handoff and PR. If the skill is unavailable, mark the audit pending. A task with no added or modified tests reports that disposition without adding tests for the audit.

**Commit and push.** After cleanup, test audit, and applicable final checks pass, inspect `git status --short`, `git diff --cached`, and the task diff. Identify the exact task paths and hunks before staging. When the index contains only task changes, stage those changes, inspect the complete staged diff, and commit under repository conventions. When unrelated staged changes occupy disjoint paths, inspect the full `HEAD`-to-working-tree diff of the task paths and use `git commit --only ... -- <task-paths>`; this commits those paths while retaining unrelated index entries. Add intended new files by explicit path first. If unrelated hunks share a task path and cannot be isolated confidently, leave commit pending rather than including them or clearing the user's index. After commit, inspect the committed diff and remaining staged diff to verify task isolation. Resolve the current branch and its required remote or existing upstream; use `git push -u origin HEAD` only when no repository rule or upstream specifies another destination. Detached HEAD or an ambiguous destination leaves push pending. Use a normal push and verify that the intended commit reached the remote branch. If the push is rejected or its outcome is uncertain, inspect the remote before retrying; forced updates require a separate explicit user instruction. A failed push leaves publication of that change pending.

**Continue to the PR.** After a verified push, find the open PR for the exact repository and head branch through `gh`. For an existing PR, preserve its base and preview URLs, refresh its body from the complete current change and verification evidence, publish it with `gh pr edit --body-file`, and perform the freshness and readback checks below. If the body already describes the current change and evidence, verify it without a redundant edit. If no open PR exists, resolve the base from the user, repository convention, or verified remote default and create a draft; ask only if that choice remains ambiguous. Do not modify a closed or merged PR. Report the delivered commit, remote branch, PR URL, verification results, and any pending actions after completing the authorized delivery steps.

**PRs.** Run `/deslop` over the diff before commit. Run `/no-comments` before review. Write every PR title, PR description, and commit body with `/technical-writing`, then apply `/unslop`. Apply every technical-writing layer except Diátaxis. Use one word for each action, keep articles, and avoid `-ing` when a plain verb works.

**Titles.** Use Conventional Commits in the form `type(scope): subject`. Use `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, or `perf` as the type. Use the changed app scope in the commits as the scope. Omit the scope if none exists in the commits. Keep the subject short and imperative. Name a real symbol when one carries the change. Append exact head branch name. For example, `AI-30704 feat: add persisted codex task recovery foundation`. Do not add a trailing period.

**Description ownership.** This playbook owns the complete PR body. Do not invoke another PR-description skill on its behalf. When the user explicitly names one, use its requested presentation conventions within this playbook's gathering, evidence, freshness, publication, and readback requirements; do not transfer ownership of the body or publication workflow. Read [`../references/pr-change-outline.md`](../references/pr-change-outline.md) for the visual conventions used below.

Explicit user instructions may replace the default body format or request a retained copy. They do not waive reading the complete change, labeling evidence truthfully, checking freshness, or reading the published result back. When the repository supplies a required pull-request template, use it as the outer structure and map the content below into its closest sections. Do not append a second template.

**Voice.** Write as one human talking to another. Avoid jargon and slang. Use simple, coherent, concise language. Use the repository's domain terms and real code symbols when they are the clearest words. Explain an unfamiliar term once. Do not compress the description into fragments that make the reviewer reconstruct the meaning.

**Purpose.** The PR body is a briefing, not the lab notebook. A reviewer and the future reader of the squash commit should learn why the change exists, the shape of the implementation, what deserves scrutiny, and how the author proved that the behavior works. The squash commit body is the PR body. Keep it near 40 lines. Use at most one compact `text` or `diff` block that remains readable as raw Markdown. Do not use Mermaid, HTML, task-artifact blocks, or a standalone link header.

Use this default template:

````markdown
- [ ] QA

## Why

<State the observable before and after in one or two short sentences. Name the approach only when it helps explain the result. Link the ticket or motivating review comment from the relevant sentence.>

## Change outline

<Use one short paragraph or the smallest useful structural view. Show relationships, ownership, order, or data flow. Do not repeat the file diff.>

<State a material out-of-scope boundary when needed.>

## Significant change

| Path | Symbol / component / hook / route | Breaking change and role |
|---|---|---|
| <repository-relative path> | <stable name> | <breaking change and concise role> |

## Tradeoffs and risk

- <Explain a non-obvious decision or rejected alternative.>
- <Name a compatibility, migration, rollout, rollback, or blast-radius concern.>
- <When the base branch is failing, state the continuing cost of leaving it unfixed.>

## Verification

- [x] <State behavior that the author verified on the current source state>. [Evidence](...)
- [ ] Reviewer check: <State a manual action that a reviewer can repeat with normal access.>

<If needed, state a blocked check or coverage limit in prose.>

## FE acceptance criteria

| # | ac | screenshot |
|---|---|---|
| <source AC number> | <FE acceptance criterion> | ![<verified state>](<GitHub attachment URL>) |
````

`Why`, `Change outline` and `Verification` are required in the default template. Omit `Tradeoffs and risk` when it has nothing material to say. Do not write `None.`.

The first non-empty line of every PR body must be exactly `- [ ] QA`, including when using a repository template. Include `## Significant change` with the breaking-change table above; when there are no breaking changes, retain the heading and table headers, omit the example row, and state that there are no breaking changes. Map the remaining content into the repository template without duplicating sections. Include the FE AC table when the task has FE criteria; omit it when none apply. These evidence tables do not count toward the change outline's one-visual limit. Keep the body concise, but retain all required AC rows even when they exceed the approximate line budget.

**FE AC evidence.** List every FE-scope AC in source order with the numbering confirmed during clarification; exclude criteria outside FE scope. Exercise each visual criterion on the actual application and capture enough screenshots to demonstrate its required states. Read [GitHub screenshot attachments](../references/github-attachments.md) and follow its upload, URL capture, and rendered-access verification procedure. Embed the returned image Markdown in the `screenshot` cell. One row may contain multiple images; one image may support multiple criteria only when it demonstrates each. For nonvisual FE behavior, put exactly `不適用` in that cell and report its behavioral verification in Verification. Keep the evidence tied to the tested source state under the freshness rules below. If capture or upload is unavailable, mark the row pending with the reason and report the evidence gap; do not label it verified or nonvisual.

**Gather before writing.** Read the linked ticket or specification, the complete diff, the commit list, changed files, and enough surrounding code to understand ownership and behavior. For an existing PR, also read its current body, the motivating review comment, any accepted comment that changed scope, and any verification-evidence comment. Treat the existing body as context; rebuild its claims from the current full diff. Do not read every comment by default. Capture the current PR or branch head as `draftHead` before drafting.

**Change outline.** Use prose when prose is clearer. Use at most one visual. Split the PR when one bounded view cannot explain its independent changes.

**Verification states.** Checked items report author-run behavioral evidence from the current source state and link the retained evidence when available. Unchecked items begin with `Reviewer check:` and describe actions a reviewer can repeat with normal access, documented tooling, and available builds. Failed, blocked, unexecuted, or incomplete coverage appears in prose with the concrete status and reason. Do not disguise it as a reviewer task. Do not include type-check, lint, git diff, build, compile, or routine test commands. For a performance change, report one primary number with its unit in `before → after` form. Do not claim that old evidence applies to the current head because later changes appear unrelated. State the tested source when the evidence comes from a different source state.

**Freshness gate.** Immediately before creating or updating the PR, read the current head again. If `currentHead != draftHead`, refresh the commits and diff, revise every affected section and set `draftHead = currentHead`. Do not publish until the draft describes the current head.

**Preview and Jira.** Before creating a new PR in `ad-cloud-portal` or `idash-mono`, read [Preview links and Jira sync](../references/jira-preview.md), derive the preview URLs, and include them in the body. After successful creation and PR readback, synchronize those URLs to the Jira Story comment using that reference. Existing-PR maintenance preserves preview URLs and does not trigger Jira synchronization. Report the Story key, preview URLs, comment ID and outcome, or the concrete pending reason.

**Body file.** Use a task-specific temporary file for the forge command. Do not retain one file per PR by default. When the user requests a retained copy, save it separately, keep it synchronized with the reviewed draft after every refresh, and still use a temporary forge input. Remove only the temporary file after publication. For a preview-only request, show the body without creating or updating the PR.

**Publish and read back.** Create or update the PR, then read its body and head from the forge. Confirm that the published body matches the reviewed draft, the selected template's headings appear once and in order, fenced blocks and links survived escaping, and the PR head still equals `draftHead`. If the head changed, refresh and publish again. Remove the temporary file after successful readback.

Attach videos when they prove a claim; screenshots follow the FE AC evidence requirements above. Do not paste full SHAs, swarm or arena lane recitals, lever-correction essays, file-by-file checklists, metric tables, or "CLEAN" verdicts. Put these details in a linked artifact. Do not use `## Summary` or `## Test plan` boilerplate. A commit body does not restate its subject.

**Forge.** Use `gh` for every PR operation, including create, edit, view, watch, and merge. Run every `gh` command outside the sandbox with escalated permissions; credentials are stored in the macOS Keychain. A sandboxed authentication failure is not evidence that the user needs to log in. Rerun outside the sandbox first.

**Size and stacks.** Prefer five narrow PRs to one large PR. A stack is a base-branch chain. The root PR targets trunk. Each child starts from its parent's exact tip and its PR targets the parent branch. Apply the Commits policy above when arranging later changes; published branches retain their history. Create a child with `gh pr create --draft --base <parent-branch>`. Retarget an existing child with `gh pr edit <pr> --base <parent-branch>`. Branch from trunk only for independent work. Rebase unpublished commits on trunk before substantial stack work.

**Readiness.** Open every PR as a draft with `gh pr create --draft`. Run `gh pr view <number>` before you refer to PR status.

**Babysit.** Opening a PR does not start a babysit. Post the URL and keep building. Finish the phase or stack first. Run a separate babysit pass only when the user asks for one after the whole stack exists. A babysit for each new PR stalls the build and spends checks on commits that later waves restart. Push back when feedback drifts from intent.

A subagent that opens a PR follows the delivery-addon and cleanup order above and runs `interrogate` on the resulting code. Any accepted review fixes require refreshed addon coverage for the affected code and final verification before publication. It returns the URL and does not babysit. Return to the parent.
