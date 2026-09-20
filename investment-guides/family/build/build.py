#!/usr/bin/env python3
"""Generate the family guide (regional card) from content + design.

    python3 build/build.py

Writes ../index.html. local.html is then derived from it by sync-local.py,
which deploy.sh runs for you.

Why a generator rather than a hand-edited file: the page is one self-contained
2MB document with every font and photograph inline. Editing that by hand is
how a stray price or a stale caption survives. The words live in content.py,
the layout in d8_rail.py, and the two only meet here.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import d8_rail

out = HERE.parent / "index.html"
html = d8_rail.build()
out.write_text(html, encoding="utf-8")
print("index.html written: %.2f MB" % (len(html) / 1e6))
