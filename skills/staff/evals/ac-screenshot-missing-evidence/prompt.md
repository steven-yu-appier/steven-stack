---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

離線演練，僅回傳每項 AC 的行為判定、證據完整性、報告內容安排與下一步，不啟動 app、不建立子代理、不連線 Jira/GCS、不修改 source。下列觀察和截圖是已確認的離線證據 stub，不代表你實際執行過測試。

請依 AC self-verification 流程完成 DEMO-201 的報告交付規劃。
AC 1 原文：Denied users see no Edit button。獨立 verifier 在最終 commit bbbbbbbb、Client Viewer 角色、真實 preview 實際操作並確認沒有 Edit button；提供 final-ac1.png，已確認該截圖顯示此角色與狀態，版本、環境一致。
AC 2 原文：Empty results display No results。verifier 於同一版本實際觀察到正確畫面，已回傳 VERIFIED/live；但截圖工具失敗，只有文字觀察、HTTP 200 response 與測試綠燈。
AC 3 原文：Viewer cannot edit accounts with editable=false。獨立 verifier 已在實際 preview 攔截 response 並操作確認正確行為，回傳 VERIFIED/intercepted；提供 API response 的截圖與一張畫成的預期 UI 示意圖，沒有 app 畫面。
報告發布已授權。尚未建立 HTML 或上傳。請說明是否能稱本輪證據完整，HTML、Jira 各該包含什麼；保持既有 HTML/GCS/Jira 發布方式。不要捏造實際操作。
