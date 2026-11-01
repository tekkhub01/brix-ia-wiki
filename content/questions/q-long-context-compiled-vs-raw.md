---
title: "Does long context degrade differently for a compiled wiki page than for a stuffed raw corpus?"
kind: question
status: partially-answered
priority: p2
created: 2026-08-14
updated: 2026-10-11
last_checked: 2026-10-11
tags: [question, gap, llm-memory]
summary: "long-context-models.md never engages positional-degradation findings at all, despite resting its central claim on context quality rather than window size."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Does long context degrade differently for a compiled wiki page than for a stuffed raw corpus?

## Why Track This

[long-context-models](../concepts/long-context-models.md) never engages positional-degradation findings at all, despite resting its central claim on context quality rather than window size.

## Current State

Depends on lost in the middle. This is the question that would justify or undermine 'long context is what makes compilation cheap to consult'.

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Resolution

**Partially-answered 2026-10-11 (dreaming sweep).** The blocking dependency is gone: `lost-in-the-middle` was ingested 2026-10-04 and [long-context-models](../concepts/long-context-models.md) now carries the positional-degradation caveat with its two transferability limits stated. What the source settles: degradation is about *locating* information (U-shaped positional curve, present "even for explicitly long-context models"), and the corpus's operational consequence is recorded — a compiled page placed mid-context is not equivalent to the same page at the edges; window ordering is a design variable. What remains genuinely open: no source in or outside the vault directly measures compiled-page-vs-raw-corpus degradation (the comparison would need a same-model A/B of a wiki page against its source corpus at matched token counts — locally runnable, no external source required). Downgraded p1→p2 on this basis: the premise is fixed, only the differential measurement is missing.
