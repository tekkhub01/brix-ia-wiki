---
id: rotorquant
pageType: entity
sourceIds:
  - sources/brix-ia-newsletter-news-aprile-2026.md
updatedAt: 2026-04-28T00:00:00Z
publish: true
---

# RotorQuant

**Type:** Quantization technique for LLMs  
**Developer:** scrya-com (open-source)  
**Release:** Early 2026  
**Repository:** https://github.com/scrya-com/rotorquant  

## Benchmark vs TurboQuant (baseline)

| Metric | RotorQuant | TurboQuant |
|--------|------------|------------|
| Perplexity | 6.91 | 7.07 |
| Decode speed | +28% | baseline |
| Prefill speed | **5.3x faster** | baseline |
| Parameter count (optimal) | **372** (44× fewer) | 16,399 |
| KV cache compression | **>10x** | ~5x |

## Context

RotorQuant replaces TurboQuant as state-of-the-art for local LLM quantization in early 2026. Extreme parameter efficiency (372 vs 16K) enables high throughput on low-power hardware (e.g., Intel N100, Apple Silicon).

**Reality check:** Some claims of "9–31x speedup" are hardware-dependent; Apple Metal support is still incomplete.

## Relevance to on-premise deployment

For a physical AI agent box targeting SMEs, quantization is the critical path to performance on affordable hardware. RotorQuant + GLM 5.1 = production-ready local agents without cloud costs.

**Mentioned in:**
- BRIX-IA Newsletter News — Aprile 2026

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)

### Related Pages

- [Claude (Anthropic)](claude-anthropic.md)
- [GLM 5.1](glm-5.1.md)
- [OpenRouter](openrouter.md)
<!-- openclaw:wiki:related:end -->
