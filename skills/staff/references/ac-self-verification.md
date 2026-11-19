# Record AC self-verification

Use for implementation or fix work with a resolved Jira task's numbered AC,
and standalone report drafts, publication, updates, and retries. This is the
engineer's verification record, separate from QA acceptance and PR reviewer
targets. Investigations and Story planning without resolved task AC are not
applicable. Local-only work and report drafts retain the report without uploads
or Jira writes.

Before delegating verification or report work, resolve its route in
[Model routing](model-routing.md#workflow-roles).

## Contents

- Resolve the verification scope
- Verify through existing skills
- Present one HTML report
- Upload the report to GCS
- Publish a Jira summary and link

## 1. Resolve the verification scope

Reuse the acceptance record from [Implementation scope](implementation-scope.md).
Keep every AC's original wording and numbering. For frontend work, apply the
[backend selection rule](jira-preview.md#select-the-backend-environment) when
applicable. Record the environment, role, backend and tested source. After uses
the final stable tested commit. For uncommitted work, record HEAD and a diff
fingerprint and keep the report local until the verification commit exists.

Before is the PR's current base branch, or the verified parent for a stack.
Record its full SHA and supply it to **verify-this** as the comparison source.
Resolve it again before publication; source or requirement changes invalidate
only affected evidence. An ambiguous base leaves comparisons pending.

## 2. Verify through existing skills

For publication-only requests, reuse completed verification whose AC, tested
source and environment still match; collect only missing or stale evidence.
When new verification is needed, assign a fresh verifier, distinct from the
implementer, through [Subagent routing](subagent-routing.md). Pass the acceptance record, source
pointers, Before/After revisions, environment, task paths and the screenshot
contract below. The verifier uses
[verify-this](../../verify-this/SKILL.md) for the AC claims and its applicable
control skills for execution. Those skills own measurement, interaction and
evidence collection; this reference owns AC coverage and delivery.

When backend APIs are unreachable or have not deployed the required contract,
use **control-ui**'s [API response interception](../../control-ui/references/api-response-interception.md)
on the actual app or preview. Exercise the flow with contract-backed response
changes instead of treating old fixture screenshots as a new verification run.
If the contract or interception capability is unavailable, report that gap.

Every AC requires actual screenshots of the exercised app or preview, mapped to
its original AC number and the states/scenarios that establish the result. Capture
Before/After for comparisons at the recorded revisions and comparable role, data
and viewport. Intercepted scenarios require screenshots of the actual UI after
it consumes the replacement response. Use **control-ui** for capture.

Record screenshot paths and their source revision, role, scenario and coverage.
Text, API responses, test output, diagrams, mockups and screenshots of those
substitutes do not replace screenshots of the exercised app. They may supplement
the explanation. Reuse a screenshot across ACs only when its actual contents
establish each claim and each mapping is explicit.

Track screenshot evidence separately from the behavioral verdict: `complete`
only when each required state has a matching actual screenshot, otherwise
`incomplete` (display `證據未完成`) with the missing AC/state and reason.
Missing, unreadable, stale or mismatched screenshots remain incomplete even if
the verifier observed correct behavior. Capture the missing evidence when
possible; otherwise retain the verdict and disclose the evidence gap. An
unexercised AC remains BLOCK. Never claim AC verification is complete with an
incomplete screenshot record.

Record each AC's verification verdict and coverage mode separately:

- `VERIFIED` becomes PASS, `NOT VERIFIED` becomes FAIL, and `INCONCLUSIVE`
  becomes BLOCK with its concrete missing evidence or prerequisite.
- Coverage is `live`, `intercepted`, or `mixed`. Name the API fields and scenarios
  intercepted. An intercepted FE pass leaves real backend integration pending;
  split FE and BE claims when the AC includes both.

The owner accounts for every AC and checks the verifier's evidence against the
current source. Fix FAIL results and refresh affected verification before
continuing delivery. BLOCK permits an authorized draft PR with pending coverage.
If independent verification is unavailable, report it pending rather than
presenting the implementer's checks as independent.

## 3. Present one HTML report

Use [show-me](../../show-me/SKILL.md) in evidence-report mode with the complete
verified record. Request a self-contained `index.html` in the task archive,
including embedded screenshots and styles. Pass the per-AC screenshot mapping
and completeness record to **show-me** as required evidence. It owns presentation,
not verdicts.
The report contains the ticket and branch, verification time with UTC offset,
Before/After SHAs, environment, every AC's status and coverage, observations,
evidence and any remaining manual or backend integration checks. Write prose
in Traditional Chinese, retaining original AC wording and UI/API identifiers.

Review the rendered report through **control-ui**. Confirm every AC is present,
its mapped actual screenshots render beside its result, and missing evidence is
labeled `證據未完成` beside the affected AC. Check screenshot provenance and
scenario coverage, not just the presence of an image. Observations, verdicts and
limitations must agree with the verifier's results.
Apply [Task files and cleanup](../playbooks/task-artifacts.md) for retention.

## 4. Upload the report to GCS

Read `upload-deletable-files --help`, then run `--status`. If the tool or gcloud
is missing, or status is nonzero, retain the report and show the concrete setup
steps. Install software only within the user's authorized scope. An upload
failure does not change the verification verdict.

For authorized publication, upload the report directory to a fresh
`<ticket>/<run-id>/` sub-folder with `upload-deletable-files`. Upload only the
report deliverable, not the whole task archive or scratch. Retain the returned
GCS path, browser URL, report SHA-256 and upload time in the task record. On an
uncertain outcome, inspect the exact object before retrying; reuse a confirmed
upload when only Jira publication needs retrying.

Download the object using `gcloud storage cp` and compare its bytes with the
local report. Open the returned browser URL in an authorized signed-in browser
and check the report and embedded images. Track upload integrity and browser
readability separately; a successful copy alone does not prove readers can open
it. Keep publication pending when those checks are incomplete.

The shared bucket requires reader access and its documented lifecycle is about
30 days. Treat its URL as temporary. Preserve the report locally, record the
retention limitation, and never claim the link is permanent.

## 5. Publish a Jira summary and link

Delegate publication and retries to a separate [using-jira](../../using-jira/SKILL.md) child. Pass the
Task key, branch, tested commit, confirmed GCS report URL, counts by status,
incomplete-evidence ACs, intercepted coverage, pending checks, and task record.
Jira receives a short summary and a link to the report in GCS.

Publish a dedicated verification comment on the Jira Task for this branch.
Verify any recorded comment ID, author and visibility. If there is no recorded
ID, find an unambiguous matching Task verification comment or create one after
confirming none exists. Record the comment ID for retries. If lookup is
unavailable or ambiguous, leave publication pending. Update the verification
section of an existing match in place, replacing its old results, image tables
and report link while preserving unrelated content, visibility and attachments.

Use ordinary text paragraphs and a link, for example:

```text
自我驗證 | <含時區的時間> | Commit: <short SHA>
結果：PASS <n>、FAIL <n>、BLOCK <n>
截圖證據：<完整 / 證據未完成：AC 編號及缺少情境>
覆蓋：<live / intercepted / mixed；尚待真實 BE 驗證的範圍>
報告：<confirmed GCS browser URL>
限制：<pending checks；報告約 30 天後清除，需 bucket 存取權限>
```

Read back the designated comment on the Jira Task under active Jira/cache
instructions. Confirm the commit, counts, screenshot completeness, coverage,
and exact report URL, with unrelated content intact. Incomplete reports may be published with their gaps
visible in both HTML and Jira; publication does not complete missing evidence.
Keep upload and Jira outcomes separate. After a timeout, inspect current state
before retrying so successful uploads and comments are not duplicated.
