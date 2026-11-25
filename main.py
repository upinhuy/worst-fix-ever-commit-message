#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes a single commit message, at most 100 characters, for the bug fix
that made everything worse, to /output/entry.txt.
"""

import os

COMMIT_MESSAGE = "fix: removed the bug and, as a precaution, the entire feature"


def main() -> None:
    # The gate requires UTF-8 text of 1 to 100 characters, not only whitespace.
    assert 1 <= len(COMMIT_MESSAGE) <= 100, len(COMMIT_MESSAGE)
    assert COMMIT_MESSAGE.strip(), "commit message must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMIT_MESSAGE + "\n")


if __name__ == "__main__":
    main()
