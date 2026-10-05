---
pageType: synthesis
id: synthesis.nvidia-parakeet-tdt-0-6b-v2
title: Nvidia Parakeet TDT 0.6B v2
sourceIds:
  - source.nvidia-parakeet-tdt-0-6b-v2
confidence: 0.7
status: active
updatedAt: 2026-09-27T04:10:00.000Z
publish: true
---

# Nvidia Parakeet TDT 0.6B v2

## Notes
<!-- openclaw:human:start -->
### Collegamenti (dreaming 2026-08-15)
- L'altra metà della catena audio: [Qwen3 Audiobook Converter](qwen3-audiobook-converter.md)

### Stato del modello (dreaming 2026-09-27)
- **Superalato da v3.** `parakeet-tdt-0.6b-v3` (HF, tech report arXiv 2509.14128) estende v2 da inglese-only a **25 lingue europee incluso l'italiano**, con language detection automatica; CC BY 4.0, timestamp a livello parola/segmento, audio fino a 24 min (full attention, A100 80GB) o 3 ore (local attention). Per la catena audio italiana della wiki, v3 è ora la scelta giusta; la v2 resta inglese + "multilingua" nel blockquote generato era impreciso (v2 = English-only). Fonte: https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3

<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Modello
**Nvidia Parakeet TDT 0.6B v2** — Modello speech-to-text (STT) open source
- HuggingFace: nvidia/parakeet-tdt-0.6b-v2
- Sviluppatore: Nvidia
- Dimensioni: 0.6B parametri (leggero)
- Architettura: TDT (Token-and-Duration Transducer)
- Lingue: Multilingua (incluso italiano)
- Uso: Trascrizione audio → testo, alternativa a Whisper
- Vantaggi: leggero, veloce, economico, buona qualità per dimensioni ridotte
- Potenziale uso: demo trascrizione audio, sostituto Whisper per task STT
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources


### Referenced By

- [NVIDIA](../entities/nvidia.md)
- [Qwen3 Audiobook Converter (WhiskeyCoder)](qwen3-audiobook-converter.md)
<!-- openclaw:wiki:related:end -->
