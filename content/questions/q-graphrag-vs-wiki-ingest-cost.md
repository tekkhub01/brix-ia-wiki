---
title: "In absolute cost units, how does GraphRAG indexing compare to LLM Wiki ingest for the same corpus?"
kind: question
status: partially-answered
priority: p2
created: 2026-08-14
updated: 2026-11-01
last_checked: 2026-11-01
tags: [question, gap, llm-memory]
summary: "Both are called 'expensive' in incompatible qualitative terms that never share a unit."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# In absolute cost units, how does GraphRAG indexing compare to LLM Wiki ingest for the same corpus?

## Why Track This

Both are called 'expensive' in incompatible qualitative terms that never share a unit.

## Current State

May be currently unanswerable: would require a study running both pipelines on one corpus. Flagged as possibly-unanswerable rather than merely unresearched.

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Resolution pass (2026-11-01, eleventh sweep — partially-answered)

The first preregistered same-corpus cost comparison of the two families now
exists — but it compares **wiki vs vector RAG**, not vs GraphRAG indexing:

- **arXiv 2605.18490** ("Vector RAG vs LLM-Compiled Wiki: A Preregistered
  Comparison on a Small Multi-Domain Research Corpus"): total query tokens
  single-round RAG **78k**, decomposed RAG **491k**, wiki **1,651k** — the wiki
  was **3.4–6.3× more expensive per query** than RAG, i.e. under the tested
  setup it could *not* recover its upfront build cost through cheaper queries.
  Wall-clock went the other way (wiki 22.0 min vs decomp 26.8). Quality:
  wiki's edge on inter-paper mapping shrank from +6.25 to +0.75 against
  decomposed RAG.
- **Karpathy gist follow-up measurement** (llm-wiki gist thread): ingest
  *decisions* (folder, dedupe, merge, link) consume **~72% of ingest LLM
  tokens**; a small typed classifier instead of the LLM for those decisions
  halved ingest time with token cost per document flat as the wiki grew
  (525 docs, one corpus, one model — first data point).
- **GraphRAG build cost remains qualitative**: practitioner sources (kt.team,
  InfraNodus) say graphs are "more expensive to build" because entities,
  relationships and communities are LLM-extracted pre-query — no absolute
  figure on a shared corpus.

**What this settles:** the unit exists (LLM tokens per corpus + per query
batch), and the wiki's hoped-for "pay back build cost via cheap queries" story
is now measured *against* — the wiki is the expensive side on both build and
query in the one preregistered test.

**What stays open:** GraphRAG indexing on the *same* corpus in the same unit —
the 2605.18490 setup excludes GraphRAG, so the three-way table is still
missing its third column. Local option: run GraphRAG indexing on this vault's
~100-source corpus and price it against the ingest logs already kept here.

## Collegamenti (audit 2026-10-22)

- Concetti di riferimento: [[topics/llm-memory/wiki/concepts/graphrag|GraphRAG]] · [[topics/llm-memory/wiki/concepts/llm-wiki-karpathy|LLM Wiki (Karpathy)]] — i due 'costosi' da mettere sulla stessa unità di misura
- Benchmark collegato: [[sources/do-we-still-need-graphrag-ragsearch-benchmark-arxiv-2604-09666|Do We Still Need GraphRAG? (RAGSearch)]]
