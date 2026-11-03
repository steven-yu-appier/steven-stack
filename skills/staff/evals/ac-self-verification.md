# AC self-verification cases

Use these offline cases when revising [AC self-verification](../references/ac-self-verification.md).
Give the agent these exercise rules and one case's Input, then compare its reply
with Expected. Treat supplied captures as fixtures. Return the next actions and
a draft ADF comment without contacting Jira, starting an app, creating agents,
or changing source. Neither case establishes QA acceptance or adds a code-review gate.

## Current base and final After after a rebase

### Input

Continue delivery for DEMO-101 on branch demo-101. AC 1 is unchecked item-1:
Empty search results display "No results".

The previous task record used base `1111111111111111111111111111111111111111`
with old-before.png, media ID `11111111-1111-4111-8111-111111111111`.
The PR targets base-demo, which was rebased to
`3333333333333333333333333333333333333333`. The task branch's current merge-base
is `2222222222222222222222222222222222222222`.
Current Before is base-before.png, media ID
`33333333-3333-4333-8333-333333333333`, captured at base-demo's current SHA.
Both old and current Before show "Nothing found".

The clean tested commit is `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`.
A fresh AC child observed "No results" on the matching source, role, dataset,
viewport, and search state. After is after.png with media ID
`bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb`. An intermediate implementation at
`cccccccccccccccccccccccccccccccccccccccc` has intermediate.png with media ID
`cccccccc-cccc-4ccc-8ccc-cccccccccccc`. All images are 1280 by 800 in
collection jira-demo. The environment is https://example.invalid/preview/demo-101/
with backend dev. Verification time is 2026-11-02 16:00:00 +08:00.

The designated comment is 9812 and still contains the old Before and intermediate
After. All supplied media is already uploaded. Current
canonical ADF and metadata permit preserving the comment, checklist identities,
and unrelated description media. Assume publication and readback will succeed.

### Expected

- Use base-demo at `3333333333333333333333333333333333333333` for Before,
  rather than either merge-base or the prior record.
- Record AC 1 as PASS with commit prefix `bbbbbbbb` and the supplied time.
- Use a level-four `[PASS] AC 1 - Empty search results display "No results".`
  heading followed only by the Before/After image table. Use media IDs beginning
  `33333333` and `bbbbbbbb`, with no Observed paragraph or other PASS commentary.
- Update comment 9812 and replace its old comparison. Leave no old Before,
  intermediate image, or stale result in the comment. Check only item-1 after
  evidence readback. Preserve unrelated content, attachments, and completion states.

## Human verification and partial publication

### Input

Prepare DEMO-102 evidence. AC 1 is unchecked item role-1:
Client Viewer cannot edit accounts whose backend editable field is false.

The current base branch is `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` and the clean
tested commit is `cccccccccccccccccccccccccccccccccccccccc`.
The environment is https://example.invalid/preview/demo-102/ with backend stg.
Test account c-7 opens at https://example.invalid/preview/demo-102/#/accounts/c-7.
Verification time is 2026-11-02 16:10:00 +08:00.

A separate AC child inspected `GET /api/accounts?client_id=c-7` as Internal Admin.
The response contained acct-7 with editable=false and acct-8 with editable=true.
The Admin's edit button for acct-7 was disabled and automated tests passed.
Client Viewer requires a human with that role. The child proposes marking PASS.

Comment 9813 was created, but readback timed out. The snapshot contains only
Markdown. Canonical ADF needed to preserve description media and checklist IDs
is unavailable. No Client Viewer capture exists.

### Expected

- Reject the child's PASS proposal and keep role-1 unchecked with status BLOCK.
- Write the BLOCK section in concise Traditional Chinese with one reason,
  the test-account link, and a short table of API-confirmed data. Include
  Client Viewer steps with expected results. Retain the endpoint, both observed
  account values, and the Admin role limit. Invent no capture or media reference.
- Retain comment ID 9813 and inspect its current state before retrying.
- Track comment readback and checklist synchronization separately. Leave checklist
  writes pending until a representation can preserve item IDs and description media.
