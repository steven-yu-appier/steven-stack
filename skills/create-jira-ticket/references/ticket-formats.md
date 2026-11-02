# Other ticket formats

Engineering tasks use [Task description](task-description.md) and put their
implementation plans in comments. The formats below apply to product Stories,
surveys, and other non-engineering-task tickets. Read only the matching section.
These are section menus, not mandatory outlines. Default to `Goal` and
`Acceptance Criteria`; add a section only when it preserves a confirmed decision,
material boundary, or required evidence.

## Contents

- [Feature or story](#feature-or-story)
- [Survey or direction-setting ticket](#survey-or-direction-setting-ticket)

## Feature or Story

Use for substantial user-facing or multi-team delivery when product, UX, runtime, release, or ownership decisions must be recorded.

```markdown
## Goal

One concise outcome statement describing what must ship and for whom.

## Product Scope

The minimum user workflow and material product boundaries. Omit when the acceptance criteria already make them clear.

## Acceptance Criteria

- Non-overlapping, observable completion conditions. Add capability subheadings only when the list would otherwise be difficult to scan.

## Out of Scope

Only plausible adjacent work that must be explicitly excluded.

## Follow-up Scope

Only confirmed follow-up work whose dependency on this story matters now.

References: Include only evidence needed to explain or trace a decision.
```

Optional sections:

- `Product Scope`: Use only when the workflow or boundary is not clear from the goal and acceptance criteria.
- `UX Decisions`: Use only when several confirmed interaction decisions must be preserved separately; otherwise express observable behavior in acceptance criteria.
- `Out of Scope`: Use only to prevent likely scope leakage.
- `Follow-up Scope`: Use only for known work that depends on this story's foundation.
- `Release Validation`: Use only when release-specific or cross-platform checks are part of accepting the story.
- `References`: Preserve screenshots and links that trace confirmed decisions; do not summarize them again without need.

## Survey or Direction-Setting Ticket

Use when the deliverable is evidence and a recommendation rather than implementation.

```markdown
## Goal

One concise decision outcome for the survey.

## Survey Scope

The few questions that must be answered and the relevant product or system boundary.

## Acceptance Criteria

- Observable evidence required to make the decision, plus the recommendation, material tradeoffs, and blockers.

## Out of Scope

Only adjacent implementation or investigation that could reasonably be mistaken as part of the survey.

References: Include only sources needed to conduct or trace the survey.
```

Optional sections:

- Split `Survey Scope` into `UX Questions` and `System Questions` only when both lists are substantial and independently owned.
- Add `Candidate Directions` only when named alternatives must be compared.
- Add `Expected Recommendation` only when its deliverable is not already clear from the goal and acceptance criteria.
- Add `Follow-up Scope` only when follow-up work is already known and materially depends on the survey.
