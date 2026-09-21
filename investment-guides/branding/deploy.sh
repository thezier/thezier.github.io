#!/usr/bin/env bash
# Build and deploy the branding guide.
#
# One card only -- no local/regional split, so no sync step.
set -euo pipefail

HERE="/Users/mikethezier/Documents/GitHub/thezier.github.io/investment-guides/branding"
TARGET="/Users/mikethezier/Documents/GitHub/mikethezier-branding"

echo "==> building index.html from build/"
python3 "$HERE/build/build.py"

echo "==> branding.mikethezier.com"
mkdir -p "$TARGET/site" "$TARGET/src"
cp "$HERE/index.html" "$TARGET/site/index.html"
cp "$HERE/worker.js"  "$TARGET/src/index.js"
( cd "$TARGET" && npx wrangler deploy )

echo
echo "A brand-new project also needs its Resend key once:"
echo "  cd $TARGET && npx wrangler secret put RESEND_API_KEY"
