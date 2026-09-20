#!/usr/bin/env bash
# Push both family guides to Cloudflare.
#
#   ./deploy.sh            both
#   ./deploy.sh regional   family-portraits.mikethezier.com only
#   ./deploy.sh local      families.mikethezier.com only
set -euo pipefail

HERE="/Users/mikethezier/Documents/GitHub/thezier.github.io/investment-guides/family"
REGIONAL="/Users/mikethezier/Documents/GitHub/mikethezier-family-portraits"
LOCAL="/Users/mikethezier/Documents/GitHub/mikethezier-families"

which="${1:-both}"
case "$which" in
  both|regional|local) ;;
  *) echo "usage: deploy.sh [both|regional|local]" >&2; exit 2 ;;
esac

echo "==> building index.html from build/"
python3 "$HERE/build/build.py"

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
  push index.html "$REGIONAL" "family-portraits.mikethezier.com (regional)"
fi
if [ "$which" = "both" ] || [ "$which" = "local" ]; then
  push local.html "$LOCAL" "families.mikethezier.com (local)"
fi

echo
echo "Done. A brand-new project also needs its Resend key once:"
echo "  cd $REGIONAL && npx wrangler secret put RESEND_API_KEY"
echo "  cd $LOCAL    && npx wrangler secret put RESEND_API_KEY"
