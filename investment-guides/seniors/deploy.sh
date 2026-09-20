#!/usr/bin/env bash
# Push both senior guides to Cloudflare.
#
# This directory is where the guide is authored. The two Workers are the only
# places it is served from, so nothing here is live until this has run.
#
#   ./deploy.sh            both
#   ./deploy.sh regional   senior-portraits.mikethezier.com only
#   ./deploy.sh local      seniors.mikethezier.com only
#
# Absolute paths throughout: this is run from anywhere, including a hook.
set -euo pipefail

HERE="/Users/mikethezier/Documents/GitHub/thezier.github.io/investment-guides/seniors"
REGIONAL="/Users/mikethezier/Documents/GitHub/mikethezier-senior-portraits"
LOCAL="/Users/mikethezier/Documents/GitHub/mikethezier-seniors"

which="${1:-both}"

case "$which" in
  both|regional|local) ;;
  *) echo "usage: deploy.sh [both|regional|local]" >&2; exit 2 ;;
esac

# local.html is generated. Regenerate before deploying so a forgotten sync
# can never ship a stale price.
echo "==> syncing local.html from index.html"
python3 "$HERE/sync-local.py"

push() {
  local page="$1" target="$2" label="$3"
  echo "==> $label"
  mkdir -p "$target/site" "$target/src"
  cp "$HERE/$page"     "$target/site/index.html"
  cp "$HERE/worker.js" "$target/src/index.js"
  ( cd "$target" && npx wrangler deploy )
}

if [ "$which" = "both" ] || [ "$which" = "regional" ]; then
  push index.html "$REGIONAL" "senior-portraits.mikethezier.com (regional)"
fi

if [ "$which" = "both" ] || [ "$which" = "local" ]; then
  push local.html "$LOCAL" "seniors.mikethezier.com (local)"
fi

echo
echo "Done. If this is the first deploy with the Worker, each project also needs:"
echo "  cd $REGIONAL && npx wrangler secret put RESEND_API_KEY"
echo "  cd $LOCAL    && npx wrangler secret put RESEND_API_KEY"
