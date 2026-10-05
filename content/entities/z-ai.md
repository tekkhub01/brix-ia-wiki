---
title: "Z.AI (Zhipu AI)"
id: z-ai
pageType: entity
entityType: organization
sourceIds:
  - sources/benchmark-open-weight-2026-08-21.md
  - sources/brix-ia-newsletter-news-aprile-2026.md
  - sources/perplexity-agenti-fisici-ai-2026-skill-mercato.md
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-10-04T04:00:00Z
publish: true
---

# Z.AI (Zhipu AI)

**Type:** organization — AI lab cinese  
**Rilevanza per questo vault:** produce la linea GLM — 5.1 è il modello candidato
per l'inferenza locale di [OfficeNode](brix-ia.md), 5.3 è il caso di open-weight che
arriva in cima all'indice di [Artificial Analysis](artificial-analysis.md)

## Prodotti

### GLM 5.3

Segnalata da un canale Telegram di aggregazione news AI il 2026-08-21: **60 punti** sull'
[Artificial Analysis Intelligence Index](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md),
alla pari con Kimi K3 e a un punto dal vertice della classifica. Il punto del
post non è il coding — dove la linea GLM era già data per forte — ma il fatto che
regga come modello *generalista*.

> **Confermato alla fonte il 2026-08-26.** GLM-5.3 (max) = **60** sull'Intelligence
> Index, alla pari con Kimi K3 (60) e a un punto da GPT-5.6 Sol (max, 61); il vertice è
> Claude Opus 5 (max) a 63. Cade invece il "Sol max a 63" del forward: 63 è di Opus 5.
> Il dato che il forward non dava: **costo per task $0,68 contro $2,34** del vertice, e
> **GLM-5.3-Flash fa 57 punti a $0,09** — un quarto del punteggio di distanza a un
> ventiseiesimo del prezzo. Vedi
> [Verifica sulle fonti primarie](../sources/verifica-leaderboard-benchmark-2026-08-26.md).

> **Aggiornamento 2026-10-04 (seconda mano, da verificare alla fonte):** dal 20
> settembre GLM-5.3 **e GLM-5.3-Flash sono disponibili come open weights**, con due
> licenze diverse (fonte: innfactory.ai, 20/9). Il refresh del listino di settembre ha
> inoltre **delistato GLM-5-Turbo e GLM-5V-Turbo** (fonte: usagepricing.com, 8/9). Se
> confermato, la variante Flash — il caso "57 punti a $0,09" — passa da endpoint
> proprietario a pesi scaricabili: cambia la premessa economica dello stack on-premise.

Se confermato, è il secondo pilastro della tesi "l'efficienza sta mangiando il
premium" insieme a [DeepSeek](deepseek.md): open-weight in top-3 di intelligenza
generale, non solo su nicchie.

### GLM 5.1

- **Release:** 27 marzo 2026
- **Licenza:** MIT — HuggingFace `zai-org/GLM-5.1`
- **Dimensioni:** full-size, parametri esatti non dichiarati
- **Risultato chiave:** primo modello open-source a superare tutti i proprietari
  su SWE-Bench Pro (58,4), battendo GPT-5.4, Claude Opus 4.6 e Gemini 3.1 Pro
- **Compatibilità:** vLLM, SGLang, KTransformers
- **Hardware:** ottimizzato per inferenza locale (GPU NVIDIA, offload CPU via
  KTransformers)

**Perché conta qui:** la licenza MIT consente l'embedding commerciale in una box
fisica, e la parità di performance sposta la proposta di valore — locale > cloud
su costo e privacy. È la premessa economica di tutto lo stack on-premise.

> Cifre non ri-verificate dopo il 2026-04-28. Trattare i benchmark come
> registrati, non confermati.

**Sources:**
- [Benchmark open-weight 2026-08-21](../sources/benchmark-open-weight-2026-08-21.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](artificial-analysis.md)
- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index](../sources/benchmark-open-weight-2026-08-21.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
- [Hugging Face](hugging-face.md)
- [OpenAI](openai.md)

### Related Pages

- [Anthropic](anthropic.md)
- [BRIX-IA](brix-ia.md)
- [DeepSeek](deepseek.md)
- [Google](google.md)
- [Karpathy, Andrej](karpathy-andrej.md)
- [OpenRouter](openrouter.md)
- [scrya-com](scrya-com.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [LLM Memory & Context Evolution — Deep Research](../sources/llm-memory-context-evolution-2026.md)
