---
title: "Alibaba"
id: alibaba
pageType: entity
entityType: organization
sourceIds:
  - sources/qwen3-8-how-to-run-locally-unsloth.md
updatedAt: 2026-10-04T04:00:00Z
publish: true
---

# Alibaba

**Type:** organization — gruppo tecnologico cinese, divisione cloud/AI (Alibaba Cloud)
**Rilevanza per questo vault:** rilascia la famiglia **Qwen**, i modelli aperti
che compaiono più spesso nelle nostre configurazioni locali

## Prodotti

### Qwen — famiglia di modelli

Modelli a pesi aperti, distribuiti anche in GGUF da terze parti. La famiglia è
ricorrente in questo vault perché è quella che regge il carico sulle macchine
locali documentate qui.

**Qwen 4** (preview 22/9/2026, Apsara Conference). Quattro tier annunciati —
**Qwen 4 Max, Qwen 4 Flash, Qwen 4 Plus, Qwen 4 27B** — senza prezzo, pesi,
contesto o punteggio pubblicati per nessuno: Alibaba ha dichiarato il modello
"currently in training", nessuna data. Annunciata anche una roadmap da 10T
parametri. Finché non escono i pesi, la famiglia aperta che regge lo stack
locale resta la 3.8 qui sotto. Seconda mano (orcarouter.ai, daily.dev,
pasqualepillitteri.it, 22-26/9) — da verificare alla fonte.

**Qwen3.8** (2026-08). Tre varianti:

| Variante | Parametri | Note |
|---|---|---|
| Qwen3.8-27B | 27B denso | vision + reasoning, contesto 256K (1M via YaRN), hybrid thinking |
| Qwen3.8-2.4T-A95B | 2,4T (95B attivi) | thinking-only, contesto ~1,01M |
| Qwen3.8-Max | — | hybrid |

Due dettagli architetturali con conseguenze operative dirette:

- **`reasoning_effort` nativo** (`xhigh` default, `medium`, `low`, none): la leva
  di costo/profondità è esposta dal modello, non dall'orchestratore.
- **Preserve Thinking**: mantiene la traccia di ragionamento del turno precedente
  — più token, potenzialmente più accuratezza sulle conversazioni lunghe.

I preset consigliati **divergono fra le due modalità** (thinking `temp 1.0`/
`top_p 0.95`; instruct `temp 0.7`/`top_p 0.80`/`presence_penalty 1.5`): una
configurazione unica per entrambe è un errore.

**Analisi hardware e quantizzazione:**
[Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale](../syntheses/qwen3-8-unsloth-inferenza-locale.md)

### Alibaba come provider di modelli

Compare anche come backend selezionabile in tool di terze parti — per esempio in
[JCode](../syntheses/jcode-agente-di-coding-super-veloce.md), accanto ad
Anthropic, OpenAI, Google e Azure. JCode **non** è un prodotto Alibaba: la
relazione è solo di provider supportato.

## Perché ci interessa

I modelli Qwen sono la famiglia aperta che compare in quasi tutti gli stack
locali censiti qui — LobeChat,
[Libre WebUI](../sources/libre-webui-github.md), il
[convertitore audiolibri](../syntheses/qwen3-audiobook-converter.md) — e Qwen3.8-27B
a 4 bit (17-19 GB) è oggi il candidato più concreto per la fascia hardware
descritta nella [guida LLM locale per PMI](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md).

**Sources:**
- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)

- [Qwen3.8-Flash-Next — How to Run Locally (Unsloth)](../sources/qwen3-8-flash-next-how-to-run-locally-unsloth.md) — 125B MoE su architettura Qwen4, contesto 262K (2026-08-28)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](artificial-analysis.md)
- [BRIX-IA](brix-ia.md)
- [Come Usare un LLM in Locale nel 2026: Guida Hardware per PMI con Prezzi, Benchmark e 3 Fasce di Budget](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
- [ggml / llama.cpp](ggml.md)
- [JCode — Agente di coding super-veloce](../syntheses/jcode-agente-di-coding-super-veloce.md)
- [Libre WebUI — Privacy-First Web Interface for Local AI](../sources/libre-webui-github.md)
- [Microsoft](microsoft.md)
- [Qwen3 Audiobook Converter (WhiskeyCoder)](../syntheses/qwen3-audiobook-converter.md)
- [Qwen3.8 — How to Run Locally (Unsloth)](../sources/qwen3-8-how-to-run-locally-unsloth.md)
- [Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale](../syntheses/qwen3-8-unsloth-inferenza-locale.md)

### Related Pages

- [NVIDIA](nvidia.md)
- [Unsloth](unsloth.md)
<!-- openclaw:wiki:related:end -->
