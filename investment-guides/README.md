# Investment guides

One design, one layout module, four live pages.

| Guide | Regional | Local |
|---|---|---|
| Senior | senior-portraits.mikethezier.com — $600 / $850 / $1,250 | seniors.mikethezier.com — $500 / $750 / $1,100 |
| Family | family-portraits.mikethezier.com — $400 / $700 / $1,500 | families.mikethezier.com — $400 / $600 / $1,400 |

```
_shared/
  rail.py      the layout and all of its CSS
  common.py    head, reset, the choose-a-session form
seniors/  family/
  build/content.py    every word on that guide
  build/assets.json   fonts, wordmark, photographs (base64)
  build/build.py      content + layout -> index.html
  sync-local.py       index.html -> local.html at the local rates
  deploy.sh           build, sync, deploy both cards
  worker.js           the /api/choose endpoint
```

**Edit `content.py`, never `index.html`.** The built page is one self-contained
1.5–2 MB document with every font and photograph inline; hand-editing it is how
a stale price or a wrong caption survives. `deploy.sh` rebuilds and re-syncs
before every deploy, so neither file can drift.

A design change in `_shared/rail.py` lands on every guide at once. That is the
point: the two senior pages once drifted $100 apart because each was maintained
by hand.

## Rules the build enforces

- **A price appears twice per tier** — as displayed type and in the `data-price`
  the form emails. `sync-local.py` rewrites both and fails unless it finds
  exactly one of each, so a page cannot show $500 while emailing $600.
- **A row is all-portrait at 3:4, or one landscape at its own ratio.** Mixing
  them crops a frame to an orientation it wasn't shot in. A row that wants that
  anyway ends with `"allow-crop"`, making it a decision rather than an accident.
- **A full-width row is capped to the frame's own pixel width**, so a 700px
  landscape is never blown up to fill a 912px column.

## The ladders

Senior: Mini $600 · **Full $850** · Keepsake $1,250
Family: Mini $400 · **1 Hour $700** · The Year $1,500

The middle tier carries the feature outline in both. On family that is
deliberate against the data — the 30-minute mini is the most-booked session,
and a "most booked" label on the cheapest tier would push people further down
the ladder, which is the problem these guides exist to fix.

## Choosing a session

Each tier is a radio in a real form posting to `/api/choose`, handled by
`worker.js` on each project. It emails Mike the tier, price, rate card and
message. It books nothing and charges nothing — HoneyBook has no write API a
Worker can reach, and telling a family they were booked when no contract exists
would be a lie with a deposit attached.

Works with JavaScript off. A bot filling the honeypot gets the same 200 a person
gets and nothing is sent. A failed send says so rather than reporting success.

Each Worker needs `RESEND_API_KEY` set once (`npx wrangler secret put`).
