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
        dest = pub.get(key)
        # Se il percorso esatto non e' pubblicato ma esiste una pagina
        # pubblicata con lo stesso nome, il link va rediretto, non
        # neutralizzato: e' il caso di una pagina spostata di layer
        # (entities/notebooklm -> concepts/notebooklm). Solo se il nome
        # e' univoco, altrimenti non sapremmo quale scegliere.
        if dest is None:
            stem = PurePosixPath(key).stem
            cand = [v for v in pub.values() if v.stem == stem]
            if len(cand) == 1:
                dest = cand[0]
        if dest is not None:
            newrel = os.path.relpath(dest.as_posix(), destdir.as_posix())
            return f"[{label}]({newrel}.md{heading})"
        n += 1
        return MARK + label

    text = WIKILINK_RE.sub(repl_wiki, text)
    text = MDLINK_RE.sub(repl_md, text)
    # Un bullet dei blocchi "related" che puntava a una pagina privata
    # resterebbe come voce nuda senza link: si elimina la riga intera.
    text = ORPHAN_LI_RE.sub("", text)
    return text.replace(MARK, ""), n


# Menzione nuda di un file .md nel corpo, fuori da link e percorsi.
# Es: "context-caching.md calls this 'possible'" nelle domande aperte:
# la relazione e' gia' scritta, manca solo la sintassi del link.
BARE_MD_RE = re.compile(r"(?<![\[\(/\w-])([a-z0-9][a-z0-9._-]*)\.md\b(?![\)\]])")
# `index` e' il nome dell'indice del vault, non una pagina del sito.
BARE_SKIP = {"index"}
FENCE_RE = re.compile(r"(```.*?```|`[^`\n]*`)", re.DOTALL)
PROV_RE = re.compile(
    r"^(?:sourceIds|sources):[ \t]*(?:\[(?P<inline>[^\]]*)\]|\n(?P<block>(?:[ \t]+-[ \t]+\S.*\n?)+))",
    re.MULTILINE)


def _by_stem(pub: dict[str, PurePosixPath]) -> dict[str, PurePosixPath]:
    """stem -> destinazione, solo per i nomi univoci."""
    out: dict[str, PurePosixPath | None] = {}
    for v in pub.values():
        out[v.stem] = None if v.stem in out else v
    return {k: v for k, v in out.items() if v is not None}


def linkify_bare(text: str, destdir: PurePosixPath,
                 stem_map: dict[str, PurePosixPath]) -> tuple[str, int]:
    """Trasforma le menzioni nude `pagina.md` in link veri, solo nel corpo.

    Il frontmatter va escluso: un valore che finisce in `.md` — per esempio
    `sourcePath: pagina.md` — verrebbe riscritto come link markdown, e il
    risultato non e' piu' YAML valido. Il build fallisce sull'intero sito,
    non solo su quella pagina.
    """
    n = 0

    def repl(m: re.Match) -> str:
        nonlocal n
        stem = m.group(1)[:-3] if m.group(1).endswith(".md") else m.group(1)
        stem = m.group(1)
        if stem in BARE_SKIP or stem not in stem_map:
            return m.group(0)
        n += 1
        rel = os.path.relpath(stem_map[stem].as_posix(), destdir.as_posix())
        return f"[{stem}]({rel}.md)"

    # Il frontmatter resta intatto: si riscrive solo da qui in poi.
    fm = FM_RE.match(text)
    head, text = (text[:fm.end()], text[fm.end():]) if fm else ("", text)

    # Non toccare il contenuto di code fence e code span.
    parts = FENCE_RE.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = BARE_MD_RE.sub(repl, parts[i])
    parts[0] = head + parts[0]
    return "".join(parts), n


def page_title(path: Path, fallback: str) -> str:
    """Titolo dal frontmatter, altrimenti dal primo heading."""
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if m:
        t = re.search(r"^title:\s*(.+?)\s*$", m.group(1), re.MULTILINE)
        if t:
            return t.group(1).strip().strip("\"'")
    h = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return h.group(1).strip() if h else fallback


def provenance_section(fm: str, destdir: PurePosixPath,
                       stem_map: dict[str, PurePosixPath],
                       selfstem: str, titles: dict[str, str],
                       already: set[str]) -> tuple[str, int]:
    """Proietta `sourceIds:` / `sources:` del frontmatter in link nel corpo.

    Il plugin registra la provenienza nei metadati, ma Quartz costruisce
    grafo e backlink solo dai link nel corpo: senza questa proiezione la
    relazione esiste nel dato e sparisce nel sito.
    """
    refs: list[str] = []
    for m in PROV_RE.finditer(fm):
        raw = m.group("inline") or m.group("block") or ""
        refs += [x.strip().strip("-").strip().strip("'\"")
                 for x in re.split(r"[,\n]", raw)]

    seen, links = set(), []
    for r in refs:
        if not r:
            continue
        stem = PurePosixPath(r).stem
        for pref in ("source.", "synthesis.", "entity."):
            stem = stem[len(pref):] if stem.startswith(pref) else stem
        # `already` = pagine gia' linkate nel corpo (tipicamente dal
        # blocco "related" del plugin): rilinkarle aggiungerebbe solo
        # rumore duplicato.
        if (stem == selfstem or stem in seen or stem not in stem_map
                or stem in already):
            continue
        seen.add(stem)
        rel = os.path.relpath(stem_map[stem].as_posix(), destdir.as_posix())
        links.append(f"- [{titles.get(stem, stem)}]({rel}.md)")

    if not links:
        return "", 0
    body = ("\n\n<!-- generato da sync.py dai metadati di provenienza "
            "del vault; non presente nella pagina originale -->\n"
            "## Fonti\n\n" + "\n".join(links) + "\n")
    return body, len(links)


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
    stem_map = _by_stem(pub)
    titles = {r.stem: page_title(VAULT / r, r.stem) for r in pubrels}
    linked_re = re.compile(r"\[[^\]]*\]\((?!https?:)([^)#]+?)\.md")
    defused = linked = proven = 0
    for rel in pubrels:
        destrel = dest_for(rel)
        dest = CONTENT / destrel
        dest.parent.mkdir(parents=True, exist_ok=True)
        src = (VAULT / rel).read_text(encoding="utf-8")

        text, n = defuse_links(src, rel, pub)
        defused += n
        text, n = linkify_bare(text, destrel.parent, stem_map)
        linked += n
        fm = FM_RE.match(src)
        if fm:
            already = {PurePosixPath(m).stem for m in linked_re.findall(text)}
            already |= {m.strip().split("/")[-1]
                        for m in WIKILINK_RE.findall(text) for m in [m[0]]}
            extra, n = provenance_section(fm.group(1), destrel.parent,
                                          stem_map, destrel.stem, titles, already)
            text, proven = text.rstrip() + "\n" + extra, proven + n

        dest.write_text(text, encoding="utf-8")

    if defused:
        print(f"  {defused} link verso pagine private convertiti in testo")
    if linked:
        print(f"  {linked} menzioni nude trasformate in link")
    if proven:
        print(f"  {proven} link di provenienza proiettati dal frontmatter")

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
