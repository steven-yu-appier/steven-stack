# Jira issue linking

Discover the project's available link types and the relationship used by related
tasks through `acli` outside the sandbox. Read related task content through
jarkdown. Do not assume `Relates` or a custom `Parent-Child` type applies everywhere.

True Jira hierarchy and issue links are different. Use a parent field only when
the chosen issue types permit that hierarchy. A linked Task is not a Sub-task.

Inspect `jira workitem link create --help` before creating a link. Confirm which
issue is the source and how each side will read. The example below documents the
known relationship semantics, not a CLI input schema.

For Jira `Parent-Child`, ticket B should be a child of ticket A:

```json
{
  "inwardIssue": "AI-30484",
  "outwardIssue": "AI-30525",
  "type": "Parent-Child"
}
```

On B this displays `is child of A`; on A it displays `is parent of B`.

Do not reverse the issues:

```json
{
  "inwardIssue": "AI-30525",
  "outwardIssue": "AI-30484",
  "type": "Parent-Child"
}
```

Resolve the intended parent and child explicitly. Verify the rendered relationship
from both issues after mutation. Preserve existing links and avoid duplicates on
retry. Do not change or delete a relationship outside the authorized scope.
