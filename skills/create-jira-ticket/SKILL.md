---
name: create-jira-ticket
description: Create or update Jira issues, descriptions, comments, metadata, relationships, and attachments under Appier conventions. Use for drafting or publishing requested Jira changes. Route unresolved Story breakdown to jira-dev-task-from-story.
---

# Create or update Jira tickets

## Scope and authorization

Resolve the target, requested operation, and prior approvals. A reference ticket
is a source, not a write target. Draft and review requests make no Jira writes.
An explicit create, update, post, or upload request authorizes that operation;
execute fully specified or previously approved changes without asking again.
Ask only about unresolved choices that affect the target, meaning, or scope,
while preparing the parts already clear.

## Select the operation

Read only the references needed for the request. Combine operations only when
requested; a field update, description edit, or upload adds no plan comment.

| Request | Route |
| --- | --- |
| Clarify a Story or break it into tasks | Use **jira-dev-task-from-story** before publication-ready task drafting. |
| Create an engineering task | [Task description](references/task-description.md) for AC; [Implementation plan](references/implementation-plan.md) for its plan comment. |
| Create a Story, survey, or other ticket type | [Ticket formats](references/ticket-formats.md). |
| Add or revise an implementation-plan comment | [Implementation plan](references/implementation-plan.md). |
| Revise numbered AC or plan items | [Dated updates](references/dated-updates.md). |
| Change fields, descriptions, or other comments | [Jira commands](references/jira-cli.md). Keep the change within the named fields or body. |
| Upload or reference a file | [Attachment commands](references/jira-attachments.md). Upload-only requests stop after attachment readback. |
| Add a relationship or hierarchy | [Relationship commands](references/issue-linking.md). |

## Prepare and execute

- Select jarkdown for planning-time Story reads and acli or REST API for other Jira operations under [Jira read policy](../staff/references/jira-read-policy.md).
- For drafts and payload files, follow [Task files and cleanup](../staff/playbooks/task-artifacts.md); reuse caller-supplied paths.
- For authored text, apply **technical-writing** and **unslop**. Preserve domain terms, identifiers, sources, and confirmed decisions.
- Before any Jira write, follow [Jira commands](references/jira-cli.md) for payloads, existing-content preservation, and readback. Attachment uploads follow their own command reference.

## Finish

Return the requested draft, or report issue links, comment IDs, verified changes,
and pending operations. Distinguish published but unverified writes from failures.
If one operation is blocked, complete independent authorized operations. Retain
successful IDs so retries resume without duplicating issues, comments, or uploads.
