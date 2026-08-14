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
from pathlib import Path

VAULT = Path.home() / ".openclaw" / "wiki"
CONTENT = Path(__file__).parent / "content"

# Cartelle del vault mai pubblicabili, a prescindere dal frontmatter.
# reports/ sono artefatti di manutenzione (lint, stale, contradictions),
# non articoli.
DENY_DIRS = {"reports", ".openclaw-wiki", ".obsidian", "_views"}

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.DOTALL)
PUBLISH_RE = re.compile(r"^publish:\s*(.+?)\s*$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
# [[target]] | [[target|label]] | [[target#h]] | [[target#h|label]]
FULL_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
# [label](qualcosa.md) — link markdown relativi, usati dai blocchi
# "related" generati dal plugin. Non sono wikilink: vanno gestiti a parte.
MDLINK_RE = re.compile(r"\[([^\]]*)\]\((?!https?:)([^)]+?\.md)(#[^)]*)?\)")
# Sentinella temporanea: marca un link neutralizzato, cosi' dopo la
# sostituzione possiamo distinguere una voce di elenco rimasta orfana
# (da eliminare) da una menzione dentro una frase (da tenere).
MARK = "\x00DEFUSED\x00"
ORPHAN_LI_RE = re.compile(r"^[ \t]*[-*+][ \t]+\x00DEFUSED\x00[^\n]*\n?", re.MULTILINE)


def frontmatter(text: str) -> str | None:
    m = FM_RE.match(text)
    return m.group(1) if m else None


def is_published(text: str) -> bool:
    """Stessa semantica di @quartz-community/explicit-publish:
    solo `true` booleano o la stringa "true"."""
    fm = frontmatter(text)
    if fm is None:
        return False
    m = PUBLISH_RE.search(fm)
    if not m:
        return False
    return m.group(1).strip().strip("\"'") == "true"


def collect() -> tuple[list[Path], list[Path]]:
    pub, priv = [], []
    for p in sorted(VAULT.rglob("*.md")):
        rel = p.relative_to(VAULT)
        if rel.parts[0] in DENY_DIRS:
            continue
        (pub if is_published(p.read_text(encoding="utf-8")) else priv).append(rel)
    return pub, priv


def check_dangling(pub: list[Path]) -> list[tuple[Path, str]]:
    """Wikilink che puntano a pagine non pubblicate -> link morti sul sito."""
    slugs = {p.stem for p in pub}
    dangling = []
    for rel in pub:
        text = (VAULT / rel).read_text(encoding="utf-8")
        body = FM_RE.sub("", text)
        for target in WIKILINK_RE.findall(body):
            stem = target.strip().split("/")[-1]
            if stem and stem not in slugs:
                dangling.append((rel, stem))
    return dangling


def defuse_links(text: str, slugs: set[str], paths: set[str],
                 srcdir: Path) -> tuple[str, int]:
    """Trasforma i wikilink verso pagine NON pubblicate in testo semplice.

    Senza questo, ogni [[fonte-privata]] diventa un link morto sul sito
    pubblico — e per giunta rivela il titolo di una pagina che abbiamo
    deciso di non pubblicare.
    """
    n = 0

    def repl_wiki(m: re.Match) -> str:
        nonlocal n
        target, _heading, label = m.group(1), m.group(2), m.group(3)
        if target.strip().split("/")[-1] in slugs:
            return m.group(0)
        n += 1
        return label if label else target.strip().split("/")[-1].replace("-", " ")

    def repl_md(m: re.Match) -> str:
        nonlocal n
        label, target = m.group(1), m.group(2).strip()
        # Se il link ha un percorso, risolvilo: stem uguali in cartelle
        # diverse esistono (sources/x.md e syntheses/x.md), e il match
        # per solo nome terrebbe buono un link verso la pagina privata.
        if "/" in target:
            ok = os.path.normpath(srcdir / target).removesuffix(".md") in paths
        else:
            ok = Path(target).stem in slugs
        if ok:
            return m.group(0)
        n += 1
        return MARK + label

    text = FULL_WIKILINK_RE.sub(repl_wiki, text)
    text = MDLINK_RE.sub(repl_md, text)
    # Un bullet dei blocchi "related" che puntava a una pagina privata
    # resterebbe come voce nuda senza link: si elimina la riga intera.
    text = ORPHAN_LI_RE.sub("", text)
    text = text.replace(MARK, "")
    return text, n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not VAULT.is_dir():
        print(f"ERRORE: vault non trovato: {VAULT}", file=sys.stderr)
        return 1

    pub, priv = collect()

    if not pub:
        print("ERRORE: nessuna pagina con `publish: true`. Non svuoto content/.",
              file=sys.stderr)
        return 1

    dangling = check_dangling(pub)

    print(f"vault     {VAULT}")
    print(f"pubbliche {len(pub)}")
    print(f"private   {len(priv)} (non copiate)")

    if dangling:
        print(f"\n⚠ {len(dangling)} wikilink verso pagine non pubblicate "
              f"(diventeranno link morti):")
        for src, target in dangling[:15]:
            print(f"    {src} -> [[{target}]]")
        if len(dangling) > 15:
            print(f"    ... e altri {len(dangling) - 15}")

    if args.dry_run:
        print("\n--dry-run: nessuna modifica.")
        for rel in pub:
            print(f"    + {rel}")
        return 0

    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    slugs = {p.stem for p in pub}
    paths = {str(p.with_suffix("")) for p in pub}
    defused = 0
    for rel in pub:
        dest = CONTENT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        text, n = defuse_links((VAULT / rel).read_text(encoding="utf-8"),
                               slugs, paths, rel.parent)
        defused += n
        dest.write_text(text, encoding="utf-8")
    if defused:
        print(f"  {defused} wikilink verso pagine private convertiti in testo")

    # La home non viene dal vault: l'index.md del vault e' generato dal
    # plugin e linka anche pagine private. Sta in home.md, versionato qui.
    home = Path(__file__).parent / "home.md"
    if home.exists():
        shutil.copy2(home, CONTENT / "index.md")
    else:
        print("⚠ home.md mancante: il sito non avra' una homepage.")

    print(f"\n✓ {len(pub)} pagine in {CONTENT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
