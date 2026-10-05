---
pageType: source
id: source.orca-ade-github
title: "Orca ADE — agente di orchestrazione per flotte di agenti paralleli (GitHub stablyai/orca)"
sourceType: web
url: https://github.com/stablyai/orca
date: 2026-10-05
tags: [source, harness, agent-ide, coding-agent, orchestrazione]
ingestedAt: 2026-10-05T10:23:00Z
updatedAt: 2026-10-05T10:23:00Z
status: active
publish: true
---

# Orca ADE — "the AI Orchestrator for 100x builders" (stablyai/orca)

**Source:** https://github.com/stablyai/orca · docs https://www.onorca.dev · sito https://onorca.dev
**Verificata:** 2026-10-05 (README via fetch + GitHub API)
**Licenza:** MIT · **Linguaggio:** TypeScript (Electron) · **Creato:** 2026-03-17

## Cos'è

Ambiente di sviluppo agentico (ADE) costruito attorno a una **flotta di agenti paralleli**:
lo stesso prompt sparato su N agenti, ciascuno nel proprio **worktree git isolato**, con
confronto dei risultati e merge del vincitore. Non è un editor a cui è cresciuto un agente:
l'unità primaria del prodotto è l'agente, non il file.

## Architettura (dal README, verificata)

- **Worktree paralleli come primitiva** — isolamento per task, review a livello di hunk, merge = git normale.
- **Agenti paralleli** — "se funziona in un terminale, funziona in Orca": l'elenco supportato
  include Claude Code, Codex, Hermes Agent, MiMo Code, DeepSeek Harness, OpenCode, Kimi,
  Qwen Code e ~35 altri CLI agent. Provider-agnostic per ospitalità, non per ri-implementazione.
- **Superfici**: desktop (macOS arm64/Intel, Windows, Linux AppImage), **compagna mobile**
  (iOS App Store + APK Android, monitoraggio e pilotaggio da telefono), **runtime remoto via SSH**
  con guida dedicata per `orca serve` su **server Linux headless**.
- **Design Mode**: clic su un elemento UI in una finestra Chromium reale → HTML, CSS e screenshot
  ritagliato finiscono nel prompt dell'agente.
- **Orca CLI**: anche gli agenti pilotano Orca (`orca worktree create`, snapshot, click, fill) —
  l'orchestratore è stesso un tool di superficie.
- **Terminale splits** con rendering WebGL e scrollback persistente; GitHub e Linear nativi in-app;
  annotazione dei diff AI; switcher account con tracking di utilizzo/rate-limit.
- Rilascio giornaliero dichiarato ("we ship daily"); il changelog è la vera lista funzionalità.

## Segnali quantitativi (API, 2026-10-05)

- **85.349 stelle**, 5.494 fork, 7.599 issue aperte — creazione marzo 2026, push attivo in giornata.
- È il progetto più stellato della sua classe nel vault, di un ordine di grandezza sopra i pari.

## Confronto diretto con bb (get-bb/bb)

Stesso genere (IDE agentico, MIT, TypeScript, 2026) ma **tesi opposte**:

| | Orca | bb |
|---|---|---|
| Claim centrale | orchestrare **una flotta di agenti altrui** | l'agente che **costruisce sé stesso** |
| Unità di lavoro | worktree git isolato per agente | thread con steering e hand-off |
| Agente | esterno, CLI già autenticata (35+) | proprio, riutilizza le CLI provider |
| Maturità | 85k stelle, ship giornaliero, mobile + SSH stabili | 4k stelle, Linux/Windows alpha |
| Server Linux headless | guida ufficiale (`orca serve`) | server API non autenticato nelle modalità remote |

Per un workflow multi-agente su un server Linux (il nostro): Orca ha il percorso documentato,
bb no. bb porta una domanda che Orca non pone: che succede quando l'harness si auto-modifica.

## Rilevanza per il topic harness

Campione 2026 di "harness come prodotto" accanto a
[bb](bb-agent-ide-github.md) e [DeepSeek Harness](deepseek-harness-github.md).
Il worktree-per-agente è la risposta organizzativa a `q-raw-boundary-concurrency`; il
pilotaggio da telefono e la CLI guidata dagli agenti toccano il tema
[harness-vs-model](../topics/harness-vs-model.md): a parità di modello,
Orca è interamente un effetto-harness sul throughput del programmatore.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [bb — The agent IDE that builds itself (GitHub get-bb/bb)](bb-agent-ide-github.md)
- [deepseek harness github](deepseek-harness-github.md)
<!-- openclaw:wiki:related:end -->
