---
pageType: source
id: source.verifica-leaderboard-benchmark-2026-08-26
title: "Verifica sulle fonti primarie dei benchmark (26 agosto 2026)"
sourceType: primary-check
sourcePath: tbench.ai · frontierbench.ai · artificialanalysis.ai
ingestedAt: 2026-08-26T00:00:00Z
updatedAt: 2026-08-26T00:00:00Z
status: active
publish: true
---

# Verifica sulle fonti primarie dei benchmark (26 agosto 2026)

## Source
- Tipo: lettura diretta delle fonti primarie in browser, sessione del 2026-08-26
- Pagine lette:
  - `https://www.tbench.ai/leaderboard/terminal-bench/2.1` — leaderboard ufficiale Terminal-Bench v2.1
  - `https://www.frontierbench.ai/` — Terminal-Bench 3.0 (ex Frontier-Bench)
  - `https://artificialanalysis.ai/methodology/intelligence-benchmarking` — metodologia e pesi
  - `https://artificialanalysis.ai/leaderboards/models` — punteggi Intelligence Index
  - `https://artificialanalysis.ai/evaluations/terminalbench-v2-1` — TB v2.1 secondo AA
- Scopo: verificare i numeri registrati nel vault a partire dai forward del 21/08

## Content

### 1. Terminal-Bench v2.1 — leaderboard **ufficiale** (tbench.ai)

17 entry, valutazione eseguita e verificata da un membro del team Terminal-Bench.
La classifica accoppia esplicitamente **agente** e **modello**, con colonna *Effort*,
*Hacks* e *Cost*.

| # | Agente | Modello | Effort | Accuracy | Costo |
|---|---|---|---|---|---|
| 1 | Claude Code | Fable 5 | xhigh | **83,8% ± 1,2** | $552,67 |
| 2 | Codex | GPT-5.5 | xhigh | 83,1% ± 1,1 | $2.059,19 |
| 3 | Terminus 2 | Fable 5 | high | 80,4% ± 1,2 | $438,64 |
| 4 | Cursor CLI | Grok 4.5 | high | 79,3% ± 1,5 | $134,09 |
| 5 | Claude Code | Opus 4.8 | high | 78,9% ± 1,3 | $286,94 |
| 6 | Codex | GPT-5.6 Terra | max | 78,4% ± 1,3 | $421,15 |
| … | | | | | |
| 12 | Claude Code | Opus 4.7 | max | 68,9% ± 1,4 | $599,52 |
| 13 | Terminus 2 | Opus 4.7 | max | 66,1% ± 1,4 | $582,26 |
| 17 | Claude Code | GLM-5.1 | max | 58,7% ± 1,2 | $277,14 |

**Nessuna entry DeepSeek**, a nessun livello. Nessuna entry all'88%.

### 2. Terminal-Bench 3.0 (frontierbench.ai, ex Frontier-Bench)

Versione più dura, già live: il vertice sta al **42,7%**.

| # | Modello | Agente | Resolution rate | Data | Token | Costo |
|---|---|---|---|---|---|---|
| 1 | Opus 5 (max) | **mini-SWE-agent** | 42,7% ± 1,6 | 24 lug 2026 | 7,3B | $5,8k |
| 2 | GPT-5.6 Sol (max) | Codex | 34,6% ± 1,6 | 9 lug 2026 | 5,8B | $4,0k |
| 3 | Fable 5 (max) | Claude Code | 34,1% ± 1,7 | 9 giu 2026 | 3,6B | $6,5k |
| 4 | Grok 4.6 (high) | Grok Build | 26,5% ± 1,5 | 12 ago 2026 | 2,9B | $2,1k |
| 10 | GLM 5.2 (max) | Claude Code | 4,6% ± 1,0 | 13 giu 2026 | 3,3B | $3,4k |

### 3. Terminal-Bench v2.1 secondo **Artificial Analysis** — numeri diversi

AA esegue una propria implementazione dello stesso benchmark. Vertice dichiarato
sulla pagina:

> GPT-5.6 Sol (xhigh) scores the highest on Terminal-Bench v2.1 with a score of
> **89,5%**, followed by Claude Opus 5 (Adaptive Reasoning, Max Effort) with a score
> of **89,1%**, and Grok 4.6 (high) with a score of **88,4%**.

Stesso nome di benchmark, stessa versione, **~6 punti di differenza al vertice** e un
vincitore diverso rispetto alla leaderboard ufficiale.

### 4. Artificial Analysis Intelligence Index v4.1.1 — pesi verificati

Dalla pagina di metodologia, verbatim:

> Intelligence Index is calculated as a weighted average across four categories:
> **Agents (34%), Coding (24%), Scientific Reasoning (24%) and General (18%)**.
> The weighting emphasizes agentic tasks.

Tabella dei pesi per singola eval:

| Categoria | Eval | Domande | Repeats | Peso | Tool use |
|---|---|---|---|---|---|
| Agents (34%) | GDPval-AA v2 | 220 task | 1 | **20%** | ✓ |
| | 𝜏³-Banking | 97 | 5 | 14% | ✓ |
| Coding (24%) | Terminal-Bench v2.1 | 89 | 3 | 16% | ✗ |
| | SciCode | 288 sub-problemi | 3 | 8% | ✗ |
| General (18%) | AA-LCR | 100 | 3 | 6% | ✗ |
| | AA-Omniscience | 6.000 | 1 | 12% (accuracy 8% + 1−hallucination 4%) | ✗ |
| Scientific Reasoning (24%) | HLE | 2.158 | 1 | 12% | ✗ |
| | GPQA Diamond | 198 | 5 | 6% | ✗ |
| | CritPt | 70 | 5 | 6% | ✗ |

**Contraddizione sulla fonte stessa.** La FAQ della pagina dell'indice dice invece:
"Four categories **each contribute 25%**: agents, coding, general capability, and
scientific reasoning." Metodologia e FAQ non concordano. La tabella dei pesi per eval
somma correttamente a 34/24/24/18, quindi la FAQ è la pagina sbagliata.

### 5. Intelligence Index — punteggi e costo per task

| Modello | Org | Score | Costo/task |
|---|---|---|---|
| Claude Opus 5 (max) | Anthropic | **63** | $2,34 |
| Claude Opus 5 (xhigh) | Anthropic | 63 | $1,80 |
| Claude Fable 5 (with fallback) | Anthropic | 62 | $3,14 |
| Claude Opus 5 (high) | Anthropic | 61 | $1,23 |
| GPT-5.6 Sol (max) | OpenAI | **61** | $0,96 |
| Kimi K3 (max) | Kimi | **60** | $0,84 |
| GLM-5.3 (max) | Z AI | **60** | $0,68 |
| GLM-5.3-Flash | Z AI | 57 | **$0,09** |
| DeepSeek V4 Pro 0813 (max) | DeepSeek | 53 | $0,27 |
| DeepSeek V4 Flash 0731 (max) | DeepSeek | 52 | $0,11 |
| DeepSeek V4 Pro (max) | DeepSeek | 45 | $0,05 |

## Notes
<!-- openclaw:human:start -->
Pagina di evidenza della sessione di ricerca del 26/08. Serve a rendere verificabili
le correzioni applicate in quella passata: senza questi numeri, le smentite sarebbero
affermazioni senza appoggio come quelle che smentiscono.
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [DeepSeek](../entities/deepseek.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
- [LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md)
- [Z.AI (Zhipu AI)](../entities/z-ai.md)
<!-- openclaw:wiki:related:end -->
