---
pageType: synthesis
id: synthesis.esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant
title: Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant
sourceIds:
  - source.l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant
claims:
  - id: gemma4-arch
    text: Gemma 4 12B Unified è un modello denso decoder-only (vedi [RotorQuant](../entities/scrya-com.md) per tecniche di quantizzazione avanzate) da 11,95B parametri
      con architettura encoder-free che proietta direttamente input multimodali
      nello spazio embedding
    status: verified
    confidence: 0.95
    evidence:
      - kind: pdf
        sourceId: pdf:Esperimenti_Quantizzazione_Gemma_4_1---96861467-650a-41d7-bc76-eedb62006fd3.pdf
        note: Sezione architettura, 48 strati, Vision Embedder 35M, Audio Wave
          Projection
  - id: qat-unsloth
    text: Unsloth Dynamic QAT raggiunge 88,76% accuratezza Top-1 vs 74,08% naive
      Q4_0 su Gemma 4 12B, con esattezza byte 99,96%
    status: verified
    confidence: 0.95
    evidence:
      - kind: pdf
        sourceId: pdf:Esperimenti_Quantizzazione_Gemma_4_1---96861467-650a-41d7-bc76-eedb62006fd3.pdf
        note: Tabella comparativa QAT, sezione Unsloth Dynamic
  - id: mtp-speedup
    text: MTP porta speedup 3,11x su Gemma 4 31B (40.3→125.3 t/s), massimo nel
      coding (3.82x)
    status: verified
    confidence: 0.9
    evidence:
      - kind: pdf
        sourceId: pdf:Esperimenti_Quantizzazione_Gemma_4_1---96861467-650a-41d7-bc76-eedb62006fd3.pdf
        note: Benchmark MTP
  - id: turboquant-context
    text: TurboQuant estende contesto da 8K a 100K token su RTX 3090 con solo -7.4%
      perdita velocità
    status: verified
    confidence: 0.9
    evidence:
      - kind: pdf
        sourceId: pdf:Esperimenti_Quantizzazione_Gemma_4_1---96861467-650a-41d7-bc76-eedb62006fd3.pdf
        note: Benchmark TurboQuant, sezione KV Cache
  - id: mtp-turboquant-incompatibility
    text: MTP e TurboQuant sono incompatibili nell'architettura Gemma 4 a causa
      dell'alternanza attention locale/globale GQA
    status: verified
    confidence: 0.85
    evidence:
      - kind: pdf
        sourceId: pdf:Esperimenti_Quantizzazione_Gemma_4_1---96861467-650a-41d7-bc76-eedb62006fd3.pdf
        note: Sezione incompatibilità software
confidence: 0.9
status: active
updatedAt: 2026-09-13T04:40:00Z
publish: true
---

# Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant

## Notes
<!-- openclaw:human:start -->
### Collegamenti nel vault
- Fonte primaria (ingerita il 28/08, prima era solo un riferimento `pdf:` che non risolveva): [L'Incrocio delle Tecnologie di Compressione Locale](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)
- [Google](../entities/google.md) — Gemma 4 12B Unified · [scrya-com](../entities/scrya-com.md) — TurboQuant · [Unsloth](../entities/unsloth.md) — Dynamic QAT
- [Qwen3.8-Flash-Next — MoE 125B locale a 75GB](qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md) — l'altra serie KLD/top-1 del vault
- [Hardware per inferenza locale domestica](hardware-per-inferenza-locale-domestica-presente-e-futuro.md) — le macchine su cui questi footprint contano
### Collegamenti (dreaming 2026-08-15)
- Secondo corpus indipendente sulle stesse tecniche: [Qwen3.8 su Unsloth](qwen3-8-unsloth-inferenza-locale.md) — concorda sul metodo, diverge su MTP
- Il metodo Dynamic misurato qui è di [Unsloth](../entities/unsloth.md); RotorQuant, successore di TurboQuant, è di [scrya-com](../entities/scrya-com.md)
- L'argomento: [quantization](../concepts/quantization.md)
- Divergenza registrata: [MTP × compressione KV](../questions/q-mtp-vs-kv-compression.md)

<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Esperimenti Quantizzazione Gemma 4 12B

## Summary
<!-- openclaw:wiki:generated:start -->

### Obiettivo
Analizzare tecniche di ottimizzazione per inferenza locale di **Gemma 4 12B Unified** su hardware consumer (16GB RAM/VRAM), bilanciando efficienza memoria, velocità e fedeltà del modello.

### Architettura Encoder-Free
- **11,95B parametri**, 48 strati transformer, decoder-only
- Contesto: 256K token, sliding window 1024 token
- **Vision Embedder (35M):** sostituisce ViT tradizionale, proietta patch immagine via singola matmul
- **Audio Wave Projection:** segnale 16 kHz in frame da 40ms, proiezione lineare senza encoder dedicato
- Pesi condivisi testo/immagini/audio → fine-tuning unificato
- Footprint: BF16 = 26,7 GB | Q4_0 = 6,7 GB

### Tre Tecnologie Analizzate

**QAT (Quantization-Aware Training)**
- Simula riduzione precisione durante training, pesi compensano errori discretizzazione
- Problema: conversione GGUF naive (scale F16 vs BF16) → accuratezza Top-1 26B-A4B al 70,20%
- Soluzione Unsloth Dynamic (UD-Q4_K_XL): allineamento scale, esattezza byte 99,96%

**MTP (Multi-Token Prediction)**
- Decodifica speculativa: drafter predice N token, modello verifica in parallelo
- Efficace fino a 2 token ipotizzati, poi saturazione per alto tasso di scarto

**TurboQuant (KV Cache Compression)**
- Compressione geometrica KV cache a 3-4 bit (PolarQuant + QJL)
- Compressione Key più critica di Value (amplificazione errori softmax)

### Risultati Chiave

| Config | Accuratezza Top-1 | KLD Media | Dimensione |
|---|---|---|---|
| Naive Q4_0 | 74,08% | 0,50702 | 6,98 GB |
| **Unsloth Dynamic QAT** | **88,76%** | **0,13288** | **6,72 GB** |

- **MTP speedup:** 40,3 → 125,3 t/s (3,11x), coding 3,82x, math 3,37x
- **TurboQuant:** contesto da 8K → 100K token su RTX 3090, solo -7,4% velocità

### Conclusioni
1. QAT + Unsloth Dynamic essenziale per preservare logica a 4 bit
2. Compressione geometrica KV efficace (Key > Value)
3. MTP limitato a 2 token, poi saturazione
4. **Incompatibilità MTP + TurboQuant** (conflitto architetturale: attention locale + globale GQA)

### Implicazioni Pratiche
- Gemma 12B Q4_0 = 6,72 GB → laptop 16GB
- ~120 t/s su RTX 4070 con QAT + MTP
- Config ottimale: MTP 2 token + KV cache asimmetrica (q4_0 Key, q3_0 Value)

<!-- openclaw:wiki:generated:end -->

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)

### Referenced By

- [Hardware per inferenza locale domestica — presente e futuro](hardware-per-inferenza-locale-domestica-presente-e-futuro.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)
- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)
- [Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale](qwen3-8-unsloth-inferenza-locale.md)
- [Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)](qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md)
- [Unsloth](../entities/unsloth.md)
<!-- openclaw:wiki:related:end -->
<!-- openclaw:wiki:generated:end -->
