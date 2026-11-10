# Appier Jarvis conventions

These defaults guide discovery for Jarvis work in the CAMD project. Explicit
user instructions and observed project conventions take precedence.

- Site: `appier.atlassian.net`. Project: `CAMD`. Label: `jarvis` when the work
  belongs to Jarvis, not merely because its key starts with CAMD.
- Infer issue type, title prefix, sprint, and Story relationship from related
  tasks. Discover metadata through the installed `acli` outside the sandbox.
  Read the source Story through jarkdown during breakdown and planning. Use acli
  or Jira REST API for other Jira object reads and writes.
- The ready-to-groom sprint has used names like `Jarvis- Ready to groom today`.
  Resolve the intended sprint and its current numeric ID. Do not reuse a saved
  sprint or custom-field ID without verification.
- A `Task` and a `Story` may share a hierarchy level. A relationship link does
  not make the Task a true subtask. Use `parent` only for an allowed hierarchy.
  Read [Issue linking](../../create-jira-ticket/references/issue-linking.md)
  before choosing and publishing the relationship.
- Backend campaign-rule work has lived under
  `services/rule_domain/app/rule_domain/` in `trading-desk-services`.
  Verify the relevant repository and files before planning. This is a starting
  point, not a default BE assignment.
