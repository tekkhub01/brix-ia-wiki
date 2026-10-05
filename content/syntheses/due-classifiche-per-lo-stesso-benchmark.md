---
pageType: synthesis
id: synthesis.due-classifiche-per-lo-stesso-benchmark
title: Due classifiche per lo stesso benchmark — perché un punteggio non è del modello
sourceIds:
  - source.verifica-leaderboard-benchmark-2026-08-26
claims:
  - text: Terminal-Bench v2.1 ha due leaderboard pubbliche con vertici diversi — 83,8%
      (ufficiale, tbench.ai) e 89,5% (Artificial Analysis) — e vincitori diversi.
    confidence: 0.95
    evidence:
      - kind: url
        sourceId: source.verifica-leaderboard-benchmark-2026-08-26
        confidence: 0.95
        note: lettura diretta delle due pagine, 2026-08-26
  - text: Sulla leaderboard ufficiale lo stesso modello cambia punteggio a seconda
      dell'agente che lo guida (Fable 5 83,8% con Claude Code, 80,4% con Terminus 2).
    confidence: 0.95
    evidence:
      - kind: url
        sourceId: source.verifica-leaderboard-benchmark-2026-08-26
        confidence: 0.95
        note: leaderboard ufficiale TB v2.1, entry 1 e 3
confidence: 0.9
status: active
publish: true
updatedAt: 2026-08-26T00:00:00Z
---

# Due classifiche per lo stesso benchmark — perché un punteggio non è del modello

## Notes
<!-- openclaw:human:start -->
Emersa nella sessione di ricerca del 2026-08-26 mentre si verificava un numero
tutt'altro: si cercava se DeepSeek V4 Flash fosse davvero all'88% su Terminal-Bench
2.1, e si è scoperto che la domanda "qual è il punteggio su Terminal-Bench 2.1" non ha
una risposta sola.
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Il fatto

Terminal-Bench v2.1 — 89 task in terminale containerizzato, benchmark del **Laude
Institute** con Stanford e community — ha due classifiche pubbliche. Al 26 agosto 2026:

| | Leaderboard ufficiale (`tbench.ai`) | Artificial Analysis (`artificialanalysis.ai`) |
|---|---|---|
| Vertice | **83,8%** — Claude Code + Fable 5 (xhigh) | **89,5%** — GPT-5.6 Sol (xhigh) |
| Secondo | 83,1% — Codex + GPT-5.5 (xhigh) | 89,1% — Claude Opus 5 (max) |
| Terzo | 80,4% — Terminus 2 + Fable 5 (high) | 88,4% — Grok 4.6 (high) |
| Come si legge una riga | *agente + modello + effort* | *modello + effort* |

Stessa versione del benchmark, **~6 punti di scarto al vertice e un vincitore diverso**.
Nessuna delle due sbaglia: eseguono lo stesso set di task dentro harness diversi.

## Perché succede

La leaderboard ufficiale accetta submission via Harbor con un agente dichiarato, e
mette l'agente in colonna. Artificial Analysis esegue le proprie run con il proprio
scaffolding, e mette in colonna solo il modello. Il numero che ne esce non misura la
stessa cosa.

Che l'harness sia una variabile di primo ordine si legge **dentro** la sola leaderboard
ufficiale, senza confrontare le due:

| Modello | Con Claude Code | Con Terminus 2 | Δ |
|---|---|---|---|
| Fable 5 | 83,8% (xhigh) | 80,4% (high) | 3,4 punti |
| Opus 4.7 | 68,9% (max) | 66,1% (max) | 2,8 punti |

Stesso modello, stesso benchmark, stesso effort nel secondo caso: cambia solo chi lo
guida, e cambia il punteggio di quanto separa il primo dal quarto in classifica.

Su [Terminal-Bench 3.0](https://www.frontierbench.ai/) — la versione dura, dove il
vertice sta al 42,7% — l'effetto è ancora più netto: in testa c'è **Opus 5 con
mini-SWE-agent**, cioè l'harness *minimale* della ricerca accademica, davanti a
Fable 5 con Claude Code (34,1%). Il codice attorno al modello non è overhead: è parte
della capacità misurata.

## Cosa se ne fa questo vault

**1. Ogni confronto da leaderboard va qualificato.** Una riga come "il modello X fa Y%"
è incompleta senza *chi eseguiva* e *a quale effort*. Le pagine di questo vault che
citano benchmark — [Z.AI](../entities/z-ai.md), [DeepSeek](../entities/deepseek.md),
[Alibaba](../entities/alibaba.md), [Anthropic](../entities/anthropic.md) — ereditano
questa incompletezza dalle proprie fonti.

**2. L'Intelligence Index eredita il problema per costruzione.** Terminal-Bench v2.1
pesa il 16% dell'
[Artificial Analysis Intelligence Index](artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md),
e le due eval agentiche a maggior peso (GDPval-AA v2 al 20%, 𝜏³-Banking al 14%) girano
anch'esse dentro uno scaffolding di AA. Il 34% "Agents" dell'indice misura
modello + harness di Artificial Analysis. È una scelta legittima e dichiarata, ma
cambia cosa significa "questo modello è più intelligente".

**3. Il verificatore è la prova per assurdo.** Se un wrapper di
[verifica a inference-time](llm-as-a-verifier-la-verifica-come-asse-di-scaling.md) vale
nove punti senza toccare i pesi, allora l'harness non è una variabile di disturbo da
normalizzare via: è metà dell'oggetto misurato.

**4. C'è un cluster che aspetta di essere aperto.** Cinque fonti in questo vault
descrivono harness per agenti — [DSH](deepseek-harness-agent-harness-everything-is-a-plugin.md),
[JCode](jcode-agente-di-coding-super-veloce.md),
[Webwright](webwright-microsoft-browser-agent.md),
[Prime Agent](prime-agent-self-improving-rlm-agent-primeintellect-ai.md),
[Archon](../sources/archon-workflow-engine.md) — e nessuna pagina spiega cosa sia un
harness né perché conti. Questi numeri sono la ragione empirica per aprirlo.

## Riferimenti

- Leaderboard ufficiale: https://www.tbench.ai/leaderboard/terminal-bench/2.1
- Terminal-Bench 3.0 (ex Frontier-Bench): https://www.frontierbench.ai/
- Implementazione Artificial Analysis: https://artificialanalysis.ai/evaluations/terminalbench-v2-1
- Dati completi: [Verifica sulle fonti primarie dei benchmark](../sources/verifica-leaderboard-benchmark-2026-08-26.md)
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Verifica sulle fonti primarie dei benchmark (26 agosto 2026)](../sources/verifica-leaderboard-benchmark-2026-08-26.md)

### Referenced By

- [Artificial Analysis](../entities/artificial-analysis.md)
- [Claude Code Mods — plugin per personalizzare interfaccia e tool call (docs ufficiali)](../sources/claude-code-mods-docs-2026-10-05.md)
- [Harness Engineering — Agent = Model + Harness: The 6-Layer Production Playbook](../sources/harness-engineering-6-layer-playbook-2026.md)
- [Laude Institute](../entities/laude-institute.md)
- [LLM-as-a-Verifier — la verifica come asse di scaling](llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
<!-- openclaw:wiki:related:end -->
