---
pageType: source
id: source.bb-agent-ide-github
title: "bb — The agent IDE that builds itself (GitHub get-bb/bb)"
sourceType: web
url: https://github.com/get-bb/bb
date: 2026-10-05
tags: [source, harness, agent-ide, coding-agent]
ingestedAt: 2026-10-05T10:13:00Z
updatedAt: 2026-10-05T10:13:00Z
status: active
publish: true
---

# bb — The agent IDE that builds itself (get-bb/bb)

**Source:** https://github.com/get-bb/bb · homepage https://getbb.app
**Verificata:** 2026-10-05 (README via fetch + GitHub API)
**Licenza:** MIT · **Linguaggio:** TypeScript · **Topic GitHub:** ade, agent-ide, claude-code, codex, devtools, ide

## Cos'è

IDE agentico il cui claim di posizionamento è che **costruisce sé stesso**: può controllare,
personalizzare e automatizzare la propria superficie, "ponendo le basi per la propria fabbrica
di software". Segnalato da Peter il 2026-10-05.

## Architettura (dal README, verificata)

- **Quattro superfici first-class** per pilotarlo: app desktop, app web, CLI e HTTP API.
- Il lavoro corre in **thread** che si possono seguire in live, dirigere in qualunque punto,
  o **passare a un altro agente** — hand-off tra agenti come primitiva di UI, non come backend.
- **Provider-agnostic by reuse**: usa la CLI del provider che hai già autenticato (topic
  `claude-code` e `codex` — stessa mossa di DeepSeek Harness: l'harness non ri-fa il provider).
- Monorepo pnpm/turbo; server + host daemon + app (Electron per il desktop). Native add-on
  (better-sqlite3, node-pty, @parcel/watcher) — da qui il caveat npm 12 `--allow-scripts`.
- Dev loop pensato per worktree multipli: data dir e porte deterministiche per checkout.

## Segnali quantitativi (API, 2026-10-05)

- **4.119 stelle**, 591 fork, 570 issue aperte — creazione 2026-02-24, push attivo in giornata.
- Attività alta: ~7 mesi di vita, 4k stelle.

## Caveat dichiarati (onestà del README)

1. **In sviluppo attivo**: architettura core stabile, workflow e superfici ancora in evoluzione.
2. Linux x64 e Windows x64 sono **alpha**; macOS Apple Silicon la via principale.
3. **Telemetria anonima di default** nelle run production (app start, conteggi thread/messaggi,
   install plugin; id random per install, nessun contenuto). Opt-out: `BB_TELEMETRY=false`.
4. **Server API senza autenticazione con esecuzione comandi e lettura file** nelle modalità
   `dev:remote` / `start:worktree-remote`: utilizzabili solo dietro confine di rete fidato
   (il README lo dice esplicitamente e consiglia firewall su Tailscale).

## Rilevanza per il topic harness

È il terzo campione 2026 di "harness come prodotto" in vault dopo
[DeepSeek Harness](deepseek-harness-github.md) e il pattern 6-layer del
[playbook](harness-engineering-6-layer-playbook-2026.md), e ci porta un elemento nuovo:
la **superficie multi-ingoresso** (desktop/web/CLI/HTTP) come parte del design dell'harness,
non come client calato sopra. Riguarda da vicino anche
[harness-vs-model](../topics/harness-vs-model.md): se l'harness si
auto-costruisce, il confine model/harness diventa una variabile del prodotto stesso.
Il thread-steering/hand-off tocca il tema di `q-workflow-vs-agent-structure`.

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
