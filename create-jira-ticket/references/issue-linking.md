# Jira Issue Linking

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

Resolve the intended parent and child explicitly, verify direction before mutation, and read the created link back afterward.
