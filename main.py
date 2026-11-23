#!/usr/bin/env python3
"""One-letter entry: coffee or tea. The letter A means coffee."""

import os

LETTER = "A"  # A = coffee, B = tea. Coffee wins: it is the one that gets the day started.

OUT_PATH = "/output/entry.txt"


def main():
    # The gate wants exactly one character, not only whitespace, and only A or B.
    if len(LETTER) != 1 or LETTER.isspace() or LETTER not in ("A", "B"):
        raise ValueError("entry must be a single letter, A or B")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
