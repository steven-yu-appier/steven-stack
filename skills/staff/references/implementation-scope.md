# Implementation scope

## Confirm requirements

Keep one acceptance record in the existing plan or task notes. Retain source AC wording and numbering, identify FE scope, and attach the relevant source pointers. For unnumbered AC, assign stable numbers in source order. Record each affected input or state, its observable expected result, and the requirement or clarification that establishes it. A separate document is unnecessary.

Follow the source's declared authority. Product requirements and explicit owner decisions establish intent; AI suggestions, generated test cases, implementation notes, and current code are supporting evidence. `[AI][verified]` may establish a code fact, not product approval. Resolve contradictions among the story, QA copies, comments, Figma, and API contracts rather than silently choosing one. When the user reports an update, refresh Jira under its read policy, reconcile the changed scope, and invalidate affected expectations and evidence. Treat a later requirement change separately from an original implementation defect.

### Recognize ambiguity

Use these cues to find missing meaning, not to ask about requirements that already specify the outcome.

| Wording | Establish before implementation |
|---|---|
| Clear, reset, remove; 清空 | Exact target, such as selection, operand, or whole condition, and the resulting UI and stored data. |
| Keep current behavior; 維持現行 | The named flow and observed baseline. Conflicting existing paths need an intent decision. |
| Require reselection; 須重選 | Whether a blank selector remains or a condition is removed, and what then permits saving. |
| Admin, others; Admin、其他 | Role namespace and relevant population, such as client versus internal users. |
| Reuse existing rules or pattern; 沿用 | The actual component, variant, or contract, including which behavior and styling it supplies. |
| Has data, empty, count; 有資料、無資料、人數 | The qualifying list and whether filtering precedes rendering, counting, and empty-state selection. |
| Time range, default, editable; 預設、可改 | Which operand or field, UI behavior versus API representation, and FE/BE ownership. |
| Live query; 即時查詢 | Fetch trigger and persisted versus draft data. |

If sources still allow different observable outcomes or contain an unresolved `[OPEN]`, name the concrete competing results and ask the user or requirement owner a focused question. Current behavior or a prototype cannot establish intended behavior. Hold only dependent implementation, delegation, and test expectations; continue independent work. Autonomy does not turn an inferred product decision into a confirmed requirement.

This gate passes when every affected result has a requirement source or recorded owner decision. Calling a plan "confirmed" is insufficient. Re-enter the gate whenever new ambiguity or conflicting evidence appears.

## Implement the confirmed scope

Give implementers and reviewers the acceptance record and original source pointers, not only a paraphrased plan. Implement the smallest change that satisfies it. Add behavior, including fallbacks or keyboard handling, only for a confirmed AC or explicit repository contract. Keep unrelated refactoring out of scope.

For UI work, inspect the relevant Figma frames and states before implementation. Map elements to existing repository components and supported variants. Resolve missing components, unsupported interactions, and AC/design conflicts through clarification. Use those components and APIs; composition, page sections, and layout adjustments are allowed. Create no substitute UI primitives or invented interactions to conceal a gap.

Before writing or changing a behavioral assertion, trace its expected result to the acceptance record. Check existing tests used as acceptance evidence against the same sources. Code output, old assertions, and AI-generated test rows do not independently establish the expected requirement. Correct implementation or tests according to the confirmed result.

## Acceptance and delivery

The delivery owner compares the final artifact with the original AC and design sources, not just the implementation report or passing tests. Account for added behavior against the confirmed scope and remove unsupported additions.

Exercise the applicable flows and states in the real application. For Figma acceptance, compare exact copy and casing, complete tooltip text, component variants, dimensions, typography, colors, spacing, and placement in the affected states. Verify conditional content, filtered counts, and empty/loading/error states where relevant. Reusing a DS component or checking one happy path does not complete this comparison. Screenshots may help local inspection; uploading them is not a gate.

Record observed results with the tested source revision and environment. Separate fixture behavior, live API save/reopen, and backend execution coverage. A merged backend contract or Done ticket does not establish the serving deployment. A local operand investigation supports only that operand's conclusion.

Acceptance passes when every applicable result has a confirmed source and current behavioral evidence, including the required visual comparison. Report unresolved, failed, blocked, or unexecuted checks and their reasons as pending. Verified slices may be published in an authorized draft with those gaps; publication is not QA readiness. Claim readiness only for the scope whose acceptance passed, and name unmet integration prerequisites.

Opening a PR formats this record into reviewer targets. Refresh affected acceptance after requirement or source changes and rebuild the handoff claims from the current results.
