---
name: jira-dev-task-from-story
description: >-
  Clarifies a Jira Story against the actual repositories and existing tickets,
  and drafts engineering task breakdowns with acceptance checklists and implementation
  plans. Use for Story grooming, grilling, breakdown, or planning before Jira publication.
---

# Plan engineering tasks from a Story

Identify uncovered work and draft the tasks needed to deliver it. Apply
[Staff's planning scope](../staff/SKILL.md#autonomy).
[Story breakdown and planning](../staff/playbooks/story-breakdown.md) owns the
subsequent review and publication approval.

Use [Task files and cleanup](../staff/playbooks/task-artifacts.md) for local
planning artifacts, reusing the caller's archive and scratch paths when supplied.

## Ground the scope

1. Resolve the Story key, target repositories, and requested scope. Start with the
   current repository and verify any other repository named by the Story.
2. Read the Story and required comments, attachments, and related task content
   through [Jira read policy](../staff/references/jira-read-policy.md). Use `acli`
   outside the sandbox for metadata discovery. Follow
   [Appier conventions](references/appier-jarvis.md) when the work belongs to Jarvis.
3. Build the acceptance record using
   [Confirm requirements](../staff/references/implementation-scope.md#confirm-requirements).
4. Use [Planning tools](references/planning-tools.md) to trace the affected code
   and resolve design questions. Verify the Story's named fields,
   symbols, contracts, existing patterns, and registration points against code.
   Record repository, branch or revision, paths, and symbols. Use line numbers
   only with that revision. Mark unavailable repositories as evidence gaps.
5. Survey linked and sibling tasks before proposing new work. Read their content
   through the same Jira policy. Distinguish covered, partial, and uncovered AC.
   Choose FE, BE, QA, or another owner from the actual gap, without a default role.
   When the substantive work is covered, report that result rather than inventing
   a task in another role.

## Grill requirements and design

Examine the affected inputs, states, defaults, empty and error behavior,
permissions, compatibility, shared consumers, persistence, and cross-team
dependencies where they affect this Story. Identify side effects beyond its
named screen or endpoint. Check contradictions among AC, comments, designs,
API contracts, and current behavior.

Resolve observable facts yourself. For unresolved product intent, present the
concrete competing outcomes and ask one focused question at a time. Record the
answer and its source. Continue independent work while dependent scope remains
open. Do not turn an assumption into an approved requirement or a code-ready task.

## Draft the breakdown

Split work by independently acceptable outcomes and real ownership or dependency
boundaries. Keep coupled work together when splitting would leave no usable
result. Account for each in-scope AC with an existing task, proposed task, or
evidence that the behavior is already satisfied. Explain deliberate exclusions
and dependencies between tasks.

Use [Breakdown format](references/breakdown-format.md) for the review package.
Draft each task using [Task description](../create-jira-ticket/references/task-description.md)
and [Implementation plan](../create-jira-ticket/references/implementation-plan.md).
For revisions, apply [Dated updates](../create-jira-ticket/references/dated-updates.md).
Keep ticket text and plan detail in their respective destinations.

Mark a task ready for publication review when its AC, code entry points, and
dependencies are established, with no open decision blocking acceptance or
execution. Keep blocked proposals marked as drafts. Return the package to the
caller, or present it directly when invoked standalone.
