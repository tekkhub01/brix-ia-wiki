---
title: "Does on-premise prefix caching (vLLM PagedAttention, KTransformers) match cloud context-caching economics?"
kind: question
status: partially-answered
priority: p2
created: 2026-08-14
updated: 2026-10-25
last_checked: 2026-10-25
tags: [question, gap, llm-memory]
summary: "context-caching.md calls this 'possible' for the on-prem use case with zero measured numbers, unlike the sharply quantified cloud section above it."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Does on-premise prefix caching (vLLM PagedAttention, KTransformers) match cloud context-caching economics?

## Why Track This

[context-caching](../concepts/context-caching.md) calls this 'possible' for the on-prem use case with zero measured numbers, unlike the sharply quantified cloud section above it.

## Current State

Answerable by benchmarking locally, which is within reach on this hardware.

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Progresso (sweep 2026-10-25) → partially-answered

Ricerca web (1 query, fonti tech 2026 — seconda mano):

- **Il risparmio GPU c'è ed è paragonabile per ordine di grandezza a quello cloud:**
  Thaki Cloud (giu 2026) riporta che vLLM APC su prefissi ripetuti (system prompt,
  tool definitions) taglia il tempo GPU **di oltre metà** — la stessa fascia del
  cache-read cloud (0.1× sul prezzo, che è ~90% di sconto ma su prezzo, non su GPU-seconds).
- **Ma c'è un costo strutturale che il cloud non ha:** SqueezeBits (giu 2026, vs
  TensorRT-LLM) misura sull'overhead computazionale di APC in vLLM −36.7% throughput
  e +25% TPOT nel caso peggiore misurato — l'economia on-prem non è "cloud gratis":
  il cache consuma GPU RAM locale e l'hashing dei blocchi ha un prezzo suo.
- DevOpsBeast (mag 2026): il cross-node prefix caching è indicato come il singolo
  maggiore lever di costo nel serving 2026 — ma è proprio la parte che on-prem
  richiede di costruirsi (Mooncake-style disaggregation), non arriva con `--enable-prefix-caching`.

**Sintesi:** la domanda "regge l'economia cloud?" ha ora una risposta direzionale:
**sì sul workload ripetitivo (≥50% GPU-time), no come meccanismo** — il cloud
sconta il prezzo del token cached, on-prem libera GPU-seconds ma paga RAM locale +
overhead di gestione, e il pezzo grosso (cross-node) è DIY. La conferma numerica
sul nostro stack (GLM 5.1 + vLLM, 4 run con/without APC su carico agentico reale)
resta il next action, ora di conferma e non di scoperta.

## Collegamenti (audit 2026-10-22)

- Concetto di riferimento: [[topics/llm-memory/wiki/concepts/context-caching|Context caching]] (la sezione on-prem non quantificata che questa domanda vuole colmare)
- Contesto più ampio: [[topics/llm-memory/wiki/topics/memory-economics|Memory economics]]
