# Date AC and plan revisions

| Change                                             | Date prefix                                                   |
| -------------------------------------------------- | ------------------------------------------------------------- |
| Initial draft                                      | None.                                                         |
| Added or substantively revised AC/plan item | Add the current date at the start of the item's visible text. |
| Previously dated item revised again                | Replace the leading prefix with the new date.                 |
| Unchanged item                                     | Preserve its text, date, and order.                           |

Use the user's date and timezone. The CAMD-28583 convention is
`MM/DD updated: ` in bold `#ff5630`; include the year when needed to distinguish
updates across years. Color only the prefix.

Insert this ADF node before the item's other text, substituting today's date:

```json
{
  "type": "text",
  "text": "11/02 updated: ",
  "marks": [
    { "type": "strong" },
    { "type": "textColor", "attrs": { "color": "#ff5630" } }
  ]
}
```

Date the changed instruction itself, not the comment heading or a separate log.
Replace obsolete instructions; retain a dated reason in the plan when a removed
requirement needs explanation. Follow [Jira commands](jira-cli.md) for publication
and formatting readback.
