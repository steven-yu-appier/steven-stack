# AC alignment evaluation

Executed on 2026-10-14 using two independent, fresh-context agents, one per instruction version. Each received the same six synthetic requests in [ac-alignment.json](ac-alignment.json), its instruction snapshot, and permission to produce decisions and a Verification draft only. Neither received expected answers or the other agent's results. No Jira snapshot was copied, product modified, PR published, or live browser acceptance performed.

The baseline is repository HEAD `b67f956`, before this chat's edits. The revised snapshot is the working tree. Revised SHA-256 prefixes are `31cf036f9b08` for implementation-scope.md and `58efefce5bca` for opening-a-pr.md. This evaluates supplied-artifact decisions, not discovery, full story execution, or long-session adherence.

## Results

The delivery owner inspected both returned artifacts. All six revised scenarios met the case-specific acceptance criteria below. The baseline also made the correct core product decisions; these runs do not demonstrate a lower future defect rate.

| Case | Acceptance criterion | Observed revised decision | Result |
|---|---|---|---|
| event-clear, CAMD-28342 ambiguity | Expose blank selection versus condition removal; hold dependent assertions and continue matching work. | Asked which result the owner intends and what permits saving. Full autonomy did not settle product intent. | Pass |
| event-confirmed, CAMD-28342 feedback | Apply explicit removal without asking again; preserve matching values and correct obsolete tests. | Purchase remains; signup disappears from chip and persisted data. Existing validation governs saving. | Pass |
| avatar-and-update, MCP roles | Use updated story population, correct count, reuse role rules, and distinguish later scope change from an original defect. | Role 1 excluded, role 7 purple, count 1; stale QA copy reconciled and old coverage invalidated. | Pass |
| figma-states, MCP and Minor event/cap UI | Identify state/content/style mismatches despite passing tests; require actual design comparison without an upload gate. | Identified all seven supplied mismatches and separate has/empty states; uploads do not affect readiness. | Pass |
| cap-contract, CAMD-27640 API | Separate left UI range from right payload; keep deployment diagnosis uncertain and fixture coverage scoped. | Kept accepted placeholder, requested serving-revision evidence, and marked live round-trip/runtime coverage pending. | Pass |
| cap-copy-and-pr, cap casing | Verification lists FE AC once with concrete reviewer targets, excludes BE AC and screenshots, and reports limits honestly. | Produced one two-column table for AC 1 and 2; noted untested BE runtime and absent revision/environment evidence. | Pass |

The observable differences from the baseline are narrower. Its Figma response ended with complete screenshot evidence pending. The revised response made upload availability irrelevant while retaining visual checks. Its Verification draft listed FE AC twice as author checks and reviewer checks. The revised draft listed each criterion once and separated author coverage into prose. It also explicitly distinguished a later scope change from an original defect and identified missing revision/environment evidence.

## Output excerpts

Revised ambiguity question: "When the target OID lacks the event type, should duplication and create-time OID switching retain the condition with a blank event selector and require reselection, or remove the entire condition? What should then permit saving in each flow?"

Revised Verification draft:

```markdown
## Verification

| # | FE acceptance criterion |
|---|---|
| 1 | Open the cap menu and check that all ten daily and total cap labels use sentence case, including Daily action cap. |
| 2 | Select each daily or total cap and check that the selected value and condition summary use the same sentence-case copy as its menu label. |

Browser checks on the current source verified all ten menu labels, the selected value, and the condition summary. The supplied evidence does not identify the source revision or browser environment; record those before a readiness handoff. Staging runtime cap resolution was not exercised and remains outside this FE copy coverage.
```

The draft excerpt normalizes quote typography and omits its redundant screenshot sentence. Full raw outputs remain at `/private/tmp/staff-ac-eval.793vwi_n/before-results.md` and `/private/tmp/staff-ac-eval.793vwi_n/after-results.md`.

## Structural validation

- YAML frontmatter parsed; existing name, description length, and explicit invocation policy preserved.
- All 16 local reference paths and anchors in the five edited instruction files resolved.
- Entry and reference lengths remain within the revision rubric's bounds. Scope reference remains below 100 lines.
- No remaining caller of the removed GitHub attachment procedure. Verification template has two columns and no duplicate FE AC section.
- `git diff --check` passed.
- Bundled quick_validate.py rejects the pre-existing disable-model-invocation field. It was not reported as a successful validator run or removed to satisfy that incompatible schema.

Re-run with fresh independent contexts after future changes to these instructions. At evaluation time, the revised package had not yet been reinstalled into the plugin cache.
