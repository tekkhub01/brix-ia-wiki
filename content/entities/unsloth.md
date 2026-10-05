---
title: "Unsloth"
id: unsloth
pageType: entity
entityType: organization
sourceIds:
  - sources/qwen3-8-how-to-run-locally-unsloth.md
updatedAt: 2026-08-15T00:00:00Z
publish: true
---

# Unsloth

**Type:** organization — progetto open-source / azienda (unslothai)
**Repository:** https://github.com/unslothai/unsloth
**Rilevanza per questo vault:** produce i quant che rendono eseguibili in locale i
modelli che ci interessano, ed è il metodo che due esperimenti indipendenti in
questo vault indicano come migliore a parità di bit

## Prodotti

### Unsloth Dynamic (quantizzazione)

Metodo di quantizzazione dinamica, arrivato alla **V3.0** (preview) con Qwen3.8.
La sua caratteristica non è il numero di bit ma **come** li alloca: l'errore di
discretizzazione non è distribuito in modo uniforme sul modello.

Due misure indipendenti, da corpora diversi:

| Modello | Confronto | Risultato |
|---|---|---|
| Gemma 4 12B | Dynamic QAT (UD-Q4_K_XL) vs Q4_0 naive | **88,76%** vs **74,08%** top-1, a parità di 4 bit |
| Qwen3.8 | IQ2_XXS (9 GB) vs BF16 (54,7 GB) | **82,5%** accuracy trattenuta, **83,5%** più piccolo |

Il primo dato viene da [Esperimenti Quantizzazione Gemma 4 12B](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md),
il secondo dalla documentazione Qwen3.8. Concordano su una cosa: **il metodo pesa
più del formato**.

### Data-type 1-bit estesi

Estensione di `IQ1_S` di llama.cpp da 1,5625 bpw a **1,1875 bpw**, riducendo le
entry del codebook da 2048 a 256 (nomi HF: `TQ2_0`, `TQ1_0`, `Q1_0`).

| Dtype | Naming | BPW | Entries |
|---|---|---:|---:|
| IQ1_S | IQ1_S | 1,5625 | 2048 |
| UD-IQ1_XS | TQ2_0 | 1,4375 | 1024 |
| UD-IQ1_XXS | TQ1_0 | 1,3125 | 512 |
| UD-IQ1_XXXS | Q1_0 | 1,1875 | 256 |

Unsloth dichiara che funzionano in **post-training quantization**, senza QAT né
QAD, «su modelli grandi». La dichiarazione è loro e i benchmark sono
esplicitamente ancora in corso: registrata come non verificata. Il costo è
comunque leggibile nei loro stessi numeri — PPL da 2,58 (IQ1_S) a 4,49
(UD-IQ1_XXXS), top-p da 78,9% a 66,3%.

### NVFP4 dinamico

Quant per GPU **Blackwell** (RTX 50x, DGX Spark, B200/B300): ~1,5x più veloce di
BF16 a dimensione file comparabile, 92-97% di recovery top-1, con calibrazione
FP8 della KV cache per raddoppiare il contesto. Si servono via vLLM o SGLang. Per
hardware pre-Blackwell restano i GGUF.

### Unsloth Desktop

App UI open-source per AI locale (macOS, Windows, Linux): download e run di GGUF
e safetensor, offload automatico su RAM, rilevamento multi-GPU, tool calling
self-healing, esecuzione codice, tuning automatico dei parametri di inferenza,
inferenza CPU+GPU via MLX e llama.cpp. Include anche training (dichiarato 2x più
veloce, -70% VRAM).

### Fork di llama.cpp

Branch `iq1-narrow` su `unslothai/llama.cpp` per i data-type 1-bit estesi, non
ancora upstream.

## Perché ci interessa

È l'anello che collega i modelli che vogliamo alla memoria che abbiamo. Ogni
valutazione hardware fatta in questo vault — la
[guida LLM locale per PMI](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md),
gli esperimenti su Gemma, la fascia di [OfficeNode](brix-ia.md) — dipende da
quale quantizzazione si assume. Assumere Dynamic invece di naive sposta la stima
di accuratezza di ~14 punti a parità di RAM.

L'argomento in sé — quantizzazione come leva sulla lunghezza di contesto
utile — è trattato in
[quantization](../concepts/quantization.md).

**Sources:**
- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)

- [Qwen3.8-Flash-Next — How to Run Locally (Unsloth)](../sources/qwen3-8-flash-next-how-to-run-locally-unsloth.md) — quant 1-bit a 75 GB con Ngram/PLE non compressi, tabella KLD/top-1 (2026-08-28)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](artificial-analysis.md)
- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [BRIX-IA](brix-ia.md)
- [Come Usare un LLM in Locale nel 2026: Guida Hardware per PMI con Prezzi, Benchmark e 3 Fasce di Budget](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md)
- [DeepSeek](deepseek.md)
- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [ggml / llama.cpp](ggml.md)
- [Hugging Face](hugging-face.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)
- [LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
- [NVIDIA](nvidia.md)
- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)

### Related Pages

- [Alibaba](alibaba.md)
<!-- openclaw:wiki:related:end -->
