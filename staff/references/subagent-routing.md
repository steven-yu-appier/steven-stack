# Subagent routing

Use this contract whenever a skill delegates work. The workflow chooses the role and route. This file chooses the control method.

## Contents

- Select a control method
- Model routes
- Enforce access
- Build the child prompt
- Use a native subagent tool
- Delegate through the herdr skill
- Handle unavailable routes

## Select a control method

1. When `HERDR_ENV=1` and the **herdr** skill is installed, load it and follow its environment checks. A separate user request for Herdr is not required. Use it for pane-backed work and model families the host cannot launch itself. If the skill or its required environment is unavailable, try the next control method.
2. Otherwise, use the host's native subagent tool only when it can honor the requested model family and reasoning effort.
3. Otherwise, follow **Handle unavailable routes**. Do not silently substitute a model or claim that an independent worker ran.

The host decides its own native tool syntax. `Task`, `Agent`, and similar names are examples of host APIs, not portable instructions.

## Model routes

| Route | Agent kind | Launch arguments | Use |
| --- | --- | --- | --- |
| `gpt-6.1-sol-medium` | `codex` | `-m gpt-6.1-sol -c model_reasoning_effort="medium"` | Default code work |
| `gpt-6.1-sol-high` | `codex` | `-m gpt-6.1-sol -c model_reasoning_effort="high"` | Cross-provider candidates, architect sketches, direct code explanation, and independent review |
| `claude-opus-5.5-med` | `claude` | `--model claude-opus-5-5 --effort medium` | Prose and Judgement |
| `claude-opus-5.5-high` | `claude` | `--model claude-opus-5-5 --effort high` | Hard cross-cutting code and design, and independent cross-provider review |

Treat each row as one route. If the installed client rejects its arguments, the route is unavailable until the configuration is corrected. Do not weaken the route to make launch succeed.

## Enforce access

Append the access arguments to the model arguments at launch. A prompt alone does not restrict tools.

| Agent kind | Read-only arguments | Write arguments |
| --- | --- | --- |
| `codex` | `-s read-only -c approval_policy="never"` | `-s workspace-write` |
| `claude` | `--permission-mode plan --disallowedTools Edit Write NotebookEdit ExitPlanMode` | `--permission-mode manual` |

Keep read-only workers in that mode for the whole task. Do not approve a switch to write access. Claude plan mode restricts tools through its permission system. It is not an OS sandbox. Disable mutating MCP tools and other write-capable extensions for either kind. If the available controls cannot enforce the required access, treat the route as unavailable.

For write delegates, put the report in a unique scratch directory that the launch policy permits. Keep source edits in the assigned worktree. Do not grant broader access just to save a report.

## Build the child prompt

Every child prompt includes:

- The staff invocation as the first characters of the prompt, with text following on the same line. Use `$staff` for Codex and `/staff` for Claude Code. Claude Code loads the skill only when `/staff` starts the message.
- The role and exact route name.
- Read-only or write access.
- The working directory or assigned worktree.
- File pointers instead of copied bulk context.
- Success criteria and the expected output. Give each write delegate an absolute scratch file path for its complete report. Require it to finish the file before replying with the path. The report names changed files, verification results, and unresolved issues.

Read-only children return text. The parent saves long replies to the assigned report path. Never relax read-only access to obtain a report file. The chosen control method handles result collection.

Tell a write-capable child which files it owns. Give concurrent writers separate worktrees or disjoint files. The parent reads every report and reviews every diff. The parent writes the final synthesis.

## Use a native subagent tool

Use the route name to select the native model and reasoning effort. Launch independent children before waiting for any child. A native tool is valid only when it can preserve the requested route, access mode, and working directory.

Do not assume that a child inherits active skills. For a native Claude Code Agent child, give the absolute path to staff's `SKILL.md` and require the child to read and follow it before starting. Do not tell it to use the Skill tool or `/staff`. A literal `/staff` in an Agent prompt does not execute a slash command, and the Skill tool refuses staff because staff sets `disable-model-invocation: true`.

## Delegate through the herdr skill

Read and follow the installed [herdr skill](../../herdr/SKILL.md) before issuing control commands. It owns pane creation, agent launch, waits, result collection, and cleanup. Pass it the chosen agent kind, model and access arguments, working directory, child prompt, and report path.

Claude Code wraps a pasted prompt of four or more lines, or about 800 characters, as pasted content, and a `/staff` inside that wrapper never loads. A full child prompt is longer than that. Write it to a brief file in a unique scratch directory, then send a one-line prompt under 700 characters that points to it, as in `/staff Role: reviewer. Route: claude-opus-5.5-high. Read and follow the brief at /abs/scratch/brief.md.`

Launch independent workers before waiting for any worker. Confirm each result belongs to the assigned task before accepting it.

## Handle unavailable routes

For optional helper work, continue in the parent and state that delegation was unavailable. For workflows that require independent or diverse judgment, including **arena** and **interrogate**, stop that workflow and name the unavailable route. Do not replace independent review with the parent's own opinion.
