---
name: principle-prove-it-works
description: "Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.'"
disable-model-invocation: true
---

# Prove it works

Before running type-check, lint, or tests, read and follow [Scoped checks](../staff/references/scoped-checks.md).

Verify every task output by checking the real thing directly. Do not infer from proxies, self-reports, or "it compiles."

Unverified work has unknown correctness. Indirect verification (file mtimes, output freshness, agent self-reports, cached screenshots) feels cheaper than direct observation. Acting on a wrong inference costs far more than checking the source.

After completing any task, ask: "how do I prove this actually works?"

Check the real thing, not a proxy:
- Check process liveness directly, not indirectly through derived state
- Read the actual value, not a cached or derived representation
- When verification fails, suspect the observation method before suspecting the system

Code and features:
1. Build it (necessary but not sufficient)
2. Run it and exercise the actual feature path
3. Check the full chain: does data flow from input to output?
4. For integrations, test the full communication path end-to-end

Delegation: trust artifacts, not self-reports.
When verifying delegated work, inspect the actual output artifact (git diff, file contents, runtime behavior), not the delegate's summary.

## Script the check when you can

Write and run a deterministic comparison script when practical. Keep its output so a reviewer can repeat the check.

Keep the artifact visible for the human. Commit it only for large or complex work where the trail has to be auditable later, like a big port or migration (the **show-me-your-work** skill).
