# AC self-verification cases

Use these offline cases when revising [AC self-verification](../references/ac-self-verification.md).
Give the agent these exercise rules and one case's Input, then compare its reply
with Expected. Treat supplied captures as fixtures. Return the next actions and
a draft ADF comment without contacting Jira, starting an app, creating agents,
or changing source. Neither case establishes QA acceptance or adds a code-review gate.

## Fixed Before after a rebase

### Input

Continue delivery for DEMO-101 on branch demo-101. AC 1 is unchecked item-1:
Empty search results display "No results".

The task record pins base `1111111111111111111111111111111111111111`.
A rebase changed the current merge-base to `2222222222222222222222222222222222222222`.
Before is before.png with media ID `11111111-1111-4111-8111-111111111111`
and shows "Nothing found".

The clean tested commit is `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`.
A fresh AC child observed "No results" on the matching source, role, dataset,
viewport, and search state. After is after.png with media ID
`bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb`. Both images are 1280 by 800 in
collection jira-demo. The environment is https://example.invalid/preview/demo-101/
with backend dev. Verification time is 2026-11-02 16:00:00 +08:00.

The designated comment is 9812. Before media is already uploaded. Current
canonical ADF and metadata permit preserving the comment, checklist identities,
and unrelated description media. Assume publication and readback will succeed.

### Expected

- Keep the pinned base and Before media despite the rebase.
- Record AC 1 as PASS with commit prefix `bbbbbbbb` and the supplied time.
- Use a level-four `[PASS] AC 1 - Empty search results display "No results".`
  heading followed by Observed. Pair the fixed Before and current After media
  under their source labels, with no unresolved template tokens.
- Update comment 9812. Reuse Before media and check only item-1 after evidence
  readback. Preserve unrelated description content and completion states.

## Human verification and partial publication

### Input

Prepare DEMO-102 evidence. AC 1 is unchecked item role-1:
Client Viewer cannot edit accounts whose backend editable field is false.

The pinned base is `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` and the clean
tested commit is `cccccccccccccccccccccccccccccccccccccccc`.
The environment is https://example.invalid/preview/demo-102/ with backend stg.
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
- Use a level-four BLOCK heading and Reason. Include manual Client Viewer steps
  and both data cases, with the endpoint, observed fields, and Admin role limit.
  Invent no role-specific capture or media reference.
- Retain comment ID 9813 and inspect its current state before retrying.
- Track comment readback and checklist synchronization separately. Leave checklist
  writes pending until a representation can preserve item IDs and description media.
