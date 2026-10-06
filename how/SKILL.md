---
name: how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
disable-model-invocation: true
---

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Route every delegate through [`../staff/references/subagent-routing.md`](../staff/references/subagent-routing.md).

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): spawn parallel explorers first, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Launch all explorers before waiting for any explorer:

- Route: `gpt-6.1-sol-medium`
- Ask each explorer to inspect the code without modifying files.

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Launch one explainer that explores and explains in one pass:

- Route: `gpt-6.1-sol-high`
- Ask the explainer to inspect the code without modifying files.

Build its prompt from `references/explainer-prompt.md`, keeping the **[Direct]** sections. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once all explorers have returned, launch one explainer to synthesize their findings into one explanation:

- Route: `claude-opus-5.5-med`
- Ask the explainer to inspect the code without modifying files.

Build its prompt from `references/explainer-prompt.md`, keeping the **[Synthesis]** sections and every explorer's findings filled in.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
