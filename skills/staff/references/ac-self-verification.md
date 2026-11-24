# AC self-verification

Staff coordinates the verification worker and a separate Jira worker. Use [model routing](model-routing.md#workflow-roles) and [subagent routing](subagent-routing.md) for assignments.

## 1. Resolve the verification scope

At delivery, use the Task and its [acceptance record](implementation-scope.md). For standalone verification, read the named Task or Story through **using-jira** under the active Jira read policy. Use that issue's AC and publish the report comment on that same key. Linked issues provide context. Preserve AC wording and numbering. Assign stable numbers in source order where needed.

Identify the branch, tested commit, environment, role and applicable [backend](jira-preview.md#select-the-backend-environment) from the issue, PR or task record. Resolve which revision the running app serves. For comparisons, record the full SHA of the PR's current base or verified stack parent. Without a PR, use a confirmed comparison revision. Recheck the base before publication. Mark unresolved comparisons or untested ACs BLOCK with the reason. If no AC can be identified, request the missing criteria.

Standalone verification authorizes the report upload and verification comment. Report failures for the implementer. Source fixes, Git delivery and Story preview sync belong to implementation. Local-only and draft requests retain the report locally. For uncommitted changes, record HEAD plus a diff fingerprint and keep the report local until the verified commit exists.

## 2. Verify each AC

Assign a fresh verifier distinct from the implementer. Pass the AC, source revisions, environment and task paths to [verify-this](../../verify-this/SKILL.md). Reuse evidence only while its requirements, source and environment still match. If independent verification is unavailable, record it as pending.

Capture actual app screenshots with **control-ui**. Map each required state to its AC, screenshot path, revision, role and scenario. Compare Before and After with equivalent data, role and viewport. Reuse an image across ACs only when it proves each mapped claim. For unavailable backend behavior, use [contract-backed interception](../../control-ui/references/api-response-interception.md) and capture the UI after it consumes the response.

Record three results per AC:

- **Behavior.** VERIFIED becomes PASS, NOT VERIFIED becomes FAIL, INCONCLUSIVE or unexercised becomes BLOCK.
- **Coverage.** Record live, intercepted or mixed. Name intercepted fields and scenarios. Keep real backend integration pending for intercepted claims.
- **Screenshot evidence.** Mark complete only when every required state has a readable, current, matching app screenshot. Otherwise record `證據未完成`, the missing state and reason, even for an observed PASS.

During implementation, fix FAIL results and refresh affected verification. An authorized draft PR can disclose blocked coverage.

## 3. Present one HTML report

Use [show-me](../../show-me/SKILL.md) in evidence-report mode to create a self-contained `index.html` in the [task archive](../playbooks/task-artifacts.md), with embedded screenshots and styles. Write in Traditional Chinese. Preserve original AC text and UI/API identifiers. Include the issue, branch, Before/After revisions, timestamp with UTC offset, environment, role, backend and outstanding checks.

Render the report with **control-ui**. Check every AC's observations, verdict, coverage and screenshot provenance against the verifier's record. Place screenshots and evidence gaps beside the corresponding result.

## 4. Upload the report to GCS

Check `upload-deletable-files --help` and `--status`. Upload only the report directory to a fresh `<ticket>/<run-id>/`. Record the GCS object path, browser URL, local SHA-256 and upload time. Download the object with `gcloud storage cp` and compare its bytes. Open the URL in an authorized signed-in browser and verify the report and embedded images load.

Keep upload integrity and browser readability pending until each check succeeds. If tools or access are unavailable, retain the local report and give the setup steps. Publication failure preserves the AC verdicts. Inspect an uncertain upload before retrying and reuse a confirmed object for Jira retries.

## 5. Publish a Jira summary and link

Assign [using-jira](../../using-jira/SKILL.md) the named issue, branch, tested commit, confirmed GCS URL and per-AC results. Match the dedicated verification comment by recorded ID or unique issue/branch match. Verify author and visibility. Create one only after confirming none exists. Ambiguous matches leave publication pending.

Update only the verification section. Preserve unrelated content, attachments and visibility. Include verification time, commit, PASS/FAIL/BLOCK counts, screenshot gaps, intercepted coverage, pending checks and the report link. Note that readers need bucket access and the object expires after about 30 days. Keep the local copy.

Read back the comment on the same issue under the active Jira/cache rules. Confirm the results, visibility and exact URL. Record the comment ID. Inspect uncertain writes before retrying. Report AC coverage, GCS publication and Jira readback separately.
