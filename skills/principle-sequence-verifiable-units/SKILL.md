---
name: principle-sequence-verifiable-units
description: Sequences multi-step edits, migrations, commits, and PRs into independently verifiable units.
disable-model-invocation: true
---

# Sequence work into verifiable units

Order work as a sequence of small units, each ending in a state you can check, and don't advance until the current one is green.

Checking each unit identifies which change caused a failure. A reviewer can repeat those checks in delivery order.

**Execution.** In a sweep, migration, or any run of similar edits, verify each change before starting the next. For each unit, capture a known-good state, make one change, and run its check before proceeding. Rebase onto clean trunk first so every check measures against the real baseline. When a lever does the edits, the per-unit check is nearly free. Run it anyway.

**Delivery.** Stack commits and PRs in the order that proves the work. The canonical shape is the failing test first, then the fix on top. Other useful orders include deletion before restructuring, baseline capture before treatment, and setup before features. Make each commit independently usable and show how its check supports the result.

## Pattern
- Pick the smallest unit that ends in a check: an edit plus its test, or a commit that stands alone.
- Verify before advancing. Red to green per unit, never deferred to a final batch.
- Order the units so the sequence builds confidence on its own, for you while executing and for a reviewer reading the stack.

The sequencing complement to the **prove-it-works** principle skill, which keeps each check real, and the **build-the-lever** principle skill, which makes the per-unit check cheap.
