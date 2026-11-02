---
name: create-jira-ticket
description: Use when you need to create or update concise implementation tasks, feature or story tickets, direction-setting surveys, or cleanup tickets from specs, related Jira issues, pull requests, or user notes under Appier Jira conventions.
---

# Create or update Jira tickets

Draft or publish the requested Jira changes. Staff coordinates engineering-task
publication through [Jira task creation and updates](../staff/playbooks/jira-task.md).
For an unresolved Story breakdown, use **jira-dev-task-from-story** before drafting
publication-ready tasks.

Use [Task files and cleanup](../staff/playbooks/task-artifacts.md) for local drafts
and payloads. Reuse the caller's task archive and scratch paths when supplied.

## Prepare a reviewable change

1. Gather the spec, acceptance record, owner decisions, code findings, and related
   issues. Read Jira content through
   [Jira read policy](../staff/references/jira-read-policy.md). Resolve project,
   issue type, title, assignee, labels, sprint, and relationships from the request
   and observed conventions. A breakdown task stays a Task unless another type
   was requested or verified as the team's convention.
2. Load the formats for the requested output:
   - Engineering-task descriptions: [Task description](references/task-description.md).
   - Implementation plan comments: [Implementation plan](references/implementation-plan.md).
   - Checklist or plan revisions: [Dated updates](references/dated-updates.md).
   - Product Stories, surveys, and other ticket types: [Other ticket formats](references/ticket-formats.md).
   - Story links or hierarchy changes: [Issue linking](references/issue-linking.md).
3. Apply **technical-writing** and **unslop**. Preserve requirement sources, exact
   identifiers, confirmed constraints, and the distinction between decisions and
   assumptions. Put repo-relative paths in published plans.
4. Present the complete proposed text, plan comment, and metadata for review.
   Publish only the user-authorized issue set and changes. Reuse approval of a
   reviewed breakdown without asking again. Exploratory or draft-only requests
   stop with the draft. A named reference ticket is a formatting source, not a
   target to update.

## Publish and verify

Follow [Jira CLI operations](references/jira-cli.md). Use `acli` outside the
sandbox for metadata and writes, and canonical jarkdown content for reads.

Before replacing a description or comment, inspect its current content and
required rich-text representation. Preserve unrelated text, checklist state,
links, existing date styling, and media outside the authorized changes.
Every existing image, video, attachment, and embed is protected. Text approval
does not authorize moving, converting, removing, or replacing media. If the
available representation cannot preserve protected content, leave that write
pending and provide the proposed text. Do not retry through a lossy format.

Select an implementation plan comment by an explicit comment ID or an
unambiguous matching plan owned by the relevant author. Reuse that comment
instead of creating duplicates. If several candidates exist, resolve the target
before editing. Preserve other comments and the plan's visibility.

After writes, refresh the canonical snapshot and verify descriptions and plan
content there. Verify comment IDs, metadata, and link direction through `acli`.
Check rich-text date marks and checklist state in canonical ADF when available.
For media-bearing updates, require verification of media count, identity, order,
and placement. Missing or transformed media is a failed update.

Report issue links, plan comment IDs, verified changes, and any pending operation.
If only part succeeds, retain the created keys and completed operations so a
retry resumes without duplicating tickets, comments, or links.
