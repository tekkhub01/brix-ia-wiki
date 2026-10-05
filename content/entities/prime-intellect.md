---
title: "Prime Intellect"
id: prime-intellect
pageType: entity
entityType: organization
sourceIds:
  - sources/prime-agent-primeintellect-2026-08-14.md
updatedAt: 2026-09-13T05:00:00Z
publish: true
---

# Prime Intellect

**Type:** organization — laboratorio AI, ecosistema open-source
**GitHub:** https://github.com/PrimeIntellect-ai
**Rilevanza per questo vault:** produce Prime Agent, l'implementazione più
esplicita di harness auto-migliorante che abbiamo tracciato

Ecosistema: oltre a Prime Agent rilasciano `verifiers` e `prime-rl`.

## Prodotti

### Prime Agent

Agente open-source per coding e ricerca, orientato a task **long-running e
autonomi**. TypeScript, licenza MIT, ~15,8k stelle al 2026-08-14.

Due astrazioni portano il peso:

- **Recursive Language Model (RLM)** — il contesto è trattato come variabili
  (*prompt-as-a-variable*) e i sub-agent ricorsivi come chiamate di funzione
  dentro un REPL persistente
- **Continual Harness** — prompt supplementari, memorie, descrizioni di skill e
  specifiche di sub-agent sono stato durevole, che l'agente affina con
  aggiornamenti basati su evidenze. Il system prompt base resta immutabile e gli
  snapshot permettono rollback

Installazione:

```bash
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

> ⚠️ Esegue Python e comandi generati dal modello con i permessi dell'utente.
> Non è un sandbox di sicurezza.

Analisi completa: [Prime Agent — Self-Improving RLM Agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md)

### Novità (verifica 2026-09-13)

- Research: "Uncovering a universal offline sandbox escape" (25 ago), "Measuring Autonomous AI Research" (14 ago), Prime Flash MoE — kernel MoE ottimizzati Blackwell (13 ago).
- Rilasci: **SYNTHETIC-2** (4M reasoning traces collaborative) e **INTELLECT-3**, MoE 100B+ trained with large-scale RL.
- Serie A da $130M (Radical Ventures) — contesto già noto al vault via la sintesi Prime Agent.

## Perché ci interessa

Il Continual Harness è la stessa idea che regge questa wiki, applicata
all'agente invece che alla conoscenza: accumulare stato riusabile invece di
ricostruirlo a ogni sessione. Il confronto naturale è con
[l'LLM Wiki](../concepts/llm-wiki-karpathy.md) — lì il
patrimonio sono pagine, qui sono skill e memorie dell'harness.

**Sources:**
- [Prime Agent — repo PrimeIntellect (2026-08-14)](../sources/prime-agent-primeintellect-2026-08-14.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [DeepSeek](deepseek.md)
- [Prime Agent — Self-Improving RLM Agent (PrimeIntellect-ai)](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md)
- [Scaling Intelligence Lab (Stanford)](scaling-intelligence-lab.md)
<!-- openclaw:wiki:related:end -->
