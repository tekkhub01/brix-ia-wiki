---
title: "What is the concurrency behavior of the read-only raw/ boundary under multi-agent ingestion?"
kind: question
status: partially-answered
priority: p2
created: 2026-08-14
updated: 2026-11-01
last_checked: 2026-11-01
tags: [question, gap, llm-memory]
summary: "llm-wiki-karpathy.md describes 5-10 agents fanning out but never asks what happens when two synthesis agents touch the same page."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# What is the concurrency behavior of the read-only raw/ boundary under multi-agent ingestion?

## Why Track This

[llm-wiki-karpathy](../concepts/llm-wiki-karpathy.md) describes 5-10 agents fanning out but never asks what happens when two synthesis agents touch the same page.

## Current State

Answerable by reading the nvk/llm-wiki implementation rather than any paper. Directly relevant to this wiki's own operation.

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Resolution pass (2026-11-01, eleventh sweep — partially-answered)

Read from the nvk/llm-wiki implementation docs and practitioner write-ups:

- **`raw/` itself is safe by design**: sources "stay immutable, support indexed
  namespaces, and can pin Git paths by commit and blob SHA without copying
  bodies" (llm-wiki.net ingest docs). Concurrent reads of an immutable store
  have no failure mode; the read-only `query-lite` profile (~2.8 KB) is the
  sanctioned concurrent path.
- **The concurrency problem lives on the wiki side, not raw/**: Sentra's
  company-scale analysis names it directly — parallel agents ingesting at once
  update the same entity pages simultaneously, and *git merge conflicts in
  model-written prose are slow to resolve*; "one-at-a-time ingest is a strength
  for one person and a bottleneck for a team." Karpathy's own practice is
  one-source-at-a-time.
- So the answer to the original question: the read-only boundary holds under
  multi-agent fan-out (immutable + namespaced + pinned), and the real
  multi-agent hazard is last-writer-wins / merge conflicts on shared wiki
  pages during the synthesis step — which the pattern handles socially
  (serial ingest), not mechanically.

**What stays open:** whether nvk/llm-wiki has any *mechanical* write lock or
page-claim protocol for the synthesis step (the docs describe plan-bound
approval for adapters, not for ingest). Reading the repo's AGENTS.md ingest
protocol for a lock/claim mechanism would close it; not worth another pass
from this vault's side.

## Collegamenti (audit 2026-10-22)

- Concetto di riferimento: [[topics/llm-memory/wiki/concepts/llm-wiki-karpathy|LLM Wiki (Karpathy)]] — il fan-out 5-10 agenti che questa domanda interroga
- Contesto: [[topics/llm-memory/wiki/concepts/agentic-rag|Agentic RAG]]
