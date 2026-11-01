---
id: source.nvidia-nemotron-3-5-parse-hf
pageType: source
title: "NVIDIA Nemotron 3.5 Parse — model card Hugging Face"
sourceType: url
sourcePath: https://huggingface.co/nvidia/Nemotron-3.5-Parse
ingestedAt: 2026-10-22T16:10:00Z
updatedAt: 2026-10-22T16:10:00Z
status: active
date: 2026-10-17
tags: [source, nvidia, ocr, document-parsing, rag, ingest]
url: https://huggingface.co/nvidia/Nemotron-3.5-Parse
publish: true
---

# NVIDIA Nemotron 3.5 Parse — model card

**Rilascio:** 17/10/2026 su Hugging Face (verificata il 22/10/2026 via web_fetch)
**Introdotta da:** post Telegram inoltrato da PK (22/10/2026) + verifica su fonte primaria

## Fatti dalla model card (verificati)

- **Che cos'è:** parser di immagini di documento → testo strutturato con classi semantiche di layout, bounding box e ordine di lettura. Output Markdown con tabelle HTML; post-processing esporta tabelle/grafici in LaTeX, HTML, markdown, JSON, json_hierarchical, CSV.
- **Architettura:** vision encoder NVIDIA C-RADIOv4-SO400M (vit_so400m_patch16_224) + adapter 1D-conv + decoder mBART causale 10 layer (16 query heads / 8 KV heads, GQA), preprocessing NaViT rettangolare dinamico, coordinate content-normalized, tokenizer multilingue 72.505 token con token di controllo (`<predict_bbox>`, `<predict_classes>`, `<predict_text_in_pic>`, `<class_Chart>`).
- **Parametri:** 630.800.496 (~0,631B) unici addestrabili, testa MTP inclusa; embedding decoder condivise contate una volta.
- **Head MTP:** una testa one-step multi-token-prediction inclusa; usata dal plugin vLLM per decodifica speculativa.
- **ParseBench:** 75,20 mean (triple-pass con union di regioni su 2.078 pagine uniche); tabelle 84,67 · grafici 64,40 · content faithfulness 87,96 · semantic formatting 68,28 · visual grounding 70,67.
- **Tabella Published ParseBench / Measured pages/s (stesse 2.078 pagine, 1× H100, BF16):**
  | Modello | ParseBench | pagine/s |
  |---|---|---|
  | Nemotron 3.5 Parse (triple-pass) | 75,20 | 10,62 |
  | LightOnOCR-3-4B | 75,10 | 2,76 |
  | Nemotron 3.5 Parse (double-pass) | 74,92 | 11,65 |
  | LightOnOCR-3-0.8B | 74,60 | 5,69 |
  | Infinity-Parser2-Flash | 73,25 | 3,06 |
  | MinerU2.5-Pro-2605-1.2B | 72,78 | 4,13 |
  | Nemotron 3.5 Parse (single-pass) | 72,74 | 15,42 |
  | LightOnOCR-3-1B | 71,40 | 2,44 |
  | PaddleOCR-VL-1.6 | 67,43 | 3,11 |
  | Nemotron Parse 2.0 | 63,91 | 3,95 |
- **Altri OCR:** IndicVisionBench 83,73 ANLS-char (876 pagine, 10 lingue); MOSCAR 99,51 character bag F1 (8.111 pagine sintetiche semplici, 163 voci lingua/script). **Caveat esplicito della card:** MOSCAR non garantisce accuratezza su scansioni complesse, corsivo, immagini degradate; il character bag F1 ignora l'ordine dei caratteri.
- **Runtime:** Transformers (`transformers==5.14.1`, `trust_remote_code`) o vLLM con plugin NVIDIA (vLLM ≥0.25,<0.33); `vllm serve` con server OpenAI-compatibile; Docker documentato.
- **Licenza:** OpenMDW 1.1 — uso commerciale o non commerciale consentito. Tokenizer MIT con attribuzione.
- **Uso dichiarato:** document intelligence, RAG, estrazione, curazione dati multimodali, agenti.

## Note di lettura

- Il punteggio migliore (75,20) è in **triple-pass**; il single-pass scende a 72,74 ma arriva a 15,42 pagine/s. Il confronto "6× più piccolo, ~4× più veloce" di LightOnOCR-3-4B vale a parità di punteggio (75,20 vs 75,10; 10,62 vs 2,76 pp/s).
- Timing: include tutti i passaggi del modello e il lavoro di crop dipendente; esclude preparazione pagine, startup, warmup, rendering finale e scritture.
- I benchmark throughput sono **auto-riportati da NVIDIA** (loro pipeline, loro H100).

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [NVIDIA Nemotron 3.5 Parse — parser di documenti da 0,63B che compete con modelli 6× più grandi](../syntheses/nvidia-nemotron-3-5-parse-parser-documenti-0-63b.md)
<!-- openclaw:wiki:related:end -->
