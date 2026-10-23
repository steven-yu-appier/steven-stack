---
name: principle-build-the-lever
description: Uses rerunnable tools for non-trivial edits, migrations, analyses, and checks.
disable-model-invocation: true
---
# Build the lever

When the work isn't trivial, build the tool that does it instead of doing it by hand.

A codemod, generator, or script makes the work repeatable and gives reviewers a way to check it.

Default to building the lever. Skip it only when the task is trivial, a couple of obvious edits you can see at a glance.

- Do the first unit by hand to learn the recipe, then build the tool. Prove it by rerunning it on that unit and diffing against your hand-done version. Make the lever safe to rerun.
- Codemod or script for edits, generator for repetitive files, a dump-to-sqlite query for analysis, a rerunnable check for verification.
- If a script can process every unit in one pass, run it yourself instead of assigning manual edits to delegates.
- When you fan work out to subagents, write the lever as a skill they all read: the recipe, the verification contract, and the edit boundaries in one artifact. Keep it outside the delegates' write scope so they can't quietly edit the contract.
- Applying this principle produces a file. If you cited it and there is no codemod, script, generator, or delegate skill in the diff, you didn't apply it.
- Commit the lever when the work outlives the session.

**Balance:** The bar is triviality, not repetition. A one-off still earns a lever when the lever is what makes the work checkable. Per the [Laziness Protocol](../principle-laziness-protocol/SKILL.md), build the smallest script that does or proves the job, never a framework.

Distinct from [Encode Lessons in Structure](../principle-encode-lessons-in-structure/SKILL.md), which makes a recurring instruction a durable guardrail. This is throughput and reviewability on the work in front of you. For scripting the verification itself, see [Prove It Works](../principle-prove-it-works/SKILL.md).
