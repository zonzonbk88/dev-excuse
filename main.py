#!/usr/bin/env python3
"""Write one funny developer excuse for broken production code.

The program writes a single line to <output_dir>/entry.txt, where the
output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
Standard library only.
"""

import os

EXCUSE = (
    "Production broke because I fixed the bug by deleting the error "
    "message, and the error took it personally."
)


def main() -> None:
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    text = EXCUSE.strip()
    assert "\n" not in text and 1 <= len(text) <= 200, (
        f"gate failed: {len(text)} chars"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
