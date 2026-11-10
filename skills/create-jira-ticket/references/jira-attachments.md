# Jira attachment commands

Use only the requested operation. Run uploads and acli outside the sandbox
through an interactive login zsh. Python 3, curl, and acli come from PATH.

Set `SKILL_DIR` to this skill's installed directory; reuse `TASK_SCRATCH`.
Set `KEY`, `FILE`, and, for comment updates, `COMMENT_ID` to the requested targets.

```sh
attachment="$SKILL_DIR/scripts/jira-attachment.py"
receipt="$TASK_SCRATCH/upload.json"
payload="$TASK_SCRATCH/attachment.adf.json"
```

## Upload a file

```sh
python3 "$attachment" upload "$KEY" "$FILE" --output "$receipt"
```

For upload-only requests, stop after readback. Use a confirmed successful receipt
for the commands below; retain its IDs and URLs and reuse it on publication retries.

## Add a comment with file links

```sh
python3 "$attachment" adf "$receipt" --output "$payload" &&
acli jira workitem comment create --key "$KEY" --body-file "$payload" --json
```

## Append file links to an existing comment

```sh
python3 "$attachment" adf "$receipt" \
  --body "$TASK_SCRATCH/existing.adf.json" --output "$payload" &&
acli jira workitem comment update --key "$KEY" --id "$COMMENT_ID" --body-adf "$payload"
```

## Append file links to the description

```sh
python3 "$attachment" adf "$receipt" \
  --body "$TASK_SCRATCH/existing.adf.json" --output "$payload" &&
acli jira workitem edit --key "$KEY" --description-file "$payload" --yes --json
```

For either update, prepare the complete original body as `existing.adf.json`
under [Jira CLI operations](jira-cli.md). If unavailable, leave that update pending.
Add `--index N` to the `adf` command for a requested top-level insertion position.
Read back through acli or REST API after writes and verify the requested change.
For uploads, verify attachment metadata and download the returned `content` URL
to compare the attachment bytes with the source file. No jarkdown refresh is required.

Uploads use REST API. On an uncertain upload result, inspect attachment metadata
before retrying. These commands produce file links; inline images require verified
Media Services references and remain pending if unresolved. Browser upload is not
a fallback.

[Script](../scripts/jira-attachment.py) · [Upload API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-issue-issueidorkey-attachments-post)
