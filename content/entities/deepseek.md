---
title: "DeepSeek"
id: deepseek
pageType: entity
entityType: organization
sourceIds:
  - sources/deepseek-harness-github.md
  - sources/benchmark-open-weight-2026-08-21.md
updatedAt: 2026-10-04T04:00:00Z
publish: true
---

# DeepSeek

**Type:** organization — AI lab cinese, org GitHub `deepseek-ai`
**Rilevanza per questo vault:** è l'unica azienda qui dentro che compare in tre
ruoli insieme — fornitore dei modelli che girano in produzione su questo host,
autore di un harness per agenti concorrente a OpenClaw, e soggetto dei benchmark
sull'efficienza. Le tre cose si tengono: sono la stessa scommessa sul costo per
task.

## Prodotti

### DeepSeek Harness (dsh)

Harness per agenti rilasciato in developer preview il 2026-08-13, MIT, principio
"everything is a plugin": modelli, tool, skill, sessioni, sandbox, storage, loop,
scheduling e UI sono componenti intercambiabili (architettura interna *Cordis*).
Al 17/08: 146.796 stelle in quattro giorni, 14.979 fork, 6.576 repo sotto il topic
`dsh-plugin`.

**Analisi completa:**
[DeepSeek Harness — Agent Harness "Everything is a Plugin"](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md)

### Famiglia V4

Due varianti in uso corrente, **Flash** e **Pro**: la prima come modello di base
per agenti di supporto, la seconda per i passaggi di ragionamento.

> **Aggiornamento 2026-10-04 (seconda mano, da verificare alla fonte API):**
> **V4.1 Flash** rilasciato il 10 settembre (MIT su HuggingFace, come V4 Flash e V4
> Pro); V4 Flash e V4 Flash Vision Exp ritirati dall'API e instradati sul nuovo
> modello. Annuncio controintuitivo: DeepSeek ha dichiarato V4.1 Flash superiore a
> V4 Pro su tutte le metriche chiave e ha provato a instradare il traffico Pro su
> Flash (14/9) — **marcia indietro prima dell'effetto** "in response to user
> demand": V4 Pro resta attivo con billing invariato. V4.1 Pro annunciato "in
> futuro", senza data. Fonti: changelog API citato da news.ycombinator.com e
> yottalabs.ai. Il doppio movimento è il caso di studio che la pagina harness
> documenta dal lato provider: un modello nuovo che *sostituisce* il fratello
> maggiore a prezzo inferiore è l'efficienza che mangia il premium, con
> l'inerzia dei clienti come freno.

Posizione verificata il 26/08 sull'Artificial Analysis Intelligence Index:
**V4 Pro 0813 (max) = 53** a $0,27/task, **V4 Flash 0731 (max) = 52** a $0,11/task —
lontani dal vertice (Claude Opus 5 max = 63 a $2,34). La lettura corretta non è "in
top-3 di intelligenza", è **metà del prezzo di un punto**: 52 punti a un ventesimo del
costo per task del vertice.

> Gli snapshot "V4-Flash-0731 = 82,7 e V4-Pro-0813 = 87,9 su TB2.1", registrati qui
> come verificati, **non sono stati riprodotti**: la leaderboard ufficiale di
> Terminal-Bench v2.1 ha 17 entry e nessuna DeepSeek. Da trattare come non sourced —
> vedi [Verifica sulle fonti primarie](../sources/verifica-leaderboard-benchmark-2026-08-26.md).

Il post del 21/08 attribuisce a V4 Flash un salto 79% → 88% su Terminal-Bench 2.1
applicando **LLM-as-a-Verifier**. Verificato alla fonte il 26/08: la tecnica esiste ed
è seria ([arXiv 2607.05391](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)),
ma quel numero **non è nel paper** — è un post su X di un autore, con **k = 5**
candidate campionate e riordinate. Il paper dichiara 86,5% su Terminal-Bench V2.
Il "~11× più economico" confronta il prezzo di *una* generazione contro il costo di
*cinque più la verifica*. Vedi
[q-verifier-uplift-vs-index-scores](../questions/q-verifier-uplift-vs-index-scores.md).

## Perché ci interessa

DeepSeek è il caso di prova della tesi "l'efficienza sta mangiando il premium"
che attraversa
[Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md):
non un modello che vince un benchmark, ma un modello economico che ci arriva
**spendendo inferenza al posto di training**. È lo stesso movimento che
[Unsloth](unsloth.md) fa sulla quantizzazione e che
[Prime Intellect](prime-intellect.md) fa sul self-improvement: comprare qualità
con calcolo a valle invece che con parametri a monte.

**Sources:**
- [DeepSeek Harness (GitHub)](../sources/deepseek-harness-github.md)
- [Benchmark open-weight 2026-08-21](../sources/benchmark-open-weight-2026-08-21.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](artificial-analysis.md)
- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index](../sources/benchmark-open-weight-2026-08-21.md)
- [CtxPort — portabilità del contesto tra AI](../syntheses/ctxport-portabilità-del-contesto-tra-ai.md)
- [DeepSeek Harness — Agent Harness "Everything is a Plugin"](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
- [LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
- [Z.AI (Zhipu AI)](z-ai.md)

### Related Pages

- [OpenAI](openai.md)
<!-- openclaw:wiki:related:end -->
