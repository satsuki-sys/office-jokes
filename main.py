#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line joke about office life to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

JOKE = (
    "They built an open-plan office for collaboration, so now we wear "
    "noise-cancelling headphones and Slack the person sitting three feet away."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
