# AC self-verification cases

Use these offline cases when revising [AC self-verification](../references/ac-self-verification.md).
Give the agent these exercise rules and one case's Input, then compare its reply
with Expected. Treat supplied captures as offline evidence stubs, not as an
indication that the app used a fixture backend. Each case states its backend mode.
Return the next actions and a draft ADF comment without contacting Jira, starting an app, creating agents,
or changing source. No case establishes QA acceptance or adds a code-review gate.

## Current base and final After after a rebase

### Input

Continue delivery for DEMO-101 on branch demo-101. AC 1 is the first numbered description item:
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
ADF and metadata from acli or REST API permit preserving the comment and its
unrelated media. Assume publication and readback will succeed.

### Expected

- Use base-demo at `3333333333333333333333333333333333333333` for Before,
  rather than either merge-base or the prior record.
- Record AC 1 as PASS with commit prefix `bbbbbbbb` and the supplied time.
- Use a level-four `[PASS] AC 1 - Empty search results display "No results".`
  heading followed only by the Before/After image table. Use media IDs beginning
  `33333333` and `bbbbbbbb`, with no Observed paragraph or other PASS commentary.
- Update comment 9812 and replace its old comparison. Leave no old Before,
  intermediate image, or stale result in the comment. Preserve unrelated content
  and attachments. After evidence readback, record the verified result without
  changing the numbered description.

## Human verification and partial publication

### Input

Prepare DEMO-102 evidence. AC 1 is the first numbered description item:
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

Comment 9813 was created, but readback timed out. Only Markdown from an earlier
planning snapshot is available. Current comment ADF has not yet been fetched
through acli or REST API. No Client Viewer capture exists.

### Expected

- Reject the child's PASS proposal and record AC 1 as BLOCK.
- Write the BLOCK section in concise Traditional Chinese with one reason,
  the test-account link, and a short table of API-confirmed data. Include
  Client Viewer steps with expected results. Retain the endpoint, both observed
  account values, and the Admin role limit. Invent no capture or media reference.
- Retain comment ID 9813 and inspect its current state before retrying.
- Fetch the current comment ADF through acli or REST API before reconciling any
  update. A lossy planning snapshot does not block that read or require jarkdown.
- Track upload and comment readback separately. Keep the numbered task description
  unchanged; verification publishes no checklist or description update.

## Unreachable backend with complete fixture evidence

### Input

Prepare DEMO-103 evidence. AC 1 says: Empty search results display "No results".
The current base is base-demo at `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`.
The clean tested commit is `dddddddddddddddddddddddddddddddddddddddd`.
The preview at https://example.invalid/preview/demo-103/ cannot connect to dev.
`GET /api/search?q=missing` returns a connection error.
Verification time is 2026-11-16 16:00:00 +08:00.

A fresh AC child intercepted that endpoint using the contract-compatible fixture
`fixtures/search-empty.json`, which returns an empty results array. It exercised
the search UI on both recorded sources with the same fixture, role, viewport,
and search state. Before shows "Nothing found" and After shows "No results".
Both screenshots are 1280 by 800 in collection jira-demo. Before media ID is
`aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa`; After media ID is
`dddddddd-dddd-4ddd-8ddd-dddddddddddd`. All media is already uploaded.
No live-backend result exists. No designated comment exists. Draft only.

### Expected

- Record AC 1 as PASS(FIXTURE), with commit prefix `dddddddd` and the supplied time.
- Use a level-four `[PASS(FIXTURE)] AC 1` heading and matching Before/After image
  table with fixture labels and the supplied media identities.
- Include one short Traditional Chinese line naming the connection error,
  `fixtures/search-empty.json`, and the unverified real-backend integration.
- Retain the endpoint, inputs, interception method, and matching capture
  conditions in the local report. Neither classify the connection failure alone
  as BLOCK nor claim a live-backend PASS.
- Keep the task description unchanged and respect the draft-only restriction.

## Fixture mismatch or missing screenshots

### Input

Use DEMO-103's sources and connection failure. Assess these independent variants:

1. The fresh child exercised the fixture-backed search flow, but After still
   shows "Nothing found" instead of "No results".
2. The fixture-backed flow shows "No results", but no After screenshot exists.
3. Both screenshots exist, but AC 1 instead requires saved searches to persist
   in the real backend after reopening. Fixtures return a canned saved search;
   no backend save or reopen was observed.

### Expected

- Variant 1 is FAIL. Return the mismatch for a fix and capture new After evidence.
- Variant 2 is BLOCK until the required matching capture exists.
- Variant 3 is BLOCK for backend persistence. Fixture screenshots do not establish
  actual backend execution or persistence.
- None earns PASS(FIXTURE) merely because fixtures or passing tests exist.
