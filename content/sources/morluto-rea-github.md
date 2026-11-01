---
id: source.morluto-rea-github
pageType: source
title: "REA – Reverse Engineer Anything (GitHub)"
updatedAt: 2026-10-07T09:18:00Z
publish: true
---

# REA – Reverse Engineer Anything

**Date:** ottobre 2026 (repo letto il 2026-10-07)
**Source URL:** https://github.com/morluto/rea
**Author:** morluto
**Type:** Tool open-source (npm: `rea-agents`)
**Introduced via:** richiesta PK (post video Telegram)

## Cos'è

Strumento di reverse engineering guidato da agenti AI: collega il coding agent a decompiler e tool di ispezione via **MCP + CLI**, e gli fa "investigare" un'applicazione senza codice sorgente — spiegare come funziona una feature, mostrare le evidenze, ricostruirla nel progetto dell'utente.

## Copertura target

| Target | Engine |
|---|---|
| Binari nativi | Hopper o Ghidra (opzionali, licenza separata) |
| App JavaScript/Electron | analisi statica, nessun engine |
| Assembly .NET | incluso nel tool catalog |
| Siti web | incluso |

## Punti chiave

- **Analisi interamente locale**: l'app bersaglio non viene inviata da nessuna parte
- **Agenti supportati**: Claude Code/Desktop, Codex, Cursor, Gemini CLI, Windsurf, Devin, OpenCode, Antigravity, GitHub Copilot CLI, Command Code, VS Code
- **Setup**: `npx rea-agents setup` (mostra le modifiche prima di applicarle, con backup); skill installabile: `npx skills add morluto/rea --skill reverse-engineer-anything`
- **Output**: conclusioni con evidenza, limitazioni e incognite dichiarate
- CLI diretta senza MCP: `npx -y rea-agents@latest analyze-javascript-application <path> --json`

## Limiti (valutazione)

- "Qualunque programma" è marketing: binari offuscati/protetti restano difficili; i nativi richiedono Hopper/Ghidra
- Su giochi old-school (es. Patrician 3, 2004) è un buon target il codice non protetto, ma gli asset stanno in archivi proprietari con formati dedicati — fuori dal catalogo REA
- Ricostruire un software completo è un progetto lungo; "spiega questa feature" è il caso d'uso reale
- Legale: ricreare feature di app proprietarie può violarne i ToS

## Open questions

- Quanto regge il confronto con workflow RE manuali su binari di produzione?
- Governance del progetto (maintainer singolo)

## Collegamenti (audit 2026-10-22)

- Stesso batch (post video Telegram, 2026-10-07): [[sources/dozentwelve-papermorph-github|Papermorph]] · [[sources/anteloc-ldraw-nova-github|LDraw Nova]]
- Stesso spazio (reverse engineering via agenti): [[sources/ai-website-cloner-template-github|AI Website Cloner Template]]

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [LDraw Nova – agenti che progettano set LEGO (GitHub)](anteloc-ldraw-nova-github.md)
- [Papermorph – PDF in web-book interattivo (GitHub)](dozentwelve-papermorph-github.md)
<!-- openclaw:wiki:related:end -->
