---
id: synthesis.codegraph
pageType: synthesis
title: CodeGraph — Pre-indexed code knowledge graph
sourceIds:
  - source.codegraph-2026-05-26
updatedAt: 2026-05-26T16:45:00Z
publish: true
---

# CodeGraph — Pre-indexed code knowledge graph per AI coding agents

**Categoria:** Tool DevOps / AI Coding  
**Stato:** ✅ Attivo, open-source  
**GitHub:** https://github.com/colbymchenry/codegraph  
**Sito:** https://colbymchenry.github.io/codegraph/  
**Autore:** Colby McHenry  
**Stars:** ~23K (maggio 2026) — crescita virale

## Cos'è

CodeGraph è un tool locale che indicizza una codebase in un **[[graphrag|knowledge graph]] queryabile** usando Tree-sitter per parsing AST. Espone il grafo agli agenti AI (Claude Code, Codex, Cursor, Gemini CLI, opencode, Hermes) tramite **server MCP**, permettendo query immediate su simboli, chiamanti, chiamati e relazioni — senza che l'agente debba scandire i file via grep/read.

## Problema che risolve

Gli agenti AI (Claude Code, Codex) in ogni nuovo chat devono:
1. Esplorare la codebase via `find`/`grep`/`read` — consumando token su ogni chiamata
2. Ricostruire la struttura del progetto da zero ogni volta
3. Spawnare sub-agenti per esplorazione, moltiplicando i costi

CodeGraph indicizza **una volta sola** e risponde istantaneamente.

## Vantaggi chiave

| Metrica | Risparmio medio (benchmark 7 codebase) |
|---------|--------------------------------------|
| **Token** | **57% in meno** |
| **Tempo** | **46% più veloce** |
| **Costo** | **35% più economico** |
| **Tool calls** | **71% in meno** |

I vantaggi crescono con la dimensione della codebase.

## Come funziona

1. `codegraph init -i` → scansione progetto, costruzione grafo in SQLite locale
2. `codegraph serve --mcp` → espone il grafo come server MCP
3. Gli agenti (Claude Code, Codex, ecc.) chiamano i tool MCP invece di grep/read
4. Auto-sync via file watcher OS (FSEvents/inotify) — sempre aggiornato

## Feature principali

- **Tree-sitter parsing** su 20+ linguaggi (TS, Python, Go, Rust, Java, Swift, Kotlin, C++, ecc.)
- **Impact analysis** — tracciamento callers/callees prima di modificare codice
- **Full-text search** FTS5 su tutta la codebase
- **Framework-aware routes** — riconosce 14 web framework
- **100% locale** — nessun dato esce dalla macchina
- **Runtime bundled** — nessuna dipendenza Node.js necessaria
- **Auto-uninstall** — `codegraph uninstall` rimuove da tutti gli agenti configurati

## Come integrare in OpenClaw

CodeGraph è già utilizzabile con Claude Code e Codex via MCP. Per integrarlo in OpenClaw:
- Configurare un MCP server in OpenClaw che punti a CodeGraph
- Oppure usare `codegraph serve --mcp` come service locale e connetterlo via MCP config

## Note

- ⚠️ Funziona meglio su codebase grandi (>500 file)
- Su codebase piccole (~100 file) il margine si assottiglia
- v0.9.4 (2026-05-24) — progetto molto attivo
- Licenza da verificare

## Risorse

- GitHub: https://github.com/colbymchenry/codegraph
- Sito: https://colbymchenry.github.io/codegraph/
- Install: `npx @colbymchenry/codegraph` o `curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh`

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [CodeGraph — Pre-indexed code knowledge graph](../sources/codegraph-2026-05-26.md)
<!-- openclaw:wiki:related:end -->
