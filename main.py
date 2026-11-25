#!/usr/bin/env python3
"""One Line, No Deadline Met -- deterministic entry writer.

Writes one single-line joke giving an excuse for missing a deadline
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only. No network, no randomness, no timestamps, no reading
anything outside this repository: the output is the same on every run.
"""

import os

JOKE = "I outsourced the deadline to future me, and future me just quit."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
