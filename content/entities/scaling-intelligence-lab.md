---
title: "Scaling Intelligence Lab (Stanford)"
id: scaling-intelligence-lab
pageType: entity
entityType: organization
sourceIds:
  - sources/llm-as-a-verifier-arxiv-2607-05391.md
updatedAt: 2026-08-26T00:00:00Z
publish: true
---

# Scaling Intelligence Lab (Stanford)

**Type:** organization — gruppo di ricerca della Stanford University
(`scalingintelligence.stanford.edu`)
**Rilevanza per questo vault:** ha proposto la **verifica come quarto asse di scaling**,
accanto a pre-training, post-training e compute a test-time.

## Ricerca

### LLM-as-a-Verifier (luglio 2026)

Framework di verifica general-purpose che non richiede training aggiuntivo: invece di
chiedere a un LM-judge un punteggio discreto, calcola l'aspettazione sulla distribuzione
dei logit dei token di scoring, ottenendo punteggi **continui** — e quindi scalabili su
granularità, ripetizione e decomposizione dei criteri.

Firme: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, **Chelsea Finn**,
**Marco Pavone**, **Ion Stoica**, **Azalia Mirhoseini**.

**Analisi completa:**
[LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)

## Perché ci interessa

È il gruppo che ha reso misurabile l'intuizione che attraversa mezzo vault: se un
modello economico può comprare qualità spendendo inferenza a valle, allora il confine
fra "modello forte" e "modello guidato bene" non è dove le classifiche lo mettono.
Stesso movimento, da un'altra direzione, di [Unsloth](unsloth.md) sulla quantizzazione e
di [Prime Intellect](prime-intellect.md) sul self-improvement.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [LLM-as-a-Verifier: A General-Purpose Verification Framework (arXiv 2607.05391)](../sources/llm-as-a-verifier-arxiv-2607-05391.md)
