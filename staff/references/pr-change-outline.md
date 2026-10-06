# PR change outlines

Use the smallest view that lets a reviewer understand the changed relationship without reconstructing it from the diff. Use prose when one or two sentences are clearer than a visual.

## Contents

- Pick the view
- Keep it bounded

## Pick the view

- Use a type or JSON shape for a changed data contract.
- Use pseudocode for changed decisions or business rules.
- Use a call tree for runtime ownership and sequence.
- Use a component tree for React ownership, hooks, state, or package boundaries.
- Use a shallow file tree for moved responsibilities.
- Use a focused `diff` block when the surrounding shape already exists.
- Use `text` for a mostly new target shape.

Use at most one view. Split the PR when one bounded view cannot explain its independent changes.

## Keep it bounded

Include only the calls, files, fields, states, and boundaries needed to review this PR. Introduce the view with one short sentence. Follow it with a material scope boundary only when needed.

Do not:

- reproduce the file diff;
- list every changed file;
- show unchanged layers for context alone;
- use Mermaid, HTML, or an image when the PR body becomes the squash commit body;
- use a diagram for a change that one sentence explains.
