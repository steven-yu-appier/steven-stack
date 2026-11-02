# Implementation plan comment format

Write the implementation plan as a comment with enough verified context for an
agent to begin work. Include applicable sections and identify open decisions.

```markdown
## Implementation plan

### Sources and baseline

Story and task AC references, confirmed clarifications, target repositories,
and inspected branch or revision. Name a required base branch when it matters.

### Contracts and constraints

Inputs, outputs, persisted values, state distinctions, compatibility requirements,
and behavior that must remain true. Explain non-obvious design decisions.

### Changes

1. Name the repo-relative file and symbol, its verified current behavior,
   the required change, and the existing pattern to reuse.
2. Continue in dependency order. Cover necessary registration points and
   affected consumers. Map the changes to the task's AC.

### Dependencies and side effects

Prerequisite task keys, shared interfaces, other owners, rollout constraints,
and affected flows outside the immediate entry point.

### Verification

Observable scenarios tied to AC, plus scoped commands when verified against
the repository's runner configuration. Distinguish proposed checks from results.

### Open decisions

Decisions still needed, their owner, and the work they block. Omit this section
when none remain. A blocking open decision makes the plan a draft.
```

Use paths and symbols as durable anchors. Line numbers supplement them only with
the inspected revision. Identify missing fields or contracts as prerequisites,
rather than inventing them. Distinguish planned edits, behavior already satisfied
by code, and observations still needed.

Read [Scoped checks](../../staff/references/scoped-checks.md) before recommending
verification commands. Separate past results from planned checks.

For revisions, apply [Dated updates](dated-updates.md) to changed items in the
same plan comment. Keep one active instruction per decision. Replace obsolete
instructions and retain a short reason when it explains the current choice.

## Example derived from CAMD-28583

Historical excerpt adapted from CAMD-28583 to illustrate the format:

```markdown
## Implementation plan

### Sources and baseline

CAMD-28532 的 URL AC。正式執行前記錄 idash-mono 的實際 branch 與 revision。

### Contracts and constraints

- campaign_status 未帶參數與空字串分開處理。未帶時套用 AC 的預設值，空字串表示全部取消。

### Changes

1. 在 apps/campaign-rules/src/components/TopFilterBar/index.tsx 的 normalize effect 一次補齊 status 與 campaign_status，避免同一次 commit 的 URL 寫入互相覆蓋。
2. 在 apps/campaign-rules/src/components/TopFilterBar/MultiFilter.tsx 保留全部取消時的空值，再接上 Campaign status filter。
3. apps/campaign-rules/src/pages/CampaignRuleDraftPreview/index.tsx 的 navigateToRules 維持只寫 oid，對應返回流程的 URL AC。

### Verification

- 首次進入、URL 帶 oid、全部取消後重新整理，以及 Draft preview 返回時，逐項對照 task AC。
```
