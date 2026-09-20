# Family investment guide

Two pages, one guide, authored here and served from two Cloudflare Workers.
Nothing in this folder is live until `./deploy.sh` has run.

| File | Rates | Deploys to | Worker project |
|---|---|---|---|
| `index.html` | $400 / $700 / $1,500 | family-portraits.mikethezier.com | `mikethezier-family-portraits` |
| `local.html` | $400 / $600 / $1,400 | families.mikethezier.com | `mikethezier-families` |

`index.html` is the source of truth; `local.html` is generated from it. Edit
the first, then `./deploy.sh` — which syncs before deploying, so a forgotten
sync can't ship a stale price. **Never edit `local.html` directly.**

## Where the words came from

Most of this page is Mike's own copy, recovered rather than written:

- **"Connection is beautiful"** and the paragraph under it are verbatim from
  the 2025 family investment PDFs (Drive → Photography → Investment PDFs).
  Those PDFs preserve a clause the website crawl lost: *"...regardless whether
  you are all looking at the camera for a more traditional group portrait or
  candidly enjoying each other's company, we get to see the genuineness of who
  your family is."*
- **Your Environment** and the **Legacy** closing line are from the old
  Squarespace `/families` page. That page now 301s to `/contact/`, so the
  vault note and these PDFs are the only surviving copies.
- The **five beats** are written to match that voice, not replace it.

The twelve photographs were lifted out of the 2025 PDF's own image streams —
originals, already chosen by Mike for exactly this purpose.

## The ladder

| Tier | Built for | Regional | Local |
|---|---|---|---|
| Mini Session | One strong set without making an event of it | $400 | $400 |
| **1 Hour Session** | Room to breathe — more than one look | $700 | $600 |
| The Year | Marking something specific, with an album | $1,500 | $1,400 |

The mini is **$400 on both cards** — it is the entry point everywhere, so
`sync-local.py` lists it under `FLAT` rather than mapping it.

**The 1 Hour carries the gold outline, not the mini** — even though the mini
is what gets booked most. That is the diagnosis this whole guide exists to fix:
everyone defaults downward. Labelling the cheapest tier "most booked" would
push them there harder. The argument lives in its *why this over the mini*
line instead.

Watch the $700 → $1,500 gap once there are a few bookings. If nobody takes
The Year, the album tier probably wants to land nearer $1,200.

## How the page is built

`build/` holds the generator; `index.html` is its output, and `local.html` is
derived from that by `sync-local.py`. `deploy.sh` runs both before deploying,
so neither can go stale.

| File | Holds |
|---|---|
| `build/content.py` | Every word on the page |
| `build/d8_rail.py` | The layout and its CSS |
| `build/common.py` | Head, reset, the choose-form markup |
| `build/assets.json` | Fonts, wordmark and the twelve photographs, base64 |

Edit the words in `content.py`, not in `index.html` — the built page is one
self-contained 2MB document, and hand-editing it is how a stale price or a
wrong caption survives.

## Choosing a session

Identical to the senior guide: a radio per tier in a real form, `POST
/api/choose`, emails Mike the tier, price and rate card. Books nothing and
charges nothing — HoneyBook has no write API a Worker can reach. Works with
JavaScript off. See `../seniors/README.md` for the full notes.

### One-time setup per project

Both projects are new, so each needs the Resend key once:

```sh
cd /Users/mikethezier/Documents/GitHub/mikethezier-family-portraits
npx wrangler secret put RESEND_API_KEY

cd /Users/mikethezier/Documents/GitHub/mikethezier-families
npx wrangler secret put RESEND_API_KEY
```

Until it's set, choosing a session shows the "something went wrong, email me
directly" message rather than failing silently.
