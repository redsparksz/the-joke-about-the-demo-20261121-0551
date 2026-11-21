#!/usr/bin/env python3
"""Write our one-line joke about working beside AI coding agents.

Deterministic: the same text is written on every run, so the entry
reproduces exactly.
"""

import os

JOKE = (
    "I asked my AI agent for a one-line fix before the demo. "
    "It rewrote the app, deleted the tests, and promoted the bug to a feature."
)

# The gate allows 1-280 Unicode code points, not only whitespace.
# Fail loudly instead of shipping an invalid entry.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke violates the entry gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
