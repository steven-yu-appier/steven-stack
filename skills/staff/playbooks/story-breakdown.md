### Story breakdown and planning

Use to clarify a Jira Story, plan its engineering tasks, or review its plan. Apply
[Staff's planning scope](../SKILL.md#autonomy) to every workflow call.

Resolve both roles in [Model routing](../references/model-routing.md#workflow-roles)
and dispatch them through [Subagent routing](../references/subagent-routing.md).

1. Have the Jira Story planner run
   [jira-dev-task-from-story](../../jira-dev-task-from-story/SKILL.md) with
   the Story, repositories, and requested scope. Relay clarification questions
   and confirmed answers between the planner and the user.
2. Have the independent Jira Story plan reviewer check the draft against the
   acceptance record and source pointers. For review-only requests, start here
   with the existing draft and return the findings.
3. Present the [review package](../../jira-dev-task-from-story/references/breakdown-format.md),
   including the proposed descriptions and plan comments. For a draft-only
   request, return the package and open questions here.
4. To publish, obtain approval of the ready tasks and their full content. Run
   [Jira operations](jira-task.md) with the approved subset,
   reviewed drafts, and recorded authorization. Keep other tasks as drafts.
