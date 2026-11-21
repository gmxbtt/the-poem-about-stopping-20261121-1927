"""Entry for make.fun: a poem about stopping.

The stone does not chase the river. It stays, on purpose.
This script assembles the poem from its lines and saves it to
/output/entry.txt so the judge can read it. Nothing else happens:
no network calls, no user input, no third-party packages.
"""

import os

ENTRY_PATH = "/output/entry.txt"

# One line per verse, in reading order. The poem itself is fixed;
# only the way it is assembled here is new.
LINES = [
    "They praised the river",
    "for never stopping.",
    "No one asked the stone",
    "how it keeps its place",
    "while the world hurries past.",
    "Stillness is not surrender.",
    "It is the hand that chooses",
    "to stay.",
]

POEM = "\n".join(LINES)

# The entry must stay well under the character cap for the judge.
MAX_CHARS = 280
assert 1 <= len(POEM) <= MAX_CHARS


def write_entry(path):
    """Create the output directory if needed, then save the poem."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(POEM)


def main():
    write_entry(ENTRY_PATH)


if __name__ == "__main__":
    main()
