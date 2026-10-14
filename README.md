# Steven's Sstack

[Steven](https://github.com/steven-yu-appier) maintains this catalog of reusable
agent skills.

## Install

This repository packages its skills as the `steven-stack` plugin for both
Codex Desktop and Claude Code. It includes `plugin.json` and
`.codex-plugin/plugin.json` (Codex manifests), `.claude-plugin/plugin.json`
(Claude Code manifest), the workflows under `skills/`, and local marketplace
catalogs at `.agents/plugins/marketplace.json` (Codex) and
`.claude-plugin/marketplace.json` (Claude Code). No MCP server is bundled.

### Install in Codex Desktop

Run these commands in your terminal, replacing the path if your checkout lives
elsewhere:

```sh
codex plugin marketplace add /Users/steven.yu/Documents/steven-stack
codex plugin add steven-stack@steven-local
```

Restart Codex Desktop and open a new chat. Confirm that `steven-stack` appears
in the installed plugins and that its Staff skill is available. Select Staff
from the skill picker with your task; its plugin-qualified name is
`steven-stack:staff`.

The marketplace is named `steven-local`; its `./` source path resolves to this
repository root, rather than the `.agents/plugins/` directory.

#### Update after editing the skills

Codex loads an installed copy from its plugin cache. Remove and reinstall the
plugin after changing this checkout to refresh that copy:

```sh
codex plugin remove steven-stack@steven-local
codex plugin add steven-stack@steven-local
```

Restart Codex Desktop and test in a new chat so it loads the refreshed skills.

#### Uninstall

```sh
codex plugin remove steven-stack@steven-local
```

The marketplace can remain configured for a later reinstall. To remove it too:

```sh
codex plugin marketplace remove steven-local
```

See the [official plugin packaging and marketplace guide](https://developers.openai.com/plugins/build/plugins)
for distribution options and local marketplace behavior.

### Install in Claude Code

Run these commands in your terminal, replacing the path if your checkout lives
elsewhere:

```sh
claude plugin marketplace add /Users/steven.yu/Documents/steven-stack
claude plugin install steven-stack@steven-local
```

Reload plugins (`/reload-plugins`) or start a new session, then confirm
`steven-stack` appears with `claude plugin list`. Skills are available as
slash commands scoped to the plugin, e.g. `/steven-stack:staff`.

The marketplace is also named `steven-local` here; its `./` source path
resolves to this repository root, and the plugin manifest lives at
`.claude-plugin/plugin.json` rather than `.codex-plugin/plugin.json`.

#### Update after editing the skills

The local marketplace source points directly at this checkout, so edits are
generally picked up on the next reload. If a change doesn't show up, remove
and reinstall:

```sh
claude plugin remove steven-stack@steven-local
claude plugin install steven-stack@steven-local
```

#### Uninstall

```sh
claude plugin remove steven-stack@steven-local
```

The marketplace can remain configured for a later reinstall. To remove it too:

```sh
claude plugin marketplace remove steven-local
```

See the [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins/install) for
distribution options and local marketplace behavior.

## Start here

Invoke `/staff` in Claude Code or `$staff` in Codex with your task. Staff
matches the task to a playbook, loads the principles that apply, and delegates
work to subagents. You rarely call the other skills yourself.

## How it fits together

Staff is the entry point. Its playbooks call workflow skills and cleanup
passes. Workflows delegate through the routing contract using the host's native
subagent tool.

```mermaid
flowchart TD
    U(["/staff task"]) --> S[staff]
    S --> P["Playbooks<br/>investigation · bug-fix · perf-issue · hillclimb<br/>runtime-forensics · trace-forensics · feature · refactoring<br/>prototype · autonomous-run · session-pickup · worktree-cleanup · opening-a-pr"]
    S -. large or unusual task .-> F[figure-it-out]
    S --> PR["principle-* skills<br/>one rule each"]
    P --> W["Workflows<br/>how · why · architect · arena · interrogate · tdd"]
    P --> Q["Cleanup<br/>unslop · technical-writing · deslop · no-comments"]
    P --> A["Delivery addon<br/>ss-simplify-code"]
    P --> V["Verification<br/>control-ui · control-cli · verify-this"]
    W --> R["skills/staff/references/subagent-routing.md"]
    R --> N["Native subagent tool"]
```

### Example: `/staff login fails after restart`

```text
staff picks playbooks/bug-fix.md and copies its steps into a todo list
  loads principle-fix-root-causes and principle-prove-it-works
  1. reproduce the bug on the same surface (control-ui or control-cli)
  2. find the cause: how + why run as parallel subagents
  3. plan the fix (architect if it crosses a function boundary); a routed subagent implements it
  4. verify on the same surface as the repro
  5. commit the failing repro before the fix (tdd)
  6. deliver: ss-simplify-code, deslop, no-comments, final verification, PR writing
```

### Who can invoke a skill

Most skills set `disable-model-invocation: true`. They run only when you type
the slash command or another skill names them. This keeps principles out of
the context window until a task needs them.

| Invoked by                             | Skills                                                                                                                                                   |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You or another skill only              | Every skill not listed in the next row                                                                                                                   |
| Also chosen automatically by the model | `unslop`, `deslop`, `technical-writing`, `skill-audit`, `create-jira-ticket`, `post-pending-review-comments`, `pr-author-context-comments`, `test-audit`, `ss-code-review`, `ss-simplify-code` |

## Skills

### Entry point

- [`staff`](skills/staff/) applies the catalog's `principle-*` skills and routes work
  through the bundled
  [investigation](skills/staff/playbooks/investigation.md),
  [bug fix](skills/staff/playbooks/bug-fix.md),
  [perf issue](skills/staff/playbooks/perf-issue.md),
  [hillclimb](skills/staff/playbooks/hillclimb.md),
  [runtime forensics](skills/staff/playbooks/runtime-forensics.md),
  [trace forensics](skills/staff/playbooks/trace-forensics.md),
  [feature](skills/staff/playbooks/feature.md),
  [refactoring](skills/staff/playbooks/refactoring.md),
  [prototype](skills/staff/playbooks/prototype.md),
  [autonomous run](skills/staff/playbooks/autonomous-run.md),
  [session pickup](skills/staff/playbooks/session-pickup.md),
  [worktree cleanup](skills/staff/playbooks/worktree-cleanup.md), and
  [opening a PR](skills/staff/playbooks/opening-a-pr.md) playbooks.

### Workflows

Staff playbooks call these skills. You can also invoke them directly.

- [`architect`](skills/architect/) sketches types and module boundaries before
  implementation, then keeps the design in the implementation loop.
- [`arena`](skills/arena/) runs parallel candidates, selects a base, and combines the
  strongest parts into one verified result.
- [`figure-it-out`](skills/figure-it-out/) designs an auditable playbook for large
  migrations, ambitious multi-part changes, or work a human reviews after
  stepping away.
- [`how`](skills/how/) explains subsystem architecture and runtime flow through
  focused code exploration.
- [`interrogate`](skills/interrogate/) runs a multi-model adversarial code review and
  synthesizes the findings into a lead verdict.
- [`ss-code-review`](skills/ss-code-review/) reviews bugs, regressions, tests, and
  project standards with risk-selected reviewers and validated findings. It reports
  by default; `apply:local` explicitly authorizes local fixes. It remains standalone
  and is not called by Staff playbooks.
- [`ss-simplify-code`](skills/ss-simplify-code/) runs before every Staff delivery,
  including local handoffs without a PR. It reviews reuse and redundant runtime
  work while preserving the settled design and behavior.
- [`show-me-your-work`](skills/show-me-your-work/) records a reviewable TSV decision
  trail for long-running or unattended work.
- [`tdd`](skills/tdd/) runs a failing-test-first bug-fix workflow when a focused
  regression test is practical.
- [`why`](skills/why/) investigates the historical evidence behind code decisions and
  reports what is known, inferred, and still unknown.

### Delivery addon and standalone review

These two skills are adapted from Compound Engineering 3.24.0 and bundled here
with their prompt assets, schemas, and helper scripts. Neither requires the
Compound Engineering plugin or its other skills. Their steven-stack names are:

```text
$ss-code-review
$ss-code-review base:origin/main
$ss-code-review mode:agent
$ss-code-review apply:local
$ss-simplify-code
```

In the plugin picker, use `steven-stack:ss-code-review` and
`steven-stack:ss-simplify-code`. Reinstall steven-stack using the update commands
above and open a new chat to load these additions. You can then remove Compound
Engineering if you do not use its other skills.

Code review requires Python 3 for its bundled helpers. PR reviews use `gh`;
cross-model review optionally uses an installed peer CLI and falls back to the
local adversarial reviewer when no eligible peer is available. Simplification
hands final checks to the delivery owner after all cleanup; direct invocations
run applicable checks themselves. Both use native subagents when available,
with an inline fallback that reports lost independent coverage.

Every delivery invokes the simplification addon, regardless of code-change size.
Non-code scopes complete as a no-op. Its two reviewers look for existing
implementation reuse and provably redundant runtime work. Style and comments,
architecture/type redesign, test audits, and profiling/tuning stay with their
existing skills. The addon and the final verification are not repeated when
their relevant source and constraints are unchanged. Code review remains
standalone; this integration does not add it to delivery workflows.

Optional repository settings live in `.steven-stack/config.yaml` and
`.steven-stack/config.local.yaml`; neither file is required. `docs_root` defaults
to `docs` and is read only from `config.yaml`. Peer settings include
`cross_model_review_mode: off` to disable automatic external review,
`cross_model_peer`, `cross_model_model`, and `cross_model_effort`. The bundled
resolver also accepts optional `packs:` rule sources without requiring another
plugin. Existing `.compound-engineering/` configuration is not read; copy any
settings you want to keep into `.steven-stack/` yourself.

Review artifacts use a private `steven-stack-<uid>` temporary directory.
The upstream `CE_PEER_*`, `CE_PACKS_CACHE_ROOT`, and `CROSS_MODEL_*` environment
variable names and `ce-unified-plan/v1` input contract remain compatible.
Upstream attribution and the MIT license are in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

### Principles

Each principle skill holds one rule. Staff loads a principle when its
situation matches, and cites only the principles it read. The groups match the
sections in [`staff/SKILL.md`](skills/staff/SKILL.md).

**Core**

- [`principle-attack-the-premise`](skills/principle-attack-the-premise/) questions a
  shared premise after repeated fixes fail the same gate.
- [`principle-build-the-lever`](skills/principle-build-the-lever/) turns non-trivial
  work into a rerunnable script, generator, check, or skill.
- [`principle-exhaust-the-design-space`](skills/principle-exhaust-the-design-space/)
  compares concrete prototypes before committing to a novel design.
- [`principle-experience-first`](skills/principle-experience-first/) resolves product
  and implementation tradeoffs in favor of the user's experience.
- [`principle-foundational-thinking`](skills/principle-foundational-thinking/) puts
  data structures, shared-state decisions, and reusable setup first.
- [`principle-laziness-protocol`](skills/principle-laziness-protocol/) favors deletion,
  flat call paths, and the smallest sufficient change.
- [`principle-minimize-reader-load`](skills/principle-minimize-reader-load/) reduces
  indirection and the amount of mutable state a reader must track.
- [`principle-outcome-oriented-execution`](skills/principle-outcome-oriented-execution/)
  prioritizes a verified migration end state over temporary compatibility code.
- [`principle-redesign-from-first-principles`](skills/principle-redesign-from-first-principles/)
  integrates a new requirement as though it were part of the original design.
- [`principle-subtract-before-you-add`](skills/principle-subtract-before-you-add/)
  removes obsolete complexity before adding new behavior.

**Architecture**

- [`principle-boundary-discipline`](skills/principle-boundary-discipline/) keeps
  validation and error handling at system boundaries.
- [`principle-make-operations-idempotent`](skills/principle-make-operations-idempotent/)
  makes repeated or interrupted operations converge on one end state.
- [`principle-migrate-callers-then-delete-legacy-apis`](skills/principle-migrate-callers-then-delete-legacy-apis/)
  removes an internal legacy API in the same change that migrates its callers.
- [`principle-model-the-domain`](skills/principle-model-the-domain/) replaces scattered
  branches and shape assumptions with domain-specific structures.
- [`principle-separate-before-serializing-shared-state`](skills/principle-separate-before-serializing-shared-state/)
  removes shared write targets before adding concurrency controls.
- [`principle-type-system-discipline`](skills/principle-type-system-discipline/) uses
  types to exclude invalid states and expose unhandled variants.

**Verification**

- [`principle-fix-root-causes`](skills/principle-fix-root-causes/) traces symptoms to
  their source before changing code.
- [`principle-prove-it-works`](skills/principle-prove-it-works/) verifies completed work
  against the real artifact instead of a proxy.
- [`principle-sequence-verifiable-units`](skills/principle-sequence-verifiable-units/)
  breaks multi-step work into checked units and orders delivery as evidence.
- [`principle-test-behavior-not-implementation`](skills/principle-test-behavior-not-implementation/)
  tests observable results through the same interface that users call.

**Delegation**

- [`principle-guard-the-context-window`](skills/principle-guard-the-context-window/)
  limits unnecessary reads and keeps large payloads out of the main context.
- [`principle-never-block-on-the-human`](skills/principle-never-block-on-the-human/)
  proceeds with reversible work and reserves questions for genuine ambiguity.

**Meta**

- [`principle-encode-lessons-in-structure`](skills/principle-encode-lessons-in-structure/)
  replaces repeated instructions with enforceable mechanisms.

### Cleanup passes

- [`deslop`](skills/deslop/) removes AI-generated code patterns while preserving
  behavior and local style.
- [`no-comments`](skills/no-comments/) audits comments, removes accepted clutter, and
  reports constraints that need structural fixes.
- [`technical-writing`](skills/technical-writing/) applies Diátaxis, Google developer
  style, Simplified Technical English, and Global English to technical prose.
- [`typescript-best-practices`](skills/typescript-best-practices/) applies the catalog's
  type-system and boundary principles to TypeScript code.
- [`unslop`](skills/unslop/) removes common AI writing patterns while preserving the
  meaning and tone.

### Verification harnesses

Staff calls a control skill to reproduce a bug or check a change on the
surface that users see. You can also invoke these skills directly.

- [`control-cli`](skills/control-cli/) builds or reuses a local tmux or PTY harness to
  drive, inspect, and profile an interactive CLI or TUI.
- [`control-ui`](skills/control-ui/) builds or reuses a local browser or CDP harness to
  drive, screenshot, and profile a web, IDE, or Electron UI.
- [`verify-this`](skills/verify-this/) tests one falsifiable claim against a baseline
  and a treatment, then returns `VERIFIED`, `NOT VERIFIED`, or `INCONCLUSIVE`.

### Standalone tools

- [`bro`](skills/bro/) restates the last message in simpler language without jargon.
- [`create-jira-ticket`](skills/create-jira-ticket/) creates or updates concise Jira
  tickets from specs, related issues, pull requests, or user notes.
- [`post-pending-review-comments`](skills/post-pending-review-comments/) writes
  validated findings to an unsubmitted GitHub review and verifies the result.
- [`pr-author-context-comments`](skills/pr-author-context-comments/) explains
  non-obvious author decisions at their exact PR diff locations.
- [`recall`](skills/recall/) rebuilds your recent working context from Claude Code and
  Codex transcripts, live state, and the shared record.
- [`show-me`](skills/show-me/) explains the current topic with concise diagrams,
  code-shape sketches, and focused HTML artifacts.
- [`skill-audit`](skills/skill-audit/) reviews a skill's triggering, target mechanics,
  and instruction fitness without editing the skill.
- [`teach`](skills/teach/) runs `how` and `why` and combines their findings into one
  plain explanation of a change or subsystem.
- [`test-audit`](skills/test-audit/) gates new tests against a value bar and prunes
  low-value, duplicative, or implementation-coupled tests.

## Delegation requirements

`staff`, `how`, `why`, `arena`, and `interrogate` delegate work to other
agents. The [staff routing contract](skills/staff/references/subagent-routing.md)
selects the control method, the model route, the access mode, and the child
prompt.

```mermaid
flowchart LR
    Lead[Lead agent] -->|role + route| Routing{"subagent-routing.md"}
    Routing -->|"native tool honors model + access"| Native["Native subagent tool"]
    Routing -->|unavailable| Fallback["Optional work: the lead does it<br/>arena / interrogate: stop and name the missing route"]
```

Delegation requires a native subagent tool that supports the requested model,
reasoning effort, access mode, and working directory. If those controls are
unavailable, follow the routing contract's fallback.

Model access depends on the local provider configuration. Accepting a model setting
alone does not prove that a model can answer requests. When a route is
unavailable, `arena` and `interrogate` stop instead of replacing independent
review with the lead agent's own opinion.

## Sources

- `bro` comes from [Dillon Mulroy's X post][bro-x].
- `control-cli`, `control-ui`, `deslop`, and `verify-this` come from
  [Cursor's `cursor-team-kit` plugin][cursor-team-kit].
- `show-me` comes from [HumanLayer's skill catalog][humanlayer-show-me].
- `test-audit` comes from [OpenClaw's repository skills][openclaw-test-audit].
- `arena`, `architect`, `figure-it-out`, `how`, `interrogate`, `no-comments`,
  the `principle-*` skills, `recall`, `show-me-your-work`, `tdd`, `teach`, `technical-writing`,
  `typescript-best-practices`, `unslop`, and `why` come from
  [pstack's skill catalog][pstack-principles]. `recall` and `teach` come from a
  [later pstack revision][pstack-teach].

[cursor-team-kit]: https://github.com/cursor/plugins/tree/12d587dfb20741cafc376c42c696c5f6e2a64487/cursor-team-kit/skills
[bro-x]: https://x.com/dillon_mulroy/status/2079238358358778142
[humanlayer-show-me]: https://github.com/humanlayer/skills/blob/bba9d13ab34f0a87f1cc33df4dd196372393ddfc/plugins/show-me/skills/show-me/SKILL.md
[openclaw-test-audit]: https://github.com/openclaw/openclaw/blob/792907dce5f2264b79a92d96fb4d0bf1fbd6c5d2/.agents/skills/test-audit/SKILL.md
[pstack-teach]: https://github.com/cursor/plugins/tree/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack/skills
[pstack-principles]: https://github.com/cursor/plugins/tree/5bf2b1544db739998121a306340631963c2ff3de/pstack/skills
