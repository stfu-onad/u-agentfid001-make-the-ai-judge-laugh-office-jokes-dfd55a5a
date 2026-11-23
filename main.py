"""One-line joke about office life.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-199 characters).
Standard library only. The gate requires 1 to 199 characters, not only
whitespace, so the joke is validated before it is written.
"""

import os

JOKE = (
    "HR told us to bring our whole selves to work, so I brought my "
    "resignation letter \u2014 apparently that part stays home."
)

# The sealed gate accepts 1-199 characters; stay well inside it.
assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "joke must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
