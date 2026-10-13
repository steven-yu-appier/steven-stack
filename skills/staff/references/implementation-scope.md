# Implementation scope

## Grill or clarify

Identify the task's acceptance criteria (AC) and the smallest change needed to satisfy them. Keep the source AC numbering and identify which criteria belong to FE scope. If the source has no numbers, assign stable numbers in source order without changing the criteria. Resolve missing or ambiguous acceptance requirements before implementing the affected behavior.

For UI work, inspect the relevant Figma frames and states, then map each UI element to an existing repository component and supported variant. Check layout, styling, and interactions against the design. Raise missing components, unsupported variants or interactions, and conflicts between Figma and AC during grill or clarify. This gate is complete when the affected UI has a confirmed design and existing-component mapping with no unresolved gaps. If a gap is discovered later, return to clarification for that part and continue independent work.

## Implement the confirmed scope

Use existing components and their supported APIs to match Figma. Composing them, extracting page sections, and adjusting layout are allowed. Creating UI primitives, rebuilding existing components, or inventing interactions is prohibited. Resolve component gaps through clarified requirements or available existing components before implementation.

Implement only the behavior needed to satisfy the confirmed AC, with the smallest necessary diff. Preserve existing component behavior. Add error handling, fallbacks, keyboard navigation, or other behavior only when required by the AC or an explicit repository contract. Hypothetical product states and general completeness do not justify extra behavior. Keep unrelated refactoring out of the task.

Before delivery, account for each added behavior against an AC or explicit repository contract and remove additions without one. Verify the implemented UI against the relevant Figma frames and states, then collect the FE AC evidence required by Opening a PR.
