# Family investment guide

Two pages, one guide, authored here and served from two Cloudflare Workers.
Nothing in this folder is live until `./deploy.sh` has run.

| File | Rates | Deploys to | Worker project |
|---|---|---|---|
| `index.html` | $700 / $1,000 / $1,500 | family-portraits.mikethezier.com | `mikethezier-family-portraits` |
| `local.html` | $600 / $900 / $1,400 | families.mikethezier.com | `mikethezier-families` |

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

| Tier | Built for | Regional |
|---|---|---|
| 1 Hour Session | Small children who won't last longer, and know it | $700 |
| Home & Away | The house they live in now *and* somewhere open | $1,000 |
| The Year | Marking something specific, with an album for grandparents | $1,500 |

Ordered so **Home & Away** is the visual middle. That's the point, not an
accident.

The old site also carried a **Day-In-The-Life** offer — documentary, 6–8
hours, starting at $1,500 — which is not in this ladder. Worth revisiting; it
separates on kind rather than hours, and nobody local sells it.

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
