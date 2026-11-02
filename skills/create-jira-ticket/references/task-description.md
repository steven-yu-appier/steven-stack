# Engineering-task description format

The description contains only the functional acceptance checklist assigned to
this task after breakdown. Each item states one observable result or required
compatibility invariant. Preserve the Story's exact domain terms.

```markdown
- [ ] An observable outcome under its relevant input or state.
- [ ] Another independently verifiable outcome covered by this task.
```

Render as Jira's native checklist in ADF. For an existing checklist, retain
unchanged task-item identities and completion states. Added items start open.
Do not mark an outcome complete based only on a plan or passing developer checks.

Keep goal paragraphs, Story summaries, implementation steps, file registrations,
and branch details out of the description. Put the Story relationship in Jira
metadata and implementation context in the plan comment. Development activities
such as type-check, lint, tests passed, code review, or QA checked are not task AC.
Tests may demonstrate a functional criterion without becoming a separate item.

For checklist revisions, use [Dated updates](dated-updates.md).

## Example derived from CAMD-28583

Historical excerpt adapted from
[CAMD-28583](https://appier.atlassian.net/browse/CAMD-28583) to show functional AC.
It does not record current completion status.

```markdown
- [ ] Rule tab 顯示 Campaign status filter；Templates 與 Scheduled on/off 不顯示。
- [ ] URL 未帶 campaign_status 時，有 oid 顯示全部，無 oid 預設選取 New、Running、Paused。
- [ ] 使用者全部取消 Campaign status 後，URL 保留空值；重新整理仍維持全部取消。
- [ ] Draft preview 返回 Rule tab 時保留只帶 oid 的連結行為，顯示全部 affected campaign 的 rule。
```
