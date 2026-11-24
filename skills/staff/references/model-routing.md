# Model routing

Read this file before choosing a delegated worker's model or reasoning effort.
Skills name workflow roles and link here instead of copying model IDs, effort
levels or model pools. Resolve the route here, then apply
[Subagent routing](subagent-routing.md) for host controls and access.

## Routes

| Route | Agent kind | Model | Reasoning effort |
| --- | --- | --- | --- |
| `gpt-6-luna-extra-high` | codex | `gpt-6-luna` | `xhigh` |
| `gpt-6-luna-high` | codex | `gpt-6-luna` | `high` |
| `gpt-6.1-sol-medium` | codex | `gpt-6.1-sol` | `medium` |
| `gpt-6.1-sol-high` | codex | `gpt-6.1-sol` | `high` |
| `gpt-6.2-sol-medium` | codex | `gpt-6.2-sol` | `medium` |
| `claude-opus-5.5-high` | claude | `claude-opus-5-5` | `high` |
| `claude-opus-5.5-med` | claude | `claude-opus-5-5` | `medium` |

Use the model and effort as separate native tool parameters. For CLI arguments,
Codex uses `-m <model> -c model_reasoning_effort="<effort>"`; Claude uses
`--model <model> --effort <effort>`. A route label is not a model ID.

## Workflow roles

| Workflow / role | Route or pool |
| --- | --- |
| Default code work | `gpt-6-luna-extra-high` |
| Exploration, general code review | `gpt-6.1-sol-medium` |
| how explorers; why investigators | `gpt-6.1-sol-medium` |
| how explainer; why synthesizer | `claude-opus-5.5-med` |
| Jira Story planner | `claude-opus-5.5-high` |
| Jira Story plan reviewer | `gpt-6.2-sol-medium` |
| recall history workers | `gpt-6.1-sol-medium` |
| no-comments Comment Sicko | `gpt-6.1-sol-medium` |
| ss-simplify-code reuse and efficiency reviewers | `gpt-6.1-sol-medium` |
| architect candidate pool | `gpt-6.1-sol-high`, `claude-opus-5.5-high` |
| interrogate Reviewer A | `gpt-6.1-sol-high` |
| interrogate Reviewer B | `claude-opus-5.5-high` |
| arena default runners and cross-judge pool | `claude-opus-5.5-med`, `gpt-6.1-sol-high`, `claude-opus-5.5-high` |
| AC self-verification and report work | `gpt-6-luna-high` only |

AC self-verification's route covers verification, report preparation and GCS
upload. If the exact model or effort is unavailable, leave that work pending.

For other workflows, preserve their required independence, model diversity and
fallback rules. An explicit user route takes precedence over defaults. A task
configuration may override defaults only where its workflow supports that input.
These are requested routes, not availability claims. Check host support before
launch; do not silently downgrade required work.

## Local code-review tiers

For ss-code-review, the orchestrator and `correctness-reviewer`,
`security-reviewer`, and `adversarial-reviewer` inherit the session model without
an override. Other personas and bundled local prompt assets use the platform's
balanced mid-tier model. In Claude Code this is the Sonnet class. In Codex,
request that tier only when the native dispatch primitive supports an explicit
model or custom-agent selector; otherwise inherit the session model. This is
ss-code-review's supported fallback, not a fallback for exclusive workflow routes.
Record the resolved selection for each reviewer and apply it on every dispatch.
Task wording alone cannot change the serving model.

## External review providers

The ss-code-review cross-model worker has a separate provider/intermediary
contract. Its executable defaults are maintained in the model/effort mapping in
[cross-model-adversarial-review.sh](../../ss-code-review/scripts/cross-model-adversarial-review.sh).
Use that mapping rather than the native-worker table above. The worker's
`route_model` and `route_effort` functions resolve requested provider settings;
existing checkout configuration and explicit user overrides retain precedence
under [Cross-model review](../../ss-code-review/references/cross-model-review.md).
Skills and references consult that mapping rather than duplicating its defaults.
This policy does not change permitted recipients or attest model independence.
