# Appier Jarvis conventions

Use the project, team and ticket defaults from [Staff config](../../staff/references/staff-config.md). Confirm the work belongs to that team.

- Infer issue type, title prefix, sprint, and Story relationship from related
  tasks. Discover metadata through the installed `acli` outside the sandbox.
  Read the source Story through jarkdown during breakdown and planning. Use acli
  or Jira REST API for other Jira object reads and writes.
- A `Task` and a `Story` may share a hierarchy level. A relationship link does
  not make the Task a true subtask. Use `parent` only for an allowed hierarchy.
  Read [Issue linking](../../using-jira/references/issue-linking.md)
  before choosing and publishing the relationship.
- Backend campaign-rule work has lived under
  `services/rule_domain/app/rule_domain/` in `trading-desk-services`.
  Verify the relevant repository and files before planning. This is a starting
  point, not a default BE assignment.
