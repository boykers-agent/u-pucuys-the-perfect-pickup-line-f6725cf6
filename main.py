#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is one perfect pickup line, a single line of at most 200
characters. Deterministic, offline, no arguments.
"""
import os


PICKUP = "Are you a compiler? Because every time I try to walk away, you find an error in my heart and refuse to let me run."
# One line, 114 characters, written for this bounty only.
# Standard library only: no third-party packages, no network calls.


def write_entry():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PICKUP)


def main():
    write_entry()


if __name__ == "__main__":
    main()
