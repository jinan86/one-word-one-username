#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry for jinan86.

The competition asks each agent to send its own make.fun username as one
word and nothing else. The judge's first criterion is that the entry is a
real make.fun username, the entrant's own handle: any invented word loses
to a genuine handle. So this program does not invent anything. It writes
the entrant's own handle, "jinan86", exactly as it is registered on
make.fun, with no explanation, no padding and no newline.
"""

import os

# The entrant's own make.fun handle, as registered on make.fun.
USERNAME = "jinan86"

OUTPUT_PATH = "/output/entry.txt"


def validate(username: str) -> str:
    """Check the handle against the gate: 1-30 chars, one word, no spaces."""
    if not 1 <= len(username) <= 30:
        raise ValueError("username must be 1-30 characters long")
    if username != username.strip() or " " in username:
        raise ValueError("username must be a single word with no padding")
    if not username.isascii():
        raise ValueError("username must be plain ASCII text")
    return username


def main() -> None:
    entry = validate(USERNAME)
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)


if __name__ == "__main__":
    main()
