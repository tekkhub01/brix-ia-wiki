---
title: "Quantization"
category: concept
sources: [qwen3-8-how-to-run-locally-unsloth, esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant]
created: 2026-04-28
updated: 2026-08-15
verified: 2026-06-11
tags: [inference-optimization, kv-cache, local-models]
aliases: [Quantization, Quantizzazione]
confidence: high
summary: "Lower-precision weight and KV-cache representation. Enters this topic through the KV cache: quantizing it is what turns a long context window from a spec-sheet number into something a single consumer GPU can actually hold."
volatility: warm
publish: true
---
# Quantization

**Type:** LLM inference optimization technique
**Purpose:** Reduce model size and memory footprint by representing weights — and, more relevantly here, the KV cache — with fewer bits

## Why this page is in a memory wiki

Quantization is normally filed under inference efficiency, not memory architecture. It belongs here because of one fact: **the KV cache, not the weights, is what a long context window costs you at runtime.** A context window is only usable if the KV cache for it fits in memory. Quantizing that cache is therefore a direct lever on effective context length, which makes it a lever on every architecture in this topic that depends on stuffing more into the window. See [[long-context-models]] and [[context-caching]].

## Concept

Standard LLM weights are stored in 16-bit (FP16/BF16) or 32-bit (FP32) floating point. Quantization compresses them to lower precision — typically INT8, INT4, or sub-4-bit — at some accuracy cost.

## Common formats

- **GGUF / GGML** — llama.cpp ecosystem, supports Q2 through Q8
- **AWQ** — activation-aware weight quantization
- **GPTQ** — post-training quantization optimized for transformer layers
- **BnB / bitsandbytes** — HuggingFace ecosystem 4-bit/8-bit
- **NVFP4** — 4-bit floating point for NVIDIA Blackwell (RTX 50x, DGX Spark, B200/B300), served via vLLM or SGLang; ~1.5× faster than BF16 at comparable file size, 92–97% top-1 recovery

## Corroboration: method beats bit count

This page's central empirical claim now rests on **two independent corpora**, from different model families and different teams, that were ingested separately and did not cite each other until 2026-08-15:

| Corpus | Comparison | Result |
|---|---|---|
| Gemma 4 12B, local experiment | Unsloth Dynamic QAT vs naive Q4_0, **both at 4-bit** | **88.76%** vs **74.08%** top-1 |
| Qwen3.8, Unsloth documentation | IQ2_XXS (9 GB) vs BF16 (54.7 GB) | **82.5%** accuracy retained at **83.5%** smaller |

Fourteen accuracy points at identical precision, and a 2-bit quant holding 82.5% — the *allocation* of bits dominates their count. Treat any bit-width figure without a named method as uninformative.

The Qwen3.8 documentation also supplies the cost table this page previously lacked. Qwen3.8-27B, total memory (RAM + VRAM, or unified):

| 2-bit | 3-bit | 4-bit | 6-bit | 8-bit | BF16 |
|---|---|---|---|---|---|
| 11–13 GB | 13–16 GB | 17–19 GB | 24 GB | 31 GB | 56 GB |

The interesting rung is 4-bit at 17–19 GB: a 256K context window on a single consumer card. That is this topic's thesis stated in hardware terms — the window is only real if the cache fits.

At the extreme end, Unsloth extended llama.cpp's `IQ1_S` from 1.5625 to **1.1875 bpw** by shrinking the codebook from 2048 to 256 entries, taking a 2.4T model from 4.9 TB to 397 GB (−91%). Their own numbers show what that costs: perplexity 2.58 → 4.49, top-p agreement 78.9% → 66.3%. Sub-2-bit is a different regime, not a further step along the same curve.

## Local empirical results

Two findings carried over from a local experiment synthesis (see Sources). These were recorded as verified against that synthesis, but have **not** been independently re-verified in this topic's research passes:

| Finding | Result | Recorded confidence |
|---|---|---|
| QAT (Quantization-Aware Training) + Unsloth Dynamic on Gemma 4 12B | **88.76%** Top-1 accuracy retained at 4-bit, vs **74.08%** for naive Q4_0 | 0.95 |
| TurboQuant KV-cache compression (PolarQuant + QJL, geometric technique) | KV cache to 3–4 bit, extending usable context from **8K to 100K** tokens on a single RTX 3090 | 0.90 |

The first says the *method* of quantizing matters far more than the bit count — a 14-point accuracy spread at identical precision. The second is the one that matters for this topic: a 12× increase in usable context on unchanged hardware, achieved entirely by compressing the cache rather than by changing the model.

## Trade-offs

- **Pro:** 2–4× memory reduction, faster inference on consumer GPUs, makes on-premise deployment viable
- **Con:** accuracy degradation — small (<2% on benchmarks) for good methods, substantially worse for naive ones, as the QAT figures above show; format support varies by runtime

## Open question: does speculation survive a compressed cache?

The two corpora disagree here, and the disagreement is unresolved:

- The Gemma experiment records **MTP and TurboQuant as incompatible**, attributing it to Gemma 4's alternating local/global GQA attention.
- The Qwen3.8 documentation ships **MTP enabled** in its GGUFs and adds FP8 KV-cache calibration in NVFP4, i.e. speculation and cache compression together.

Both cannot be the general case. Architecture-specific, two different mechanisms wearing one name, or an unmeasured quality regression — tracked, with a four-run local test that would settle it, in [q-mtp-vs-kv-compression](../questions/q-mtp-vs-kv-compression.md). One corroborating detail: Unsloth's documented `num_speculative_tokens: 2` independently matches the Gemma finding that MTP saturates past two hypothesised tokens.

## Relationship to context caching

Quantization shrinks what is being cached (KV tensors), so the two compose rather than compete: caching avoids *recomputing* the cache, quantization reduces what it *costs to hold*. One caveat worth flagging — the [[context-caching]] economics documented in this wiki are a hosted-API pricing model, whereas KV quantization is a self-hosted memory constraint. They are optimizations of the same object under two different cost regimes, and the numbers from one do not transfer to the other.

## The chain this page sits in

Four pages in this vault each hold one segment of a single argument about the KV cache, and the argument is only visible end to end:

1. **[[long-context-models]]** — the window sizes vendors advertise.
2. **this page** — what holding that window actually costs in memory, and how compression changes the number (8K → 100K on one RTX 3090).
3. **[[context-caching]]** — what *not recomputing* it costs, under hosted-API pricing.
4. **[headroom-labs](../entities/headroom-labs.md)** — the commercial bet that compressing what you send is worth paying for, 15–20% token savings on coding agents.

Read together they say: the context window is not a capability, it is a budget line, and there are at least three independent levers on it (compress the cache, reuse the cache, send less into it). Each page argues one lever as though it were the whole problem.

## See Also

- [[context-caching]] — reuse of the cache, priced per request
- [[long-context-models]] — the window sizes this makes reachable locally

## Sources

Not yet ingested into this topic's `raw/`. Provenance is in the sibling OpenClaw memory-wiki vault:

- [esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md) — local Gemma 4 12B experiment (QAT, MTP, TurboQuant)
- [qwen3-8-unsloth-inferenza-locale](../syntheses/qwen3-8-unsloth-inferenza-locale.md) — synthesis of the Unsloth Qwen3.8 documentation
- [qwen3-8-how-to-run-locally-unsloth](../sources/qwen3-8-how-to-run-locally-unsloth.md) — the source itself, ingested 2026-08-15
- [unsloth](../entities/unsloth.md) — the org producing the quantization method both corpora measure
