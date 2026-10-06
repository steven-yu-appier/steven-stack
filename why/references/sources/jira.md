# Jira tickets

## What this source contains

- Ticket descriptions explain features, bugs, requirements, and the problems they address.
- Comments record survey conclusions, product decisions, rejected approaches, clarifications, and follow-up work.
- Parent fields, epics, subtasks, and issue links connect broader requirements with implementation tasks, bugs, and dependencies.
- Linked Confluence pages, repository specs, PR discussions, Slack messages, and attachments may contain the detailed rationale.
- Status history, resolution, versions, and dates help place those decisions in time.

Ticket formats vary. Read the available content without requiring Goal or Acceptance Criteria sections.

## How to search it

Use the Jira connector and its supported search and fetch operations. Do not use browser or computer use when the connector is available.

1. **Fetch the referenced tickets.** Start with ticket keys in the supplied context. Read the description and comments, including any specifically linked comment.
2. **Search for related tickets.** Search by feature name, symbol, or business term. Try alternative wording and expand across projects when relevant.
3. **Follow ticket relationships.** Read parents, epics, and related issues for broader context. Check native Parent fields and custom `Parent-Child` links separately, including their direction.
4. **Read linked specifications.** Open relevant specs, Confluence pages, attachments, and other sources linked from descriptions or comments. Read the sections that explain the requirement or decision.
5. **Check decisions and timing.** Review comments and history for changed scope or rejected approaches. Use labels and release dates as context for the motivation.

## What good evidence looks like here

- An attributed statement that names the problem, affected user, or external constraint.
- A decision comment that selects an approach and explains the tradeoff.
- A survey result that links its conclusion to implementation tickets.
- A bug report with reproduction evidence and a verified connection to the earlier change.
- A dated scope change that explicitly replaces or defers a requirement.
- A linked spec or PR that supports the exact claim under investigation.

Treat titles, labels, status, and proximity in time as search clues. They do not establish motivation by themselves.

## Common pitfalls

- **The description predates the decision.** Read the result comments before treating an initial survey proposal as the chosen approach.
- **A custom issue link resembles a native parent.** Record both relationships as returned. Flag conflicting directions instead of silently repairing or interpreting them.
- **A later requirement becomes an invented historical reason.** Keep the original decision and subsequent scope change separate.
- **A concise ticket appears incomplete.** Follow its linked spec or decision comment before inventing missing requirements.
- **An attachment disappears in text conversion.** Preserve the attachment reference and inspect the original when relevant. Do not infer image content from a filename.
- **Incomplete retrieval.** Check connector responses for pagination and truncation. Fetch remaining relevant comments or history before concluding. Report unavailable content as a gap.
- **No result becomes proof of absence.** State the terms, sources, and period searched. Report missing access, incomplete history, and unread attachments separately.
- **Related work expands the task.** Keep dependencies and deferred work separate from the ticket's own requirements.

## What to return

For each relevant ticket:

- Ticket ID and title.
- Exact description or comment excerpt explaining the problem or motivation. Preserve the wording so the synthesizer can cite it.
- Labels, parent issue, project.
- Author, created date, closed date.
- Ticket URL, when available.
