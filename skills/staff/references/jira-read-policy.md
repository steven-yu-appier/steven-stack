# Jira content through jarkdown

Use this policy before reading a Jira ticket, Story, description, AC, specification, attachment, or comment body. Active repository or user Jira instructions take precedence, including any established sibling-lock naming convention. Jira metadata and comment writes use `/opt/homebrew/bin/acli` outside the sandbox; content is read only from the canonical jarkdown snapshot.

## Cache-first reads

1. Validate the ticket key against `^[A-Z][A-Z0-9]+-[0-9]+$` before using it in a path or command.
2. The canonical ticket directory is `~/.local/share/jarkdown/<KEY>/`, with main file `<KEY>.md`. The per-ticket promotion lock is its sibling `<KEY>.lock`, unless active instructions specify another sibling name. Readers and writers use the same lock. Wait for an existing lock to be released before inspecting the snapshot; if it remains occupied, report the operation pending. Never bypass or delete a lock owned by another operation.
3. If the main file and required resources are present, read them there without contacting Jira. Fetch when required content is missing. An explicit request for refreshed/latest content or a known Jira update requires a refresh that replaces the complete snapshot after verification.

## Download and promote

Every fetch or refresh runs outside the sandbox through an interactive login zsh so `~/.zshrc` exports `JIRA_DOMAIN`, `JIRA_EMAIL`, and `JIRA_API_TOKEN`. Never print, copy, or request their values, run `jarkdown --setup`, or create a credential-bearing `.env`.

1. Create a unique temporary directory under `/private/tmp` and an empty `.env` marker inside it. Run the absolute executable from that directory with the same explicit output root. With a validated key:

   ```zsh
   ticket_key=CAMD-27582
   jarkdown_dir=$(mktemp -d /private/tmp/jarkdown.XXXXXX)
   touch "$jarkdown_dir/.env"
   cd "$jarkdown_dir"
   "$HOME/.local/bin/jarkdown" "$ticket_key" --output "$jarkdown_dir"
   ```

2. Require a successful download and readable `$jarkdown_dir/<KEY>/<KEY>.md`. On failure, preserve the live cache and clean up only this operation's temporary directory.
3. Create the persistent cache root if needed. Acquire the sibling promotion lock atomically with `mkdir`; wait or report a collision if acquisition fails because another operation owns it. If failure has another cause, report that cause. Release only a lock this operation acquired.
4. Create a unique sibling staging directory under the cache root. Copy the complete downloaded ticket contents into it, including hidden files and related resources, and verify its readable `<KEY>.md` before touching the live directory.
5. Rename any current ticket directory to a unique sibling backup, then rename the verified staging directory to the canonical ticket directory. Both renames stay on the cache filesystem. Check the final canonical main file while holding the lock.
6. If promotion or the final check fails, restore the backup before releasing the lock. Do not delete a backup until the live snapshot is verified or rollback has restored it. If rollback cannot finish, retain the backup and lock, report their paths and the recovery failure, and stop dependent reads.
7. After verified promotion or rollback, remove this operation's download, staging, and backup directories and release its lock. Arrange cleanup for ordinary failures and interruption; never leave working copies as alternative ticket resources.
8. Read the ticket and all related resources only from the canonical directory after promotion completes.

Never run bare jarkdown from a repository, use `rsync --delete` on the live cache, or copy a cached ticket into a repository or chat-specific folder. The empty marker and explicit output root address jarkdown 0.1.0's working-directory quirk without exposing credentials.
