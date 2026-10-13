# Preview links and Jira sync

Use this reference only when creating a new PR in `ad-cloud-portal` or `idash-mono`. Existing-PR maintenance does not trigger Jira synchronization.

## Derive preview URLs before creation

For `ad-cloud-portal`, use `https://adcloud-stg.appier.info/preview/<branch-name>#`, substituting the exact PR head branch name and retaining the trailing `#`.

For `idash-mono`, run the repository's existing helper from its root:

```sh
node .agents/skills/create-draft-pr/pr-facts.cjs --base <target-base>
```

Use the returned `previewLinks` verbatim. The URL shape is `https://idash-staging.appier.org/pr/<branch>/<folder>/#/`, always on staging regardless of the selected environment. `configs/appNameToFolderName.js` owns app-to-folder mapping; the helper owns changed-app detection. Do not duplicate either lookup here or derive the URLs by hand. Include one link per changed app. If `noApps` is true, omit preview links and report that no changed app produced a preview; skip Jira preview synchronization. A missing helper, nonzero exit, or missing app mapping leaves preview generation pending; report the error and resolve it before creating the PR.

Include the derived URLs in the PR body before creation. Synchronization starts only after a new PR was successfully created in this execution and its remote body was verified.

## Synchronize the Story comment

All Jira CLI operations, including comment metadata queries, creation, and updates, use `/opt/homebrew/bin/acli` outside the sandbox with escalated permissions. Before reading ticket, Story, or comment content, read [Jira content through jarkdown](jira-read-policy.md) and follow its cache, lock, download, promotion, and rollback procedure. If the policy cannot be read, leave synchronization pending rather than inventing a download procedure.

1. Read the preview URLs from the current remote PR body and use them exactly. For multiple iDash apps, preserve all app labels and URLs. Missing or ambiguous links block only synchronization; ask for the unresolved choice.
2. Resolve the Jira Story from the conversation, branch, task documents, or PR. Validate keys against `^[A-Z][A-Z0-9]+-[0-9]+$` before use. Resolve a subtask's parent through the Jira read policy. Ask only when the Story is unresolved or ambiguous.
3. Read Story/comment content through jarkdown. Obtain comment IDs and freshness metadata with `acli jira workitem comment list --key <STORY_KEY> --paginate --json`. Refresh the canonical snapshot when the required comment content or current revision is absent.
4. Match a preview comment associated with this PR URL; otherwise use a single preview comment with no PR association. Leave other PRs' comments untouched. Ask which comment to use if multiple candidates remain.
5. Update only the preview entries, preserving other content. If already current, make no write. If no comment exists, create one containing `Preview: <preview-url>` and `PR: <pr-url>` on separate lines; for multiple apps, put one labeled preview entry per app before the PR line.

Write the comment body to a temporary file. Use `/opt/homebrew/bin/acli jira workitem comment update --key <STORY_KEY> --id <COMMENT_ID> --body-file <FILE>` for a match, or `create --key <STORY_KEY> --body-file <FILE>` otherwise. Remove the temporary body file after use.

Refresh the canonical jarkdown snapshot after writing and verify the Story, comment ID, PR association, and every preview URL. If a write fails or its outcome is uncertain, inspect current state before retrying to avoid duplicates. Report the verified outcome or pending inputs and failures without claiming synchronization succeeded.
