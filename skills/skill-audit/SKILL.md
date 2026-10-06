---
name: skill-audit
description: Review a skill’s triggering, environment compatibility, and instructions for its intended model. Use to diagnose skipped skills, audit behavior, or assess simplification and portability. Produces evidence-backed recommendations; leaves the target unchanged.
---

# Skill Audit

Answer two questions:

1. **Mechanics:** Will the skill be discovered, selected, loaded, and supported
   correctly in its target environment?
2. **Substance:** Does the guidance help the intended model make the decisions
   needed to complete the task reliably and within scope?

A well-formed skill can still be mostly ceremony, while a strong workflow behind
bad discovery metadata may never run.

## Establish the target and evidence

Start with the requested audit question, the description, and `SKILL.md`. List
supporting resources when needed to understand the package. Read resources that
govern the behavior under review or could change a finding, including host
metadata when relevant. For a whole-skill audit, account for each resource's role;
inspect its contents in proportion to its relevance. State material coverage
limits.

Identify the host, distribution form, and intended model or model range from the
request and available context. Ask only when missing information would materially
change the findings; otherwise state the assumption. Apply current official
documentation or the target's validator for host mechanics. Tag host-specific
findings rather than transferring requirements between hosts.

Judge instructions against the intended model's demonstrated behavior. For GPT-6
Astra, investigate unnecessary approval pauses, premature stopping, excessive
verification, and rigid execution sequences as hypotheses, not presumed defects.
For shared skills, distinguish portable task requirements from model-specific
tuning; guidance useful to one model may overconstrain another.

Separate concrete failures from authoring judgment. Invalid metadata, unresolved
paths, unavailable dependencies, and contradictory authorization are mechanics;
wording preferences and organizational conventions are not.

## Check mechanics

Select checks that bear on the requested scope and material findings.

- **Required structure and metadata:** Parse rather than eyeball metadata. Check
  required fields, naming, directory alignment, supported fields, and limits for
  the actual target.
- **Discovery and triggering:** Decide whether the description front-loads the
  capability, use case, and useful boundaries. Use relevant positive and adjacent
  non-trigger scenarios when they can clarify selection. Distinguish implicit
  selection from explicit invocation, and predicted selection from observed
  behavior in the actual host.
- **Codex:** Require `name` and `description` in `SKILL.md`. Implicit matching uses
  that description. Treat `agents/openai.yaml` interface fields as UI metadata;
  separately inspect `policy.allow_implicit_invocation` and declared tool
  dependencies. When diagnosing skipped or duplicate skills, also inspect
  discovery locations, disabled configuration, and same-name skills when those
  are accessible.
- **Resources:** Resolve referenced paths and check that conditional detail is
  discoverable without duplicating its policy in the entrypoint. Treat folder
  shape, naming, and contents sections as maintainability choices unless the
  target or repository makes them requirements.
- **Scripts and tooling:** Ask whether each script earns its place through
  deterministic behavior, reuse, or external tooling. Check declared
  dependencies, safe failure behavior, documented interfaces, and actual
  execution when relevant and permitted. Apply tool and hook rules only to hosts
  that support those mechanisms.
- **Authorization:** Compare claimed behavior with the permissions and tools
  actually available in the target environment. If prose cannot technically
  enforce a boundary, report that limitation without inventing an unsupported
  enforcement mechanism.

## Preserve the behavioral contract

Keep instructions whose removal could cause a concrete failure:

- the observable outcome, required evidence, success criteria, and stopping
  conditions;
- authorization and side-effect boundaries, destructive or irreversible gates,
  and fail-closed behavior;
- exact schemas, interface contracts, and ownership boundaries;
- non-obvious domain constraints the model cannot infer from available context.

Also check for missing guidance: can the model determine the intended result,
recognize sufficient evidence, make routine decisions within scope, and identify
when user input is necessary? Recommend additions only when a specific ambiguity
could cause a wrong result, unnecessary pause, premature completion, or work
beyond the task. Where approval is needed, check whether authorized preparation
can continue until the user has a concrete result to review.

## Challenge unnecessary choreography

Ask what decision or failure each remaining instruction changes. Scrutinize fixed
phase sequences, mandatory artifacts and template sections, exact item counts,
universal checkpoints, unconditional subagents, routine approval pauses, generic
advice, and repeated repository conventions.

Match rigidity to uncertainty, consequence, reversibility, duration,
coordination cost, and contractual or safety sensitivity. File count, step count,
and elapsed time are weak proxies. A mechanical many-file edit may be simple; a
one-line authorization change may deserve extensive validation.

Prefer positive decision rules with reasons over repeated prohibitions. Reserve
absolute language for genuine invariants and state each policy once. Routing,
severity, schemas, validation commands, and posting behavior should each have one
authoritative owner.

## Support recommendations with proportionate evidence

For each material addition, removal, or rewrite, identify the decision affected,
explain the expected effect for the intended model, and state the supporting
evidence. Brevity alone does not establish improvement.

Distinguish static inspection, a reasoned scenario walkthrough, and an executed
behavioral evaluation. A walkthrough can reveal ambiguity but cannot establish
actual triggering or execution behavior. Structural validation cannot establish
behavioral value. Label unmeasured behavioral improvements as hypotheses.

When behavioral validation would materially change confidence, select the
smallest relevant contrast from cases such as simple versus high-risk work,
ambiguous work, an adjacent non-trigger, or an authorization boundary. Do not
require every case for every audit. When practical, compare the original and
proposed instructions on the same relevant task; otherwise state what remains
untested.

This audit is read-only. Never alter the target to test a proposed change. If a
counterfactual evaluation is justified and permitted, use an isolated temporary
copy; otherwise recommend the scenario for a later revision workflow.

## Report

Lead with the few findings that materially affect discovery, correctness,
safety, or instruction fitness. Give each a plain severity, evidence, and a
concrete fix. Group findings only when grouping improves clarity; do not force
empty sections or compute a weighted score.

Identify contracts worth preserving and scenarios still needed before revision.
State the limits of the pass: authoring mechanics and instruction fitness do not
prove that domain logic or algorithms are correct, and a shared assumption can
remain a shared blind spot. Recommend independent adversarial review only when
the skill's stakes justify it.

Finish when the requested scope has been assessed, material findings support
concrete recommendations, and remaining uncertainty is stated. Expand inspection
or verification only when it could change a material finding. A valid audit may
recommend no changes.

Report and stop. Leave the audited skill unchanged unless the user separately
asks for revision. Apply the same proportionality standard to this audit: do not
manufacture requirements such as mandatory failure branches, fixed eval counts,
or universal definitions of done.
