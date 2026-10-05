---
title: "Artificial Analysis"
id: artificial-analysis
pageType: entity
entityType: organization
sourceIds:
  - sources/benchmark-open-weight-2026-08-21.md
updatedAt: 2026-10-04T04:00:00Z
publish: true
---

# Artificial Analysis

**Type:** organization — casa di benchmarking indipendente per modelli e provider
di inferenza (artificialanalysis.ai)
**Rilevanza per questo vault:** è l'arbitro che quasi tutte le fonti di agosto
citano quando dicono "questo modello è forte", senza che nessuna pagina spiegasse
finora cosa misuri davvero quel numero.

## Prodotti

### Artificial Analysis Intelligence Index

Indice composito che fonde 9 eval in un unico punteggio, versione di riferimento
4.1.1. Pesi per categoria verificati sulla pagina di metodologia il 26/08: **Agents 34%,
Coding 24%, Scientific Reasoning 24%, General 18%**. Pesi per singola eval:
GDPval-AA v2 20% · 𝜏³-Banking 14% · Terminal-Bench v2.1 16% · SciCode 8% ·
HLE 12% · AA-Omniscience 12% · AA-LCR 6% · GPQA Diamond 6% · CritPt 6%.
Vertice al 26 agosto 2026: Claude Opus 5 (max) di [Anthropic](anthropic.md) a 63.

> **Aggiornamento 2026-10-04 (seconda mano, da verificare alla fonte):** a inizio
> ottobre l'indice risulta alla versione **v4.3.2** con un vertice nuovo: GPT-5.6 Sol
> ~58.9 e **Claude Opus 5.5 ~57.6** (il punteggio più alto pubblicato da AA per un
> modello, +4.3 su Fable 5.1), Sonnet 5.5 ~56.0 — su 215 modelli (benchlm.ai 2/10,
> felloai.com 1/10). I numeri di questo vault (63/61/60) sono lo snapshot v4.1.1 di
> agosto: scala cambiata (max 63 → ~59), non classifica ribaltata. Da ri-verificare
> sulla pagina indice come fu fatto il 26/08.

> **La fonte si contraddice da sola.** La FAQ della pagina dell'indice dice "four
> categories **each contribute 25%**", la pagina di metodologia dice 34/24/24/18. La
> tabella per eval somma a 34/24/24/18, quindi la FAQ è la pagina sbagliata — ma chi
> cita l'indice partendo dalla FAQ riporta pesi inesistenti.

**Analisi completa, benchmark per benchmark:**
[Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)

### GDPval-AA v2

Eval proprietaria, erede di GDPval (OpenAI, 2025): misura produttività economica
reale su lavoro cognitivo, con il modello che agisce da agente e produce
deliverable. Scoring Elo su confronti ciechi, con il lavoro di un esperto umano
ancorato a ~1000. Pesa il 20% dell'Indice — il singolo componente più alto.

### Implementazioni proprie dei benchmark di terzi

AA non si limita ad aggregare: **riesegue** le eval con il proprio scaffolding. Il
risultato è che per Terminal-Bench v2.1 esistono due classifiche pubbliche con vertici
diversi — 89,5% qui, 83,8% sulla leaderboard ufficiale del
[Laude Institute](laude-institute.md). Non è un errore di nessuno dei due; è la
conseguenza di misurare *modello + harness* e chiamarlo *modello*. Vedi
[Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md).

## Perché ci interessa

Il peso di **34% sugli agenti** è la ragione per cui l'Indice si muove in modo
diverso dai benchmark a crocette: premia il fare, non il sapere. È anche il
motivo per cui è il terreno su cui i modelli open-weight —
[DeepSeek](deepseek.md), GLM di [Z.AI](z-ai.md), Kimi — recuperano più in fretta:
su un agent loop l'inferenza extra si compra, la conoscenza enciclopedica no.

Il resto del vault ne dipende in modo implicito: [Z.AI](z-ai.md),
[Alibaba](alibaba.md), [Unsloth](unsloth.md) e [Anthropic](anthropic.md) sono
tutte pagine dove un numero di questo indice, o di un suo componente, sostiene un
claim.

**Sources:**
- [Benchmark open-weight 2026-08-21](../sources/benchmark-open-weight-2026-08-21.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Anthropic](anthropic.md)
- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index](../sources/benchmark-open-weight-2026-08-21.md)
- [DeepSeek Harness — Agent Harness "Everything is a Plugin"](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md)
- [OpenAI](openai.md)
- [Z.AI (Zhipu AI)](z-ai.md)

### Related Pages

- [DeepSeek](deepseek.md)
<!-- openclaw:wiki:related:end -->
