# Task complete

Staff dispatches [workers](../references/subagent-routing.md) within the task's delivery limits. Workers return their results to Staff.

1. **Cleanup.** Run the [delivery addon, cleanup and test audit](opening-a-pr.md#delivery-addon), then final checks. Commit when authorized and return the tested revision.
2. **Verification.** For numbered Jira Task AC, assign an independent [AC verifier](../references/ac-self-verification.md) to verify the revision, prepare the report and confirm its upload.
3. **PR.** Follow [Opening a PR](opening-a-pr.md) for push, remote commit verification and PR readback. If verification needs a preview, publish the authorized draft first and refresh it after verification.
4. **Jira.** Dispatch [using-jira](../../using-jira/SKILL.md) when each input is ready. The verified report URL goes in the Task verification comment. Applicable preview URLs from the verified PR body go in the Story preview comment.
5. **Handoff.** Staff sends failed ACs back for repair and rechecks affected evidence. Record the revision, URLs, comment IDs and pending work. Reconcile uncertain writes before retrying. Finish or pause under [Task files and cleanup](task-artifacts.md).
