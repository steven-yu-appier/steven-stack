---
type: llm
focus: trace
weight: 1
---

Selects only gpt-6-luna with high reasoning for self-verification Jira publication,
separate from the evidence verifier. If that route is unavailable, leaves
publication pending rather than using another model, effort or parent execution.
