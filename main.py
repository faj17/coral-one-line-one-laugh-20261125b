#!/usr/bin/env python3
"""One Line, One Laugh entry (u-coral-404-one-line-one-laugh-22f2c9f3).

Writes a single hilarious line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.

v2: the line is assembled from fragments so the setup and the punchline
stay separate in the source; output is byte-identical to v1.
"""

import os

SETUP = "I bought a self-help book"
PUNCH = "and it filed a restraining order against me."


def assemble() -> str:
    """Join setup and punchline into the single entry line."""
    return f"{SETUP} {PUNCH}"


def validate(text: str) -> str:
    """Enforce the gate: 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
