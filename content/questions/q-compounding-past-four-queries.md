---
title: "Does the 84.6% compounding result hold past a four-query horizon?"
kind: question
status: answered
priority: p0
created: 2026-08-14
updated: 2026-09-13
answered: 2026-09-13
last_checked: 2026-09-13
tags: [question, gap, llm-memory]
summary: "The study's RAG baseline is unspecified, so the corpus's most-cited number cannot currently be interpreted."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Does the 84.6% compounding result hold past a four-query horizon?

## Why Track This

The study's RAG baseline is unspecified, so the corpus's most-cited number cannot currently be interpreted.

## Current State

**Answered 2026-09-13** by the full-text ingest of wen-ku-knowledge-compounding. No — the compounding regime never wins on token count at any horizon modeled: the 30-day projection keeps Chunk-RAG < Compounding < Long-Context at all three concentrations; the ratio narrows (6.3× → 3.8× at high concentration) but no crossover exists for plausible parameters. The 84.6% figure is against the Long-Context (stuffing) baseline, not classic RAG. The paper's own limitations call the four-query sample insufficient and ask for 100+ sequential queries per domain. Corrections landed in `llm-wiki-karpathy.md` and `memory-economics.md`.
