---
pageType: source
id: source.llm-as-a-verifier-arxiv-2607-05391
title: "LLM-as-a-Verifier: A General-Purpose Verification Framework (arXiv 2607.05391)"
sourceType: url
sourcePath: https://arxiv.org/abs/2607.05391
ingestedAt: 2026-08-26T00:00:00Z
updatedAt: 2026-08-26T00:00:00Z
status: active
publish: true
---

# LLM-as-a-Verifier: A General-Purpose Verification Framework (arXiv 2607.05391)

## Source
- Type: `url` — https://arxiv.org/abs/2607.05391
- Autori: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini
- Gruppo: Scaling Intelligence Lab, Stanford University
- Submission history: v1 lunedì 6 luglio 2026 17:59 UTC · v2 martedì 7 luglio 2026 17:26 UTC
- Letta sulla pagina abs e sull'HTML v2 il 2026-08-26

## Content

### Abstract (verbatim, estratti)

> Scaling pre-training, post-training, and test-time compute have become the central
> paradigms for improving the capabilities of LLMs. In this work, we identify
> **verification**, the ability to determine the correctness of a solution, as a new
> scaling axis. To unlock this and demonstrate its effectiveness, we introduce
> LLM-as-a-Verifier, a general-purpose verification framework that provides
> fine-grained feedback for agentic tasks **without requiring additional training**.
> Unlike standard LM judges that prompt LLMs to produce discrete scores for candidate
> solutions, LLM-as-a-Verifier **computes the expectation over the distribution of
> scoring token logits to generate continuous scores**.

> This probabilistic formulation enables verification to scale along multiple
> dimensions: (1) score granularity, (2) repeated evaluation, and (3) criteria
> decomposition. In particular, we show that scaling the scoring granularity leads to
> better separation between positive and negative solutions, resulting in more
> calibrated comparisons. Moreover, scaling repeated evaluation and criteria
> decomposition consistently lead to additional gains in verification accuracy through
> variance and complexity reduction. We further introduce a **cost-efficient ranking
> algorithm** for selecting the best solution among candidates using the verifier's
> continuous scores.

### Risultati dichiarati nel paper

| Benchmark | Risultato |
|---|---|
| Terminal-Bench **V2** | **86,5%** |
| SWE-Bench Verified | 78,2% |
| RoboRewardBench | 87,4% (Trajectory Preference Accuracy) |
| MedAgentBench | 73,3% |

Il paper dichiara inoltre estensioni per Claude Code e Codex che usano i segnali
fine-grained del verificatore come **proxy di avanzamento del task**.

### Cosa NON c'è nel paper

Il testo di v2 (7 luglio 2026) **non contiene** il risultato "DeepSeek V4 Flash
79% → 88% su Terminal-Bench 2.1" che circola nelle segnalazioni. L'unica occorrenza
di "DeepSeek" nel documento è la citazione bibliografica di DeepSeek-R1. Quel numero
proviene da un post successivo di un autore (Jacky Kwok, @jackyk02, su X, metà agosto
2026), ripreso da Marco Pavone su LinkedIn e da vari canali di aggregazione: dice che
campionando **5 soluzioni** con DeepSeek V4 Flash e riordinandole con lo stesso
modello via LLM-as-a-Verifier si passa dal 79% all'88%.

Distinzione da tenere: 86,5% su Terminal-Bench V2 è una cifra del paper; 88% su
Terminal-Bench 2.1 con V4 Flash è una cifra da social, non ancora in un paper.

## Notes
<!-- openclaw:human:start -->
Ingerita nella sessione di ricerca del 2026-08-26, aperta per chiudere
[q-verifier-uplift-vs-index-scores](../questions/q-verifier-uplift-vs-index-scores.md).
Il `k=5` che la domanda chiedeva è qui: viene dal post degli autori, non dal paper.
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
<!-- openclaw:wiki:related:end -->
