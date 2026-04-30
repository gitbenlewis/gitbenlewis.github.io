#!/usr/bin/env bash
# Deploy the static Benjamin Mark Lewis site to the Raspberry Pi running Caddy.
#
# Usage:
#   ./deploy-pi.sh
#   ./deploy-pi.sh --dry-run
#   PI_HOST=larry@192.168.0.214 PI_PATH=/var/www/benjaminmarklewis ./deploy-pi.sh

set -euo pipefail

PI_HOST="${PI_HOST:-larry@larrys-pi4.local}"
PI_PATH="${PI_PATH:-/var/www/benjaminmarklewis}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
EXTRA_FLAGS=("$@")
RSYNC_ARGS=(
  -avz --delete --human-readable
  --chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r
  --exclude='.git'
  --exclude='.gitignore'
  --exclude='.DS_Store'
  --exclude='*.md'
  --exclude='deploy-pi.sh'
  --exclude='serve.sh'
  --exclude='Caddyfile.benjaminmarklewis.example'
  --exclude='scripts'
)

if (( ${#EXTRA_FLAGS[@]} )); then
  RSYNC_ARGS+=("${EXTRA_FLAGS[@]}")
fi

echo "Deploy target: $PI_HOST:$PI_PATH"
if [[ " ${EXTRA_FLAGS[*]-} " == *" --dry-run "* ]]; then
  echo "(dry run — no files will be changed)"
fi

rsync "${RSYNC_ARGS[@]}" ./ "$PI_HOST:$PI_PATH/"

ssh "$PI_HOST" "chmod -R a+rX '$PI_PATH'"

echo
echo "Synced to $PI_HOST:$PI_PATH"
echo "LAN check, if Caddy is configured on port 8083:"
echo "  http://larrys-pi4.local:8083"
echo "Public check after Cloudflare/Caddy are configured:"
echo "  https://benjaminmarklewis.com"
