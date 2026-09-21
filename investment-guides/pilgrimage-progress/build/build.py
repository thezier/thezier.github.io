#!/usr/bin/env python3
"""Generate the Progress Sessions guide.

    python3 build/build.py

Writes ../index.html. Unlike the portrait guides there is no local card:
business buyers are quoted one rate, and the site already says Southern
California.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "_shared"))

import content as C
from common import load_assets
import rail

html = rail.build(C, load_assets(HERE))
(HERE.parent / "index.html").write_text(html, encoding="utf-8")
print("index.html written: %.2f MB" % (len(html) / 1e6))
