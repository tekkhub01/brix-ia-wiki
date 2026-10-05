---
title: "scrya-com"
id: scrya-com
pageType: entity
entityType: organization
sourceIds:
  - sources/brix-ia-newsletter-news-aprile-2026.md
updatedAt: 2026-09-13T05:00:00Z
publish: true
---

# scrya-com

**Type:** organization — progetto open-source  
**Repository:** https://github.com/scrya-com/rotorquant  
**Rilevanza per questo vault:** autore di RotorQuant, la tecnica di
quantizzazione nello stack di [OfficeNode](brix-ia.md)

## Tecniche

### RotorQuant

Release inizio 2026. Sostituisce TurboQuant come stato dell'arte per la
quantizzazione di LLM locali.

| Metrica | RotorQuant | TurboQuant (baseline) |
|--------|------------|------------|
| Perplexity | 6,91 | 7,07 |
| Decode speed | +28% | baseline |
| Prefill speed | **5,3×** | baseline |
| Parametri (ottimale) | **372** (44× meno) | 16.399 |
| Compressione KV cache | **>10×** | ~5× |

L'efficienza estrema sui parametri (372 contro 16K) è ciò che rende praticabile
il throughput su hardware a basso consumo: Intel N100, Apple Silicon.

> Cifre ri-verificate il 2026-09-13 contro README GitHub e sito scrya.com: coerenza piena (PPL 6,91 vs 7,07; decode +28%; prefill 5,3×; 372 parametri, 44× meno). Il paper è di marzo 2026 (John D. Pope, Scrya), nessuna release successiva trovata.

**Analisi tecnica:** la quantizzazione come argomento — e in particolare la
compressione della KV cache come leva sulla lunghezza di contesto utile — è
trattata in [quantization](../concepts/quantization.md)
nel topic wiki.

**Sources:**

## Collegamenti (dreaming 2026-08-15)

- L'altro metodo di quantizzazione misurato in questo vault: [Unsloth](unsloth.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)

### Related Pages

- [Anthropic](anthropic.md)
- [BRIX-IA](brix-ia.md)
- [Hugging Face](hugging-face.md)
- [OpenRouter](openrouter.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->
