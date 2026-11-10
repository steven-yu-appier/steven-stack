# Jira relationship commands

Use acli outside the sandbox or Jira REST API for relationship operations and
related-ticket reads under [Jira operations](jira-cli.md). Set `PARENT` and `CHILD`
to the intended endpoints.

## Inspect relationship types and existing links

```sh
acli jira workitem link type --json
acli jira workitem link list --key "$PARENT" --json
acli jira workitem link list --key "$CHILD" --json
```

Choose the project's confirmed type and direction. A Jira parent field creates
hierarchy only for compatible issue types; a `Parent-Child` link does not turn a
Task into a Sub-task.

## Create a Parent-Child link

For the confirmed `Parent-Child` convention, the parent is inward and the child
is outward. The child displays `is child of <parent>`; the parent displays
`is parent of <child>`.

```sh
acli jira workitem link create --in "$PARENT" --out "$CHILD" \
  --type 'Parent-Child' --yes
```

For another type, use its confirmed name or outward description and matching
inward/outward endpoints. Inspect `acli jira workitem link create --help` if the
input is uncertain. For true hierarchy at creation, use `--parent "$PARENT"`
with the compatible issue type in the [create command](jira-cli.md#create-or-update).

## Verify

Read both endpoints with the list commands above and verify the requested
relationship in each direction. On a retry, reuse an existing matching link.
Preserve relationships outside the requested change.
