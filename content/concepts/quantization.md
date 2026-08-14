---
title: "Quantization"
category: concept
sources: []
created: 2026-04-28
updated: 2026-08-14
verified: 2026-06-11
tags: [inference-optimization, kv-cache, local-models]
aliases: [Quantization, Quantizzazione]
confidence: medium
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

## Relationship to context caching

Quantization shrinks what is being cached (KV tensors), so the two compose rather than compete: caching avoids *recomputing* the cache, quantization reduces what it *costs to hold*. One caveat worth flagging — the [[context-caching]] economics documented in this wiki are a hosted-API pricing model, whereas KV quantization is a self-hosted memory constraint. They are optimizations of the same object under two different cost regimes, and the numbers from one do not transfer to the other.

## See Also

- [[context-caching]] — reuse of the cache, priced per request
- [[long-context-models]] — the window sizes this makes reachable locally

## Sources

Not yet ingested into this topic's `raw/`. Provenance is a local experiment synthesis in the sibling OpenClaw memory-wiki vault:

