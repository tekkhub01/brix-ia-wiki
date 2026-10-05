---
title: "ggml / llama.cpp"
id: ggml
pageType: entity
entityType: organization
sourceIds:
  - sources/qwen3-8-how-to-run-locally-unsloth.md
  - sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md
updatedAt: 2026-09-01T00:00:00Z
publish: true
---

# ggml / llama.cpp

**Type:** organization — progetto open source e azienda (ggml.ai, fondata da Georgi Gerganov)
**Repository:** https://github.com/ggml-org/llama.cpp
**Rilevanza per questo vault:** è il runtime su cui poggia praticamente ogni
deployment locale discusso qui, e il formato in cui sono distribuiti i pesi che
questo vault raccomanda — eppure non compare mai come soggetto, solo come
infrastruttura data per scontata

## Nota di provenienza, in cima perché conta

**Tutto ciò che questo vault sa di llama.cpp è di seconda mano.** Nessuna fonte
primaria del progetto è mai stata ingerita, e il nome del suo autore non compare
in nessuna pagina del vault. Ogni dato qui sotto arriva da chi ci costruisce sopra
— [Unsloth](unsloth.md) e l'esperimento Gemma — cioè da parti interessate a
mostrare che i propri metodi funzionano. La pagina esiste perché l'assenza era
peggiore dell'imprecisione, non perché il materiale sia solido.

## Prodotti

### llama.cpp

Runtime di inferenza in C/C++ per esecuzione locale su CPU e GPU consumer. Nel vault
appare esclusivamente come dipendenza: build con `-DGGML_CUDA=ON`, fork per feature
non ancora upstream, formato di distribuzione dei quant.

### GGUF / GGML

Il formato di file. È di fatto lo standard di distribuzione dei pesi open-weight per
uso locale in tutto questo vault: i modelli [Alibaba](alibaba.md) sono "distribuiti
anche in GGUF da terze parti", i quant [Unsloth](unsloth.md) sono GGUF, l'esperimento
Gemma misura conversioni GGUF.

Un dato che merita attenzione perché è l'unico caso qui in cui il *formato* causa
una perdita misurata: la conversione naive di un checkpoint QAT verso GGUF porta la
top-1 al **70,20%**, per un disallineamento di scala F16 vs BF16. La correzione
Unsloth (UD-Q4_K_XL) riporta la byte-exactness al **99,96%**. Il formato non è
neutro: sbagliare la conversione costa più di scendere di un livello di bit.

### Quantizzazioni della famiglia

`IQ1_S`, `TQ2_0`, `TQ1_0`, `Q1_0`, `Q4_0`, `Q4_K_M`, `Q4_K_XL`, `Q6_K`. Unsloth ha
esteso `IQ1_S` da 1,5625 a 1,1875 bpw riducendo le entry del codebook da 2048 a 256,
con il costo registrato: perplexity 2,58 → 4,49 e accordo top-p dal 78,9% al 66,3%.

### Fork

Il vault ne registra due che contano, entrambi **non upstream**: il branch
`iq1-narrow` su `unslothai/llama.cpp`, e `atomicmilkshake` per i kernel CUDA
TurboQuant + TriAttention. È un segnale strutturale: le tecniche più interessanti
misurate in questo vault girano su fork privati, non sul runtime che tutti installano.

## Perché ci interessa

Perché è il punto in cui le raccomandazioni di questo vault diventano eseguibili, e
perché è il livello dove i risultati smettono di essere riproducibili senza dirlo.
Quando una pagina qui afferma un throughput o una qualità di quantizzazione, il
numero vale per una certa build, di un certo fork, con certi flag — e quasi nessuna
delle fonti lo dichiara.

Da ingerire, prima di trattare qualunque cifra su GGUF come solida: la documentazione
primaria del progetto.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Hugging Face](hugging-face.md)
- [NVIDIA](nvidia.md)

### Related Pages

- [Alibaba](alibaba.md)
- [Unsloth](unsloth.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT,](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)
