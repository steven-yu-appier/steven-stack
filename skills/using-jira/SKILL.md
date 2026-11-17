---
name: using-jira
description: Handles Jira reads, issues, descriptions, comments, metadata, relationships, and attachments under Appier conventions. Use for Jira operations, including drafting, publishing, updating, or retrying AC self-verification results. Route unresolved Story breakdown to jira-dev-task-from-story.
---

# Use Jira

## Delegate Jira operations

The coordinator delegates this workflow to a Jira operations child on the
`gpt-6.1-terra-medium` route through
[Subagent routing](../staff/references/subagent-routing.md). Pass the requested
operation, targets, source pointers, task paths, publication authority, and any
known comment or attachment IDs. Follow active user and repository Jira
instructions for reads, writes, credentials, and cache handling.

An assigned Jira operations child executes its scope directly without delegating
this workflow again. An implementation child hands Jira operations back to its
coordinator for routing. The coordinator reviews the result and owns delivery.
If the required route or tool access is unavailable, leave Jira operations
pending and report the missing capability. Do not substitute a parent-run operation.

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
| Draft, publish, update, add images to, or retry task AC self-verification results | Read [AC self-verification](../staff/references/ac-self-verification.md) before preparing the comment. It owns comment selection, the ADF template, evidence, and readback. Use Jira commands only to execute that workflow. |
| Create an engineering task | [Task description](references/task-description.md) for AC; [Implementation plan](references/implementation-plan.md) for its plan comment. |
| Create a Story, survey, or other ticket type | [Ticket formats](references/ticket-formats.md). |
| Add or revise an implementation-plan comment | [Implementation plan](references/implementation-plan.md). |
| Revise numbered AC or plan items | [Dated updates](references/dated-updates.md). |
| Change fields, descriptions, or other comments | [Jira commands](references/jira-cli.md). Keep the change within the named fields or body. |
| Upload or reference a file | [Attachment commands](references/jira-attachments.md). Upload-only requests stop after attachment readback. |
| Add a relationship or hierarchy | [Relationship commands](references/issue-linking.md). |

The AC self-verification route takes precedence over generic comment and file-link
routes, including standalone publication with no implementation request. Reuse
valid evidence and the designated comment; publication alone does not require
repeating completed verification or authorize source changes.

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
