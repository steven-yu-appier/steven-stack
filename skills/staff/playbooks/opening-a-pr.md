### Opening a PR

Invoked at the end of every other playbook.

**Worktree.** Work from a git worktree off main. Delegates receive its path explicitly. Concurrent writers on the same branch each get their own worktree, or `git fetch && git reset --hard origin/<branch>` between them. Dirty branch with unrelated work: patch out, fresh worktree, apply. Snarled worktree: reset from main, redo minimally.

**Commits.** Commit liberally. Rebase into small, ordered commits before opening PRs. Each commit is a future PR: landable, ordered to tell the story. Amend when the fix belongs in a just-made commit. New commit when separable. Follow the format in [`/playbooks/writing-a-commit.md`](writing-a-commit.md).

**PRs.** Run `/deslop` over the diff before commit. Run `/no-comments` before review. Write every PR title, PR description, and commit body with `/technical-writing`, then apply `/unslop`. Apply every technical-writing layer except Diátaxis. Use one word for each action, keep articles, and avoid `-ing` when a plain verb works.

**Titles.** Use Conventional Commits in the form `type(scope): subject`. Use `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, or `perf` as the type. Use the changed app scope in the commits as the scope. Omit the scope if none exists in the commits. Keep the subject short and imperative. Name a real symbol when one carries the change. Append exact head branch name. For example, `AI-30704 feat: add persisted codex task recovery foundation`. Do not add a trailing period.

**Description ownership.** This playbook owns the complete PR body. Do not invoke another PR-description skill on its behalf. When the user explicitly names one, use its requested presentation conventions within this playbook's gathering, evidence, freshness, publication, and readback requirements; do not transfer ownership of the body or publication workflow. Read [`../references/pr-change-outline.md`](../references/pr-change-outline.md) for the visual conventions used below.

Explicit user instructions may replace the default body format or request a retained copy. They do not waive reading the complete change, labeling evidence truthfully, checking freshness, or reading the published result back. When the repository supplies a required pull-request template, use it as the outer structure and map the content below into its closest sections. Do not append a second template.

**Voice.** Write as one human talking to another. Avoid jargon and slang. Use simple, coherent, concise language. Use the repository's domain terms and real code symbols when they are the clearest words. Explain an unfamiliar term once. Do not compress the description into fragments that make the reviewer reconstruct the meaning.

**Purpose.** The PR body is a briefing, not the lab notebook. A reviewer and the future reader of the squash commit should learn why the change exists, the shape of the implementation, what deserves scrutiny, and how the author proved that the behavior works. The squash commit body is the PR body. Keep it near 40 lines. Use at most one compact `text` or `diff` block that remains readable as raw Markdown. Do not use Mermaid, HTML, task-artifact blocks, or a standalone link header.

Use this default template:

````markdown
## Why

<State the observable before and after in one or two short sentences. Name the approach only when it helps explain the result. Link the ticket or motivating review comment from the relevant sentence.>

## Change outline

<Use one short paragraph or the smallest useful structural view. Show relationships, ownership, order, or data flow. Do not repeat the file diff.>

<State a material out-of-scope boundary when needed.>

## Tradeoffs and risk

- <Explain a non-obvious decision or rejected alternative.>
- <Name a compatibility, migration, rollout, rollback, or blast-radius concern.>
- <When the base branch is failing, state the continuing cost of leaving it unfixed.>

## Verification

- [x] <State behavior that the author verified on the current source state>. [Evidence](...)
- [ ] Reviewer check: <State a manual action that a reviewer can repeat with normal access.>

<If needed, state a blocked check or coverage limit in prose.>
````

`Why`, `Change outline` and `Verification` are required in the default template. Omit `Tradeoffs and risk` when it has nothing material to say. Do not write `None.`.

**Gather before writing.** Read the linked ticket or specification, the complete diff, the commit list, changed files, and enough surrounding code to understand ownership and behavior. For an existing PR, also read its current body, the motivating review comment, any accepted comment that changed scope, and any verification-evidence comment. Treat the existing body as context; rebuild its claims from the current full diff. Do not read every comment by default. Capture the current PR or branch head as `draftHead` before drafting.

**Change outline.** Use prose when prose is clearer. Use at most one visual. Split the PR when one bounded view cannot explain its independent changes.

**Verification states.** Checked items report author-run behavioral evidence from the current source state and link the retained evidence when available. Unchecked items begin with `Reviewer check:` and describe actions a reviewer can repeat with normal access, documented tooling, and available builds. Failed, blocked, unexecuted, or incomplete coverage appears in prose with the concrete status and reason. Do not disguise it as a reviewer task. Do not include type-check, lint, git diff, build, compile, or routine test commands. For a performance change, report one primary number with its unit in `before → after` form. Do not claim that old evidence applies to the current head because later changes appear unrelated. State the tested source when the evidence comes from a different source state.

**Freshness gate.** Immediately before creating or updating the PR, read the current head again. If `currentHead != draftHead`, refresh the commits and diff, revise every affected section and set `draftHead = currentHead`. Do not publish until the draft describes the current head.

**Body file.** Use a task-specific temporary file for the forge command. Do not retain one file per PR by default. When the user requests a retained copy, save it separately, keep it synchronized with the reviewed draft after every refresh, and still use a temporary forge input. Remove only the temporary file after publication. For a preview-only request, show the body without creating or updating the PR.

**Publish and read back.** Create or update the PR, then read its body and head from the forge. Confirm that the published body matches the reviewed draft, the selected template's headings appear once and in order, fenced blocks and links survived escaping, and the PR head still equals `draftHead`. If the head changed, refresh and publish again. Remove the temporary file after successful readback.

Attach videos or screenshots when they prove a claim. Do not paste full SHAs, swarm or arena lane recitals, lever-correction essays, file-by-file checklists, metric tables, or "CLEAN" verdicts. Put these details in a linked artifact. Do not use `## Summary` or `## Test plan` boilerplate. A commit body does not restate its subject.

**Forge.** Resolve the forge before the first PR operation and keep that choice for create, edit, view, watch, and merge. GitHub CLI (`gh`) is the default. If `command -v origin` succeeds and Origin can resolve the repository, prefer `origin pr ...`. If Origin is absent or cannot resolve the repository, stay on `gh` and record the fallback. Do not require Graphite (`gt`).

**Size and stacks.** Prefer five narrow PRs to one large PR. A stack is a base-branch chain. The root PR targets trunk. Each child branch rebases onto its parent's exact tip and its PR targets the parent branch. Create a child with `origin pr create --status open --base <parent-branch>` or `gh pr create --base <parent-branch>` according to the resolved forge. Retarget an existing child with `origin pr edit <pr> --base <parent-branch>` or `gh pr edit <pr> --base <parent-branch>`. Branch from trunk only for independent work. Rebase on trunk before substantial stack work.

**Readiness.** Open every PR as a draft. With Origin, pass `--status draft`. With `gh`, pass `--draft`. Run `origin pr view <number>` or `gh pr view <number>` before you refer to PR status.

**Babysit.** Opening a PR does not start a babysit. Post the URL and keep building. Finish the phase or stack first. Run a separate babysit pass only when the user asks for one after the whole stack exists. A babysit for each new PR stalls the build and spends checks on commits that later waves restart. Push back when feedback drifts from intent.

A subagent that opens a PR runs `interrogate`, `/deslop`, and `/no-comments`. It returns the URL and does not babysit. Return to the parent.
