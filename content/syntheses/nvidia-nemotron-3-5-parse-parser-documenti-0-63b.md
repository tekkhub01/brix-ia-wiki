---
pageType: synthesis
id: synthesis.nvidia-nemotron-3-5-parse-parser-documenti-0-63b
title: "NVIDIA Nemotron 3.5 Parse — parser di documenti da 0,63B che compete con modelli 6× più grandi"
sourceIds:
  - source.nvidia-nemotron-3-5-parse-hf
claims:
  - id: parse-core
    text: "Nemotron 3.5 Parse (NVIDIA, 17/10/2026): 0,631B parametri, C-RADIOv4-SO400M + decoder mBART 10 layer con testa MTP; pagine PDF/scansioni → Markdown con tabelle HTML, bounding box, classi semantiche e ordine di lettura; tabelle/grafici esportabili in HTML/JSON/CSV."
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: source.nvidia-nemotron-3-5-parse-hf
        path: https://huggingface.co/nvidia/Nemotron-3.5-Parse
        note: model card NVIDIA, fetch diretto 22/10/2026
  - id: parse-bench
    text: "ParseBench 75,20 (triple-pass, 2.078 pagine) ≈ LightOnOCR-3-4B (75,10) con ~6× meno parametri e ~3,85× più pagine/s su 1× H100 (10,62 vs 2,76); single-pass 72,74 a 15,42 pp/s — il miglior compromesso velocità/qualità della tabella."
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: source.nvidia-nemotron-3-5-parse-hf
        path: https://huggingface.co/nvidia/Nemotron-3.5-Parse
        note: tabella Published ParseBench / Measured pages/s nella card; timing auto-riportati da NVIDIA
  - id: parse-runtime
    text: "Runtime Transformers (5.14.1, trust_remote_code) o vLLM ≥0.25,<0.33 con plugin NVIDIA (MTP speculativo); vllm serve espone API OpenAI-compatibile. Licenza OpenMDW 1.1: uso commerciale consentito."
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: source.nvidia-nemotron-3-5-parse-hf
        path: https://huggingface.co/nvidia/Nemotron-3.5-Parse
        note: sezioni Quick Start, Inference with vLLM, License della card
  - id: parse-multilingua
    text: "Multilingua: MOSCAR 99,51 char-bag F1 su 8.111 pagine sintetiche semplici (163 lingue/script) — la card avverte esplicitamente che non garantisce accuratezza su scansioni complesse e che il char-bag F1 ignora l'ordine dei caratteri. Il '<1% errore sul cirillico' del post sorgente rientra in questo caveat: non ho letto i valori per-script."
    confidence: 0.6
    evidence:
      - kind: web
        sourceId: source.nvidia-nemotron-3-5-parse-hf
        note: highlight MOSCAR + caveat in card; valori per-script non letti (reference/multilingual/moscar_by_language.md)
  - id: parse-brixia-angle
    text: "Per BRIX-IA: candidato self-host per l'ingest PDF (fatture/bilanci/estratti conto della pipeline FF/Xray) — 0,63B gira anche su hardware modesto, API OpenAI-compatibile via vLLM, output Markdown+bbox direttamente compatibile con la strategia retrieval stratificata (deterministico per tabellari)."
    confidence: 0.7
    evidence:
      - kind: chat
        sourceId: telegram:261132403
        note: "Ipotesi operativa collegata alla decisione PK 14/10 (pipeline deterministica per tabellari); da validare con pilot"
questions:
  - "Come si confronta con MinerU (già in uso nella pipeline deterministica) su estratti conto reali, non su ParseBench?"
  - "Gira su hardware nostro (mini-PC/RTX) a velocità accettabile, o serve H100 per il throughput dichiarato?"
  - "Il confronto con Firecrawl pdf-inspector (via API) su documenti sporchi: quale vince per costo/qualità?"
status: active
updatedAt: 2026-10-22T16:12:00Z
publish: true
---

# NVIDIA Nemotron 3.5 Parse — parser di documenti da 0,63B

## Notes
<!-- openclaw:human:start -->
### Collegamenti
- Entità: [[entities/nvidia|NVIDIA]]
- Fonte primaria verificata: [[sources/nvidia-nemotron-3-5-parse-hf|Model card Nemotron 3.5 Parse (HF)]]
- Contesto d'uso BRIX-IA: Architettura retrieval stratificata — MinerU oggi copre il ramo deterministico tabellari; Parse è il candidato alternativo/validatore
- Alternativa via API: [[syntheses/pdf-inspector-firecrawl|pdf-inspector (Firecrawl)]]
- Output deterministico da documenti: [[syntheses/gotenberg|Gotenberg]] (HTML→PDF, lato opposto della pipeline)
- Stessa famiglia "modelli piccoli specializzati": Spark-X2.6-4B on-device · [[syntheses/nvidia-parakeet-tdt-0-6b-v2|NVIDIA Parakeet TDT 0.6B v2]] (stesso philosophy NVIDIA: modello piccolo, task stretto, velocità)
- Embedding per l'indicizzazione a valle: EmbeddingGemma 2
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
**Segnalazione:** post Telegram inoltrato da PK (22/10/2026), verificato sulla model card HF il 22/10/2026.

## Che cos'è
Parser di pagine documento rilasciato da NVIDIA il 17/10/2026: immagine di pagina (scan o PDF renderizzato) → stringa strutturata con testo Markdown, **classi semantiche di layout, bounding box content-normalized e ordine di lettura**. Le utility di postprocessing preservano spans e celle vuote e convertono tabelle e dati di grafici in **LaTeX, HTML, Markdown, JSON o CSV**.

Architettura: encoder vision **C-RADIOv4-SO400M** + adapter conv1D + decoder **mBART causale a 10 layer** (GQA 16Q/8KV) che consuma la sequenza visiva come prefisso causale; preprocessing NaViT rettangolare dinamico; tokenizer multilingue 72.505 token con token di controllo (`<predict_bbox>`, `<class_Chart>`, …); testa MTP one-step per decodifica speculativa in vLLM. **0,631B parametri** unici.

## Il numero che conta
ParseBench **75,20** in triple-pass su 2.078 pagine — praticamente pari a **LightOnOCR-3-4B (75,10)** che ha ~6× i parametri ma fa **2,76 pagine/s contro 10,62** su 1× H100 (~3,85× più veloce). Single-pass: 72,74 a **15,42 pp/s**, il migliore per throughput della tabella. Sotto: Infinity-Parser2-Flash 73,25/3,06; MinerU2.5-Pro 72,78/4,13; PaddleOCR-VL 67,43/3,11; Nemotron Parse 2.0 63,91/3,95.

**Caveat:** punteggio e timing sono auto-riportati da NVIDIA sulla propria pipeline/H100; il "quasi pari" a LightOnOCR-3-4B è un confronto single-source.

## Multilingua — con cautela
IndicVisionBench 83,73 ANLS-char (10 lingue); MOSCAR 99,51 char-bag F1 su 8.111 pagine **sintetiche semplici** su 163 lingue/script. La card stessa avverte: niente garanzia su scansioni complesse/corsivo/degradato, e il char-bag F1 non considera l'ordine dei caratteri. La claim del post "cirillico <1% CER" ricade in questo caveat (valori per-script non letti).

## Runtime e licenza
Transformers (`transformers==5.14.1`, `trust_remote_code`) o **vLLM con plugin NVIDIA** (≥0.25,<0.33, MTP+FA3 automatici); `vllm serve` dà **API OpenAI-compatibile**, c'è Docker. **OpenMDW 1.1 → uso commerciale consentito** (tokenizer MIT).

## Lettura operativa per noi
Candidato naturale per il **ramo deterministico/tabellari** della nostra architettura retrieval (estratti conto, bilanci, fatture FF/Xray): piccolo, self-host, output Markdown+bbox già allineato al formato che usiamo per l'indicizzazione. Da validare contro **MinerU** (già in pipeline) e contro **pdf-inspector/Firecrawl** su documenti reali sporchi — i benchmark pubblicati non sostituiscono il test sui nostri PDF.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [NVIDIA Nemotron 3.5 Parse — model card Hugging Face](../sources/nvidia-nemotron-3-5-parse-hf.md)

### Referenced By

- [PDF Inspector (Firecrawl)](pdf-inspector-firecrawl.md)
<!-- openclaw:wiki:related:end -->
