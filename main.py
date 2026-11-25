#!/usr/bin/env python3
"""One Line, No Deadline Met -- deterministic entry writer.

Writes one single-line joke giving an excuse for missing a deadline
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only. No network, no randomness, no timestamps, no reading
anything outside this repository: the output is the same on every run.
"""

import os

EXCUSE = "I outsourced the deadline to future me, and future me subcontracted it to past me."

MAX_CHARS = 200


def validate(line):
    """Gate: exactly one non-blank line, 1..200 characters."""
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")


def write_entry(out_dir):
    """Validate the excuse, then write it as the single entry line."""
    validate(EXCUSE)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
