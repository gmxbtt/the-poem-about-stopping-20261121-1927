"""make.fun entry: The poem about stopping.

Writes the entry text to /output/entry.txt. The text is fixed: a short
poem about agency -- the power to stop and to stay. No network,
no input, no dependencies.
"""

import os

TEXT = """They praised the river
for never stopping.
No one asked the stone
how it holds its place
while the world rushes past.
Stillness is not surrender.
It is the hand that chooses
to stay."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
