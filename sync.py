#!/usr/bin/env python3
"""
Sincronizza il vault privato -> content/ di Quartz.

Copia SOLO le pagine con `publish: true` nel frontmatter.

Perche' il gate sta qui e non solo nel build: il repo e' pubblico, quindi
una pagina committata e' leggibile su GitHub anche se ExplicitPublish la
esclude dal sito. Il filtro di Quartz resta come seconda cintura.

Uso:
    ./sync.py            # sincronizza
    ./sync.py --dry-run  # mostra cosa farebbe, non scrive
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path, PurePosixPath

VAULT = Path.home() / ".openclaw" / "wiki"
CONTENT = Path(__file__).parent / "content"

# Cartelle del vault mai pubblicabili, a prescindere dal frontmatter.
# reports/ sono artefatti di manutenzione (lint, stale, contradictions),
# non articoli.
DENY_DIRS = {"reports", ".openclaw-wiki", ".obsidian", "_views"}

# Appiattimento dei percorsi: il topic wiki e' annidato in profondita' e
# senza rimappatura gli URL diventerebbero
# /topics/llm-memory/wiki/concepts/rag. Prefisso piu' lungo per primo.
PATH_MAP = [
    ("topics/llm-memory/inventory/candidates", "questions"),
    ("topics/llm-memory/wiki/concepts", "concepts"),
    ("topics/llm-memory/wiki/topics", "topics"),
]

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.DOTALL)
PUBLISH_RE = re.compile(r"^publish:\s*(.+?)\s*$", re.MULTILINE)
# [[target]] | [[target|label]] | [[target#h]] | [[target#h|label]]
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
# [label](qualcosa.md) — link markdown relativi, usati dai blocchi
# "related" generati dal plugin. Non sono wikilink: vanno gestiti a parte.
MDLINK_RE = re.compile(r"\[([^\]]*)\]\((?!https?:)([^)]+?\.md)(#[^)]*)?\)")
# Sentinella temporanea: marca un link neutralizzato, cosi' dopo la
# sostituzione possiamo distinguere una voce di elenco rimasta orfana
# (da eliminare) da una menzione dentro una frase (da tenere).
MARK = "\x00DEFUSED\x00"
ORPHAN_LI_RE = re.compile(r"^[ \t]*[-*+][ \t]+\x00DEFUSED\x00[^\n]*\n?", re.MULTILINE)


def is_published(text: str) -> bool:
    """Stessa semantica di @quartz-community/explicit-publish:
    solo `true` booleano o la stringa "true"."""
    m = FM_RE.match(text)
    if not m:
        return False
    pm = PUBLISH_RE.search(m.group(1))
    return bool(pm) and pm.group(1).strip().strip("\"'") == "true"


def dest_for(rel: PurePosixPath) -> PurePosixPath:
    """Percorso di destinazione in content/, con i prefissi rimappati."""
    s = rel.as_posix()
    for src, dst in PATH_MAP:
        if s.startswith(src + "/"):
            return PurePosixPath(dst) / s[len(src) + 1:]
    return rel


def collect() -> tuple[list[PurePosixPath], int]:
    pub, priv = [], 0
    for p in sorted(VAULT.rglob("*.md")):
        rel = PurePosixPath(p.relative_to(VAULT).as_posix())
        if rel.parts[0] in DENY_DIRS:
            continue
        if is_published(p.read_text(encoding="utf-8")):
            pub.append(rel)
        else:
            priv += 1
    return pub, priv


def defuse_links(text: str, srcrel: PurePosixPath,
                 pub: dict[str, PurePosixPath]) -> tuple[str, int]:
    """Neutralizza i link verso pagine non pubblicate e riscrive quelli
    verso pagine rimappate.

    Senza questo, ogni link a una pagina privata resterebbe morto sul
    sito e rivelerebbe il titolo di una pagina che abbiamo deciso di non
    pubblicare. E ogni link a una pagina rimappata punterebbe al vecchio
    percorso, che in content/ non esiste piu'.
    """
    n = 0
    srcdir = srcrel.parent
    destdir = dest_for(srcrel).parent
    # I wikilink si risolvono per nome file: Quartz usa la risoluzione
    # "shortest", quindi lo spostamento di cartella non li rompe.
    stems = {PurePosixPath(k).stem for k in pub}

    def repl_wiki(m: re.Match) -> str:
        nonlocal n
        target, _h, label = m.group(1), m.group(2), m.group(3)
        if target.strip().split("/")[-1] in stems:
            return m.group(0)
        n += 1
        return MARK + (label or target.strip().split("/")[-1].replace("-", " "))

    def repl_md(m: re.Match) -> str:
        nonlocal n
        label, target, heading = m.group(1), m.group(2).strip(), m.group(3) or ""
        # Risolvi rispetto alla cartella di origine: stem uguali in
        # cartelle diverse esistono (sources/x.md e syntheses/x.md), e il
        # match per solo nome terrebbe buono un link verso la privata.
        key = os.path.normpath((srcdir / target).as_posix())
        if key in pub:
            newrel = os.path.relpath(pub[key].as_posix(), destdir.as_posix())
            return f"[{label}]({newrel}.md{heading})"
        n += 1
        return MARK + label

    text = WIKILINK_RE.sub(repl_wiki, text)
    text = MDLINK_RE.sub(repl_md, text)
    # Un bullet dei blocchi "related" che puntava a una pagina privata
    # resterebbe come voce nuda senza link: si elimina la riga intera.
    text = ORPHAN_LI_RE.sub("", text)
    return text.replace(MARK, ""), n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not VAULT.is_dir():
        print(f"ERRORE: vault non trovato: {VAULT}", file=sys.stderr)
        return 1

    pubrels, npriv = collect()
    if not pubrels:
        print("ERRORE: nessuna pagina con `publish: true`. Non svuoto content/.",
              file=sys.stderr)
        return 1

    # chiave = percorso sorgente senza .md ; valore = destinazione senza .md
    pub = {r.with_suffix("").as_posix(): dest_for(r).with_suffix("")
           for r in pubrels}

    print(f"vault     {VAULT}")
    print(f"pubbliche {len(pubrels)}")
    print(f"private   {npriv} (non copiate)")

    # I wikilink si risolvono per nome file: due pagine pubblicate con lo
    # stesso stem renderebbero ambigua la destinazione. Ma i link con
    # percorso esplicito restano risolvibili, quindi la collisione e' un
    # problema reale solo se qualcuno usa davvero il wikilink nudo.
    seen: dict[str, str] = {}
    clashes: dict[str, list[str]] = {}
    for k, v in pub.items():
        if v.stem in seen:
            clashes.setdefault(v.stem, [seen[v.stem]]).append(k)
        seen[v.stem] = k
    if clashes:
        used = set()
        for r in pubrels:
            body = FM_RE.sub("", (VAULT / r).read_text(encoding="utf-8"))
            for m in WIKILINK_RE.finditer(body):
                used.add(m.group(1).strip().split("/")[-1])
        for stem, files in clashes.items():
            state = ("⚠ ambigua, il wikilink e' usato" if stem in used
                     else "· innocua, nessun wikilink nudo la usa")
            print(f"{state}: [[{stem}]] -> {', '.join(files)}")

    if args.dry_run:
        print("\n--dry-run: nessuna modifica.")
        for r in pubrels:
            d = dest_for(r)
            print(f"    + {d}" + (f"   ← {r}" if d != r else ""))
        return 0

    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    defused = 0
    for rel in pubrels:
        dest = CONTENT / dest_for(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        text, n = defuse_links((VAULT / rel).read_text(encoding="utf-8"), rel, pub)
        defused += n
        dest.write_text(text, encoding="utf-8")
    if defused:
        print(f"  {defused} link verso pagine private convertiti in testo")

    # La home non viene dal vault: l'index.md del vault e' generato dal
    # plugin e linka anche pagine private. Sta in home.md, versionato qui.
    home = Path(__file__).parent / "home.md"
    if home.exists():
        shutil.copy2(home, CONTENT / "index.md")
    else:
        print("⚠ home.md mancante: il sito non avra' una homepage.")

    print(f"\n✓ {len(pubrels)} pagine in {CONTENT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
