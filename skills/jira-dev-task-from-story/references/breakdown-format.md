# Story breakdown review format

Keep the review package in the caller's task archive and reuse its acceptance
record. Show full proposed descriptions and comments for publication approval.
Link supporting investigations and designs. Omit empty sections.

```markdown
## Story scope and decisions

Confirmed outcomes, material boundaries, clarifications, and source pointers.

## AC coverage

| Story AC | Outcome | Existing task, proposed task, or baseline evidence | Dependency or open decision |
| --- | --- | --- | --- |

## Proposed tasks

For each task: title, owner or role, proposed Jira metadata and Story
relationship, numbered functional AC in the description, and implementation plan comment.

## Side effects and ordering

Cross-task dependencies, affected shared consumers, compatibility or rollout
constraints, and implementation order.

## Open decisions

Concrete unresolved choices, who must decide them, and which tasks they block.

## Planning evidence

Repositories and inspected revisions, code entry points, source pointers,
and workflows used with their conclusions or pending requirements.
```

Label confirmed facts, owner decisions, assumptions, and blocked task drafts.
