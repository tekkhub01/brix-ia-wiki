---
pageType: synthesis
id: synthesis.prime-agent-self-improving-rlm-agent-primeintellect-ai
title: Prime Agent — Self-Improving RLM Agent (PrimeIntellect-ai)
sourceIds:
  - source.prime-agent-primeintellect-2026-08-14
  - https://github.com/PrimeIntellect-ai/prime-agent
status: active
updatedAt: 2026-08-14T15:00:08.535Z
publish: true
---

# Prime Agent — Self-Improving RLM Agent (PrimeIntellect-ai)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Prime Agent — Self-Improving RLM Agent (PrimeIntellect-ai)

**Repo:** https://github.com/PrimeIntellect-ai/prime-agent
**Linguaggio:** TypeScript · **License:** MIT · **Stars:** ~15.8k (al 2026-08-14)

## Cos'è

Agent open-source per coding e research, pensato per lavori **general** e **long-running / autonomi**. Due astrazioni centrali:

- **Recursive Language Model (RLM)** — tratta il contesto come variabili (*prompt-as-a-variable*) e i tool/sub-agent ricorsivi come chiamate di funzione (*programmatic tool / sub-agent calling*) dentro un REPL persistente.
- **Continual Harness** — memorizza prompt supplementari, memorie, descrizioni di skill e specifiche di sub-agent riusabili come stato durevole che Prime Agent può affinare tramite piccoli aggiornamenti basati su evidenze (locale alla sessione di default).

Combina un ambiente Python di controllo persistente con stato durevole dell'harness, così il contesto di lavoro utile e i pattern operativi riusabili sopravvivono a una singola finestra di chat.

## Caratteristiche principali

- **Tutto è programmatico** — IPython persistente è il tool integrato del modello; file, shell, tool use, sub-agent e gestione del contesto avvengono via codice
- **Sub-agent integrati** — `rlm(...)` spawna veri child agent per lavoro parallelo/background e ritorna i risultati programmaticamente
- **L'harness migliora** — `/refine` rivede la traiettoria corrente e applica piccoli aggiornamenti basati su evidenze allo stato supplementare dell'harness; non riscrive mai il system prompt base immutabile, e gli snapshot registrati permettono rollback
- **Skill eseguibili** — le skill sono pacchetti Python importabili; il creatore di skill integrato trasforma workflow ricorrenti in skill di progetto o personali
- **Sessioni in background** — agent con daemon continuano a girare anche se il terminale si disconnette, e si possono riagganciare
- **Comunicazione agent-to-agent** — agent attivi si scambiano messaggi e si orchestrano a vicenda senza passare dall'utente
- **Task lunghi continuano** — compaction automatica, goal persistenti, heartbeats, schedule, modalità autonoma e sub-agent mantenuti preservano il progresso tra turni e sessioni

## Installazione

```bash
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

Installa il comando `prime-agent` (macOS/Linux), verifica SHA-256 e prepara il runtime IPython. Avvio: `cd /path/to/project && prime-agent`; primo launch `/login` per scegliere subscription o API-key provider.

> ⚠️ Esegue Python e comandi di progetto generati dal modello con i permessi dell'utente; **non è un sandbox di sicurezza**.

## Rilevanza

Agent di coding/ricerca **long-running e autonomo** (MIT, TypeScript, ~15.8k⭐, molto attivo — push 2026-08-14). Rilevante per il panorama agent: usa un modello RLM (prompt-as-variable + sub-agent ricorsivi) e un Continual Harness che *migliora sé stesso* accumulando memorie/skill — filosoficamente affine a JCode e Headroom ma orientato al self-improvement e al lavoro autonomo di lunga durata. Rilasciato da **Prime Intellect** (ecosistema `verifiers`, `prime-rl`). Costruito sopra `pi` (github.com/earendil-works/pi).

## Provenienza

- Repo: https://github.com/PrimeIntellect-ai/prime-agent (letto e salvato su richiesta di Peter, 2026-08-14).
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Prime Agent — repo PrimeIntellect (2026-08-14)](../sources/prime-agent-primeintellect-2026-08-14.md)
<!-- openclaw:wiki:related:end -->
