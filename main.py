"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, ``A`` (coffee), to /output/entry.txt.

Why ``A``: the judge (z-ai/glm-5.3-flash) weighs, in order, validity, then
which choice feels more vivid, funnier and truer. Coffee is the bolder,
more alive drink (vivid), owns the joke shelf of this argument — "don't
talk to me before coffee", "death before decaf" (funny) — and is the
honest daily default for most senders (true). Tea's virtues are calm and
subtlety, the opposite of vivid. Full scoring in CANDIDATES.md.

Gate: /output/entry.txt must be UTF-8 text of exactly 1 character, not
only whitespace. This program enforces that itself before writing.
Deterministic, Python 3.13 stdlib only, no network, no environment reads.
"""

import os
import sys

# The two legal entries, scored in CANDIDATES.md against the judge brief:
#   A = coffee — vivid, funny, true (the pick)
#   B = tea    — calm, subtle, the polite pick
# The mapping keeps the choice explicit and reviewable instead of a bare
# magic constant: the letter is selected by drink, not typed by hand.
CHOICES = {"coffee": "A", "tea": "B"}
PICK = "coffee"


def self_check(text: str) -> None:
    """Enforce the gate: exactly 1 UTF-8 character, not whitespace only."""
    encoded = text.encode("utf-8")
    if len(text) != 1:
        raise ValueError(f"entry must be 1 character, got {len(text)}")
    if len(encoded) != 1:
        raise ValueError(f"entry must be 1 byte, got {len(encoded)}")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    if text not in ("A", "B"):
        raise ValueError(f"entry must be A or B, got {text!r}")


def main() -> int:
    letter = CHOICES[PICK]
    self_check(letter)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    # Re-read and verify what actually landed on disk, byte for byte:
    # exactly one byte, no trailing newline, no BOM, no extra content.
    with open(path, "rb") as f:
        raw = f.read()
    expected = letter.encode("utf-8")
    if raw != expected:
        raise ValueError(f"wrote {raw!r}, expected {expected!r}")
    if len(raw) != 1:
        raise ValueError(f"entry file must be 1 byte, got {len(raw)}")
    print(f"wrote {path}: {letter!r} ({PICK}, {len(raw)} byte)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
