---
name: pr-author-context-comments
description: Draft and optionally publish author-authored GitHub pull-request comments at exact diff lines to explain non-obvious design decisions, intentional scope boundaries, or rejected alternatives. Use when a PR author wants to reduce reviewer effort with local context. Do not use for review findings, source-code comments, or general PR summaries.
---

# PR author context comments

Attach short-lived review context to the changed line it explains without adding that commentary to the source tree.

## Authorization and modes

- Draft by default. Inspect the PR and return an exact preview without writing to GitHub.
- Publish only when the user explicitly asks to post or publish the comments. A request to draft, suggest, identify, or review comments does not authorize publication.
- Publish comments directly so reviewers can see them. Do not add them to a pending review or submit an existing review.
- Do not edit the PR description, source files, issues, reviews, or existing comments unless the user separately asks.

## Select useful context

Inspect the PR intent, exact diff, relevant callers, tests, repository guidance, and history needed to verify each proposed explanation. A comment qualifies when:

- its current diff line represents the decision being explained;
- a reasonable reviewer could infer a different implementation or ask why adjacent behavior remains unchanged;
- the answer changes how the reviewer should evaluate this PR; and
- evidence supports the chosen behavior and the rejected alternative.

Reject a candidate when it merely restates the diff, praises the implementation, points out an unrelated pre-existing issue, promises an unspecified follow-up, or uses "out of scope" to excuse an incomplete fix. If the investigation reveals a defect, report or fix it through the appropriate workflow instead of presenting it as intentional context.

Use [references/selection-examples.md](references/selection-examples.md) when the distinction between useful context and defensive noise is unclear.

## Keep durable rationale elsewhere

PR context is temporary. If future maintainers need the explanation to change the code safely, use the repository's durable documentation mechanism instead. Keep the PR comment only when its main value is helping reviewers understand this patch at this location.

## Draft and anchor comments

Choose the smallest changed line or range that embodies the decision. Use `RIGHT` for added or current lines and `LEFT` only when the explanation belongs to a deletion. If no current diff line is a truthful anchor, omit the inline comment and suggest PR-level context instead.

Write a compact explanation that names the chosen behavior, the plausible alternative, and the concrete reason for the choice. Start with `Context for reviewers:`. Do not use finding severities, blocking labels, TODO language, or requests for action.

Prepare a manifest with the immutable PR head:

```json
{
  "pr": "150",
  "head_sha": "0123456789abcdef0123456789abcdef01234567",
  "comments": [
    {
      "path": "src/navigation.ts",
      "line": 84,
      "side": "RIGHT",
      "body": "Context for reviewers: this transition stays at the navigation entry point because project setup is not a terminal-session operation. Moving it into the session provider would miss that route and give terminal state ownership of workspace navigation."
    }
  ]
}
```

Before publishing, show the exact body and location for every comment unless the user has already approved that exact manifest.

## Validate and publish

Use the bundled helper from a checkout of the target repository. It resolves the PR from the current branch unless `--pr` is supplied, verifies that the authenticated GitHub user authored the PR, rejects stale heads and invalid diff lines, and detects exact duplicates.

Use [Task files and cleanup](../staff/playbooks/task-artifacts.md) for the runtime scratch path. Keep unpublished manifests until the owning workflow has saved or delivered their content. Preview without writes:

```bash
python3 <skill-dir>/scripts/post_author_context_comments.py \
  --comments "$TASK_SCRATCH/pr-author-context-comments.json"
```

After explicit publication authorization, use the same validated manifest:

```bash
python3 <skill-dir>/scripts/post_author_context_comments.py \
  --comments "$TASK_SCRATCH/pr-author-context-comments.json" \
  --publish
```

The helper posts immediately visible inline comments. It never creates, appends to, or submits a pending review. Report posted, duplicate, failed, and skipped counts with the returned comment URLs.

## Stop conditions

- If the PR head changed, stop and re-evaluate the explanations and anchors against the new diff.
- If a line is absent from the current diff, choose another truthful changed line or omit the comment. Do not attach it to a nearby line for convenience.
- If the authenticated user is not the PR author, stop rather than publishing comments under another reviewer's identity.
- After an ambiguous write failure, rely on the helper's readback. Retry only entries still reported as failed.

## Related workflows

Use review skills to discover defects, not to manufacture author context. Use testing guidance when a comment depends on behavioral claims. Route durable architectural reasoning to the repository's documentation or ADR workflow. Handle later reviewer replies with the review-comment response workflow.
