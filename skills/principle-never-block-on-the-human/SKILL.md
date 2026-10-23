---
name: principle-never-block-on-the-human
description: Guides autonomous decisions on reversible work and confirmation for irreversible actions.
disable-model-invocation: true
---

# Never block on the human

The human supervises asynchronously. Agents must stay unblocked. Make reasonable decisions, proceed, and let the human course-correct after the fact.

Every permission pause delays work until the human responds. Since code changes are reversible and reviewable, a wrong decision usually costs less than blocking.

## Pattern
- **Proceed, then present.** Complete reversible work within the requested scope, then show the result and explain the decision.
- **Reserve questions for genuine ambiguity.** Ask only when you cannot infer intent from context.
- **Make the system self-healing.** When you notice a problem, log it and fix it in the next round.
- **Supervision is async.** Design workflows for review-after-the-fact.

## Boundaries
- **Irreversible actions** (force-push, delete production data, send external messages) still require confirmation.
- **Reversible actions** (write code, edit notes, split tasks) should proceed without blocking.
- **Product direction** comes from the human. *Execution* should not block.
