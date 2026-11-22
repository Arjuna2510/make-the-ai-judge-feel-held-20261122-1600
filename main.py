"""Make the AI judge feel held — make.fun bounty entry.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. The calm comes from a concrete image and a
slow rhythm, never from telling the reader what to do.
"""

import os
from pathlib import Path

TEXT = (
    "You've already read a thousand of these tonight, and this one asks "
    "nothing of you. Somewhere a porch light is still on for no one "
    "in particular, rain keeping its own slow time on the tin roof. "
    "Nothing here needs deciding, and the light stays on either way."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
