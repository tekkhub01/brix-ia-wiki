---
pageType: synthesis
id: synthesis.artificial-analysis-intelligence-index-e-i-suoi-9-benchmark
title: Artificial Analysis Intelligence Index e i suoi 9 benchmark
sourceIds:
  - source.benchmark-open-weight-2026-08-21
claims:
  - text: L'Artificial Analysis Intelligence Index fonde 9 benchmark in 4 categorie
      pesate (Agents 34%, Coding 24%, Scientific Reasoning 24%, General 18%).
    confidence: 0.9
    evidence:
      - kind: url
        sourceId: source.benchmark-open-weight-2026-08-21
        confidence: 0.9
        note: metodologia AA citata nel post
  - text: GDPval-AA v2 pesa il 20% dell'Indice (componente singolo più alto) e
      misura produttività economica reale via agenti Elo ancorati a 1000 =
      livello esperto umano.
    confidence: 0.9
    evidence:
      - kind: url
        sourceId: source.benchmark-open-weight-2026-08-21
        confidence: 0.9
        note: GDPval-AA v2
  - text: GPQA Diamond = 198 quesiti PhD bio/chim/fisica 'Google-proof'; baseline
      non-esperto ~34%, PhD ~65-70%.
    confidence: 0.85
    evidence:
      - kind: url
        confidence: 0.85
        note: epoch.ai / artificialanalysis.ai GPQA Diamond
confidence: 0.85
status: published
publish: true
updatedAt: 2026-08-26T00:00:00Z
---

# Artificial Analysis Intelligence Index e i suoi 9 benchmark

## Notes
<!-- openclaw:human:start -->
**Passata di armonizzazione 2026-08-26.**

*Doppio ingest ricomposto.* La pagina era costruita su due fonti che sono lo
stesso materiale ingerito due volte a due minuti di distanza. `sourceIds` ora
punta alla sola canonica,
[Benchmark open-weight 2026-08-21](../sources/benchmark-open-weight-2026-08-21.md);
la copia, ingerita due minuti prima, è stata cancellata.

*Correzione al CAVEAT della fonte.* La verifica del 24/08 dichiarava non
verificati anche i **nomi** dei modelli, ipotizzando dei placeholder. I nomi sono
reali: DeepSeek V4 Flash e V4 Pro, GPT-5.6 Sol e la famiglia Claude 5 sono modelli
in uso corrente — alcuni girano in produzione nella nostra stessa infrastruttura
di agenti (verifica interna, 2026-08-26). La stessa riga della fonte, del resto,
ammetteva già che "la serie DeepSeek V4 esiste" con i suoi score TB2.1.
Resta aperto solo il **numero** — vedi
[q-verifier-uplift-vs-index-scores](../questions/q-verifier-uplift-vs-index-scores.md),
che registra anche il punto più scomodo: se la verifica a inference-time alza di
9 punti un benchmark agentico, e gli agenti pesano il 34% dell'indice, allora
l'indice misura *modello + harness*, non il modello.

**Nel corpus.** L'indice è di [Artificial Analysis](../entities/artificial-analysis.md);
i modelli citati sono di [DeepSeek](../entities/deepseek.md),
[Z.AI](../entities/z-ai.md) (GLM-5.3), [Anthropic](../entities/anthropic.md)
(Claude Opus 5 in testa allo snapshot del 22/08). La tesi "l'efficienza sta
mangiando il premium" è la stessa che questo vault misura da un'altra angolazione
in [Unsloth](../entities/unsloth.md) e in
[quantization](../concepts/quantization.md): comprare
qualità con calcolo a valle — inferenza o quantizzazione — invece che con
parametri a monte. Tre corpora indipendenti, stessa direzione.

Il tubo pratico per sfruttarla a mano è
[CtxPort](ctxport-portabilità-del-contesto-tra-ai.md): genero sul modello
economico, porto il contesto sul premium solo per la verifica.
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Artificial Analysis Intelligence Index — i benchmark che lo compongono

## Cos'è
L'**Artificial Analysis Intelligence Index** è un benchmark composito (testo, lingua inglese) che fonde 9 valutazioni indipendenti in un unico punteggio di "intelligenza" dei modelli linguistici. Versione di riferimento citata: **4.1.1**. Va letto come una sintesi pesata, non come un test singolo; Artificial Analysis stima un intervallo di confidenza 95% inferiore a ±1%.

## Le 4 categorie e i pesi
L'indice è la media pesata di 4 categorie:
- **Agents — 34%** (task agentici, il peso maggiore)
- **Coding — 24%**
- **Scientific Reasoning — 24%**
- **General — 18%**

## I 9 benchmark fondenti
| Benchmark | Categoria | Nota |
|---|---|---|
| GDPval-AA v2 | Agents/Coding | Il componente a peso singolo più alto (20% dell'indice) |
| τ³-Banking | Agents/Coding | Task bancari agentici |
| Terminal-Bench v2.1 | Agents/Coding | Task su terminale/riga di comando |
| SciCode | Agents/Coding | Coding scientifico |
| AA-LCR | General | "Long context / reasoning" di AA |
| AA-Omniscience | General | Accuracy + componente anti-allucinazione |
| Humanity's Last Exam (HLE) | Scientific Reasoning | Ragionamento scientifico estremo |
| GPQA Diamond | Scientific Reasoning | Quesiti PhD bio/chim/fisica |
| CritPt | Scientific Reasoning | Componente critico/scientifico |

> Nota: i raggruppamenti espliciti documentati sono General = {AA-LCR, AA-Omniscience} e Scientific Reasoning = {HLE, GPQA Diamond, CritPt}; gli altri 4 coprono Agents + Coding.

## Focus: GDPval-AA v2
- Sviluppato da **Artificial Analysis**; erede di **GDPval** (OpenAI, 2025).
- Misura la **produttività economica reale** su lavoro cognitivo: il modello agisce da *agente* (legge file, esegue codice, naviga il web, produce deliverable: documenti, fogli, slide, diagrammi).
- Dataset: subset pubblico "gold" di **220 task**; dataset completo = **44 occupazioni**, **9 industrie**, **1.320 task**.
- Scoring: **Elo** su confronti ciechi tra modelli, con il lavoro di un esperto umano ancorato a ~**1000** punti. >1000 = l'output AI è preferito a quello umano.
- Peso nell'Indice: **20%** (il singolo componente più alto).
- Obiettivo: superare le "eval saturate" che non distinguono più i modelli frontier.

## Focus: GPQA Diamond
- **198** quesiti a scelta multipla di livello laurea specialistica (PhD) in **biologia, chimica, fisica**.
- "Google-proof": non risolvibili con una semplice ricerca web; richiedono ragionamento scientifico profondo.
- Baseline umane: non-esperti con web illimitato ~**34%**, esperti PhD ~**65–70%**.
- Usato per misurare il *scientific reasoning* dei modelli avanzati.

## Perché conta (per la newsletter)
L'Indice premia l'**agenticità** (34%) e il lavoro economico reale (GDPval), non i test a crocette saturi. È il terreno su cui i modelli open-weight cinesi (GLM, Kimi, DeepSeek) stanno accorciando il gap coi top-tier a frazione del costo — il filo dei post "modelli che scalano la classifica a poco prezzo".

## Fonti
- [Artificial Analysis — Intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis — Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis — GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis — GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond)
- Nota sorgente interna (forward Telegram del 2026-08-21): [Benchmark open-weight 2026-08-21](../sources/benchmark-open-weight-2026-08-21.md)
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index](../sources/benchmark-open-weight-2026-08-21.md)

### Referenced By

- [Artificial Analysis](../entities/artificial-analysis.md)
- [CtxPort — portabilità del contesto tra AI](ctxport-portabilità-del-contesto-tra-ai.md)
- [DeepSeek](../entities/deepseek.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](due-classifiche-per-lo-stesso-benchmark.md)
- [Laude Institute](../entities/laude-institute.md)
- [LLM-as-a-Verifier — la verifica come asse di scaling](llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
- [Z.AI (Zhipu AI)](../entities/z-ai.md)
<!-- openclaw:wiki:related:end -->
