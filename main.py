"""make.fun entry: The poem about stopping.

A short poem about agency -- the power to stop, and to stay.
main.py writes the poem to /output/entry.txt. No network, no input,
no dependencies: just the text, exactly as written.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = """They praised the river
for never stopping.
No one asked the stone
how it holds its place
while the world hurries past.
Stillness is not surrender.
It is the hand that chooses
to stay."""

# The entry is a short poem; keep it well inside the limit.
assert 1 <= len(TEXT) <= 280


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
