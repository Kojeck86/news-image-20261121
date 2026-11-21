#!/usr/bin/env python3
"""news-image-20261121 entry (Python 3.13, standard library only).

The finished front page is the entry.png beside this file; the program
copies it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set).

Outside the grader's container:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
_DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(_DST_DIR, exist_ok=True)
# A plain copy is byte-for-byte deterministic: two runs write identical bytes.
shutil.copyfile(_SRC, os.path.join(_DST_DIR, "entry.png"))
