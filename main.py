"""make.fun entry — the poem about stopping.

A short poem about choosing to stay still while the world rushes on.
main.py writes the poem, exactly as written, to /output/entry.txt.
No network, no input, no dependencies.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = """They praised the river
for never stopping.
No one asked the stone
how it keeps its place
while the world hurries past.
Stillness is not surrender.
It is the hand that chooses
to stay."""

# A short poem: keep it well inside the 280-character limit.
assert 1 <= len(TEXT) <= 280


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
