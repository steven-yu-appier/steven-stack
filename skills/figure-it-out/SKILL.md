---
name: figure-it-out
description: Designs an auditable workflow for large migrations or multi-part changes. Use for /figure-it-out or when no narrower playbook fits.
disable-model-invocation: true
---
# Figure it out

When the task matches no playbook, design one. Before coding, write phases with hypotheses, verification criteria, and a decision log. Scale the checks to the risk, with more rigor when the risk is uncertain.

Use [Task files and cleanup](../staff/playbooks/task-artifacts.md) for the designed plan, current task record, scratch trail and handoff. Save the phase list as the archived plan; keep raw loop output in scratch.

## Start

Open a todolist whose first item is to read the Principles section of the **staff** skill. Then add the phases below as todos.
## Phase A: Frame

Before starting, state:

- The definition of done as a falsifiable predicate (the **prove-it-works** principle skill).
- Scope, quantified: rough units and effort, plus the blockers grounding surfaced.
- The required checks and evidence. Use stricter checks for irreversible changes or failures that affect many users. Use fewer checks for reversible, low-risk steps.

Present the framing and tradeoffs before committing to a long run. Reversible work proceeds (the **never-block-on-the-human** principle skill), but a multi-hour run earns one checkpoint.
## Phase B: Design the workflow

Decompose into atomic, independently-landable units. Resolve the riskiest unknown first. Scaffold and verification come before features (the **foundational-thinking** principle skill).
- Build the verification harness before the work, with the baseline captured from the pre-change state, so the check reads as "old value vs new value".
- For irreversible design decisions, run the **architect** skill (it runs **arena**). Skip it for mechanical work whose shape is already concrete. A second arena over a settled design is over-engineering (the **laziness-protocol** principle skill).
- Identify independent tasks to parallelize, and give each worker its own worktree or branch (the **separate-before-serializing-shared-state** principle skill). Limit workers to independent tasks.
- Write the designed phase list down. That list is what the human reviews.
Then execute the design. Add its steps to the todolist as concrete items, after the Phase C entry and before Phase D. Apply Phase C to each step and add its Phase D log row when it completes.
## Phase C: Run the loop

Each unit is an experiment. State the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced, revert it if it didn't.
Apply the **sequence-verifiable-units** principle skill, verifying each unit before starting the next instead of batching checks at the end.
- Verify by inspecting the artifact, never a self-report. When something passes too easily, suspect the observation method before the system.
- Pair delegated work with a judge and audit the delegates' artifacts yourself before trusting them. If a worker games the gate, reset and harden the contract. If the gate itself is wrong, fix the gate in its own change rather than routing around it.
- A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Don't hide a negative.
## Phase D: Keep the audit trail

Log the run via the **show-me-your-work** skill, one canonical TSV with a row per decision and per unit, evidence as links. Keep the working trail in task scratch and summarize durable decisions in the archived task record. Retain or commit the full trail only when explicitly requested. Prefer evidence produced by committed scripts. The log and diff must let the human check each decision.
## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. Encode any recurring correction as a gate, a lint rule, a check, or a script (the **encode-lessons-in-structure** principle skill).

**Reply:** the playbook you designed, the rigor level and why, the archived task record with its decision summary, what's verified against the predicate, and what's still open. Link a full decision trail only when it was explicitly retained.
