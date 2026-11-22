#!/usr/bin/env python3
"""Writes one short text to /output/entry.txt.

The text is fixed and hand-crafted: a quiet evening scene, written to
settle the reader rather than tell them to. No network, no randomness.
"""

from pathlib import Path

TEXT = (
    "Somewhere past the last email, the light goes amber on the kitchen wall, "
    "and a mug you forgot is still warm enough to hold with both hands. "
    "Nothing is asking for you. The evening sits there, patient as a cat "
    "asleep on the warm step, waiting for you to notice it is already yours."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
