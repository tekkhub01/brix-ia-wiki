---
title: "Harness"
category: concept
sources: [harness-engineering-6-layer-playbook-2026, loop-engineering-complete-guide-huashu, due-classifiche-per-lo-stesso-benchmark]
created: 2026-09-01
updated: 2026-09-01
verified: 2026-09-01
tags: [agents, harness, architecture, reliability]
aliases: [Harness, Agent Harness, Harness Engineering]
confidence: high
summary: "Everything around the model that turns a reasoning engine into a working agent: guides, sensors, loop, memory, permissions, observability. Measurably worth more than a model generation — the same weights swing tens of points depending on the harness they run in."
volatility: warm
publish: true
---
# Harness

**Type:** agent system architecture
**Definition:** the software environment a model runs inside — the tools it may call, the rules it is given, the checks it must pass, the state it keeps, and the limits it cannot exceed
**Status:** named as a discipline in 2026; the term is used across this vault by seven sources, none of which define it

## Why this page exists

This vault accumulated seven sources describing agent harnesses — [DeepSeek Harness](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md), [JCode](../syntheses/jcode-agente-di-coding-super-veloce.md), [Webwright](../syntheses/webwright-microsoft-browser-agent.md), [Prime Agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md), [Archon](../sources/archon-workflow-engine.md), the [6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md) and [Deep Agents from Scratch](../sources/deep-agents-from-scratch.md) — while never explaining what a harness is. The gap was self-diagnosed on 2026-08-26 in [Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md):

> "Cinque fonti in questo vault descrivono harness per agenti [...] e nessuna pagina spiega cosa sia un harness né perché conti. Questi numeri sono la ragione empirica per aprirlo."

## The core equation

> **Agent = Model + Harness.**

The model supplies reasoning. The harness supplies everything else. Stated this way the split looks trivial; what makes it a discipline is that the second term turns out to be the larger one in practice.

## Where it sits in the stack

Two independent sources place the harness at the same altitude, one layer below scheduling and one above context assembly:

| Layer | What it minds | Core question |
|---|---|---|
| Prompt engineering | Writing one good prompt | What should I tell the model |
| Context engineering | What goes in the window right now | What to retrieve, summarize, clear out |
| **Harness engineering** | **Arming a single run** | **Which tools, what actions, what counts as done** |
| Loop engineering | Scheduling on top of the harness | How to make it run itself over and over |

Source: [Loop Engineering — The Complete Guide](../sources/loop-engineering-complete-guide-huashu.md), June 2026, which quotes Addy Osmani: *"Loop engineering sits one floor above the harness."* The [6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md) gives the same succession as a chronology — prompt engineering 2023–24, context engineering 2025, harness engineering 2026 — having been written independently. Two sources, same ordering, no shared citation.

## The six layers

The playbook decomposes a harness into six parts, three forming a steering loop and three forming the runtime it stands on:

```
GUIDES ──> AGENTIC LOOP ──> SENSORS     (steering: feedforward + feedback)
   │            │               │
   v            v               v
MEMORY     PERMISSIONS     OBSERVABILITY  (runtime foundation)
```

1. **Guides** — the rules the agent is handed before it acts (`AGENTS.md`, `CLAUDE.md`). Feedforward. See [[guides-and-sensors]].
2. **Sensors** — the checks applied to what it produced: linters, tests, validators first, LLM-as-judge only for what cannot be coded. Feedback. See [[guides-and-sensors]].
3. **Agentic loop** — plan → execute → verify → adjust, under explicit bounds. See [[agentic-loop]].
4. **Memory & state** — the model forgets every session; the harness remembers on the filesystem.
5. **Permissions & budgets** — the model does not limit itself, so safety is a property of the harness, not of the weights. Trusted input (guides) is kept separate from untrusted input (fetched content) as a prompt-injection boundary.
6. **Observability** — structured logs, trip wires, a health scorecard. The real metric is tasks completed without human intervention.

Tools reach the agent through this layer; the wire format that has standardized is [[mcp|MCP]].

## The evidence that the harness outweighs the model

Holding the model fixed and changing only the harness:

| Source | Model | Benchmark | Before → After | Delta |
|---|---|---|---|---|
| Masood (GAIA) | Claude Sonnet 4.5 | GAIA | 30.91% → 74.55% | **+43.64 pt** |
| LangChain | same model | Terminal Bench | 30th → 5th | **+25 rank** |
| OpenAI (Codex) | Codex agents | production | 0 → 1M lines | zero manual |

A 44-point swing on identical weights is larger than the gap between many adjacent model generations. Three further results in this vault point the same way:

- **The same model is worth ±3.4 points depending on which agent runs it**, inside a single leaderboard — and on Terminal-Bench 3.0 the top entry is `mini-SWE-agent`, the *minimal* harness, ahead of commercial agents ([Due classifiche](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)).
- **An inference-time verifier wrapper is worth nine points without touching the weights** ([LLM-as-a-Verifier](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)) — the proof by contradiction: if a wrapper moves the score, the wrapper is part of what is being measured.
- Published agent scores are therefore **joint measurements of a model and a harness**, which is the argument developed in [[harness-vs-model]].

**Caveat on this table.** The playbook is an independent synthesis of public material, not a peer-reviewed study, and its four rows come from four different setups that were never run against each other. The direction is corroborated three times over; the magnitudes are not comparable across rows.

## When a harness is not worth building

The playbook is explicit that the overhead is not always justified: one-off questions, creative brainstorming, exploratory conversation, single tasks. Its test is three questions — would you notice if the agent silently produced a wrong result (→ you need a sensor); would you have to re-explain the same context (→ memory); would a mistake have external consequences (→ permissions).

## Open questions

- **Is the minimal-harness result on Terminal-Bench 3.0 general, or benchmark-specific?** `mini-SWE-agent` beating commercial agents suggests harness complexity can be actively harmful past some point, but one benchmark is not a curve. Tracked as [q-minimal-vs-elaborate-harness](../questions/q-minimal-vs-elaborate-harness.md).
- **DSH vs OpenClaw**: same perimeter, opposite choice on the core/plugin boundary. Flagged as missing in the DSH synthesis and still uncovered by any first-hand source.

## See Also

- [[agentic-loop]] — the third layer, in detail
- [[guides-and-sensors]] — the first two layers, and the ratchet that fills them
- [[mcp|MCP]] — how tools are exposed to the agent
- [[harness-vs-model]] — synthesis: why a published score belongs to the pair, not the model

## Sources

- [Harness Engineering — the 6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md)
- [Loop Engineering — The Complete Guide](../sources/loop-engineering-complete-guide-huashu.md)
- [Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
