#!/usr/bin/env python3
"""
Installa la location /wiki/ nel server block del funnel nginx.

Va lanciato con sudo. E' idempotente: se la location c'e' gia', non
fa nulla.

    sudo python3 deploy/install-nginx.py

Cosa fa:
  1. crea /srv/www/wiki e la assegna all'utente che ha invocato sudo
  2. inserisce lo snippet PRIMA della `location /` finale (quella che
     ritorna 404), non in fondo al file: in nginx l'ordine conta e una
     prefix location piu' specifica deve precedere il catch-all
  3. valida con `nginx -t` e ricarica; se la validazione fallisce,
     ripristina il backup e non ricarica
"""

import os
import pwd
import shutil
import subprocess
import sys
from pathlib import Path

CONF = Path("/etc/nginx/sites-available/funnel")
SNIPPET = Path(__file__).parent / "wiki.nginx.conf"
TARGET = Path("/srv/www/wiki")
ANCHOR = "    # Tutto il resto: 404 pulito"


def main() -> int:
    if os.geteuid() != 0:
        print("Serve sudo:  sudo python3 deploy/install-nginx.py", file=sys.stderr)
        return 1
    for p in (CONF, SNIPPET):
        if not p.is_file():
            print(f"ERRORE: non trovo {p}", file=sys.stderr)
            return 1

    # 1. directory di destinazione, di proprieta' dell'utente reale
    user = os.environ.get("SUDO_USER") or pwd.getpwuid(os.getuid()).pw_name
    rec = pwd.getpwnam(user)
    TARGET.mkdir(parents=True, exist_ok=True)
    os.chown(TARGET, rec.pw_uid, rec.pw_gid)
    print(f"✓ {TARGET} (owner: {user})")

    # 2. inserimento snippet
    conf = CONF.read_text()
    if "location /wiki/" in conf:
        print("✓ location /wiki/ gia' presente, non tocco la config")
    else:
        if ANCHOR not in conf:
            print(f"ERRORE: non trovo il punto di inserimento ({ANCHOR!r}).\n"
                  f"La config e' cambiata: inserisci lo snippet a mano PRIMA\n"
                  f"della location / finale.", file=sys.stderr)
            return 1
        backup = CONF.with_suffix(".bak")
        shutil.copy2(CONF, backup)
        body = "\n".join("    " + ln if ln.strip() else ln
                         for ln in SNIPPET.read_text().splitlines())
        CONF.write_text(conf.replace(ANCHOR, body + "\n\n" + ANCHOR, 1))
        print(f"✓ snippet inserito (backup: {backup})")

        # 3. valida, e in caso di errore ripristina
        test = subprocess.run(["nginx", "-t"], capture_output=True, text=True)
        if test.returncode != 0:
            shutil.copy2(backup, CONF)
            print("✗ nginx -t fallito, config ripristinata:\n" + test.stderr,
                  file=sys.stderr)
            return 1
        print("✓ nginx -t")

    subprocess.run(["systemctl", "reload", "nginx"], check=True)
    print("✓ nginx ricaricato\n")
    print("Ora, come utente normale:  ./deploy/deploy.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
