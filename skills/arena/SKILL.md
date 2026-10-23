---
name: arena
description: Combines independent candidate solutions for one task. Use for /arena or when competing designs need comparison.
disable-model-invocation: true
---

# Arena

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Integrate useful ideas from the other candidates. Verify the synthesized result.

Route every delegate through [`../staff/references/subagent-routing.md`](../staff/references/subagent-routing.md). Arena requires independent workers. If a required route is unavailable, stop and report it.

Read [Task files and cleanup](../staff/playbooks/task-artifacts.md) before assigning output paths. Reuse the caller's task paths. Candidate reports and rejected sketches are scratch; put the selected plan and useful screenshots in the archive and condense the synthesis decision into the task record. Retain a full candidate package only when explicitly requested.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

Give all N candidates the same task prompt.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. Use the rubric in Phase D. Candidates only see the task.
3. Pick the runners. Default to one each on `claude-opus-5.5-med`, `gpt-6.1-sol-high`, and `claude-opus-5.5-high`. Launch more when the arena covers multiple design directions. Use the same route N times when the work is generation-bound rather than judgment-sensitive.
4. Assign output paths. Each candidate writes to its own location (a git worktree where possible, otherwise `<task-scratch>/arena/candidate-<n>/`), per the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

Launch all N candidates before waiting for any candidate. Give each the task, the path to the shared grounding, its own output path, and instructions to produce both the artifact and a short rationale.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After all Phase B candidates complete, choose one route from the default cross-judge pool. The pool contains `claude-opus-5.5-med`, `gpt-6.1-sol-high`, and `claude-opus-5.5-high`. Prefer a different model family from the parent's. Launch one read-only judge on that route. It sees the rubric and the candidates by path label, scores each criterion, and recommends a base with rationale. It runs in parallel with the parent's reading in Phase D, not with the candidates themselves. Don't launch the judge while candidates are still writing.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against every rubric criterion. Compare against the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Integrate each selected idea by hand, per the **redesign-from-first-principles** principle skill. Don't paste mechanically. Keep the combined design consistent.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. If candidates differ too much to compare against the rubric, clarify Phase A and rerun.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **prove-it-works** principle skill.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Resolve the cause before returning.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.
