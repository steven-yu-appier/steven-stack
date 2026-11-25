"""Check the verdict and BLOCK evidence fields for every assigned AC."""

import argparse
import re
import sys
from pathlib import Path


def check(record, expected):
    errors = []
    seen = set()
    sections = re.split(r"^## AC ([^\n]+)\n", record + "\n", flags=re.MULTILINE)
    for ac, body in zip(sections[1::2], sections[2::2]):
        ac = ac.strip()
        if ac in seen or ac not in expected:
            errors.append(f"AC {ac}: unexpected or duplicate section")
        seen.add(ac)
        verdicts = re.findall(r"^Verdict:[ \t]*(.*)$", body, re.MULTILINE)
        if len(verdicts) != 1 or verdicts[0].strip() not in {"PASS", "FAIL", "BLOCK"}:
            errors.append(f"AC {ac}: expected one PASS, FAIL or BLOCK verdict")
        elif verdicts[0].strip() == "BLOCK":
            for field in ("Attempt", "Error"):
                values = re.findall(rf"^{field}:[ \t]*(.*)$", body, re.MULTILINE)
                if len(values) != 1 or values[0].strip().casefold() in {
                    "", "-", "n/a", "none", "todo", "tbd",
                }:
                    errors.append(f"AC {ac}: missing {field} evidence")
    errors.extend(f"AC {ac}: missing section" for ac in sorted(expected - seen))
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("ac", nargs="+", help="expected AC identifiers")
    args = parser.parse_args()
    errors = check(args.record.read_text(encoding="utf-8"), set(args.ac))
    if errors:
        sys.exit("\n".join(errors))
