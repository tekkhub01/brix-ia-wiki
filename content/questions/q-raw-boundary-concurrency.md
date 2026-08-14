---
title: "What is the concurrency behavior of the read-only raw/ boundary under multi-agent ingestion?"
kind: question
status: proposed
priority: p2
created: 2026-08-14
updated: 2026-08-14
last_checked: 2026-08-14
tags: [question, gap, llm-memory]
summary: "[llm-wiki-karpathy](../concepts/llm-wiki-karpathy.md) describes 5-10 agents fanning out but never asks what happens when two synthesis agents touch the same page."
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
