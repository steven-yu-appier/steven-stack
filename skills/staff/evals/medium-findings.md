# Medium finding regression checks

Validated on 2026-10-16 against baseline `d4a71d7`. Scope is executable home paths, evidence reuse during session pickup, and delivery-rule/reference consolidation.

## Executable examples

The baseline Jira command contains shell redirection tokens in its user-path placeholder. After revision, the two marketplace-add examples and Jira executable line were run through zsh with harmless CLI stubs and a fixture home/output directory containing spaces. Only the home-variable name was substituted with a fixture variable; the real `HOME` was unchanged. All three commands delivered the expected argument list. No actual Codex, Claude, or Jira operation ran in these fixture checks.

## Instruction walkthroughs

These are manual rule traces, not independent model executions.

| Input | Required revised decision |
| --- | --- |
| Prior evidence names the artifact, revision, environment, and unchanged requirements. | Reuse that coverage and resume pending work. |
| Prior agent says “done” but provides no artifact evidence. | Verify the missing claims on the real artifact. |
| One requirement or relevant source/environment changed. | Refresh affected coverage and preserve applicable results. |
| Current evidence already satisfies the original goal. | Report completion without repeating the task. |
| Local code handoff or PR delivery. | Follow the same Delivery addon section; reuse its result only while scope and constraints remain unchanged. |
| Non-code delivery or review-only assignment. | Non-code addon is a no-op; review-only assignments skip delivery addons. |

The addon trigger now links to its single detailed policy in Opening a PR. Staff directly links every file in `references/`, plus the commit format. Local target and anchor checks passed. The acceptance/source, Figma, backend-selection, and preview rules were retained. This revision changes no runtime implementation; simplification is a documentation-only no-op and no new tests were added.
