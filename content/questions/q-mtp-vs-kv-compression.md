---
title: "Is the MTP × KV-cache-compression incompatibility specific to Gemma 4's GQA, or general?"
kind: question
status: proposed
priority: p1
created: 2026-08-15
updated: 2026-08-15
last_checked: 2026-08-15
tags: [question, gap, llm-memory, quantization, kv-cache, speculative-decoding]
summary: "The Gemma 4 experiment records MTP and TurboQuant as incompatible; the Qwen3.8 documentation ships MTP enabled alongside FP8 KV-cache calibration. Both cannot be the general case."
confidence: medium
origin: "2026-08-15 dreaming pass, cross-reading the Gemma quantization synthesis against the Qwen3.8/Unsloth source"
publish: true
---

# Is the MTP × KV-cache-compression incompatibility specific to Gemma 4's GQA, or general?

## Why Track This

Two sources in this vault make claims that cannot both be general, and neither
page cites the other:

| Source | Claim |
|---|---|
| [Esperimenti Quantizzazione Gemma 4 12B](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md) | MTP and TurboQuant are **incompatible** on Gemma 4, attributed to the alternating local/global attention in GQA. Recorded `verified`, confidence 0.85. |
| [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md) | Qwen3.8 GGUFs ship with **MTP enabled**; NVFP4 quants add **FP8 KV-cache calibration** for 2× context. vLLM is documented serving both together. |

This matters beyond trivia. MTP is the biggest measured single-machine speedup in
this vault (3.11× on Gemma 4 31B, 3.82× on coding). KV-cache compression is the
biggest measured single-machine *context* win (8K → 100K on one RTX 3090). If
they compose, the local-inference ceiling is much higher than either page
suggests alone. If they don't, every local configuration recommendation has to
pick a side.

## Current State

At least three readings fit the evidence, and nothing in the vault distinguishes
them:

1. **Architecture-specific.** Gemma 4's local/global attention alternation is the
   culprit and Qwen3.8's attention layout doesn't have it. The incompatibility is
   real but narrow.
2. **Different objects.** TurboQuant is *geometric compression* of the cache
   (PolarQuant + QJL, 3-4 bit); NVFP4's FP8 calibration is a different mechanism.
   "KV compression" names two things that behave differently under speculation.
3. **Silent quality regression.** They run together and neither party measures the
   accuracy cost of doing so. Unsloth's own 1-bit benchmarks are explicitly still
   in progress.

Note also that Unsloth's speculative config is documented at
`num_speculative_tokens: 2` — which independently matches the Gemma finding that
MTP saturates past 2 hypothesised tokens. That agreement is evidence the two
setups are comparable enough for the contradiction to be a real one.

## Next Action

Locally testable, and cheaply: serve Qwen3.8-27B with MTP on, then off, with and
without FP8 KV-cache calibration, and measure t/s plus a KLD or top-1 check
against the BF16 reference. Four runs on one machine settles reading 1 vs 3.

Until measured, **do not** collapse the two claims into one. Cite both with
attribution — the precedent set on 2026-08-14 for the Headroom and Hermes figures.
