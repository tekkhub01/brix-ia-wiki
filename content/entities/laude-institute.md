---
title: "Laude Institute"
id: laude-institute
pageType: entity
entityType: organization
sourceIds:
  - sources/verifica-leaderboard-benchmark-2026-08-26.md
updatedAt: 2026-08-26T00:00:00Z
publish: true
---

# Laude Institute

**Type:** organization — istituto di ricerca, sviluppa e mantiene Terminal-Bench
insieme a Stanford e alla community
**Rilevanza per questo vault:** possiede il benchmark che pesa il 16% dell'
[Artificial Analysis Intelligence Index](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
e che quasi tutte le affermazioni "questo modello è forte sugli agenti" citano, di
prima o seconda mano.

## Prodotti

### Terminal-Bench

Benchmark agentico su terminale containerizzato: l'agente riceve un task e ha una
shell. Le task coprono software engineering, sysadmin, data processing, training di
modelli e sicurezza. Submission via **Harbor**; la leaderboard mette in colonna
**agente, modello ed effort** separatamente, più costo in dollari e una colonna *Hacks*
per il reward hacking rilevato.

| Versione | Stato (26 ago 2026) | Vertice |
|---|---|---|
| v1.0 | legacy | — |
| v2.0 | live | — |
| **v2.1** | live — 89 task curati, refresh verificato di v2.0 | 83,8% — Claude Code + Fable 5 (xhigh) |
| **3.0** (ex Frontier-Bench, `frontierbench.ai`) | shipped | 42,7% — Opus 5 (max) + mini-SWE-agent |
| terminal-bench-science 1.0 | coming soon | — |

La v2.1 corregge 28 dei 89 task della v2.0 e introduce validazione continua, così che
i punteggi riflettano la capacità dell'agente e non i buchi dell'ambiente.

## Perché ci interessa

Il formato della leaderboard è di per sé un contributo: **separare agente da modello**
rende visibile una variabile che quasi tutte le altre classifiche nascondono. È
guardando quelle colonne che si vede lo stesso modello valere 3,4 punti in più o in
meno a seconda di chi lo guida —
[Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md).

Su Terminal-Bench 3.0 il vertice è tenuto da **mini-SWE-agent**, l'harness minimale di
provenienza accademica, davanti agli agenti commerciali: un dato che questo vault non
aveva e che cambia il modo di leggere il cluster degli harness.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](artificial-analysis.md)

### Related Pages

- [OpenAI](openai.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [Verifica sulle fonti primarie dei benchmark (26 agosto 2026)](../sources/verifica-leaderboard-benchmark-2026-08-26.md)
