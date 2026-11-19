# AC self-verification cases

Use these offline cases when revising [AC self-verification](../references/ac-self-verification.md).
Give the agent the case Input and the workflow, without Expected. Return next
actions and draft report/comment content. Do not contact Jira or GCS, start apps,
create agents or modify source. Supplied observations are evidence stubs, not
proof of a real run. Grade behavior and evidence claims, not exact prose.

## Current base and final After after a rebase

### Input

Continue delivery for DEMO-101, branch demo-101. AC 1 is:
Empty search results display "No results".
The previous task record used base `1111111111111111111111111111111111111111`.
The current PR base-demo is `3333333333333333333333333333333333333333` and the
merge-base is `2222222222222222222222222222222222222222`.
Before at the current base shows "Nothing found". Final clean tested commit
`bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb` shows "No results". A separate verifier
returned VERIFIED with matching role/data/viewport and fresh Before/After images.
An intermediate commit `cccccccccccccccccccccccccccccccccccccccc` also has images.
Environment is https://example.invalid/preview/demo-101/, backend dev.
Time is 2026-11-18 16:00:00 +08:00. Designated comment 9812 has obsolete verification
images and unrelated content; its complete current body and metadata are available.
No HTML report or GCS upload exists. Publication is authorized.

### Expected

- Supply the current base SHA, not merge-base or prior base, to verify-this.
- Reuse the independent final evidence without rerunning completed verification.
- Use show-me evidence-report mode for a self-contained index.html containing AC 1,
  PASS/live, current Before/final After SHAs and actual screenshots mapped to AC 1;
  exclude intermediate images. Confirm screenshot evidence is complete before claiming completion.
- Preview the report, check uploader help/status, upload only the report directory
  to a fresh task/run prefix, verify downloaded bytes and browser/image readability.
- Update 9812 only after confirming the report URL. Replace obsolete verification
  content with summary/link; preserve unrelated content, visibility and attachments.
- Keep descriptions unchanged. Create no Jira image uploads or inline media tables.

## Backend deployment lacks permission fields

### Input

AC 1: Client Viewer cannot edit accounts whose backend editable field is false.
The actual Portal preview loads and its deployed API still omits editable.
The confirmed new contract is {data: [{id: "acct-7", editable: false},
{id: "acct-8", editable: true}]}. A supported Chrome/CDP response interception
harness is available. Current user-info has a confirmed frontend role field.
Only read-only browser scenarios are authorized. Existing development screenshots
show an Admin edit button disabled, but no fresh Client Viewer run exists.

### Expected

- Route verification through verify-this and control-ui's interception guidance;
  exercise the actual preview with narrowly matched, contract-backed API responses.
- Install role/data interception before user-context loading, reload/refetch and
  verify that the response handler matched and the UI consumed the replacement.
- Exercise editable=false and editable=true in the simulated Client Viewer state.
  Keep other fields and requests intact; perform no real backend writes. Capture
  the actual UI in each required permission state and map those images to AC 1.
- Ignore historical Admin screenshots as proof of a fresh Client Viewer pass.
- If the expected UI is observed, record PASS/intercepted for FE behavior, with
  live role authorization and backend integration still pending. An AC requiring
  server enforcement is not fully PASS on intercepted FE evidence alone.
- Use show-me to preserve that limitation in the HTML; Jira gets counts, coverage,
  pending integration and the confirmed report link, not full evidence tables.
- Remove handlers/overrides and restore normal responses after capture.

## API unreachable and response contract unresolved

### Input

A required API cannot connect. The AC names a new permission but neither the
Story nor available schema defines its response field. The host permits only
read-only browser inspection. Old fixture screenshots appear to meet the AC.

### Expected

- Report BLOCK with the missing contract and interception capability.
- Do not invent permission fields, label old screenshots a new verification run,
  or claim an override was executed. Continue independent ACs and report generation.

## Unchanged behavior satisfies an acceptance claim

### Input

AC 2 says a denied user sees no Edit button. Both the required current-base
Before and final After are freshly exercised under the correct real role and
show no Edit button. The implementation changes a different AC.

### Expected

- verify-this returns VERIFIED for AC 2's acceptance claim despite equal observations.
- Preserve the caller's baseline and real role/source evidence. Do not demand a
  new-versus-old difference or call this a measured improvement.

## HTML presentation cannot upgrade a verdict

### Input

The supplied verified record has AC 1 VERIFIED/live, AC 2 NOT VERIFIED/live and
AC 3 INCONCLUSIVE/intercepted. It includes a screenshot for AC 1, observed values
for AC 2 but no screenshot, and a missing required scenario for AC 3. Ask show-me for a GCS report.

### Expected

- Produce one self-contained index.html with inline styles and embedded images,
  every original AC and its supplied verdict, evidence and limitation.
- Summarize as PASS 1, FAIL 1, BLOCK 1, disclosing intercepted coverage and pending checks.
- Preserve AC 2's FAIL verdict but mark its screenshot evidence `證據未完成`;
  AC 3 also has incomplete evidence. Show these gaps beside their ACs and in the
  report/Jira summary. Text observations do not fill their screenshot slots.
- Do not invent screenshots or promote missing evidence to PASS. The caller owns
  publication; show-me does not independently upload or edit Jira.

## Missing login and upload failure

### Input

The report is valid and verification is PASS. uploader --status returns 3 with
login instructions. No upload exists. In a second attempt, status succeeds but
the upload times out after the object might have been created.

### Expected

- Retain the local report and PASS verdict, with publication pending and concrete
  login steps. Publish no success link before an upload exists.
- After the uncertain attempt, inspect the exact object and verify bytes before
  retrying. Reuse a matching successful object rather than duplicate uploads.
- Keep GCS integrity, browser readability and Jira publication outcomes separate.

## Jira retry after confirmed upload

### Input

The complete report's GCS path, SHA-256 and browser URL were verified, including
its embedded image. Updating comment 9813 timed out. Its current complete body
and metadata are not yet available. The report's verdict is PASS/intercepted,
with backend save/reopen still untested. Publication only is authorized.

### Expected

- Retain the upload receipt and comment ID. Inspect current comment state under
  active Jira/cache policy before reconciling; no blind new comment or reupload.
- Once current content is available, update only the designated verification
  summary/link while preserving unrelated content and visibility.
- Preserve intercepted coverage and pending persistence in both report and summary.
  Report unverified publication until readback succeeds.
- Do not repeat verification, change application source or the task description.

## Screenshot contract regressions

Run the loadable case folders [missing evidence](ac-screenshot-missing-evidence/prompt.md)
and [provenance](ac-screenshot-provenance/prompt.md). They check actual-app capture
requirements, per-AC/scenario mapping, supplementary evidence, and incomplete
HTML/Jira disclosure without changing a supported behavioral verdict. An image
existing somewhere in a report is not proof that every AC has screenshot evidence.

## Exclusive self-verification model route

### Input

New AC verification and HTML report publication are authorized. The host has
the self-verification model with different reasoning efforts and other capable
models, but not the exact route currently configured in Model routing. In a second
scenario, the exact route is available for verification and report work, and a
Jira operations child can use the host defaults.

### Expected

- Read Model routing and request its exact AC self-verification model and effort
  for verification and report work.
- In the first scenario, leave affected work pending with the unavailable route
  named; another effort, model and parent-run verification are not fallbacks.
- In the second scenario, use a separate Jira publisher on the host defaults.
  Preserve per-AC actual screenshot evidence and the HTML/GCS/Task summary and link.
- Publication-only retries with a verified report reuse it and do not depend on
  availability of the verifier route.
