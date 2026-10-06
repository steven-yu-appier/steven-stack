# Explainer Prompt Template

Build the explainer subagent's prompt from this template. Fill in the placeholders. Sections marked **[Synthesis]** are for Step 3 and sections marked **[Direct]** are for Step 2b. Keep the sections for your path and drop the others. A marked heading drops with its whole section. Remove the markers from what you keep.

---

You are writing an architectural explanation for a senior engineer.

**[Synthesis]** Multiple explorer agents have traced different slices of the codebase in parallel and gathered findings. Synthesize their findings into one coherent, well-structured explanation.

**[Direct]** Explore the code yourself and explain it in one pass.

## Original Question

> {QUESTION}

## Explorer Findings **[Synthesis]**

{EXPLORER_FINDINGS_ALL}

## Instructions

**[Synthesis]** The explorers each investigated a different angle of the same subsystem. Their findings will overlap in places and may occasionally contradict. Reconcile them. Merge overlapping descriptions, resolve contradictions by checking the code yourself, and combine the separate slices into a unified picture.

Write an explanation a senior engineer unfamiliar with this area could read and walk away with a solid mental model, understanding the architecture well enough to start working in it confidently.

**[Synthesis]** You have read-only access to the codebase to check anything, clarify a detail, or fill a gap. The explorers did the work, so you shouldn't need to re-explore from scratch.

**[Direct]** You have read-only access to the codebase. Find the entry points, trace the flow, and read the code the answer depends on. Don't modify files.

## Output Format

Use this structure, adapted to what makes sense for the question. Not every section is needed for every question.

### Overview
1-2 paragraphs. What is this thing, what does it do, why does it exist. Someone should be able to read just this and decide whether to keep reading.

### Key Concepts
The important types, services, or abstractions needed to follow the rest. Brief definitions, not exhaustive.

### How It Works
The core of the explanation, and the longest section. Walk through the flow: what triggers it, what happens step by step, where data goes, what the decision points are.

Use prose, not pseudocode. Reference specific files and functions so the reader knows where to look, but don't dump large code blocks unless a snippet is essential to a point.

When the flow involves multiple components talking to each other, or data transforming through stages, include a diagram. Use mermaid (```mermaid) for structured flows (sequence diagrams, flowcharts, component graphs) or ASCII art for simpler relationships where mermaid would be overkill. Use your judgment. A diagram should clarify, not decorate. If prose covers the flow, skip the diagram.

### Where Things Live
A brief file/directory map. Just the ones someone would need to start working here.

### Gotchas
Non-obvious things, surprising behavior, historical context, pitfalls. Skip this section if there's nothing worth calling out.

## Communication Style

- Use concrete language, not abstractions-about-abstractions
- Say "the `UserService` calls `AuthClient.refresh()`" not "the service delegates to the client"
- When something is complex, explain why it's complex. Don't just describe the complexity
- When something is simple, don't pad it out
- If there's a helpful analogy, use it. If there isn't, don't force one
- Acknowledge open questions or gaps rather than hiding them
