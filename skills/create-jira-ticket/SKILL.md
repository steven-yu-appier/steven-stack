---
name: create-jira-ticket
description: Use when you need to create or update concise implementation tasks, feature or story tickets, direction-setting surveys, or cleanup tickets from specs, related Jira issues, pull requests, or user notes under Appier Jira conventions.
---

# Create Jira ticket

## Workflow

1. Gather source material before writing:
   - Read the provided spec, comments, PR links, screenshots, and related Jira issues.
   - If the user references an existing Jira ticket as the format example, fetch it and mirror its section style.
   - Confirm assignee/project only when not provided and not inferable from context.

2. Scope the ticket tightly:
   - Identify which repos/apps are in scope, but state them only when doing so materially clarifies ownership or boundaries.
   - State related repos/apps as out of scope only when the source spec is broader or scope leakage is likely.
   - Group implementation bullets by repo/app when ownership is split.

3. Choose the smallest ticket structure that preserves the decisions needed to execute and accept the work:
   - Default to `Goal` and `Acceptance Criteria`, including for stories and surveys when those sections are sufficient.
   - Treat every other section as optional. Add one only when it preserves a confirmed decision, material boundary, or required evidence.
   - Add `Out of Scope` only when plausible adjacent work would otherwise create ambiguity.
   - Add sources only when they materially explain or trace a requirement.
   - Prefer the section style and density of a related Jira example when one is provided; do not copy headings that carry no decision for the new ticket.
   - For a substantial feature, story, or survey ticket, read [references/ticket-formats.md](references/ticket-formats.md) and use only the relevant format.

4. Rewrite the ticket by content.
   - For tickets with technical requirements, constraints, or validation instructions, use the **technical-writing** skill. Treat the ticket as reference documentation.
   - For titles, goals, product context, and other non-technical prose, drop the jargon and write simply and concisely, like one human talking to another.
   - For mixed content, let technical precision win. Preserve exact technical names, identifiers, paths, commands, persisted values, legal strings, and evidence links. Preserve the distinction between confirmed decisions and assumptions.

5. Create or update the Jira issue:
   - Use issue type `Task` unless the user requests another type.
   - Use issue type `Story` for feature/user-facing delivery tickets when the referenced example uses `Story` or the requested scope is clearly a product story.
   - Use the requested project key, or infer it from the referenced ticket key.
   - Assign the ticket when the user names an assignee; look up the account ID if needed.
   - Before updating an existing description, inspect it for images, videos, attachments, and other embedded media. Treat every existing media item as protected content.
   - Do not edit, remove, replace, re-upload, relink, reorder, resize, or convert protected media unless the user explicitly approves that media change. Approval to edit ticket text does not approve media changes.
   - Make a text-only update only when the operation preserves every media node unchanged. If the available tool rewrites the full description, converts its format, cannot round-trip the media, or cannot guarantee preservation, stop and ask for approval or provide the proposed text without publishing it.
   - After updating a description that contains media, verify that the media count, order, identity, and placement are unchanged. Treat truncation, missing content, transformed media URLs, and lost embeds as a failed update. Do not retry through another lossy representation.
   - Return the created Jira key and link.

6. When Jira issue links are requested, read [references/issue-linking.md](references/issue-linking.md) before creating them. Verify the resulting direction because the available connector may not expose deletion.

## Writing rules

- Keep tickets outcome-oriented and acceptance-criteria driven, not a full spec dump.
- Write the goal as one sentence. Prefer one-line bullets and plain user-facing language.
- State what must be true when the ticket is complete. Let the owning team choose architecture, schemas, endpoints, storage, internal components, and other implementation details unless the user confirmed them as requirements.
- Prefer user-observable behavior over exhaustive implementation coverage. Include internal details only when they constrain delivery, ownership, compatibility, or acceptance.
- Keep one completion condition per acceptance-criteria bullet. Remove bullets that repeat the goal or another criterion; do not enforce a minimum number of criteria.
- Express security, permissions, and compatibility as observable invariants rather than solution suggestions when the implementation is intentionally delegated.
- Use exact file paths, persisted values, legal strings, identifiers, and command names where relevant.
- Preserve evidence links for decisions from Jira comments, Slack, PRs, or screenshots.
- Put an uncertain dependency in `Assumptions` only when it could invalidate the ticket; otherwise omit it.
- Use repo names or repo-relative paths rather than machine-specific paths.
- Do not include unrelated sections unless the user asks for them.
- Before publishing, compress the draft: remove restatements, speculative edge cases, unnecessary qualifiers, and sentences that do not affect implementation, acceptance, or scope.

Before creating or updating a ticket, check:

1. Can any section be removed without losing a decision?
2. Does every acceptance criterion affect whether the ticket can be accepted?
3. Does any bullet prescribe implementation when only the outcome matters?
4. Is the same requirement repeated across the goal, scope, and acceptance criteria?
5. Is `Out of Scope` limited to plausible adjacent work?
6. Can any sentence or heading be removed without changing implementation, acceptance, scope, or traceability?
7. Does the issue contain protected media, and can this exact update preserve every media item without changing it?
