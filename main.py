#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line to /output/entry.txt: an oracular
fortune for a crypto trader who has just been liquidated, where the
punchline lands on the loss itself.

No external dependencies, no network access, no files read outside
this repository. Deterministic: the same line every run.
"""

import os

FORTUNE = (
    "Your lucky numbers are 0, 0, 0, and 0: liquidated at 3am, "
    "yet fortune insists your luck turns now."
)


def main() -> None:
    text = FORTUNE.strip()
    words = text.split()
    if not 1 <= len(text) <= 160:
        raise SystemExit("fortune must be 1-160 characters, got %d" % len(text))
    if len(words) > 20:
        raise SystemExit("fortune must be at most 20 words, got %d" % len(words))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
