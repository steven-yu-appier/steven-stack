# Story and survey formats

For engineering tasks, use [Task description](task-description.md) and a separate
[Implementation plan](implementation-plan.md). For the ticket types below, start
with `Goal` and `Acceptance Criteria`; add only sections needed for a confirmed
decision, material boundary, or required evidence.

## Feature or story

```markdown
## Goal

What must ship and for whom.

## Acceptance Criteria

- Observable, non-overlapping completion conditions.
```

| Add section        | When needed                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| Product Scope      | The minimum workflow or boundary is unclear from the goal and AC.                                     |
| UX Decisions       | Several confirmed interaction decisions need a separate record. Otherwise express the behavior in AC. |
| Out of Scope       | Adjacent work is likely to be mistaken for part of this ticket.                                       |
| Follow-up Scope    | Confirmed follow-up work depends on this story.                                                       |
| Release Validation | Release-specific or cross-platform checks are part of acceptance.                                     |
| References         | Screenshots or links trace a decision. Preserve the evidence without repeating its contents.          |

Add capability subheadings to AC only when they make a long list easier to scan.

## Survey or direction-setting ticket

Use when the deliverable is evidence and a recommendation.

```markdown
## Goal

The decision this survey must support.

## Acceptance Criteria

- Evidence needed to make the decision.
- A recommendation with material tradeoffs and blockers.
```

| Add section                     | When needed                                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Survey Scope                    | The questions or investigation boundary are unclear from the goal and AC.                              |
| UX Questions / System Questions | Both question sets are substantial and independently owned. Use them instead of a single Survey Scope. |
| Candidate Directions            | Named alternatives must be compared.                                                                   |
| Expected Recommendation         | The required deliverable is unclear from the AC.                                                       |
| Out of Scope                    | Adjacent implementation or investigation could be mistaken for survey work.                            |
| Follow-up Scope                 | Confirmed follow-up work depends on the survey.                                                        |
| References                      | Sources are needed to conduct the survey or trace a decision.                                          |
