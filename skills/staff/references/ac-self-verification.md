# Record AC self-verification

Use for Staff implementation or fix work with a Jira task acceptance checklist.
This engineer's record is separate from QA acceptance, the PR's reviewer targets,
and the Story's preview comment. It adds no code-review gate. For investigations,
Story planning, prototypes, or work without a resolved Jira task checklist,
report it as not applicable. Follow active Jira write restrictions. Local-only
work retains evidence and the payload without publishing to Jira.

## 1. Freeze the Before evidence

Before changing source, resolve this task branch's base and record its full
commit SHA in the existing task record. Use the PR's target or the verified
parent branch for a stack, then pin the branch's initial merge-base. Resolve an
ambiguous base before capture. Reuse that SHA after rebases, target advances,
and follow-up fixes.

For every AC a screenshot can demonstrate, use **control-ui** with Chrome to
capture Before at that exact base. Use an isolated worktree or an existing
verified base deployment rather than switching the active checkout. Record the
role, data, viewport, UI state, environment, and source revision. Keep the images
in the task archive and reuse them on reruns. Capture Before for new AC at the
same pinned base. Disclose environment or dataset changes that limit comparison.

If work has already started, recover the original base from verified Git or PR
history and the task record. Capture missing Before evidence there. If that
base or capture is unavailable, mark the affected comparison BLOCK with the reason.

## 2. Delegate AC evidence collection

After cleanup and final checks, use a stable tested commit for After. Record
the self-verification time with its UTC offset and an eight-character commit
prefix. Match the running app to that source and backend. If a matching preview
requires a push or draft PR, complete that authorized publication with coverage
marked pending, then resume verification and refresh the PR's evidence claims.
For local-only work with uncommitted changes, record HEAD plus a diff fingerprint
and label it as uncommitted. Do not present HEAD alone as the tested source.

Assign a fresh AC verifier child, distinct from the implementation owner,
through [Subagent routing](subagent-routing.md). Give it the task's canonical
Jira pointers, acceptance record, pinned Before evidence, tested source and
environment, **control-ui**, and an assigned evidence/report path. It owns AC
evidence, not source changes or Jira publication. Grant only the tools needed
for those actions. If required delegation is unavailable, report that coverage
pending instead of presenting the parent's checks as an independent run.

The child accounts for every task AC with its original wording, numbering, and
item identity. Number unnumbered items in source order. Classify each AC:

- **PASS.** The child exercised the relevant flow and observed the expected
  result. For visual AC, include the fixed Before and current After images.
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

The report includes every AC's status, Observed or Reason, evidence paths,
coverage limits, and any manual steps and cases. The owner checks it against
the current source and AC before publication. Refresh affected After coverage
when source, requirements, or environment changes. Fix FAIL results before
continuing delivery. BLOCK permits an authorized draft PR with pending coverage.

## 3. Build the comment payload

Start from [the ADF template](../assets/ac-self-verification.adf.json). Keep one
header, repeat the relevant visual or manual section per AC in source order,
and remove unused sections. Set values with a JSON parser.

Keep the short form:

```markdown
Self-verification | <time with offset> | Commit: <short hash>
Environment: <app URL and backend>

#### [PASS or FAIL] AC <number> - <original AC>

Observed: <actual result, including the mismatch for FAIL>

| Before - <fixed base> | After - <tested commit> |
| --- | --- |
| <image> | <image> |

#### [BLOCK] AC <number> - <original AC>

Reason: <why human verification or missing evidence prevents a result>

Test steps
1. <precondition and entry>
2. <action and expected result>

Test data/cases

| Case | Role / data | API evidence | Expected |
| --- | --- | --- | --- |
| <case> | <identifiers> | <endpoint and observed fields> | <result> |
```

For directly observable nonvisual AC, use the result heading and Observed with
the relevant runtime evidence instead of an image table. For BLOCK without
accessible data, state what is missing rather than inventing table rows.

Upload new Jira image attachments through Chrome only when active Jira
instructions permit browser attachment writes. Otherwise retain local evidence
and report image publication pending. Reuse uploaded Before media. Copy real
Jira media references from the upload or editor response, including actual image
dimensions. The template's 1280 by 800 dimensions are examples. An attachment ID
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
record, keep the branch, comment ID, fixed base, uploaded media references, and
checklist items this workflow checked. Reuse the ID on reruns. Without a recorded
ID, match an unambiguous comment for this branch through metadata and canonical
content. Resolve ambiguity before writing. Keep its visibility and preserve
other authors' content and media.

Write the complete ADF from a task-owned scratch file to the designated comment.
Create a comment only when none exists. After readback, verify that uploaded
images render in Before/After order.

Then synchronize the task description's checklist with acli, preserving item
IDs, text, order, protected content, and unrelated or human-owned completion
states. Check a PASS only after verifying its published evidence. FAIL and BLOCK
add no check. Revoke this workflow's prior check when its evidence fails or
becomes stale. If the canonical representation cannot preserve the description,
leave synchronization pending rather than rebuilding it from lossy Markdown.

Track upload, comment, and checklist outcomes separately. Retain successful IDs
so partial failures do not repeat uploads or comments. Archive the result and
evidence links under [Task files and cleanup](../playbooks/task-artifacts.md).
