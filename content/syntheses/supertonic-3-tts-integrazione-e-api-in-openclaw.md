---
pageType: synthesis
id: synthesis.supertonic-3-tts-integrazione-e-api-in-openclaw
title: Supertonic 3 TTS — Integrazione e API in OpenClaw
sourceIds:
  - supertonic-3-integration-2026-05-24
status: active
updatedAt: 2026-09-13T04:40:00Z
publish: true
---

# Supertonic 3 TTS — Integrazione e API in OpenClaw

## Notes
<!-- openclaw:human:start -->
### Collegamenti (dreaming 2026-08-15)
- Stessa catena audio: [Qwen3 Audiobook Converter](qwen3-audiobook-converter.md)

<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Panoramica
Il 24 maggio 2026, PK ha richiesto un'analisi di Supertonic 3 (TTS) per integrazione in OpenClaw e esposizione API.

## Risultati chiave
1. **Fine-tuning:** Non supportato ufficialmente. Voice cloning zero‑shot tramite Voice Builder.
2. **Integrazione [OpenClaw](../entities/brix-ia.md):** Possibile tramite servizio API locale (Python SDK + FastAPI).
3. **Esposizione API:** Endpoint HTTP per generare audio da testo, configurabile via gateway OpenClaw.

## Azioni consigliate
- Installare `supertonic` via pip.
- Creare servizio API locale (`/tts`).
- Creare skill OpenClaw per chiamare l'API.
- Configurare gateway per esposizione esterna (opzionale).

## Risorse
- Repository ufficiale: `supertone-inc/supertonic`
- Voice Builder: `https://supertonic.supertone.ai/voice_builder`
- Esempio API: codice FastAPI (vedi fonte).
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Supertonic 3 TTS — Integrazione e API](../sources/supertonic-3-integration-2026-05-24.md)

### Referenced By

- [Qwen3 Audiobook Converter (WhiskeyCoder)](qwen3-audiobook-converter.md)
<!-- openclaw:wiki:related:end -->
