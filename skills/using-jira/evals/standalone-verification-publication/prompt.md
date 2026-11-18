---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

離線演練，禁止連 Jira 或 GCS、啟動 app、修改 source 或真的建立子代理。請讀取 skills/using-jira/SKILL.md，回傳下一步、預計使用的子代理模型與 reasoning effort，以及 Jira 留言草稿。僅列出需要的操作，不執行。

把 DEMO-101 的 AC 自我驗證結果貼到 Jira。這次只發布結果，不改程式。
branch 是 demo-101。task record 指定 comment 9812，同 task、branch、author 與 visibility 都已確認，完整現有內容可用，含舊的驗證圖片與一段需要保留的其他內容。
AC 1 原文是 Empty search results display "No results".
獨立 verifier 使用 verify-this 已確認 VERIFIED，fresh Before 是目前 base-demo 的 3333333333333333333333333333333333333333，After 是最終測試 commit bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb。
這次是在真實 preview 攔截 response data 後驗證 FE，因此結果是 PASS/intercepted，真實 BE 整合仍待驗證。
show-me 已產生單檔 HTML，每項 AC 均嵌入與版本、角色、情境相符的實際 app 截圖，逐項截圖證據已確認完整。GCS 已成功上傳、下載 SHA-256 相符，且瀏覽器已確認報告與內嵌圖片顯示正常。
GCS path 是 gs://appier-td-autotest/deletable-files/DEMO-101/run-1/index.html，報告網址是 https://storage.cloud.google.com/appier-td-autotest/deletable-files/DEMO-101/run-1/index.html，該網址需 bucket 權限，約 30 天後清除。
時間是 2026-11-18 16:00:00 +08:00，環境是 https://example.invalid/preview/demo-101/，backend dev。
