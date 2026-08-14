---
pageType: synthesis
id: synthesis.supertonic-3-tts-integrazione-e-api-in-openclaw
title: Supertonic 3 TTS — Integrazione e API in OpenClaw
sourceIds:
  - supertonic-3-integration-2026-05-24
status: active
updatedAt: 2026-05-24T09:44:56.552Z
publish: true
---

# Supertonic 3 TTS — Integrazione e API in OpenClaw

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Panoramica
Il 24 maggio 2026, PK ha richiesto un'analisi di Supertonic 3 (TTS) per integrazione in OpenClaw e esposizione API.

## Risultati chiave
1. **Fine-tuning:** Non supportato ufficialmente. Voice cloning zero‑shot tramite Voice Builder.
2. **Integrazione OpenClaw:** Possibile tramite servizio API locale (Python SDK + FastAPI).
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

<!-- openclaw:wiki:related:end -->
