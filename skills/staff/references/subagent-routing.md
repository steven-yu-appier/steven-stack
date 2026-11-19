# Subagent routing

Use this contract whenever a skill delegates work. The workflow chooses the role and whether delegation is required. [Model routing](model-routing.md) defines prescribed model routes. This file chooses the control method. Explicit independence or model-diversity gates remain required.

## Contents

- Select a control method
- Model routes
- Enforce access
- Build the child prompt
- Use a native subagent tool
- Handle unavailable routes

## Select a control method

1. Check the actual tool schema and host policy before planning a fan-out. Use the host's native subagent tool only when it can honor the requested model family, reasoning effort, access mode, and working directory. A skill does not override host restrictions on spawning or model selection.
2. Otherwise, follow **Handle unavailable routes**. Do not silently substitute a model or claim that an independent worker ran.

The host decides its own native tool syntax. `Task`, `Agent`, and similar names are examples of host APIs, not portable instructions.

## Model routes

When a workflow prescribes a model route, resolve its model and reasoning effort
in [Model routing](model-routing.md). For workflows without a prescribed route,
use the host defaults unless the user specifies a route. This file owns launch,
access control and result collection.

## Enforce access

Append the access arguments to the model arguments at launch. A prompt alone does not restrict tools.

| Agent kind | Read-only arguments                                                             | Write arguments            |
| ---------- | ------------------------------------------------------------------------------- | -------------------------- |
| `codex`    | `-s read-only -c approval_policy="never"`                                       | `-s workspace-write`       |
| `claude`   | `--permission-mode plan --disallowedTools Edit Write NotebookEdit ExitPlanMode` | `--permission-mode manual` |

Keep read-only workers in that mode for the whole task. Do not approve a switch to write access. Claude plan mode restricts tools through its permission system. It is not an OS sandbox. Disable mutating MCP tools and other write-capable extensions for either kind. If the available controls cannot enforce the required access, treat the route as unavailable.

For write delegates, assign a unique subdirectory of the task owner's scratch under [Task files and cleanup](../playbooks/task-artifacts.md). Pass the archive and scratch paths as runtime inputs. Keep source edits in the assigned worktree. Do not grant broader access just to save a report. Children return results without deleting shared task files; the parent condenses important results into the task record and owns cleanup.

## Build the child prompt

Every child prompt includes:

- The staff invocation as the first characters of the prompt, with text following on the same line. Use `$staff` for Codex and `/staff` for Claude Code. Claude Code loads the skill only when `/staff` starts the message.
- The role and any prescribed route name.
- Read-only or write access.
- The working directory or assigned worktree.
- File pointers instead of copied bulk context.
- The task's check scope and the absolute path to [Scoped checks](scoped-checks.md), with a required read before running or recommending checks.
- Success criteria and the expected output. Give each write delegate an absolute scratch file path for its complete report. Require it to finish the file before replying with the path. The report names changed files, verification results, and unresolved issues.

Read-only children return text. The parent saves long replies to the assigned report path. Never relax read-only access to obtain a report file. The native subagent tool handles result collection.

Tell a write-capable child which files it owns. Give concurrent writers separate worktrees or disjoint files. The parent reads every report and reviews every diff. The parent writes the final synthesis.

## Use a native subagent tool

When a route is prescribed, use its model and reasoning effort as native tool parameters. Otherwise omit those overrides. Translate the CLI settings in the tables into native tool controls; CLI arguments are not native tool parameters. A prompt-only access instruction does not satisfy **Enforce access**. Launch independent children before waiting for any child. A native tool is valid only when it can preserve any requested route, the access mode, and the working directory. Confirm each result belongs to the assigned task before accepting it.

Do not assume that a child inherits active skills. For a native Claude Code Agent child, give the absolute path to staff's `SKILL.md` and require the child to read and follow it before starting. Do not tell it to use the Skill tool or `/staff`. A literal `/staff` in an Agent prompt does not execute a slash command, and the Skill tool refuses staff because staff sets `disable-model-invocation: true`.

## Handle unavailable routes

For optional helper work, continue in the parent and state that delegation was unavailable. For required delegation or independent judgment, including **architect**, **arena**, and **interrogate**, mark the affected step pending and name the missing model or access control. Continue only work that does not depend on that step; do not ship while required work is pending. Never replace independent review with the parent's opinion, silently downgrade a route, or label a write-capable child read-only because its prompt asks it not to edit.
