"""Invent a Word We Need — one new word and its definition.

The program writes a single line to /output/entry.txt: one
newly coined English word together with its one-line
definition, at most 140 characters.
"""

import os

MAX_CHARS = 140
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# Chairdrobe: the chair where clothes too dirty for the closet
# but too clean for the wash wait out their fate. The gap is
# real — every home has one — and the word is English grown by
# analogy (like floordrobe, the floor version): chair + wardrobe,
# sayable, spellable, memorable. The definition lands in one
# reading, and the twist arrives at the last word: fate.
# It beats the near-misses: roomnesia names a real gap too, but
# the blend already circulates and sounds clinical; sockorphan
# is clunky to say and spell. Chairdrobe is the fresh one.
LINE = "Chairdrobe (n.): the chair where clothes too dirty for the closet but too clean for the wash wait out their fate."


def build_line():
    """Return the entry line, checked: one line, 1-140 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-140 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
