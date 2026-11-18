---
name: verify-this
description: Tests an acceptance claim or before/after improvement against fresh evidence. Use for verification requests, before-and-after comparisons, or proof that a fix works.
disable-model-invocation: true
---

# Verify this

Prove or disprove a specific claim with repeatable evidence.

## When to use

- The user asks "verify this", "prove it works", "did this fix it", or "show me the evidence".
- A bug fix needs a before/after repro.
- A UI, CLI, API, performance, or memory claim needs measurement.
- A test passes but the user-visible behavior still needs confirmation.

Do not use this for vague claims like "the code is cleaner". Ask for a measurable claim first.

## Workflow

1. Restate the claim in falsifiable form: conditions and observable expected result, or a metric and threshold for a measured improvement.
2. Choose the smallest local test or interaction that can disprove it.
3. For a comparison, use the caller's specified baseline; otherwise resolve the old state from the merge base, parent commit, failing branch, or broken repro. An acceptance claim may be checked against its expected result without a baseline. Capture Before when the caller requires it.
4. Exercise the tested state. For a comparison, match command, data, warmup and environment to the baseline. Record the tested revision, role and coverage mode.
5. Honor the caller's required evidence format and per-claim mapping when
   collecting and returning evidence. Missing required captures stay explicitly
   incomplete even when observations establish a behavioral verdict. For AC
   self-verification, take the screenshot contract from the caller; supplementary
   text, API responses, test output or generated visuals cannot satisfy it.
6. Compare raw artifacts: numbers, screenshots, terminal transcripts, HTTP responses, profiles, heap snapshots, or test output.
7. For UI claims whose backend is unavailable or outdated, use **control-ui**'s [API response interception](../control-ui/references/api-response-interception.md). Report intercepted FE coverage and pending live integration separately.
8. Return exactly one verdict: `VERIFIED`, `NOT VERIFIED`, or `INCONCLUSIVE`.

## Local surfaces

- Code behavior: focused unit/integration tests or a minimal repro script.
- CLI/TUI behavior: `control-cli`, terminal transcript, or demo recording.
- UI behavior: `control-ui`, screenshots, accessibility snapshots, or browser traces.
- API behavior: local HTTP/RPC request and response diff.
- Performance: same-machine baseline/treatment timings or CPU profiles.
- Memory: heap snapshots before and after the suspected operation.

## Artifact layout

Read [Task files and cleanup](../staff/playbooks/task-artifacts.md) before writing artifacts, including standalone use. Capture raw baseline, treatment and comparison output in scratch:

```text
<task-scratch>/verify-this/<claim-slug>/
├── claim.md
├── timeline.md
├── baseline/
├── treatment/
├── diff/
└── verdict.md
```

If artifacts may contain sensitive code, prompts, screenshots, HTTP bodies, or heap data, keep only the minimal inline evidence unless the user agrees to disk storage.

Before cleanup, put the claim, measured result and limitations in the archived task record and useful screenshots in its screenshot directory. Preserve additional raw artifacts only when they are necessary deliverables. The task owner finishes cleanup after consuming this verdict.

## Verdict rules

- `VERIFIED`: the exercised state meets the acceptance claim, including preserved behavior, or the comparison meets its claimed threshold with no obvious confound. Equal Before/After can verify an unchanged acceptance requirement; it cannot establish a claimed improvement.
- `NOT VERIFIED`: the exercised state contradicts the acceptance expectation, or a claimed improvement is unchanged, moves the wrong way, or misses its threshold.
- `INCONCLUSIVE`: missing evidence, a missing required baseline, noisy signal, failed measurement, or an environment difference prevents the claim from being decided. Intercepted responses establish only the exercised FE behavior, not live backend authorization or persistence.

## Output

Use this shape:

```text
VERIFIED | NOT VERIFIED | INCONCLUSIVE
Claim: <falsifiable claim>

Evidence:
<artifact/observation>: expected=<...>, observed=<...>
<for comparisons>: baseline=<...>, treatment=<...>, delta=<...>, threshold=<...>
Coverage: <live / intercepted / mixed; tested revision, role and limitations>
Required evidence: <complete / incomplete; mapped capture paths and provenance, or missing states/reasons>

Reasoning:
<one tight paragraph naming the evidence and any confounds>
```

State `NOT VERIFIED` plainly when the evidence rejects the claim.
