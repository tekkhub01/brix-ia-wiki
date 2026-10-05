---
pageType: synthesis
id: synthesis.qwen3-8-unsloth-inferenza-locale
title: Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale
sourceIds:
  - source.qwen3-8-how-to-run-locally-unsloth
  - https://unsloth.ai/docs/models/qwen3.8
claims:
  - id: qwen38-27b-4bit-footprint
    text: Qwen3.8-27B a 4 bit gira in 17-19 GB di memoria totale (RAM+VRAM o unificata),
      con finestra di contesto 256K
    status: verified
    confidence: 0.9
    evidence:
      - kind: doc
        sourceId: source.qwen3-8-how-to-run-locally-unsloth
        note: Tabella "Hardware requirements", sezione Usage Guide
  - id: unsloth-1bit-dynamic
    text: I GGUF Dynamic 1-bit portano Qwen3.8-2.4T-A95B da 4,9 TB (BF16) a 397 GB,
      -91%, con nuovo data-type a 1,1875 bpw ottenuto riducendo il codebook a 256 entry
    status: verified
    confidence: 0.9
    evidence:
      - kind: doc
        sourceId: source.qwen3-8-how-to-run-locally-unsloth
        note: Sezione "New 1-bit data-types", tabella Dtype/BPW/entries
  - id: ptq-senza-qat
    text: Unsloth dichiara buoni risultati sui nuovi data-type 1-bit in post-training
      quantization, senza QAT né QAD — su modelli grandi
    status: unverified
    confidence: 0.6
    evidence:
      - kind: doc
        sourceId: source.qwen3-8-how-to-run-locally-unsloth
        note: "«we also found these new data-types to be fine for PTQ without the
          need for QAT or QAD»; benchmark dichiarati ancora in corso"
  - id: nvfp4-speedup
    text: I quant NVFP4 girano ~1,5x più veloci di BF16 su GPU Blackwell mantenendo
      92-97% di accuracy recovery (top-1) rispetto a BF16
    status: verified
    confidence: 0.85
    evidence:
      - kind: doc
        sourceId: source.qwen3-8-how-to-run-locally-unsloth
        note: Tabella batch/tok-s su 1x B200 e tabella KLD/top-1 per corpus
  - id: mtp-abilitato-qwen38
    text: I GGUF Unsloth di Qwen3.8 hanno MTP abilitato, e vLLM espone speculative
      decoding MTP con num_speculative_tokens=2
    status: verified
    confidence: 0.9
    evidence:
      - kind: doc
        sourceId: source.qwen3-8-how-to-run-locally-unsloth
        note: Elenco feature dei quant Unsloth + comando `vllm serve --speculative-config`
confidence: 0.85
status: active
updatedAt: 2026-08-15T00:00:00Z
publish: true
---

# Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale

## Notes
<!-- openclaw:human:start -->
### Collegamenti
- Modello di [Alibaba](../entities/alibaba.md) (famiglia Qwen), quantizzato da [Unsloth](../entities/unsloth.md)
- Il "come" della quantizzazione è trattato come argomento in
  [quantization](../concepts/quantization.md)
- Secondo corpus indipendente sulle stesse tecniche:
  [Esperimenti Quantizzazione Gemma 4 12B](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- Rilevante per la fascia hardware di
  [OfficeNode](../entities/brix-ia.md) e per la
  [guida LLM locale per PMI](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md)
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->

## Cosa aggiunge questa fonte

La documentazione Unsloth per Qwen3.8 non è un annuncio di modello: è una **scala
hardware**. Dice, per ogni livello di bit, quanta memoria serve — che è la
domanda operativa che il vault si pone da mesi in `brix-ia-llm-locale` e in
`quantization`, e a cui finora rispondeva solo un esperimento su Gemma.

### La scala, per Qwen3.8-27B

| 2-bit | 3-bit | 4-bit | 6-bit | 8-bit | BF16 |
|---|---|---|---|---|---|
| 11-13 GB | 13-16 GB | 17-19 GB | 24 GB | 31 GB | 56 GB |

Unità = memoria totale (RAM + VRAM, o unificata). Il gradino che conta è **4-bit
a 17-19 GB**: entra in una 5080/4090 o in un Mac da 24 GB, con 256K di contesto
(estendibile a 1M via YaRN) e capacità vision.

### La scala, per Qwen3.8-2.4T-A95B

| Dynamic 1-bit XXXS | Dynamic 1-bit Standard | Dynamic 2-bit | Q8_0 | BF16 |
|---|---|---|---|---|
| 397 GB | 508 GB | 657 GB | 2,6 TB | 4,9 TB |

Da 4,9 TB a 397 GB è **-91%**. Non è un modello per hardware nostro, ma il
metodo sì: Unsloth ha esteso IQ1_S da 1,5625 bpw a **1,1875 bpw** riducendo le
entry del codebook da 2048 a 256. Il costo è leggibile nella loro stessa tabella —
PPL da 2,58 a 4,49, top-p da 78,9% a 66,3% — e va letto come tale: la
compressione estrema **non è gratis**, è un cambio di regime.

### NVFP4 — l'altra strada

~1,5x più veloce di BF16 a parità di dimensione file, 92-97% di recovery
top-1, più calibrazione FP8 della KV cache per contesto doppio. Richiede però
**Blackwell** (RTX 50x, DGX Spark, B200/B300). Per il parco macchine esistente
restano i GGUF; NVFP4 è la strada di chi compra ora.

## Il punto che emerge solo incrociando le fonti

Il vault ha ora **due corpora indipendenti** sulla stessa domanda — quanto conta
il *metodo* di quantizzazione rispetto al *numero di bit*:

| | Fonte | Risultato |
|---|---|---|
| Gemma 4 12B | [esperimenti-quantizzazione](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md) | Unsloth Dynamic QAT **88,76%** top-1 vs **74,08%** Q4_0 naive — a parità di 4 bit |
| Qwen3.8 | questa fonte | Dynamic V3.0 è il metodo con cui sono prodotti i GGUF ufficiali day-zero; IQ2_XXS trattiene **82,5%** essendo **83,5%** più piccolo |

Due modelli, due team, stessa conclusione: **a parità di bit, il metodo vale più
del formato**. Nessuna delle due pagine lo sapeva dell'altra prima di questo
passaggio.

### Divergenza aperta: MTP e compressione della KV cache

Qui i due corpora **non** concordano, ed è la cosa più interessante del confronto:

- La sintesi Gemma registra **MTP e TurboQuant incompatibili** sull'architettura
  Gemma 4, per via dell'alternanza attention locale/globale in GQA.
- Questa fonte dichiara **MTP abilitato** nei GGUF Qwen3.8, e documenta NVFP4 con
  **calibrazione FP8 della KV cache** — cioè le due cose insieme.

Le letture possibili sono almeno tre: incompatibilità specifica di Gemma 4 e non
generale; oppure differenza fra compressione geometrica (TurboQuant) e
calibrazione FP8; oppure regressione silenziosa di qualità che nessuno dei due
misura. **Non risolta qui**, per scelta: registrata come domanda aperta in
[q-mtp-vs-kv-compression](../questions/q-mtp-vs-kv-compression.md).

## Rilevanza operativa

- **Fascia 24 GB**: Qwen3.8-27B 4-bit è oggi il candidato più forte per una
  macchina singola con vision + 256K di contesto.
- **`reasoning_effort` nativo** (`xhigh`/`medium`/`low`/none) è una leva di costo
  esposta dal modello, non dall'orchestratore — rilevante per il routing degli
  agenti.
- **Preserve Thinking** mantiene la traccia di ragionamento fra i turni: più
  token spesi in cambio di accuratezza sulle conversazioni lunghe. È la stessa
  economia trattata in [context-caching](../concepts/context-caching.md),
  vista dal lato locale invece che dal lato API.
- I parametri raccomandati divergono fra thinking (`temp 1.0`, `top_p 0.95`) e
  instruct (`temp 0.7`, `top_p 0.80`, `presence_penalty 1.5`): un preset unico
  per entrambe le modalità è un errore di configurazione.

<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)

### Referenced By

- [Alibaba](../entities/alibaba.md)
- [Come Usare un LLM in Locale nel 2026: Guida Hardware per PMI con Prezzi, Benchmark e 3 Fasce di Budget](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md)
- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [Hardware per inferenza locale domestica — presente e futuro](hardware-per-inferenza-locale-domestica-presente-e-futuro.md)
- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)
- [Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)](qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md)
<!-- openclaw:wiki:related:end -->
