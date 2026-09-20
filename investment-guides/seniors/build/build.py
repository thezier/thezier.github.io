#!/usr/bin/env python3
"""Generate the seniors guide (regional card).

    python3 build/build.py

Writes ../index.html. local.html is derived from it by sync-local.py, which
deploy.sh runs for you.

The words live in content.py; the layout is shared with every other guide in
../../_shared/rail.py, so a design fix lands on all of them at once.
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
