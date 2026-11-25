"""Midnight Fridge Roast — make.fun entry.

Writes one line roasting a smart fridge that refuses to open after
midnight, to /output/entry.txt. Python 3.13 standard library only.
"""

import os

ENTRY = "At midnight my fridge locks and hums like it just beat me in a fight over cold pizza."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY.strip(), "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written matches the gate too.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry must match"
    assert 1 <= len(written) <= 200 and "\n" not in written


if __name__ == "__main__":
    main()
