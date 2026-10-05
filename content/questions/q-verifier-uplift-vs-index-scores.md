---
title: "Does LLM-as-a-Verifier really buy +9 points on Terminal-Bench 2.1, and at what real cost?"
kind: question
status: partially-answered
priority: p2
created: 2026-08-26
updated: 2026-08-26
last_checked: 2026-08-26
answered: 2026-08-26
tags: [question, gap, benchmarks, agents, inference-time-compute, cost]
summary: "A forwarded post claims DeepSeek V4 Flash goes 79% → 88% on Terminal-Bench 2.1 with self-verification at ~11x lower cost per task than the premium tier. The benchmarks are verified real; the numbers are not, and the cost claim ignores the extra inference the method spends."
confidence: medium
origin: "2026-08-26 harmonisation pass, cross-reading the 2026-08-21 benchmark source against this host's own openclaw.json"
publish: true
---

# Does LLM-as-a-Verifier really buy +9 points on Terminal-Bench 2.1, and at what real cost?

## Why Track This

The source
[Benchmark open-weight 2026-08-21](../sources/benchmark-open-weight-2026-08-21.md)
carries two sets of numbers that would, if true, change how this vault reasons
about model choice:

| Claim | Number |
|---|---|
| DeepSeek V4 Flash + LLM-as-a-Verifier on Terminal-Bench 2.1 | 79% → **88%** success rate, no fine-tuning |
| Cost per task vs the premium tier | ~**11×** cheaper (the chart in the same post says "4× cheaper") |
| GLM-5.3 on the Artificial Analysis Intelligence Index | **60**, tied with Kimi K3, one point off the top |

The ingest pass verified the *structures* — Terminal-Bench 2.1 and the
Artificial Analysis Intelligence Index are real, with documented methodology —
and then flagged both the model **names** and the **scores** as unverified,
"likely placeholders for future models".

**Half of that flag is wrong.** The model names are real and in current use:
DeepSeek V4 Flash and V4 Pro, GPT-5.6 Sol and the Claude 5 family (Opus 5, Fable
5, Sonnet 5) — several of them run in production in our own agent stack (internal
check, 2026-08-26). The same verification block also states, one line earlier, that "the
DeepSeek V4 series exists" with its own TB2.1 snapshots (V4-Flash-0731 = 82,7 —
which incidentally sits *between* the claimed 79 and 88). The models are real.

What is genuinely open is the arithmetic.

## Current State

Three things are unresolved, and they interact:

1. **Which baseline is the 79%?** The vault's own recorded snapshot for
   V4-Flash-0731 is 82,7 on TB2.1 — higher than the claimed pre-verifier 79%.
   Either the post uses a different checkpoint, a different harness, or a
   different subset. Without that, the +9 is not a delta anyone can reproduce.

2. **The cost claim counts the wrong thing.** LLM-as-a-Verifier generates *k*
   candidates and then spends more inference judging them. A per-token price
   comparison against a premium model is not a per-task cost comparison unless
   *k* and the verifier's token spend are in it. The post itself is internally
   inconsistent (11× in the text, 4× in the chart), which is what an unstated
   *k* looks like.

3. **Whether it composes with what this vault already measures.** The
   [Artificial Analysis Intelligence Index](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
   weights Agents at 34% and includes Terminal-Bench v2.1 as a component. If
   inference-time verification lifts an agentic benchmark by 9 points, it lifts
   the index too — meaning the index measures "model + harness", not "model".
   Every leaderboard comparison in this vault silently assumes otherwise.

## What Would Close It

- Pull the actual Terminal-Bench 2.1 leaderboard entry for the DeepSeek V4
  checkpoints and the AA Intelligence Index snapshot for GLM-5.3 / Kimi K3 from
  the primary sources, rather than from a forward.
- Find the verifier framework the post calls "free and open source" and read off
  its default *k*. Cost per task = k × generation + verification, not 1 ×
  generation.
- Cheapest local test: run the same agentic task set on DeepSeek V4 Flash with
  and without a self-verification wrapper, and measure tokens, not just success
  rate — the model is already available in our stack.

## Related

- [DeepSeek](../entities/deepseek.md) — the model family under test
- [Artificial Analysis](../entities/artificial-analysis.md) — the index owner
- [Z.AI (Zhipu AI)](../entities/z-ai.md) — GLM-5.3, the other unverified number
- [q-agentic-loop-vs-caching](q-agentic-loop-vs-caching.md) — the same "how much does the loop cost" question, asked of retrieval instead of verification


## Resolution (2026-08-26, primary sources)

A research pass went to the primary sources. Most of the question is now closed; one
part is closed in a way that reframes it.

**Closed — the framework is real, and *k* is 5.** LLM-as-a-Verifier is
[arXiv 2607.05391](../sources/llm-as-a-verifier-arxiv-2607-05391.md) (Scaling
Intelligence Lab, Stanford; v2, 7 Jul 2026). It scores by taking the expectation over
scoring-token logits rather than asking for a discrete judge score, and scales on
granularity, repeated evaluation and criteria decomposition. Cost per task is therefore
**5 generations + verification**, not one — so the "~11× cheaper" figure compares the
wrong unit, exactly as suspected.

**Closed — the 88% is not in the paper.** The paper reports **86,5% on Terminal-Bench
V2**. The "DeepSeek V4 Flash 79% → 88% on Terminal-Bench 2.1" line comes from an
author's X post in mid-August, not from the publication. The only occurrence of
"DeepSeek" in the v2 full text is the DeepSeek-R1 citation.

**Closed — the Index scores check out, the vault's summary of them did not.**
On artificialanalysis.ai: GLM-5.3 (max) = **60** ✓, Kimi K3 (max) = **60** ✓,
Claude Opus 5 (max) = **63** (top) ✓. But "Sol max = 63" was wrong: GPT-5.6 Sol (max)
is **61**. DeepSeek is nowhere near the top — V4 Pro 0813 (max) = **53**, V4 Flash 0731
(max) = **52**. The category weights the vault recorded (34/24/24/18) are confirmed on
the methodology page, with per-eval weights now recorded too.

**Not reproducible — the numbers this vault had marked "verified".** The recorded
"V4-Flash-0731 = 82,7 and V4-Pro-0813 = 87,9 on TB2.1" appear on **neither** primary
leaderboard. The official Terminal-Bench v2.1 board has **17 entries and no DeepSeek at
all**. Treat those two figures as unsourced until someone produces the page they came
from.

**Reframed — the third point turned out to be checkable without the verifier.** The
question asked whether inference-time verification means the index measures
"model + harness". It does, and the proof needs no verifier: Terminal-Bench v2.1 has
**two public leaderboards** whose tops differ by ~6 points with different winners
(83,8% official vs 89,5% Artificial Analysis), and within the official board the same
model scores 3,4 points apart under two different agents. See
[Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md).

**Still open.** Where the 82,7 / 87,9 figures originated; and whether the +9 uplift
reproduces on a local DeepSeek V4 Flash with k=5 — the cheap local test in the section
above is still the way to find out, and now has a documented *k* to use.
