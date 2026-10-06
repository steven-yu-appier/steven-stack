---
name: post-pending-review-comments
description: Post GitHub PR review findings as pending draft review threads at code locations, including Start Review comments, batched unsubmitted comments, or adding more comments to an existing pending review.
---

# Post Pending Review Comments

Use this workflow when the user wants review findings posted to GitHub PR code locations as draft review comments, without submitting the review.

## Guardrails

- Never submit the review unless the user explicitly asks.
- Do not set a REST review `event`.
- Do not use normal PR issue comments for code-location feedback.
- A user can have only one pending review per PR. If one exists, append threads to it.
- Prefer the bundled helper script over hand-built nested `gh api -f threads[][path]=...` flags.
- Refuse an empty comment list; never create an empty pending review.

## Finding Format

Start every comment with a severity-prefixed title, followed by one blank line
and self-contained actionable feedback:

```md
[P1] Do not classify arbitrary valid skill directories as managed

<review feedback>
```

Use these fixed merge semantics:

- `P0`, `P1`, and `P2` are blocking. Do not add a `Blocking` label.
- `P3` is non-blocking. Format its title as `[P3] Non-blocking: <title>`.

Do not use `Non-blocking` with P0-P2 or omit it from P3. Normalize input bodies
to this format before invoking the helper; the helper rejects mismatches.

## Inputs

Each review comment needs:

```json
{
  "path": "src/App.tsx",
  "line": 103,
  "body": "[P2] Preserve the existing empty-state contract\n\nReview comment body",
  "side": "RIGHT"
}
```

Use `side: "RIGHT"` for added/current lines unless the user is commenting on removed code.

Infer the PR from the current branch with `gh pr view --json number,url,headRefOid`. If the user gives a PR number or URL, pass it to `gh pr view`.

## Workflow

1. Resolve the repository, PR number, current head SHA, and PR node id.
2. Find the current user's existing pending review, if any.
3. If no pending review exists, create one with REST:
   - `POST /repos/{owner}/{repo}/pulls/{number}/reviews`
   - omit `event`
   - include `commit_id`
   - use `threads` entries with `path`, `line`, `side`, `body`
4. If a pending review exists, append each comment with GraphQL `addPullRequestReviewThread`.
5. Verify with:
   - `GET /repos/{owner}/{repo}/pulls/{number}/reviews/{review_id}/comments`
6. Report the PR, pending review id, added locations, and that the review remains unsubmitted.

## Helper Script

Use `scripts/post_pending_review_threads.py` when possible:

```bash
python3 $HOME/.agents/skills/post-pending-review-comments/scripts/post_pending_review_threads.py \
  --comments /tmp/review-comments.json
```

Optional flags:

- `--pr <number-or-url>`: target a specific PR instead of the current branch.
- `--repo OWNER/REPO`: target a specific repository.
- `--dry-run`: resolve context and print what would be posted.

The script accepts either a JSON array of comments or an object with a `comments` array.

For a handoff from another validated review workflow, pass its internal manifest directly. It may additionally contain `pr` and `head_sha`; use `--pr` or the manifest PR and require `head_sha` to match the current PR head before posting. Do not reconstruct comments from a human-readable review brief.

## API Notes

REST pending review creation:

```json
{
  "commit_id": "<head sha>",
  "threads": [
    {
      "path": "src/App.tsx",
      "line": 103,
      "side": "RIGHT",
      "body": "[P1] Preserve the authorization boundary\n\nComment text"
    }
  ]
}
```

GraphQL append mutation:

```graphql
mutation($reviewId: ID!, $path: String!, $line: Int!, $side: DiffSide!, $body: String!) {
  addPullRequestReviewThread(input: {
    pullRequestReviewId: $reviewId,
    path: $path,
    line: $line,
    side: $side,
    body: $body
  }) {
    thread { id path line }
  }
}
```

## Failure Handling

- If REST creation fails with `User can only have one pending review per pull request`, query pending reviews and append with GraphQL.
- If GitHub rejects a `line`, fetch PR file patches and verify the line is in the diff.
- If the PR head moved, use the current `headRefOid` for new pending-review creation. Existing pending reviews can still receive appended threads by review id.
- If the supplied manifest includes `head_sha`, stop instead of posting when the current head differs. The review findings were validated against the recorded revision.
