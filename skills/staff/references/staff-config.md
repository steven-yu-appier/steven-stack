# Staff config

Read task-relevant settings from `~/.config/steven-stack/staff-config.toml` and pass them to workers. Use the [template](staff-config.example.toml) for setup. Explicit task instructions override defaults.

- **Git.** Set `git.name` and `git.email` per commit with `git -c user.name=… -c user.email=… commit`. Verify the author and `git.final_trailer`.
- **GitHub and Jira.** Match the authenticated identity to `github.user` or `jira.user` on the target host. Use that same account as the default assignee for new PRs or engineering Tasks. Resolve Jira names to unique accounts. Preserve assignments on updates.
- **Jira team.** Assign or mention a contact only when requested. Use task context to select among role members.
- **Ticket defaults.** Apply the label and sprint at creation when project and team both match. Resolve the sprint's current ID.

Credentials stay with the CLI or connector. A missing setting blocks only operations that need it.
