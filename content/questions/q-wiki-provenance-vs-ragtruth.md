---
title: "Does the LLM Wiki's 'inherent provenance' claim survive RAGTruth-style span checking?"
kind: question
status: partially-answered
priority: p1
created: 2026-08-14
updated: 2026-10-25
last_checked: 2026-10-25
tags: [question, gap, llm-memory]
summary: "The corpus asserts wiki provenance is structurally safer than RAG citation but never tests it on a shared yardstick."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Does the LLM Wiki's 'inherent provenance' claim survive RAGTruth-style span checking?

## Why Track This

The corpus asserts wiki provenance is structurally safer than RAG citation but never tests it on a shared yardstick.

## Current State

A genuine unaddressed gap rather than an unfetched source — no current citation answers it. Also an Open Thread, and the core of [grounding-across-architectures](../topics/grounding-across-architectures.md).

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Risposta parziale (sweep 2026-10-25) → partially-answered

Nessuna ricerca esterna necessaria: la metà concettuale della domanda era già
risolta dentro il vault, da `topics/llm-memory/wiki/topics/grounding-across-architectures.md`
(lettura incrociata delle tre fonti ora tutte in vault: RAGTruth 2401.00396 ingerita
27/09, Cited-but-Not-Verified 2605.06635 ingerita 04/10, span-level-attribution).
La risposta che quella pagina già contiene:

1. La provenienza "inherent" dell'LLM Wiki opera a **livello documento** — il tier
   che span-level-attribution dichiara "largely solved". La claim sopravvive, ma solo lì.
2. Il tier non risolto (supporto span-specifico di una frase compilata) non è
   **affatto** tentato dal pattern wiki: la claim non sopravvive a un controllo
   RAGTruth-style, perché non lo implementa — il failure mode proprio è compiled
   drift, non grounded hallucination.
3. Il rischio aggravante è la sintesi multi-sorgente (10-15 pagine toccate per
   ingest), che Cited-but-Not-Verified misura come il punto di rottura peggiore.

Resta **non fatta** solo la metà empirica: un audit span-level reale su un campione
di pagine compilate di questo stesso vault (il vault come cavia — il test non
esiste in letteratura, è eseguibile localmente). Il residuo è locale e auto-riferito;
la domanda concettuale è chiusa.

## Collegamenti (audit 2026-10-22)

- Fonte dati per il test: [[sources/ragtruth-a-hallucination-corpus-wu-et-al-arxiv-2401-00396|RAGTruth — hallucination corpus (Wu et al.)]]
- Concetto di riferimento: [[topics/llm-memory/wiki/concepts/llm-wiki-karpathy|LLM Wiki (Karpathy)]] — l'assunto di provenienza più sicura da testare
