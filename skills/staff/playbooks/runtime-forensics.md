### Runtime forensics

**You own the diagnosis. Ground it in runtime evidence.** The deliverable is a cited diagnosis. Start with observation; diagnosis alone does not authorize source edits or runtime state changes.

1. Capture the live signal on the matching surface via the control skill: a CPU profile for a spinning process, a heap snapshot for a leak, a CDP trace for a visual glitch. A real artifact, not a guess.
2. Reduce the artifact to the smoking gun: the function on the hot path, the retainer chain from the leaked object to a GC root, the loop firing without input. Parse large artifacts in the parent or an optional supported read-only delegate, keeping the reduced finding in the main thread.
3. Test the mechanism against captured evidence first. Injecting instrumentation, changing globals, hotfixing live code, or replaying state-changing actions requires existing authorization for that action on an isolated target. Without it, report the strongest supported hypothesis and the proposed experiment, with causal confirmation pending. Do not treat CDP eval as inherently passive.
4. Map the finding back to source: file, symbol, the line that allocates or schedules.
5. Record the actual mode: passive observation, or the authorized runtime experiment and its isolated target. Do not label runtime mutation read-only.

**Reply:** the signal captured, the reduced finding, how you proved the mechanism, the source location, artifact paths. No fix unless asked. Hand back to Bug fix or Perf once the cause is known.
