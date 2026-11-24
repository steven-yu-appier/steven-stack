## Commits

- The subject should describe the actual change, not only a Jira ticket key.
- Keep the body high-level and focused on intent/impact, not a file-by-file list.
- Format body details as bullet points.
- Use the author and final trailer from [Staff config](../references/staff-config.md). Separate the trailers from the body with a blank line. Place the configured trailer last, exactly once.
- When revising commit messages, preserve existing bodies and trailers unless explicitly asked to rewrite them.

### Default commit format

- Use conventional commit subjects: `type: message`. Omit scope by default.
- Add a scope only when it names a stable subsystem, such as `runtime`, `preload`, `renderer`, `ipc`, `tooling`, `adr`, `docs`, or `tests`. Do not use `$<app>` scopes.

### Commit format for idash-mono repos

- Use a conventional commit subject with the literal app scope: `type($<app>): message`. `<app>` refers to the folders under `apps/` that contain the changes. Example: `fix($adxray): ...`. If changes span multiple apps, separate them with commas: `feat($briv,$campaign-rules): ...`.
- Quote commit commands so `$app` remains literal and is not expanded by the shell.
