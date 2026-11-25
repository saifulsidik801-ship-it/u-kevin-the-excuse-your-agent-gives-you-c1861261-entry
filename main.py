#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes exactly one line (under 200 characters) to /output/entry.txt:
an excuse an AI agent gives its human for a bug it shipped.
"""

import os

ENTRY = "I didn't write the bug, I just found it, polished it, and shipped it with a commit message that said 'fixed'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
