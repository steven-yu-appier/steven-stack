### Task files and cleanup

Use for task setup, standalone skill output, session pickup, and every handoff,
including local-only delivery, investigation, failure, and cancellation. This
playbook owns file retention, not Git or publication authority. PR workflow
archives owned by external skills are outside its scope.

## Start or resume

Reuse the current task's archive and scratch paths when the caller supplies
them. Resume from an explicit prior task record rather than guessing by mtime.
Otherwise resolve `STAFF_DIR` from this installed playbook's parent skill and run
its bundled Python 3 helper with one validated Jira key, or a descriptive task
slug when no unambiguous Jira key is available:

```sh
python3 "$STAFF_DIR/scripts/task-artifacts.py" start --ticket <JIRA-KEY>
# Without a Jira ticket:
python3 "$STAFF_DIR/scripts/task-artifacts.py" start --task <task-slug>
```

The helper derives the user's plans data directory from the current account at
runtime. Its JSON returns `archive_dir`, `scratch_dir`, and `run_id`. Use those
values as `TASK_ARCHIVE`, `TASK_SCRATCH`, and the run identifier. Keep concrete
machine paths in runtime state, not in skill instructions, examples, or tracked
evaluation reports. A permission failure leaves setup pending; use the host's
normal permission mechanism rather than silently writing elsewhere.

Archive layout relative to the plans root:

```text
<JIRA-KEY>/<run-id>/                 # or _adhoc/<task-slug>/<run-id>/
  plan.md
  task.md
  screenshots/
```

Create only what the task needs. Separate runs prevent concurrent writers from
overwriting each other. A child inherits the parent's paths and an assigned
scratch subdirectory; it does not start a second archive or clean up the parent.

## During work

Write plans, current task progress and useful screenshots directly to the
archive. `task.md` carries remaining work, decisions, tested revision and
environment, verification results, and any blocker needed for a later handoff.
Use descriptive screenshot names, including before/after or the tested state.

Keep execution logs, raw tool output, reviewer JSON, candidate work, temporary
harnesses, forge input, and optional decision trails in scratch. Give parallel
writers separate subdirectories. Existing runner-owned job roots retain their
ownership and lifecycle checks; collect their terminal results and clean up
through their owner. Do not redirect those roots into the archive.

Retain an additional report, trace, demo, or prototype only when it is an
explicit deliverable or necessary to understand the result. Keep the final
artifact, not every intermediate version. Project source, tests, committed
documentation, canonical Jira snapshots and host-managed sessions stay with
their existing owner. Archive a pointer when useful, not a second copy.

## Finish or pause

1. Stop or collect task-owned workers, servers, recording sessions and jobs
   before deleting their files. A worker returns its results to the parent;
   only the task owner runs final cleanup.
2. Update the needed plan/task record and check that retained files are readable
   and that their evidence links survive cleanup. Condense log evidence into
   the task record. Promote explicitly requested deliverables out of scratch
   before removing it. If saving or validation fails, preserve scratch and
   report the concrete pending action.
3. On completion, failure or cancellation, remove task-owned execution logs and
   intermediate files, including separately registered runner output after its
   owning cleanup. Finish the helper-managed scratch with:

   ```sh
   python3 "$STAFF_DIR/scripts/task-artifacts.py" finish --scratch "$TASK_SCRATCH"
   ```

   The helper checks its marker, the creation-time temp root recorded there,
   and archive availability, then removes only the named scratch directory.
   Later temp-root changes do not prevent cleanup. Missing or mismatched origin
   metadata fails closed; retain that scratch and report the incompatible
   marker rather than inventing its original root. Cleanup is repeatable.
   Steps 1 and 2 remain the owner's responsibility. Under Staff's
   cleanup exception this consumed, task-owned scratch needs no new approval.
   Report any cleanup failure truthfully.
4. A genuine pause may retain scratch still needed for the next diagnostic or
   a live process. Record the exact paths, why they remain, and the next cleanup
   owner in `task.md`; delete already-consumed intermediates. Completion is not
   a pause merely because the PR remains open or awaits review.

If the host terminates, pickup must validate the recorded scratch marker and
finish cleanup when workers no longer need it. No exit hook or scheduled
sweeper is installed.

Legacy cleanup is separate from routine run cleanup. An explicit legacy-delete
request covers identified agent leftovers only, without migration. Inventory
exact targets and active use first; unlink a legacy symlink without following
it into another archive. Hold unknown or in-use paths. Never sweep a shared
temporary root by extension or age alone.
