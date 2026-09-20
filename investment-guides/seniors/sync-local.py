#!/usr/bin/env python3
"""Regenerate local.html from index.html.

index.html is the source of truth. The local page is the same guide at the
local rates, so it is derived rather than maintained by hand -- editing both
copies independently is what let the two live senior pages drift $100 apart.

Run this after any edit to index.html:

    python3 sync-local.py
"""
import re
import pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE / "index.html"
DST = HERE / "local.html"

# Regional price -> local price. Order matters: longest first is not an issue
# here because each appears only inside a <span class="price"> tag.
PRICES = {"$600": "$500", "$850": "$750", "$1,250": "$1,100"}

REGIONAL_TRAVEL = (
    "Orange County, San Diego and the coast are all regular trips and "
    "carry no separate travel fee at these rates."
)
LOCAL_TRAVEL = (
    "These are my local rates, for sessions in the San Jacinto Valley and the "
    "Temecula Valley. Ask me about dates further out and I&rsquo;ll send the "
    "rates for those."
)


def main():
    s = SRC.read_text(encoding="utf-8")

    # A price appears twice per tier: once as displayed type, once in the
    # data-price the choose control sends to Mike. Missing the second one would
    # show $500 on the page and email $600 -- the page and the inbox
    # disagreeing about what someone just agreed to buy.
    FORMS = ['<span class="price">%s</span>', 'data-price="%s"']

    n = 0
    for regional, local in PRICES.items():
        for form in FORMS:
            if form % regional not in s:
                raise SystemExit(
                    "price %s not found in index.html as %s" % (regional, form % "X"))
            s = s.replace(form % regional, form % local)
            n += 1

    if REGIONAL_TRAVEL not in s:
        raise SystemExit("travel paragraph not found -- update REGIONAL_TRAVEL")
    s = s.replace(REGIONAL_TRAVEL, LOCAL_TRAVEL)

    s = s.replace("the Temecula Valley", "Hemet, in the San Jacinto Valley")
    s = s.replace("senior-portraits.mikethezier.com", "seniors.mikethezier.com")

    DST.write_text(s, encoding="utf-8")
    print("local.html regenerated: %d price strings swapped, %.2f MB" % (n, len(s) / 1e6))


if __name__ == "__main__":
    main()
