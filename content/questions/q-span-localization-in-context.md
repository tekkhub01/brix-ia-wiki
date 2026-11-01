---
title: "Why does span-level localization fail when the document is already in context?"
kind: question
status: partially-answered
priority: p1
created: 2026-08-14
updated: 2026-10-18
last_checked: 2026-10-18
tags: [question, gap, llm-memory]
summary: "Recorded in Open Threads with no candidate source attached and no mechanism proposed."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Why does span-level localization fail when the document is already in context?

## Why Track This

Recorded in Open Threads with no candidate source attached and no mechanism proposed.

## Current State

The most genuinely open of the carried-over threads: no queued source clearly answers it.

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Resolution (sweep 2026-10-18) — partially-answered from material already in the vault

The mechanism candidate is positional attention, and the source is in the vault
since 2026-10-04: [lost-in-the-middle](../sources/lost-in-the-middle-abs.md)
(arXiv 2307.03172) — U-shaped accuracy over document position. Span localization
*is* a locating task, so it sits exactly in the regime the paper measured: spans
in the middle of an already-in-context document are the ones the model fails to
attribute even when it can use their content. Two caveats the page itself records
(long-context-models.md, verified 2026-10-04) limit the transfer: the 2023
measurements predate 1M-context models, and the paper's own framing is
locating-vs-reasoning — which is precisely the distinction this question needs.
What remains genuinely open: whether attribution failure tracks *position*
(lost-in-the-middle) or *attention dilution* (more candidate spans → lower
per-span salience), which the 2023 design does not separate. No 2025-26 source
found that does.
