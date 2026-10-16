### Feature

**You own the design, implementation, and verification.** Use optional delegates for independent slices under Staff's routing contract.
1. Complete [Confirm requirements](../references/implementation-scope.md#confirm-requirements), then `how` over the affected subsystem.
2. State the intended shape. Use `architect` for material architectural uncertainty per Staff's trigger; otherwise follow the established structure and name that choice.
3. Write the throughput checkpoint as four todo items. A dimension that genuinely does not apply (single file, no fan-out) keeps its item with `n/a: <reason>` rather than being dropped:
   - **Blocking first steps.** Gates run before fan-out.
   - **Independent workstreams.** Disjoint files, services, or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Default to splitting the target (the **separate-before-serializing-shared-state** principle skill). Serialize only for real invariants.
   - **Smallest safe decomposition.** If one worker is best, name why.
4. Implement in the parent or delegate independent slices through [`../references/subagent-routing.md`](../references/subagent-routing.md). Give each slice file ownership, the named data shape, and success criteria; review every delegated diff. Use **arena** when materially competing designs need experiments or the user requests a bakeoff. Keep comments per **Comments** and verify every affected consumer of a shared primitive.
5. Complete [Acceptance and delivery](../references/implementation-scope.md#acceptance-and-delivery) on the matching surface.
6. Arrange small, ordered commits under **Opening a PR**'s Commits policy. Stack follow-ups while preserving published history.
   Use the **sequence-verifiable-units** principle skill, building, verifying, and committing each small unit before the next.
7. If the design is contested, `interrogate` before shipping.
8. Run **Opening a PR**.
Code-coupled work (one feature, one migration) goes to a single owner with the checkpoint inline. That owner may delegate independent slices after the blocking phase under Staff's routing contract. Parent-level fan-out is for slices that produce independent artifacts (audits, cross-subsystem investigations, competing experiments). Rewrite the checkpoint at phase boundaries. Spawn a fresh owner rather than chaining interrupts.
**Reply:** what you built, what you chose and why, the throughput checkpoint, open decisions. Tables for design alternatives.
