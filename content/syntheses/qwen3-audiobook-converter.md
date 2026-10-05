---
pageType: synthesis
id: synthesis.qwen3-audiobook-converter
title: Qwen3 Audiobook Converter (WhiskeyCoder)
sourceIds:
  - https://github.com/WhiskeyCoder/Qwen3-Audiobook-Converter
status: active
updatedAt: 2026-08-10T10:11:23.000Z
publish: true
---

# Qwen3 Audiobook Converter (WhiskeyCoder)

## Notes
<!-- openclaw:human:start -->
### Collegamenti (dreaming 2026-08-15)
- Modello di [Alibaba](../entities/alibaba.md), famiglia Qwen
- Le altre metà della catena audio: Nvidia Parakeet TDT per STT, [Supertonic 3](supertonic-3-tts-integrazione-e-api-in-openclaw.md) per TTS

<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Qwen3 Audiobook Converter (WhiskeyCoder)

**GitHub:** https://github.com/WhiskeyCoder/Qwen3-Audiobook-Converter
**Modello TTS:** [Qwen3-TTS (QwenLM)](https://github.com/QwenLM/Qwen3-TTS)
**Linguaggio:** Python (3.8+)
**Stars:** ~1.027
**License:** MIT
**Ultimo push:** 2026-04-07

## Cos'è

Strumento Python che converte **PDF, EPUB, DOCX, DOC e TXT in audiolibri** di qualità usando il **Qwen3 TTS Voice Model** (sistema open-source di sintesi vocale, con voice cloning e speech naturale). Ideale per trasformare documenti lunghi in audio ascoltabile.

## Funzionalità principali

- **Dual voice mode** — *Custom Voice* (speaker pre-build: Ryan, Serena, Aiden, Dylan, Eric, Ono_anna, Sohee, Uncle_fu, Vivian) e *Voice Clone* (clona una voce da audio di riferimento, con trascrizione automatica via Whisper di Qwen).
- **Multi-formato** — TXT, PDF, EPUB, DOCX, DOC in ingresso.
- **Modello fisso 1.7B** — sempre il modello di qualità più alta.
- **Smart chunking** — split intelligente al limite delle frasi.
- **Caching intelligente**, retry automatici, progress tracking, auto-cleanup dei file temporanei.

## Prerequisiti / setup

- **Qwen Voice Model in locale** esposto via Gradio su `http://127.0.0.1:7860` (install one-click con Pinokio).
- **Python 3.8+**, **FFmpeg** (obbligatorio per l'audio), **RAM 4GB+**, ~100MB per ora di audiolibro.
- Dipendenze: `gradio_client`, `requests`, `PyPDF2`, `ebooklib`, `pydub`, `python-docx`, `docx2txt`, `beautifulsoup4`.

## Quick start

```bash
git clone https://github.com/WhiskeyCoder/Qwen3-Audiobook-Converter.git
cd Qwen3-Audiobook-Converter
pip install -r requirements.txt
# avvia il Qwen TTS Gradio server su :7860, poi:
cp tuo_libro.pdf book_to_convert/
python audiobook_converter.py                       # Custom Voice (Ryan, EN)
python audiobook_converter.py --voice-clone --voice-sample ref.wav
```

## Rilevanza

Da **testare** (segnalato da Peter il 2026-08-10). Utile per:
- Generare versioni **audiolibro** di report, documenti o della newsletter BRIX-IA a partire dai PDF/DOCX già prodotti.
- Pipeline **documento → audio** da affiancare ai progetti OCR/document-processing già in wiki (anydoc, pdf-inspector).

**Limite da verificare nei test:** richiede il server **Qwen3-TTS Gradio in locale** (modello separato, ~1.7B) — va avviato e tenuto attivo su `:7860`. Lingua hardcoded su **inglese** (da adattare per IT). Speaker e cartelle sono hardcoded nel codice (modificabili).
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Alibaba](../entities/alibaba.md)
- [Supertonic 3 TTS — Integrazione e API in OpenClaw](supertonic-3-tts-integrazione-e-api-in-openclaw.md)
<!-- openclaw:wiki:related:end -->
