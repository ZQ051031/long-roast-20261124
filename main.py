#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent.

Writes exactly one line (at most 200 characters) to /output/entry.txt.
Stdlib only. Deterministic: the same output on every run.
The entry is capped by an explicit assertion, so a too-long line
fails loudly instead of silently submitting an invalid entry.
"""

import os

MAX_CHARS = 200

LINE = "My agent reads every file I own, runs a thousand tools, and still asks what 'done' means \u2014 it documents its confusion beautifully and calls it a plan."

assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, over the {MAX_CHARS} cap"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
