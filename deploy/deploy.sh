#!/usr/bin/env bash
# Rigenera la wiki e la pubblica su /srv/www/wiki.
#
# Non serve sudo: /srv/www/wiki appartiene a brix-ia dopo il setup
# iniziale (vedi README). Serve sudo UNA volta sola, per creare la
# directory e inserire lo snippet nginx.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET=/srv/www/wiki

cd "$REPO"

if [[ ! -d $TARGET ]]; then
    echo "ERRORE: $TARGET non esiste. Setup iniziale (una tantum):" >&2
    echo "  sudo mkdir -p $TARGET && sudo chown $USER:$USER $TARGET" >&2
    exit 1
fi

echo "── sync dal vault ──"
python3 sync.py

echo
echo "── build ──"
npx quartz build

echo
echo "── deploy ──"
# --delete per non lasciare in giro pagine spubblicate: se una pagina
# perde `publish: true`, deve sparire anche dal server.
rsync -a --delete public/ "$TARGET/"

echo
echo "✓ https://share.transizione-digital.it/wiki/"
echo "✓ https://brix-ia-linux.tail216abe.ts.net:10000/wiki/"
