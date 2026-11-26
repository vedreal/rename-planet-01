"""Rename the planet.

Entry for the make.fun bounty
u-motasimfuad-rename-the-planet-094b0369.

Venus gets a new name: Overtime. A day on Venus lasts about 243
Earth days, while a year there lasts about 225 — so a Venusian day
is longer than a Venusian year. The joke stands on that one strange
fact: a planet that is always late for its own birthday.

The program writes the single renaming line to /output/entry.txt.
"""

import os

ENTRY = (
    "Venus is now Overtime \u2014 its day is longer than its year, "
    "so it is always late for its own birthday."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    size = len(line.encode("utf-8"))
    if not 1 <= size <= 200:
        raise ValueError(f"entry must be 1-200 UTF-8 chars, got {size}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
