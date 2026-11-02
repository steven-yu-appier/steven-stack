# Jira CLI operations

All Jira metadata and writes use the installed absolute `acli` executable outside
the sandbox. Active user CLI instructions select its path and login shell.
Never treat a sandbox authentication error as a request for the user to log in.
Inspect installed command help when a required option or JSON schema is uncertain.

Read ticket and comment bodies only under
[Jira read policy](../../staff/references/jira-read-policy.md). Cached content is
not fresh after a write. Refresh through jarkdown before content readback, using
its verified promotion and cleanup procedure. Do not store a second ticket
snapshot with plans or CLI inputs.

## Write from files

Prepare exact payloads in task-owned scratch. Keep prose out of shell arguments.
The installed CLI supports these inputs:

| Operation | Input |
| --- | --- |
| Create issue | `jira workitem create --project <KEY> --type <TYPE> --summary <TITLE> --description-file <ADF_FILE> --json` |
| Update description | `jira workitem edit --key <KEY> --description-file <ADF_FILE> --yes --json` |
| Create plan comment | `jira workitem comment create --key <KEY> --body-file <ADF_FILE> --json` |
| Update plan comment | `jira workitem comment update --key <KEY> --id <COMMENT_ID> --body-adf <ADF_FILE>` |

ADF files contain the complete document, not just a text node. Quote shell values
properly, validate issue keys, and target only approved issues. Avoid JQL or filter
bulk writes for a named task set and avoid `--edit-last` for a designated plan.

For fields not exposed as flags, inspect `--generate-json` in isolated scratch
and the command's help before preparing `--from-json` input. Do not guess custom
field keys or assume a connector payload works with this CLI. Resolve the sprint's
numeric ID and supported write path when sprint assignment is requested.
If the installed CLI cannot set a required field, leave that field pending and
report the limitation. Do not switch to a direct HTTP write or another connector.

## Preserve and read back

Use canonical ADF where needed to preserve rich text and protected media. If a
required representation is missing, refresh through jarkdown. If the downloader
still omits it and preservation cannot be established, leave the affected update
pending rather than reconstructing protected content from lossy Markdown.

Obtain comment IDs, authorship, revision metadata, and link metadata through
`acli`. Select only the required metadata from its output. Inspect current
metadata immediately before updating a designated comment. If it changed since
the draft, refresh the content and reconcile the draft before writing.

Verify description checklist text and state, implementation plan text, changed
date marks where available, comment identity, requested fields, and Story link
direction. A command's success status alone is insufficient. Missing readback
evidence stays pending.

If an operation fails or times out, discover whether it already took effect
before retrying. Resume at the failed operation using the known issue key or
comment ID. Do not create a second issue because its comment or sprint update
failed. Remove task-owned payload files after verified use or record why they
must remain for a pending operation.
