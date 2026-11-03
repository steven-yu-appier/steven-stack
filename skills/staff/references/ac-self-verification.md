# Record AC self-verification

Use for Staff implementation or fix work with a Jira task acceptance checklist.
This engineer's record is separate from QA acceptance, the PR's reviewer targets,
and the Story's preview comment. It adds no code-review gate. For investigations,
Story planning, prototypes, or work without a resolved Jira task checklist,
report it as not applicable. Follow active Jira write restrictions. Local-only
work retains evidence and the payload without publishing to Jira.

## 1. Resolve the Before source

Before is the current version of the PR's base branch for this verification run.
Use the verified parent branch for a stack. Record its branch name and full
commit SHA in the task record. Resolve an ambiguous base before capture.
The task branch's initial merge-base does not define Before.

Resolve the base again on each run and before publication. If it advanced or
was rebased, capture Before at the new base SHA and replace the old comparison.

For every AC a screenshot can demonstrate, use **control-ui** with Chrome to
capture Before at that exact base. Use an isolated worktree or an existing
verified base deployment rather than switching the active checkout. Match the
Before and After role, data, viewport, and UI state. Keep source and environment
details in the task record. Reuse images only while the base SHA and comparison
conditions match. If the source or matching capture is unavailable, mark the
affected AC BLOCK.

## 2. Delegate AC evidence collection

After cleanup and final checks, use a stable tested commit for After. Record
the self-verification time with its UTC offset and an eight-character commit
prefix. Every After image must come from that exact commit. Match the running
app to that source and backend. If a matching preview requires a push or draft
PR, complete that authorized publication with coverage
marked pending, then resume verification and refresh the PR's evidence claims.
For local-only work with uncommitted changes, record HEAD plus a diff fingerprint
and label it as uncommitted. Keep it local until the verification commit exists.

Assign a fresh AC verifier child, distinct from the implementation owner,
through [Subagent routing](subagent-routing.md). Give it the task's canonical
Jira pointers, acceptance record, current Before evidence, tested source and
environment, **control-ui**, and an assigned evidence/report path. It owns AC
evidence, not source changes or Jira publication. Grant only the tools needed
for those actions. If required delegation is unavailable, report that coverage
pending instead of presenting the parent's checks as an independent run.

The child accounts for every task AC with its original wording, numbering, and
item identity. Number unnumbered items in source order. Classify each AC:

- **PASS.** The child exercised the relevant flow and observed the expected
  result. Include matching Before and After screenshots from the recorded sources.
  Passing tests or reading source alone does not establish PASS.
- **FAIL.** The child exercised the flow and observed a mismatch. State the
  expected and actual result. Return the defect to the implementation owner
  for a fix, then refresh affected After evidence at the new commit.
- **BLOCK.** The AC needs human verification with a particular role or backend
  data. Use **control-ui** to operate Chrome and inspect actual API responses
  to find usable cases. Record the role, stable data identifiers, endpoint,
  relevant response fields, steps, and expected results. Finding the data or
  exercising one example does not turn this manual case into PASS. Also use
  BLOCK for missing access, data, environment, or required evidence. State the
  reason and distinguish observed response values from proposed cases.

Use the authorized test environment. Limit data changes to authorized test
records. Retain relevant response fields, not credentials or whole network
captures. For visual evidence, match the Before conditions where reproducible
and disclose differences. A screenshot supports only what it actually shows.

The child's local report includes every AC's status, observations, evidence
paths, coverage limits, and any manual steps and cases. The owner checks it
against the current source and AC before publication. Refresh affected evidence
when source, requirements, or environment changes. Fix FAIL results before
continuing delivery. Keep failure details in the local report until re-verification.
BLOCK permits an authorized draft PR with pending coverage.

## 3. Build the comment payload

Start from [the ADF template](../assets/ac-self-verification.adf.json). Keep one
verification header with the time, commit, and environment. Repeat the relevant
PASS or BLOCK section per AC in source order and remove unused sections. Set
values with a JSON parser. Write commentary in Traditional Chinese, retaining
original AC wording, UI labels, API fields, and identifiers.

For PASS, publish only the AC heading and Before/After image table. Keep
observations, measurements, execution logs, and verification summaries in the
local report. The comment contains only the current base and tested commit,
with no screenshots or results from intermediate implementation versions.

For BLOCK, give one short reason, a usable test-account link, API-verified data,
and numbered steps with expected results. Follow the concise Traditional Chinese
style of [the BLOCK example](https://appier.atlassian.net/browse/CAMD-28516?focusedCommentId=2246714).
Explain missing access or data directly. Omit unavailable links or data instead
of inventing them. Keep browser-control failures and partial debug observations
in the local report.

Keep the short form:

```markdown
自我驗證 | <含時區的時間> | Commit: <short hash>
環境：<app URL 與後端>

#### [PASS] AC <編號> - <原始 AC>

| Before - <base branch 與 SHA> | After - <驗證 commit> |
| --- | --- |
| <截圖> | <截圖> |

#### [BLOCK] AC <編號> - <原始 AC>

阻擋原因：<一句話>
測試帳號：[<帳號 ID>](<可直接開啟的連結>)

| 案例 | 角色與資料 | API 已確認資料 | 預期結果 |
| --- | --- | --- | --- |
| <案例> | <識別資訊> | <endpoint 與實際欄位值> | <預期結果> |

驗證步驟

1. <前置條件與入口>
2. <操作與預期結果>
```

Upload new Jira image attachments through Chrome only when active Jira
instructions permit browser attachment writes. Otherwise retain local evidence
and report image publication pending. Reuse only media matching the current
Before and After sources. Copy real Jira media references from the upload or
editor response, including actual image dimensions. The template's 1280 by 800
dimensions are examples. An attachment ID
or local path is not a Media Services ID. If upload or reference resolution
fails, leave image publication pending. Publish only resolved media, with no
placeholder IDs or filename substitutes.

Validate the instantiated ADF, AC coverage, status values, and media identity
and order. Resolve all template tokens before publishing. The formats follow
[ADF structure](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/)
and [media nodes](https://developer.atlassian.com/cloud/jira/platform/apis/document/nodes/media/).

## 4. Publish and synchronize checklist state

Use [Jira read policy](jira-read-policy.md) for content and
[Jira CLI operations](../../create-jira-ticket/references/jira-cli.md) for acli
commands, freshness, content preservation, readback, and retry handling.

Use one designated self-verification comment per task and branch. In the task
record, keep the branch, comment ID, base branch and SHA, uploaded media
references, and checklist items this workflow checked. Reuse the ID on reruns.
Without a recorded ID, match an unambiguous comment for this branch through metadata and canonical
content. Resolve ambiguity before writing. Keep its visibility and preserve
other authors' content and media.

Write the complete ADF from a task-owned scratch file to the designated comment.
Create a comment only when none exists. On reruns, replace its prior AC results
and images instead of appending history. Preserve unrelated content and attachments.
After readback, verify source labels and Before/After order, and confirm that
no intermediate-version images or old results remain in the comment.

Then synchronize the task description's checklist with acli, preserving item
IDs, text, order, protected content, and unrelated or human-owned completion
states. Check a PASS only after verifying its published evidence. FAIL and BLOCK
add no check. Revoke this workflow's prior check when its evidence fails or
becomes stale. If the canonical representation cannot preserve the description,
leave synchronization pending rather than rebuilding it from lossy Markdown.

Track upload, comment, and checklist outcomes separately. Retain successful IDs
so partial failures do not repeat uploads or comments. Archive the result and
evidence links under [Task files and cleanup](../playbooks/task-artifacts.md).
