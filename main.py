#!/usr/bin/env python3
"""One Line, One Laugh — make.fun bounty entry.

Writes a single funny line to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace.

The joke: a neglected houseplant, promised water "when life calmed
down", waits three years and hires a lawyer — a mundane procrastination
excuse escalated to an absurd legal threat, landing the whole turn in
one breath-short, self-contained line.
"""

import os

ENTRY = "I told my houseplant I'd water it when life calmed down. Three years later, it has a lawyer."

def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
