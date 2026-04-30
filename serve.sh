#!/usr/bin/env bash
set -euo pipefail
PORT="${PORT:-8080}"
echo "Serving Benjamin Mark Lewis site at http://localhost:${PORT}"
exec python3 -m http.server "$PORT"
