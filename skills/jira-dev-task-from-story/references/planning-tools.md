# Planning tools

Pass each workflow the Story sources, acceptance record, repository pointers,
current findings, and requested output. Apply [Staff's planning scope](../../staff/SKILL.md#autonomy)
to the call and its nested workflows. Describe this as `planning-only` in the
prompt, not as a tool flag. Reuse findings that still answer the question.

| Condition | Workflow and required result |
| --- | --- |
| Every Story breakdown | [how](../../how/SKILL.md) traces runtime behavior, ownership, reusable patterns, and code entry points. |
| Existing behavior or ownership needs historical explanation | [why](../../why/SKILL.md) traces the relevant decision. |
| Material uncertainty about state, ownership, types, or API boundaries | [architect](../../architect/SKILL.md) runs Ground and Sketch. Return the design and rationale at Agree. Its arena candidates remain planning artifacts. |
| Competing approaches need independent comparison | [arena](../../arena/SKILL.md) compares plans or isolated experiments. Reuse Architect's comparison when it answers the same question. |
| A behavioral or visual question needs observation | [Prototype](../../staff/playbooks/prototype.md) runs in isolated scratch and returns evidence to Story planning. |
| A proposed plan is contested or needs adversarial challenge | [interrogate](../../interrogate/SKILL.md) reviews the plan, acceptance record, and constraints. Supply their paths as the explicit review scope to avoid default branch-diff selection. |
| The Story needs a multi-phase execution workflow | [figure-it-out](../../figure-it-out/SKILL.md) runs Frame and Design the workflow, then returns the proposed phases. |

Use [Subagent routing](../../staff/references/subagent-routing.md) for required
workers. An unavailable required route leaves the dependent design or review
pending. Continue planning that does not depend on it.
