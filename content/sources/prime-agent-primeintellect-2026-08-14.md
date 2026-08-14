---
pageType: source
id: source.prime-agent-primeintellect-2026-08-14
title: "Prime Agent — repo PrimeIntellect (2026-08-14)"
sourceType: local-file
sourcePath: prime-agent-primeintellect-2026-08-14.md
ingestedAt: 2026-08-14T15:01:11.559Z
updatedAt: 2026-08-14T15:01:11.559Z
status: active
publish: true
date: 2026-08-14
tags: [ai-agent, rlm, coding-agent, autonomous-agent, long-running, primeintellect, typescript, mit]
url: https://github.com/PrimeIntellect-ai/prime-agent
---

# Prime Agent — repo PrimeIntellect (2026-08-14)

## Source
- Origine: https://github.com/PrimeIntellect-ai/prime-agent
- Ingerita da file locale `prime-agent-primeintellect-2026-08-14.md` il 2026-08-14
- Bytes: 3667

**Repo:** https://github.com/PrimeIntellect-ai/prime-agent
**Linguaggio:** TypeScript · **License:** MIT · **Stars:** ~15.8k (al 2026-08-14)
**Descrizione ufficiale:** "A self-improving RLM agent for coding workflows and long-running autonomous tasks."

## Cos'è

Agent open-source per coding e research, pensato per lavori generali e **long-running / autonomi**. Due astrazioni centrali:

- **Recursive Language Model (RLM)** — tratta il contesto come variabili (*prompt-as-a-variable*) e i tool/sub-agent ricorsivi come chiamate di funzione dentro un REPL persistente.
- **Continual Harness** — memorizza prompt supplementari, memorie, descrizioni di skill e specifiche di sub-agent riusabili come stato durevole che Prime Agent può affinare tramite piccoli aggiornamenti basati su evidenze (locale alla sessione di default).

Combina un ambiente di controllo Python persistente con stato durevole dell'harness, così il contesto utile e i pattern operativi riusabili sopravvivono a una singola finestra di chat.

## Caratteristiche principali

- **Tutto è programmatico:** IPython persistente è il tool integrato del modello; file, shell, tool use, sub-agent e gestione del contesto avvengono via codice
- **Sub-agent integrati:** `rlm(...)` spawna veri child agent per lavoro parallelo/background e ritorna i risultati programmaticamente
- **L'harness migliora:** `/refine` rivede la traiettoria corrente e applica piccoli aggiornamenti basati su evidenze allo stato supplementare dell'harness (non riscrive mai il system prompt base immutabile; snapshot registrati permettono rollback)
- **Skill eseguibili:** le skill sono pacchetti Python importabili; il creatore di skill integrato trasforma workflow ricorrenti in skill di progetto o personali
- **Sessioni in background:** agent con daemon continuano a girare anche se il terminale si disconnette, e si possono riagganciare
- **Comunicazione agent-to-agent:** agent attivi possono scambiarsi messaggi e orchestrarsi a vicenda senza passare dall'utente
- **Task lunghi continuano:** compaction automatica, goal persistenti, heartbeats, schedule, modalità autonoma e sub-agent mantenuti preservano il progresso tra turni e sessioni

## Installazione

```bash
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

Installa il comando `prime-agent` (macOS/Linux), verifica SHA-256 e prepara il runtime IPython. Avvio: `cd /path/to/project && prime-agent`; primo launch `/login` per scegliere provider/API key.

> ⚠️ Esegue Python e comandi di progetto generati dal modello con i permessi dell'utente; **non è un sandbox di sicurezza**.

## Rilevanza

Agent di coding/ricerca **long-running e autonomo** (MIT, TypeScript, ~15.8k⭐, molto attivo). Interessante per il panorama agent: usa un modello RLM (prompt-as-variable + sub-agent ricorsivi) e un Continual Harness che *migliora sé stesso* accumulando memorie/skill — affine per filosofia a JCode e Headroom, ma orientato al self-improvement e al lavoro autonomo di lunga durata. Rilasciato da Prime Intellect (stesso ecosistema di `verifiers` e `prime-rl`).

## Provenienza

- Repo: https://github.com/PrimeIntellect-ai/prime-agent (letto e salvato su richiesta di Peter, 2026-08-14).


## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Prime Agent — Self-Improving RLM Agent (PrimeIntellect-ai)](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md)
<!-- openclaw:wiki:related:end -->
