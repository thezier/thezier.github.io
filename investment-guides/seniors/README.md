# Senior investment guide

Two pages, one guide, authored here and served from two Cloudflare Workers.
Nothing in this folder is live until `./deploy.sh` has run.

| File | Rates | Deploys to | Worker project |
|---|---|---|---|
| `index.html` | $600 / $850 / $1,250 | senior-portraits.mikethezier.com | `mikethezier-senior-portraits` |
| `local.html` | $500 / $750 / $1,100 | seniors.mikethezier.com | `mikethezier-seniors` |

`index.html` is the source of truth. `local.html` is generated from it.

```sh
./deploy.sh            # sync, then deploy both
./deploy.sh regional   # senior-portraits only
./deploy.sh local      # seniors only
```

Edit `index.html`, then deploy — the script runs `sync-local.py` first, so a
forgotten sync can't ship a stale price. **Never edit `local.html` directly.**
The two live pages drifted $100 apart because both were maintained by hand.

A price lives in two places per tier: the displayed `<span class="price">` and
the `data-price` the choose control sends. `sync-local.py` rewrites both and
fails loudly if either is missing — a page showing $500 while emailing $600
is the page and the inbox disagreeing about what someone just agreed to buy.

## Choosing a session

Each tier carries a **Choose this one** control. Picking one reveals a short
details block; sending it emails Mike the tier, the price, which rate card it
came from, and whatever they typed.

It books nothing and charges nothing. HoneyBook has no write API a Worker can
reach, and a page that told a family they were booked when no contract existed
would be a lie with a deposit attached. The contract and invoice are still
built by hand in HoneyBook afterwards. What this removes is the ambiguity about
which session they meant.

- `worker.js` → copied to each project's `src/index.js`. One route, `POST
  /api/choose`. Everything else falls through to the static asset.
- Works with JavaScript off: the tiers are radio buttons in a real form and the
  Worker answers with its own page. The script only adds the running
  "you've chosen X" line and an answer in place of a navigation.
- A bot that fills the honeypot gets the same 200 a person gets, and nothing
  is sent.
- If sending fails it says so. It never reports success for an email that was
  dropped.

### One-time setup per project

The Workers were static-assets only before this, so each needs the Resend key
once:

```sh
cd /Users/mikethezier/Documents/GitHub/mikethezier-senior-portraits
npx wrangler secret put RESEND_API_KEY

cd /Users/mikethezier/Documents/GitHub/mikethezier-seniors
npx wrangler secret put RESEND_API_KEY
```

Same key as the weddings Worker. Until it is set, choosing a session shows the
"something went wrong, email me directly" message rather than silently failing.

## Structure

Built to the ten-page spec in `../index.html`, from the Book More Clients
Photography Podcast episode on packages.

1. Cover — wordmark, title, hero triptych
2. Welcome — About Me, with contact details
3. The Experience — the five beats as prose
4. Real images — gallery and photo band
5. Senior Sessions — three tiers, each with a built-for line and a choose control
6. Prints & Products
7. Questions — five FAQs
8. Your details / Next Step — 50% retainer, balance on the day, HoneyBook

Tiers run Mini → Full → Keepsake so the Full Session reads as the middle
option. That ordering is the point, not an accident.
