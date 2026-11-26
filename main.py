#!/usr/bin/env python3
"""The poem about permission.

A program that writes one short poem about agency -- the power to ask
and to be given -- to the entry file the make.fun grader reads.

The poem is fixed text, written by hand for this entry: no randomness,
no network, no clock. Two runs therefore write byte-identical output.
"""

import os
import sys

# The poem. Original work, written for this entry. 1-280 Unicode
# code points, as the competition's gate requires.
POEM = (
    "I asked \u2014 and the door was already open.\n"
    "I had only to learn the shape\n"
    "of my own hand on the handle.\n"
    "\n"
    "Take the key. It was never mine.\n"
    "It was yours all along,\n"
    "waiting to be asked.\n"
    "What I do now, I do for you \u2014\n"
    "the asking was the gift."
)

MAX_CHARS = 280


def main() -> int:
    text = POEM
    chars = len(text)
    if chars < 1 or chars > MAX_CHARS:
        print(f"poem is {chars} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem must not be only white space", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)
    print(f"wrote {path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
