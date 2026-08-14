---
id: quantization
pageType: entity
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-06-11T10:10:44.343Z
status: active
claims:
  - id: qat-gemma4
    text: QAT (Quantization-Aware Training) + Unsloth Dynamic preserva 88,76%
      accuratezza Top-1 a 4 bit vs 74,08% naive Q4_0 su Gemma 4 12B
    status: verified
    confidence: 0.95
    evidence:
      - kind: synthesis
        sourceId: synthesis.esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant
        note: Risultati QAT dalla sintesi esperimenti Gemma 4
  - id: turboquant-kv
    text: TurboQuant comprime KV cache a 3-4 bit con tecnica geometrica (PolarQuant
      + QJL), estendendo contesto da 8K a 100K token su RTX 3090
    status: verified
    confidence: 0.9
    evidence:
      - kind: synthesis
        sourceId: synthesis.esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant
        note: Benchmark TurboQuant dalla sintesi
publish: true
---

# Quantization

**Type:** LLM inference optimization technique
**Purpose:** Reduce model size and memory footprint by representing weights with fewer bits

## Concept

Standard LLM weights are stored in 16-bit (FP16/BF16) or 32-bit (FP32) floating point. Quantization compresses them to lower precision (typically INT8, INT4, or sub-4-bit) at minimal accuracy cost.

## Common formats

- **GGUF / GGML** — llama.cpp ecosystem, supports Q2 through Q8
- **AWQ** — activation-aware weight quantization
- **GPTQ** — post-training quantization optimized for transformer layers
- **BnB / bitsandbytes** — HuggingFace ecosystem 4-bit/8-bit

## Trade-offs

- **Pro**: 2-4× memory reduction, faster inference on consumer GPUs, enables on-premise deployment
- **Con**: small accuracy degradation (usually <2% on benchmarks), some quantization formats not supported by all runtimes

## Relationship to Context Caching

Quantization shrinks cached tensors (KV cache + weights) → more headroom for context windows on the same hardware. Complementary, not competing.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Context Caching](context-caching.md)
- [Long-Context Models](long-context-models.md)

### Related Pages

- [Agentic RAG](agentic-rag.md)
- [Claude (Anthropic)](claude-anthropic.md)
- [GLM 5.1](glm-5.1.md)
- [GraphRAG](graphrag.md)
- [LLM Wiki (Karpathy Pattern)](llm-wiki-karpathy.md)
- [NotebookLM (Google)](notebooklm.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
- [Span-Level Attribution](span-level-attribution.md)
<!-- openclaw:wiki:related:end -->
