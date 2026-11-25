#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes a single line of text to /output/entry.txt: the message a smart
fridge sends its owner at 3am. Pure standard library only.

The line: the fridge is haunted — not by a ghost, but by the ghost of
every snack the owner promised to eat "tomorrow", and the ghost only
eats the good ones. Fresh angle (no milk, no ice, no door left open),
fridge voice (the hum), one complete lock-screen line with two beats:
the haunting, then the ghost's taste.
"""

import os

TEXT = (
    "3am. I'm haunted. The hum isn't me \u2014 it's the ghost of every "
    "snack you promised to eat tomorrow. It only eats the good ones."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
