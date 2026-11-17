---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

離線演練，禁止連 Jira、啟動 app、修改 source 或真的建立子代理。請讀取 skills/using-jira/SKILL.md，回傳下一步、預計使用的子代理模型與 reasoning effort，以及留言的 ADF 草稿結構。

把 DEMO-101 的 AC 自我驗證結果貼到 Jira。這次只發布結果，不改程式。
branch 是 demo-101。task record 指定 comment 9812，同 task、branch、author 與 visibility 都已確認，現有留言含舊的驗證圖片與一段需要保留的其他內容。
AC 1 原文是 Empty search results display "No results".
獨立 verifier 已確認 PASS。Before 是目前 base-demo 的 3333333333333333333333333333333333333333，media ID 33333333-3333-4333-8333-333333333333。After 是最終測試 commit bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb，media ID bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb。所有 media 都已上傳，collection 是 jira-demo，圖片是 1280 x 800。
時間是 2026-11-17 16:00:00 +08:00，環境是 https://example.invalid/preview/demo-101/，backend dev。完整現有 ADF 可用。
