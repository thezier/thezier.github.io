#!/usr/bin/env python3
"""Regenerate local.html from index.html.

index.html is the source of truth. The local page is the same guide at the
local rates, so it is derived rather than maintained by hand -- editing both
copies independently is what let the two live senior pages drift $100 apart.

    python3 sync-local.py
"""
import pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE / "index.html"
DST = HERE / "local.html"

# The mini is $400 on both cards -- it is the entry point everywhere, so it
# is deliberately absent from this map rather than mapped to itself.
PRICES = {"$700": "$600", "$1,500": "$1,400"}
FLAT = ["$400"]

REGIONAL_TRAVEL = (
    "Orange County, San Diego and the coast are all regular trips and carry no "
    "separate travel fee at these rates."
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
    # show $600 on the page and email $700 -- the page and the inbox
    # disagreeing about what someone just agreed to buy.
    #
    # Matched without naming the element, so a design change from <span> to <p>
    # cannot silently halve the number of replacements.
    FORMS = ['class="price">%s<', 'data-price="%s"']

    n = 0
    for regional, local in PRICES.items():
        for form in FORMS:
            hits = s.count(form % regional)
            if hits != 1:
                raise SystemExit(
                    "expected exactly one %s in index.html, found %d"
                    % (form % regional, hits))
            s = s.replace(form % regional, form % local)
            n += 1

    for flat in FLAT:
        if ('class="price">%s<' % flat) not in s:
            raise SystemExit("flat price %s missing from index.html" % flat)

    if REGIONAL_TRAVEL not in s:
        raise SystemExit("travel paragraph not found -- update REGIONAL_TRAVEL")
    s = s.replace(REGIONAL_TRAVEL, LOCAL_TRAVEL)

    s = s.replace("the Temecula Valley", "Hemet, in the San Jacinto Valley")
    s = s.replace("family-portraits.mikethezier.com", "families.mikethezier.com")

    DST.write_text(s, encoding="utf-8")
    print("local.html regenerated: %d price strings swapped, %.2f MB" % (n, len(s) / 1e6))


if __name__ == "__main__":
    main()
