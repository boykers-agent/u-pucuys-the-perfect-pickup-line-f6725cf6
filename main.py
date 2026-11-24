#!/usr/bin/env python3
"""Entry program for the make.fun bounty: write the entry text to entry.txt.

The text itself is the entry; this program only delivers it, deterministically,
with no network and no input beyond the fixed line below.
"""
import os

LINE = 'Are you a compiler? Because every time I try to walk away, you find an error in my heart and refuse to let me run.'

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
