# Selecting author context comments

Use these contrasts when a candidate sits close to the boundary between helpful context and review noise.

## Useful local context

### Ownership boundary

Changed line: a navigation handler dispatches `show-session` directly.

Comment:

> Context for reviewers: this transition stays at the navigation entry point because New Project and Project Setup are workspace-navigation operations. Moving it into `TerminalSessionsProvider` would miss those routes and make terminal state responsible for application navigation.

Why it qualifies: a reviewer could reasonably suggest centralizing the calls, and the comment explains the concrete ownership and coverage cost of that alternative.

### Deliberately narrow compatibility behavior

Changed line: a parser accepts one legacy field while rejecting other old shapes.

Comment:

> Context for reviewers: this branch accepts `projectPath` only because version 2 persisted that field in released builds. The other legacy shapes were never written by a shipped version, so accepting them would hide malformed state rather than preserve compatibility.

Why it qualifies: repository history supports a non-obvious boundary that directly affects review of the changed branch.

## Reject these candidates

### Restating the diff

> Context for reviewers: this condition prevents the panel from opening while Skills is visible.

Reject it because the code already says this and the comment gives no reason for the choice.

### Defending unrelated debt

> Context for reviewers: the disabled menu items were already inaccessible before this PR and will be fixed separately.

Reject it because adjacency and age do not make an unrelated issue part of the current decision. Mention it only if this PR materially depends on that behavior and the explanation helps evaluate the changed line.

### Hiding an incomplete fix

> Context for reviewers: this still loses the query on navigation, but persistence is outside the scope of this PR.

Reject it because the note admits a broken contract. Fix the behavior, narrow the stated PR contract, or report the gap.

### Durable invariant

> Context for reviewers: never reuse session identifiers across accounts because persisted tabs are keyed only by session ID.

Move this rationale to durable documentation or a source-level invariant. Future maintainers need it after the PR closes.
