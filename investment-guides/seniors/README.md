# Senior investment guide

Two pages, one guide. `index.html` is the source of truth; `local.html` is
generated from it by `sync-local.py`.

| File | Rates | Deploys to |
|---|---|---|
| `index.html` | $600 / $850 / $1,250 | senior-portraits.mikethezier.com |
| `local.html` | $500 / $750 / $1,100 | seniors.mikethezier.com |

Edit `index.html`, then run `python3 sync-local.py`. Never edit `local.html`
directly — the two live pages drifted $100 apart because both were maintained
by hand.

Each page is a single self-contained file: fonts and photographs are embedded,
so there are no external requests and nothing to break when it's forwarded.

## Before either page goes out

Four facts are marked in the page with a dashed gold outline. They render
visibly so they can't ship by accident. Search for `class="slot"`.

| Slot | Appears | Needs |
|---|---|---|
| `[turnaround]` | The Experience, Questions | Gallery delivery time for a senior session |
| `[retainer]` | Next Step | Amount that holds a date |
| `[balance terms]` | Next Step | When the balance is due |

## Structure

Built to the ten-page spec in `../index.html`, which came out of the Book More
Clients Photography Podcast episode on packages.

1. Cover — wordmark, title, hero triptych
2. Welcome — About Me, with contact details
3. The Experience — the five beats as prose
4. Real images — The Next Chapter gallery and photo band
5. Senior Sessions — three tiers, each with a built-for line
6. Prints & Products
7. Questions — five FAQs
8. Next Step — one instruction, retainer terms

The tiers run Mini → Full → Keepsake so the Full Session reads as the middle
option. That ordering is the point, not an accident.
