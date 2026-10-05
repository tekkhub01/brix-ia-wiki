---
title: "NVIDIA"
id: nvidia
pageType: entity
entityType: organization
sourceIds:
  - sources/qwen3-8-how-to-run-locally-unsloth.md
  - sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md
  - sources/nvidia-parakeet-tdt-0-6b-v2.md
updatedAt: 2026-09-01T00:00:00Z
publish: true
---

# NVIDIA

**Type:** organization — hardware, formati numerici, modelli open
**Sito:** https://nvidia.com
**Rilevanza per questo vault:** è il vincolo fisico sotto quasi ogni discussione di
inferenza locale qui dentro. Ogni raccomandazione hardware per PMI, ogni formato di
quantizzazione e ogni cifra di throughput passa da una sua architettura, e fino al
2026-09-01 non aveva una scheda

## Prodotti

### Blackwell e NVFP4

Formato a virgola mobile a 4 bit che richiede GPU Blackwell (RTX 50x, DGX Spark,
B200/B300), servito via vLLM o SGLang.

- ~**1,5× più veloce di BF16** a dimensione file comparabile
- **92–97% di recovery top-1** rispetto a BF16

Cifre **dichiarate da [Unsloth](unsloth.md)**, non misurate indipendentemente in
questo vault. Il formato è rilevante qui perché è il caso in cui il vendor hardware
detta la forma della quantizzazione: NVFP4 non è un metodo scelto dal quantizzatore
ma un percorso aperto dal silicio. Vedi
[Quantization](../concepts/quantization.md).

### DGX Spark / GB10 Grace Blackwell

La macchina che il vault valuta e, di fatto, sconsiglia per il caso d'uso PMI:

| | GB10 |
|---|---|
| Memoria | 128 GB LPDDR5X unificata a 273 GB/s |
| Prezzo | €3.900–4.200 |
| Dense 70B | **4,7 tok/s** |
| MoE | 82–102 tok/s |

Il dato interessante è la forbice: la stessa macchina è inutilizzabile su un modello
denso e accettabile su un MoE. È la ragione per cui l'architettura del modello, non
la VRAM, è la prima variabile in
[Hardware per inferenza locale domestica](../syntheses/hardware-per-inferenza-locale-domestica-presente-e-futuro.md).

La [guida hardware PMI](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md)
apre esplicitamente contro i claim di marketing di questa classe di prodotti
("*Claimed 40 tok/s… Reality max 3.3 tok/s theoretical*"), che è il motivo per cui
le sue cifre sono fra le poche qui a non provenire dal produttore.

### Rubin

Architettura successiva a Blackwell, attesa H2 2026. Nessun dato di prima mano.

### Parakeet TDT 0.6B v2

Modello STT open source. È l'unico prodotto NVIDIA in questo vault che sia un
*modello* e non un vincolo hardware, ed è coperto da una
scheda propria — la più povera del
corpus, versionata e destinata a invecchiare male.

### CUDA, TensorRT-LLM, NVLink-C2C

Citati come dipendenze operative (`-DGGML_CUDA=ON` nelle build di
[llama.cpp](ggml.md)), mai come oggetto di analisi.

## Contraddizione aperta che passa di qui

Su hardware NVIDIA converge una divergenza non risolta: l'esperimento su Gemma 4
registra **MTP e compressione della KV cache come incompatibili** (attribuito
all'attention locale/globale alternata in GQA), mentre la documentazione Qwen3.8 su
Blackwell documenta NVFP4 con calibrazione FP8 della KV cache *insieme* a MTP.
Tracciata in
[q-mtp-vs-kv-compression](../questions/q-mtp-vs-kv-compression.md).
Su H100 il vault registra invece un dato di terzi: 40,3 → 125,3 t/s con MTP (3,11×).

## Perché ci interessa

Due ragioni distinte, che conviene non confondere. Come **fornitore di capacità**,
determina cosa BRIX-IA può proporre a una PMI a un dato budget. Come **fonte di
cifre**, è un attore di parte: quasi tutti i numeri NVIDIA in questo vault sono
dichiarati da lui o da chi ne integra i formati, e le uniche misure indipendenti
disponibili — la guida hardware — lo ridimensionano.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Hugging Face](hugging-face.md)

### Related Pages

- [Alibaba](alibaba.md)
- [BRIX-IA](brix-ia.md)
- [ggml / llama.cpp](ggml.md)
- [Unsloth](unsloth.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)
