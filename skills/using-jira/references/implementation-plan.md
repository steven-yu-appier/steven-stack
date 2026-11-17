# Implementation plan comment template

Fill the template with verified implementation context. Keep only applicable
sections. A blocking open decision keeps the plan a draft.

```markdown
## Implementation plan

### Sources and baseline

<Story and task AC references, confirmed clarifications, target repositories,
and inspected branch or revision. Required base branch when relevant.>

### Contracts and constraints

<Inputs, outputs, persisted values, state distinctions, compatibility
requirements, and non-obvious design decisions.>

### Changes

1. <Repo-relative file and symbol>: <verified current behavior, required change,
   and existing pattern to reuse>. Covers <task AC group and item number>.
2. <Next change in dependency order, including necessary registration points
   and affected consumers>. Covers <task AC group and item number>.

### Dependencies and side effects

<Prerequisite task keys, shared interfaces, other owners, rollout constraints,
and affected flows outside the immediate entry point.>

### Verification

<Observable scenarios tied to task AC, with relevant inputs or actions and
expected results. Scoped commands verified against the repository's runner
configuration. Distinguish proposed checks from observed results.>

### Open decisions

<Unresolved decisions, their owner, and the work each blocks.>
```

Include line numbers only with the inspected revision. Before giving verification
commands, read [Scoped checks](../../staff/references/scoped-checks.md).

For revisions, use the explicit comment ID or an unambiguous matching plan owned
by the relevant author. Resolve multiple candidates before writing. Update that
same comment using [Dated updates](dated-updates.md), preserving its visibility
and other comments. Replace obsolete instructions and retain reasons that explain
current choices.
