#!/usr/bin/env python3
"""Dad Joke Showdown entry — writes one dad joke to /output/entry.txt.

The joke: a classic question-and-answer dad joke, told the way a father
would tell it across the dinner table. The setup names an ordinary
barbecue; the punchline turns on "steaks" / "stakes" — the steaks are
high, so Dad brings a ladder. One clean pun, understood on the first
read, punchline at the very end.

Deterministic: the same bytes on every run. Standard library only, no
network, no input. The output directory itself is never removed — only
its contents are cleared — so the program also works when /output is
owned by root inside a sticky parent.
"""

import os
import sys

JOKE = "Why did the dad bring a ladder to the barbecue? He heard the steaks were high."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    text = JOKE
    if not (1 <= len(text) <= 200):
        print(f"joke is {len(text)} characters, outside the 1-200 gate", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1

    # Never remove the output directory itself; clear only its contents.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
