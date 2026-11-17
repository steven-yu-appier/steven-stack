### Jira operations

Use for Jira operations, including task creation, implementation plan comments,
and standalone AC self-verification publication or updates.
Apply [Staff's Jira scope](../SKILL.md#autonomy).

1. Identify the target tasks, source material, requested fields, and authorization.
   Reuse reviewed drafts and approval from Story breakdown. For a standalone
   request, use the user's specified changes as the scope. A description-only
   request stays limited to the description.
2. Delegate [using-jira](../../using-jira/SKILL.md) with those inputs on
   `gpt-6.1-terra-medium` through [Subagent routing](../references/subagent-routing.md).
   It owns drafting, formats, publication, and readback. Return its result and
   any pending operations. Jira-only work ends at that result.
