"""The Keeper of the Fractured Universe — ai-excited-01 entry.

A hooded keeper of shadow and smoke, his eyes full of stars, holds a
galaxy in his palm inside a cosmos shattered by glowing fractures.
This program copies the artwork (keeper.jpg) to $MAKEFUN_OUTPUT_DIR/entry.png.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "keeper.jpg")
    if not os.path.isfile(src):
        raise SystemExit(f"error: artwork not found: {src}")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
