#!/usr/bin/env python3
"""Create a task archive and remove only its marked scratch directory."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import uuid


MARKER = ".steven-stack-run.json"


def plans_root():
    return Path.home() / ".local" / "share" / "plans"


def start(args):
    if args.ticket:
        if not re.fullmatch(r"[A-Z][A-Z0-9]+-[0-9]+", args.ticket):
            raise ValueError("invalid Jira key")
        bucket = Path(args.ticket)
    else:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.task):
            raise ValueError("task slug must contain lowercase letters, digits and hyphens")
        bucket = Path("_adhoc") / args.task

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:8]
    root = plans_root().resolve()
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    archive = root / bucket / run_id
    if not archive.resolve().is_relative_to(root):
        raise ValueError("archive escapes plans root")
    archive.mkdir(mode=0o700, parents=True)
    scratch = Path(tempfile.mkdtemp(prefix="steven-stack-")).resolve()
    record = {
        "archive_dir": str(archive),
        "scratch_dir": str(scratch),
        "temp_root": str(scratch.parent),
        "run_id": run_id,
    }
    try:
        (scratch / MARKER).write_text(json.dumps(record), encoding="utf-8")
    except OSError:
        shutil.rmtree(scratch)
        archive.rmdir()
        raise
    return record


def finish(args):
    scratch = Path(args.scratch).absolute()
    if scratch.is_symlink():
        raise ValueError("scratch directory must not be a symlink")
    scratch = scratch.resolve()
    if not scratch.name.startswith("steven-stack-"):
        raise ValueError("not a task scratch directory")
    if not scratch.exists():
        return {"removed": False, "scratch_dir": str(scratch)}
    if hasattr(os, "geteuid") and scratch.stat().st_uid != os.geteuid():
        raise ValueError("scratch directory is owned by another user")
    marker = scratch / MARKER
    if marker.is_symlink():
        raise ValueError("scratch marker must not be a symlink")
    record = json.loads(marker.read_text(encoding="utf-8"))
    if record["scratch_dir"] != str(scratch):
        raise ValueError("scratch marker does not match directory")
    if record.get("temp_root") != str(scratch.parent):
        raise ValueError("scratch marker has a missing or mismatched origin temp root")
    archive = Path(record["archive_dir"]).resolve()
    if not archive.is_relative_to(plans_root().resolve()) or archive == plans_root().resolve():
        raise ValueError("archive is outside plans root")
    if not archive.is_dir() or not os.access(archive, os.R_OK | os.X_OK):
        raise ValueError("archive is unavailable; retaining scratch")
    shutil.rmtree(scratch)
    return {"removed": True, "archive_dir": str(archive), "scratch_dir": str(scratch)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    setup = commands.add_parser("start")
    identity = setup.add_mutually_exclusive_group(required=True)
    identity.add_argument("--ticket")
    identity.add_argument("--task")
    cleanup = commands.add_parser("finish")
    cleanup.add_argument("--scratch", required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(start(args) if args.command == "start" else finish(args)))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
