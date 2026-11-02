# Dated checklist and plan updates

Prefix each added or substantively changed item in an existing checklist or
implementation plan with the update date. Put the prefix at the start of the
item's visible text. A completion-state change also counts as an update. Leave
untouched items, their dates, and their states unchanged. Initial drafts need
no update prefix.

The default matches CAMD-28583:

- Text: `MM/DD updated: ` using the user's current date and timezone. Include the
  year when needed to distinguish updates across years.
- Color: `#ff5630`.
- Weight: bold.
- Scope: the date prefix is colored, not the whole item.

For a second revision of the same item, replace its leading prefix with the new
date. Keep the current instruction readable. If a removed requirement needs an
explanation, record the dated decision in the plan rather than leaving a stale
active instruction in the checklist.

ADF text-node example:

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

Insert this node before the item's other text. Date the changed instruction or
decision itself rather than the comment heading or a separate update log.

Color requires the ADF `textColor` mark. Follow
[Jira CLI operations](jira-cli.md) for publication and formatting readback.
