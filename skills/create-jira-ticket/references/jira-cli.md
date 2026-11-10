# Jira operations

Use acli or Jira REST API for Jira object reads, writes, and readback. Run acli
outside the sandbox using the active CLI instructions. Only planning-time source
Story reads use [jarkdown](../../staff/references/jira-read-policy.md).
Attachment uploads use [REST API](jira-attachments.md).
A sandbox authentication failure requires a retry outside the sandbox, not a login request.

## Create or update

Set the variables for the selected operation. `ADF_FILE` contains the complete
ADF document in task scratch. Run only the requested command.

| Operation          | Command                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Create issue       | `acli jira workitem create --project "$PROJECT" --type "$TYPE" --summary "$TITLE" --description-file "$ADF_FILE" --json` |
| Update title       | `acli jira workitem edit --key "$KEY" --summary "$TITLE" --yes --json`                                                   |
| Assign issue       | `acli jira workitem edit --key "$KEY" --assignee "$ASSIGNEE" --yes --json`                                               |
| Update description | `acli jira workitem edit --key "$KEY" --description-file "$ADF_FILE" --yes --json`                                       |
| Add comment        | `acli jira workitem comment create --key "$KEY" --body-file "$ADF_FILE" --json`                                          |
| Update comment     | `acli jira workitem comment update --key "$KEY" --id "$COMMENT_ID" --body-adf "$ADF_FILE"`                               |

For comment updates, `--body-adf` reads ADF; `--body-file` reads plain text.
Keep exact bodies in files. Target named keys and comment IDs rather than JQL,
filters, or `--edit-last`.

For fields absent from the table, inspect the command's `--help`. Where supported,
use `--generate-json` to inspect the schema before preparing `--from-json` input.
Resolve custom field keys and numeric sprint IDs from metadata. Use Jira REST API
when it better supports the requested operation or acli cannot represent it.
The same target, scope, preservation, and authorization rules apply to both tools.

## REST API operations

Run outside the sandbox through an interactive login zsh, using the existing
`JIRA_DOMAIN`, `JIRA_EMAIL`, and `JIRA_API_TOKEN`. Validate issue keys against
`^[A-Z][A-Z0-9]+-[0-9]+$` before using them in paths or commands. Keep credentials
out of logs, arguments, and files; supply curl authentication through stdin with
`--config -` and keep TLS verification enabled. Keep request bodies in payload
files. Use the operation's documented method, endpoint, response status, and schema;
retain returned issue, comment, and attachment IDs. Attachment-specific requirements
remain in [Attachment commands](jira-attachments.md).

## Before replacing a body

| Available evidence                                 | Action                                                                                                   |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Complete original ADF                              | Edit the requested nodes and preserve unrelated content, identities, states, marks, and media.           |
| Markdown without structure needed for preservation | Fetch complete ADF through acli or REST API before editing. If unavailable, leave only that replacement pending. |
| No existing body, such as a new comment            | Author a new ADF document.                                                                               |

Obtain the current complete description or comment ADF through acli JSON output
or Jira REST API before replacement. If one tool omits the structure needed for
preservation, use the other. Leave only the dependent update pending if neither
can provide it. A planning snapshot is not the current body for an edit.

Before updating a comment, obtain its ID, author, and revision metadata:

```sh
acli jira workitem comment list --key "$KEY" --paginate --json
```

Read the current body and metadata through acli or REST API. If the revision
changed since drafting, fetch the current body and reconcile the edit before
writing. Preserve the comment's visibility. Text approval does not authorize moving, converting,
removing, or replacing existing media.

## Verify or retry

| Operation                              | Readback                                                                                                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Metadata change                        | Verify only the changed fields through acli or REST API.                                                                              |
| Description or comment write           | Read back through acli or REST API and verify text, target identity, and requested placement.                             |
| Numbered list, styled text, or media write | Verify list type and order, relevant identities, marks, and media in structured content. Markdown alone cannot prove preservation. |
| Relationship change                    | Verify both endpoints under [Issue linking](issue-linking.md).                                                            |
| Failed or uncertain write              | Inspect current state before retrying. Reuse successful issue, comment, and attachment IDs.                               |

Missing or transformed media is a failed update. A completed write with missing
formatting evidence is published but unverified.
Retain its ID; republishing does not resolve missing readback. A successful CLI
exit alone is not verification. Remove consumed payloads under the caller's task
cleanup policy, or record why a pending operation still needs them.
