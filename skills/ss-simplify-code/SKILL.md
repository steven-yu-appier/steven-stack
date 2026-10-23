---
name: ss-simplify-code
description: "Delivery addon for behavior-preserving reuse of existing implementations and removal of redundant runtime work in settled code. Use before every steven-stack delivery, or when explicitly asked to simplify code."
---

# Delivery simplification

Run before every steven-stack delivery, including small fixes and local handoffs without a PR. Keep the settled design and behavior. A pass with no worthwhile findings is complete.

## Responsibility boundary

This addon owns two remaining opportunities: replacing newly duplicated implementation with an existing behavior-equivalent utility or built-in, and eliminating provably redundant runtime work or overly broad reads. It does not repeat the following work:

| Existing owner | Work excluded from this addon |
| --- | --- |
| [deslop](../deslop/SKILL.md) | Style, abnormal defensive checks, type-bypass casts, and nested-condition cleanup |
| [no-comments](../no-comments/SKILL.md) | Comment removal, suppression analysis, and refactors prompted by comment findings |
| [architect](../architect/SKILL.md) and [Refactoring](../staff/playbooks/refactoring.md) | State, parameter, type, module, and abstraction redesign; wrapper/dead-code removal; caller migrations and compatibility cleanup |
| [test-audit](../test-audit/SKILL.md) | Test-quality audits and removal of production interfaces used only by tests |
| [Perf issue](../staff/playbooks/perf-issue.md) and [Hillclimb](../staff/playbooks/hillclimb.md) | Performance diagnosis, profiling, tuning, concurrency changes, caching policy, and optimization experiments |
| The caller's verification phase | Final typecheck, lint, tests, runtime proof, and measurement |

These are ownership references, not instructions to launch those workflows again. Keep findings outside this boundary with their existing owner. Bugs, leaks, security defects, and contract changes are also outside this addon; report a material incidental defect to the caller rather than fixing it here.

## Step 1: Identify scope

For a delivery, the caller supplies the delivery's changed files or diff, settled behavior/structure constraints, and any completed cleanup or optimization findings relevant to this scope. An explicitly empty delivery scope means there is no code to simplify; do not substitute an unrelated dirty checkout. Read-only investigations have no mutation scope.

For a direct invocation, use the user's named scope first. Otherwise use the current branch versus its resolved base, including staged and unstaged changes; if no base is usable, use `git diff HEAD`. Outside git, use the files edited in this conversation. If no scope is available, report that there is nothing to simplify.

Documentation, generated/vendored code, lockfiles, dependencies, and purely mechanical changes produce a no-op result without reviewers. Mixed scopes retain substantive authored code, including agent-authored code. There is no size or cost exemption for a code delivery.

Use prior outcomes to avoid reopening accepted or rejected cleanup choices on unchanged code. A new code change can invalidate those outcomes. Preserve caller-supplied structure pins, including deliberate duplication or separation.

## Step 2: Review reuse and redundant work

Read both prompt assets in full and supply the resolved scope and constraints:

- [Code reuse reviewer](references/personas/code-reuse-reviewer.md)
- [Efficiency reviewer](references/personas/efficiency-reviewer.md)

Route both reviewers through [staff's subagent routing contract](../staff/references/subagent-routing.md) using `gpt-6.1-sol-medium`, with read-only access to the project. Launch them concurrently when supported and collect both terminal outcomes before applying anything. They return text; the parent saves any report. Do not grant writes just to save a report.

These are leaf review assignments. Give each child the Staff context required by the routing contract, plus its prompt asset, scope, constraints, and expected findings. Its success criterion is its assigned review only; it does not run a delivery, open a PR, invoke this addon recursively, or delegate another review.

Respect the host's active-agent cap. Capacity rejection leaves a pass queued. If the requested route or enforceable read-only access is unavailable, perform that pass inline with the same rubric and disclose the loss of independent review. Collect started agents' terminal outcomes before falling back. If a reviewer fails or returns unusable findings, complete that pass inline and report the substitution; a missing outcome is not a clean result. Use caller-owned cleanup only when the host supports it.

## Step 3: Apply supported findings

Deduplicate by change and fix. An existing-implementation replacement belongs to reuse; efficiency owns redundant execution that remains after reuse. Apply only findings inside this addon's responsibility boundary. Record false positives, previously resolved findings, and low-value changes as skipped.

Inspect surrounding code to establish equivalence, but edit only the resolved scope and its necessary import/export seams. For user-named files or directories, the seams must also be inside that boundary.

Preserve outputs, errors, side effects, observable call counts, ordering, identity, and resource lifetime. A repeated API call or file read is not redundant merely because the arguments match. Prove its observable behavior is unchanged, or skip it. Preserve trust-boundary validation, data-loss protection, security checks, and accessibility affordances. Do not replace serializers or coercions without evidence covering the relevant value types.

Reuse existing behavior pins and comparisons to establish a candidate's equivalence. This is evidence for accepting the change, not a second project-wide verification phase. Do not add abstractions, migrate APIs, thin guards, change scheduling, or redesign the settled structure to create a simplification opportunity.

## Step 4: Hand off verification

Return changed paths, accepted/skipped findings, equivalence evidence, and checks needed to the caller. The delivery workflow runs its final verification once after all cleanup mutations. Do not rerun the caller's typecheck, lint, test suite, control-surface verification, or performance measurement here.

For a direct invocation without a delivery owner, run the project's applicable checks for the changed scope before returning. Use the matching control skill or `verify-this` when a behavioral claim needs runtime proof. Report unavailable or blocked checks. Correct or revert only this addon's changes when verification fails; preserve other work and never weaken tests or types to pass.

## Step 5: Summarize

Report applied findings by reuse and redundant work, skipped findings, changed paths, and verification ownership. A delivery result is pending final verification until the caller completes it. If nothing changed, say so. Use reduced duplication or work as the outcome, not net lines removed.
