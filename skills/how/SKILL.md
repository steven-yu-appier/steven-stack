---
name: how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
disable-model-invocation: true
---

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

The parent handles simple explanations directly. Delegation below is optional for complex exploration and synthesis; if a route or enforced read-only access is unavailable, perform that work in the parent under the same inspection-only scope. Route every delegate through [`../staff/references/subagent-routing.md`](../staff/references/subagent-routing.md).

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. The parent explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): use parallel explorers and a synthesis delegate when supported and useful; otherwise explore and synthesize in the parent. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. When delegating, launch all supported explorers before waiting for any explorer:

- Route: `gpt-6.1-sol-medium`
- Ask each explorer to inspect the code without modifying files.

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Inspect the code without modifying files and explain it in the parent. Use the **[Direct]** sections of `references/explainer-prompt.md` as the output guide. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Synthesize the exploration in the parent, or, when supported and useful, launch one explainer after all explorers return:

- Route: `claude-opus-5.5-med`
- Ask the explainer to inspect the code without modifying files.

Build its prompt from `references/explainer-prompt.md`, keeping the **[Synthesis]** sections and every explorer's findings filled in.

## Step 4. Present

Present the resulting explanation to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
