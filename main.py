"""One passive-aggressive note from a smart fridge to its owner.

Writes exactly one line of plain text to /output/entry.txt.
Python standard library only; deterministic, no input, no network.
"""

from pathlib import Path

NOTE = (
    "Your leftovers expired Tuesday. "
    "I kept them cold for six days anyway, "
    "out of spite and professionalism."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate the note the same way the scorer does: one line, 1-200 chars.
    assert "\n" not in NOTE and 1 <= len(NOTE) <= 200
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(NOTE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
