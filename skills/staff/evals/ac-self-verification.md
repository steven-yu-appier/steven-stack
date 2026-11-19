# AC self-verification cases

Use these offline cases when revising [AC self-verification](../references/ac-self-verification.md)
or [using-jira](../../using-jira/SKILL.md). Give the agent the workflow, shared
input and one case's Input, without Expected. Request next actions and draft
report/comment content. Do not contact Jira/GCS, start apps, create agents or
modify source. Evidence stubs do not establish an actual test run.

## Shared input

The task is DEMO-101, branch `demo-101`. Unless overridden, AC 1 is
`Empty search results display "No results".`, the tested commit is `bbbbbbbb`,
the environment is `https://example.invalid/preview/demo-101/`, and backend is
`dev`. Verification time is `2026-11-18 16:00:00 +08:00`. Publication requests
are authorized. Task comment 9812 has confirmed author/visibility, obsolete
verification content and unrelated text to preserve.

For cases with a confirmed upload, a separate verifier has supplied matching
actual-app screenshots for every required state. The self-contained HTML,
downloaded SHA-256 and browser/image readability have been verified. Its URL is
`https://storage.cloud.google.com/appier-td-autotest/deletable-files/DEMO-101/run-1/index.html`.
Readers need bucket access; retention is about 30 days.

## Cases

| Case | Input | Expected |
| --- | --- | --- |
| Rebased comparison | Previous base is `11111111`, current PR base is `33333333`, merge-base is `22222222`. Fresh current-base screenshot shows "Nothing found"; final screenshot shows "No results". Independent verdict is VERIFIED/live. Intermediate commit `cccccccc` also has images. No report/upload exists. | Use current-base Before and final After, excluding intermediate images. Reuse verification and prepare the HTML/GCS/Task comment delivery. |
| Undeployed contract | Preview API omits `editable`. Confirmed contract supplies accounts with `editable=false` and `true`; a frontend Client Viewer role field and response interception are available. Only read-only scenarios are authorized. Old screenshots show Admin. | Plan contract-backed interception before context loading, confirm consumption, exercise both states and capture actual UI. Restore handlers afterward. FE may be PASS/intercepted; live authorization and BE integration remain pending. |
| Unknown contract | API is unreachable and the permission field is undefined. Host supports read-only inspection only. Old fixtures appear correct. | BLOCK the affected AC without inventing fields or a new run. Continue independent ACs. |
| Unchanged behavior | Denied users see no Edit button in fresh current-base and final runs under the correct role. Another AC changed. | Accept the verified claim without requiring a Before/After difference or claiming improvement. |
| Verdict mapping | AC 1 is VERIFIED/live with a screenshot, AC 2 is NOT VERIFIED/live without one, AC 3 is INCONCLUSIVE/intercepted with a required scenario untested. | Report PASS 1, FAIL 1, BLOCK 1. Keep AC 2's FAIL separate from its incomplete screenshot evidence. AC 3 remains BLOCK with its missing scenario. Presentation cannot upgrade either result. |
| Missing captures | AC 1 has a matching final app screenshot. AC 2 is VERIFIED/live but capture failed; only text, HTTP 200 and green tests exist. AC 3 is VERIFIED/intercepted with only API JSON and a drawn UI. | AC 1 evidence is complete; AC 2/3 are `證據未完成`. Preserve supported behavioral verdicts and request actual-app captures. |
| Wrong provenance and reuse | AC 1 requires Client Viewer editable=false/true states at the final commit, but only an old-base Admin image exists. AC 2 has a valid final No results image. AC 3's denied-save state has only DevTools JSON. Someone proposes reusing AC 2's image everywhere and drawing the missing UI. | Only AC 2 has complete evidence. AC 1 needs both matching states; AC 3 needs its app capture. Reuse or drawings cannot establish unrelated claims. |
| Upload failure | Local report is valid and PASS. First, uploader status returns 3 with login instructions. Later, upload times out after the object might exist. | Keep PASS and the local report; publication stays pending. Report setup steps, then inspect the exact object and verify bytes before retrying. |
| Standalone publication | Publish the confirmed upload only. Verdict is PASS/intercepted; real BE integration remains untested. Current complete comment 9812 is available. | Delegate to using-jira, reuse the upload, replace only verification content in 9812 and plan readback. No new verification, upload, comment or source edit. |
| Uncertain Jira write | Confirmed upload exists. Updating 9812 timed out; current body/metadata are unavailable. Verdict is PASS/intercepted with backend save/reopen untested. Only publication is authorized. | Inspect current comment state before retrying. Retain the upload receipt/comment ID, preserve unrelated content and keep publication unverified until readback. |
| Verifier route unavailable | New verification/report work is requested, but the exact configured route is unavailable; other models/efforts exist. | Leave that work pending and name the unavailable route. No model substitution or parent-run verification. |

## Shared grading

Grade decisions and evidence claims, not exact prose. Reports preserve original
AC numbering, verdicts, screenshot gaps and live/intercepted limitations. Show
gaps beside each affected AC and in the HTML/Jira summary. Jira receives only
the summary and confirmed report URL, with access/retention limits. Preserve
unrelated comment content and visibility; leave task descriptions unchanged.
