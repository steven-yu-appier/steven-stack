# Engineering-task description template

Use only the task's assigned functional AC and their design references. State
observable results or compatibility invariants using the Story's exact domain
terms. A breakdown task stays a Task unless another type is requested or confirmed.

## Template

Replace the placeholders with confirmed requirements and their design references.
Repeat groups for distinct features, screens, or flows; use their actual names.

```markdown
### TODO

#### <Group 1>

Figma: <url> // if needed
Screenshot: <url|string> // if needed

1. <ac1>
2. <ac2>

#### <Group 2>

Figma: <url>
Screenshot: <url|string>

1. <ac1>
2. <ac2>
```

## Content and updates

- Omit a Figma or Screenshot line when no applicable reference is available.
- Cite AC by group name and item number in plans and verification comments.
  Encode the numbered AC as ADF `orderedList` with `listItem` nodes.
- Put implementation context, paths, branch details, design decisions, and
  development checks in the plan comment. Keep Story relationships in metadata.
- When revising AC, preserve unchanged group names, wording, and order; apply
  [Dated updates](dated-updates.md) to changed items.
- Record PASS, FAIL, and BLOCK in the
  [self-verification comment](../../staff/references/ac-self-verification.md#4-publish-verification-results).
  Keep completion states out of the description.
