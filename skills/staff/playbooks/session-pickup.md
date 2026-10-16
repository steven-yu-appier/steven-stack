### Session pickup

**You own the resume point. Read the prior trail, don't redo it.**

1. Locate the prior trail: a Claude Code or Codex session transcript, or a pushed branch. Claude Code writes transcripts to `/Users/<$USER>/.claude/projects/<encoded-cwd>/<session-id>.jsonl`, where the directory name is the working directory with each `/` and `.` replaced by `-`. Codex writes them to `/Users/<$USER>/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`, and each file's first `session_meta` record names its `cwd`. Take the transcript the user names, or the newest one whose working directory is this repo or one of its worktrees. Do not search transcripts from other projects, that crosses workspace boundaries and reads private chats from unrelated work. Read the session metadata and last messages first, then scan back for the decision points. Parse a long transcript in a subagent and keep the reduced timeline in the main thread (the **principle-guard-the-context-window** skill).
2. Reconstruct operational state. The branch and worktree, what already landed (`git log`, `git diff` against the base), the open todos, the decisions made. The prior trail is authoritative input. Resist the bias to re-derive it.
3. Diff done vs pending. Compare what shipped against what was planned, name the resume point, do not re-run the prior repro or redo completed work. A "let me verify from scratch" pass means you're treating the trail as untrustworthy when it's authoritative.
4. Route the remaining work to the matching playbook and pick the verdict: continue the execution, ship a finished recommendation, ratify or override a prior conclusion, or postmortem a failed run. The pickup playbook ends here. The routed playbook owns the rest.
5. Verify the inherited claims against the original goal on the real artifact (the **principle-prove-it-works** skill). A passing prior self-report is not the proof.

**Reply:** where the prior agent stopped, what you inherited vs redid (ideally nothing redone), the resume point, and the outcome.
