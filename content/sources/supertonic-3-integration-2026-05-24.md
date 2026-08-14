---
id: supertonic-3-integration-2026-05-24
pageType: source
updatedAt: 2026-05-24T09:44:00Z
claims: []
links: []
publish: true
---

# Supertonic 3 TTS — Integrazione e API

## Fonte
- **Data:** 24 maggio 2026
- **Richiedente:** PK (@pk21kps)
- **Contesto:** Analisi di Supertonic 3 (TTS) per integrazione in OpenClaw

## Fine-tuning
- **Supporto ufficiale:** Nessuno. Il repository ufficiale non fornisce codice di training.
- **Dichiarazione:** "This open‑weight repository focuses on fixed‑voice, local TTS and does not include an official voice‑cloning pipeline."
- **Alternative:** Voice Builder per zero‑shot voice cloning (crea file JSON di stile vocale).
- **Repository di terze parti:** `saurabhv749/supertonic3‑voice‑clone` per addestrare voice styles.

## Integrazione in OpenClaw
- **Possibile:** Sì, Supertonic 3 è un modello on‑device che può essere eseguito localmente.
- **Metodo:** Installare `supertonic` via pip e creare un servizio API locale (FastAPI/Flask).
- **Esempio endpoint:** `POST /tts` con parametri `text`, `voice`, `lang` che ritorna audio WAV.
- **Integrazione skill:** Creare una skill OpenClaw che chiama l'API locale per generare audio.

## Esposizione API
- **Server locale:** Python SDK di Supertonic 3 + FastAPI per esporre endpoint HTTP.
- **Configurazione gateway:** OpenClaw gateway può esporre l'API esternamente se necessario.
- **Performance:** CPU‑only, ottimizzato per velocità (RTF 0.2 su CPU 16‑thread).
	

## Passi operativi
1. Installare Supertonic: `pip install supertonic`
2. Creare servizio API (esempio FastAPI).
3. Creare skill OpenClaw per chiamare l'API.
4. Configurare gateway per esposizione esterna (opzionale).

## Considerazioni
- **Licenza:** OpenRAIL‑M (uso commerciale con restrizioni).
- **Voice cloning:** Zero‑shot tramite Voice Builder, no fine‑tuning.
- **Alternative:** Skill `tts` esistente in OpenClaw (ElevenLabs, Gemini) può essere estesa.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

<!-- openclaw:wiki:related:end -->
