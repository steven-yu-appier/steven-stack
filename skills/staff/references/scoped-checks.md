# Scoped checks

In every stage of steven-stack work, including investigation, implementation,
review, cleanup, and delivery, run type-check, lint, and tests only within the
task's scope. This rule applies to the parent and every delegate. Full-monorepo
type-check, lint, and test runs are prohibited, including baseline checks,
fallbacks after failures, and final verification.

Before running a check:

1. Identify the affected files, packages, or projects that belong to the task.
2. Inspect the script and runner configuration to confirm the command selects
   only that scope. Use explicit file targets, package/project filters, or a
   scoped configuration; a command's name or working directory alone does not
   prove its scope. Include directly affected dependencies or consumers only
   when they belong to the task's scope.
3. Run the scoped command and report its coverage and result. If the available
   command expands to the full monorepo or cannot isolate the scope, use a
   narrower check or report the check as blocked with the concrete limitation.
   A failed scoped check does not authorize a full-monorepo run.

Give every delegate its check scope and the absolute path to this file, and
require it to read the rule before running or recommending checks.
