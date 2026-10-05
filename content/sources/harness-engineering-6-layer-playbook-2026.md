---
id: source.harness-engineering-6-layer-playbook-2026
pageType: source
title: "Harness Engineering — Agent = Model + Harness: The 6-Layer Production Playbook"
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/archive/harness-engineering-6-layer-playbook-2026.pdf
ingestedAt: 2026-09-01T13:23:00Z
updatedAt: 2026-09-01T13:23:00Z
status: active
publish: true
date: 2026-09-01
tags: [harness-engineering, ai-agents, agentic-loop, sensors, guides, permissions, observability, production]
---

# Harness Engineering — Agent = Model + Harness: The 6-Layer Production Playbook

**Date:** 2026-08 (indipendente, non affiliato a Google/OpenAI/Anthropic/HashiCorp)
**Tipo:** Sintesi pratica / playbook di engineering
**PDF archiviato:** `../../workspace/archive/harness-engineering-6-layer-playbook-2026.pdf` (originale: `harness_final.pdf`)
**Introduced via:** PK (invio file su Telegram)

## Tesi centrale

> **Agent = Model + Harness.**

Il modello fornisce il ragionamento. L'*harness* fornisce tutto il resto: guide che prevengono fallimenti noti, sensori che ne catturano di nuovi, un agentic loop con retry limitati, memoria persistente, permessi forzati e osservabilità completa.

Il gap che uccide il 95% degli agent enterprise prima della produzione non è il modello: è l'harness. La disciplina del 2026 (dopo Prompt Engineering 2023-24 e Context Engineering 2025) è l'**harness engineering** — progettare l'ambiente in cui l'agente opera, non solo ciò che vede o dice.

## La prova che l'harness batte il modello

Tenendo fisso il modello e cambiando solo l'harness:

| Fonte | Modello | Benchmark | Prima → Dopo | Delta |
|---|---|---|---|---|
| Masood (GAIA) | Claude Sonnet 4.5 | GAIA | 30.91% → 74.55% | **+43.64 pt** |
| LangChain | stesso modello | Terminal Bench | 30° → 5° | **+25 rank** |
| Hashline | 16 LLM | coding bench | baseline → migliorato | harness only |
| OpenAI (Codex) | Codex agents | produzione | 0 → 1M righe di codice | **zero manuale** |

Uno swing di 44 punti sullo *stesso* modello è più grande della differenza tra molte generazioni di modelli adiacenti.

## Le 6 layer dell'harness

```
GUIDES ──> AGENTIC LOOP ──> SENSORS     (steering loop: feedforward + feedback)
   │            │               │
   v            v               v
MEMORY     PERMISSIONS     OBSERVABILITY  (runtime foundation)
```

1. **Guides (feedforward)** — `AGENTS.md` / `CLAUDE.md` / `.cursorrules`. Ogni riga = un fallimento passato convertito in prevenzione permanente. Regole devono essere verificabili, datate, tracciate a un fallimento osservato.
2. **Sensors (feedback)** — linter, test, validatori (deterministici, veloci, gratuiti) primi; LLM-as-judge (lenti, costosi, non deterministici) solo per check semantici non codificabili. Pattern self-verification: l'agente esegue sensori esterni e agisce sui risultati.
3. **Agentic Loop** — piano → esegui → verifica → aggiusta, con bound: max 3 retry/step, 30 min wall-clock, 100K token, $5/task, 50 tool call. Escalation ≠ fallimento.
4. **Memory & State** — il modello dimentica ogni sessione; l'harness ricorda via filesystem (`plan.md`, `decisions.jsonl`, checkpoint). Compaction server-side per run lunghe. Promuovi preferenze stabili da memory a guide.
5. **Permissions & Budgets** — il modello non si limita da solo; la sicurezza è proprietà dell'harness. Capability budget (scope, rate, reversibility, visibility) + least privilege. Separa input trusted (guide) da untrusted (contenuto esterno) contro la prompt injection.
6. **Observability** — log strutturati, trip wires (costo > 2x media, stesso errore ×3, sensor pass-rate cala), health scorecard. Metrica reale: task completati senza intervento umano + evidenza accettabile.

## Il principio ratchet (Hashimoto)

Ogni fallimento migliora permanentemente il sistema, in una direzione sola:

1. L'agente sbaglia → 2. identifica la *classe* di fallimento → 3. scegli il layer più forte (guida / sensore / permesso / ambiente) → 4. codifica la fix → 5. verifica che prevenga la ricorrenza → 6. monitora regressioni.

Una patch di prompt aggiusta una conversazione. Una regola di guida aggiusta ogni run futura. Un vincolo d'ambiente rende l'errore *strutturalmente impossibile*.

**La regola di Lauren Tan (Cursor):** quando un revisore umano scrive lo stesso commento ≥3 volte, quel commento diventa un vincolo strutturale (guida → sensore che blocca l'output).

## Ladder di affidabilità dei controlli

| Layer | Esempio | Affidabilità | Costo |
|---|---|---|---|
| Memory | correzione in chat | Bassa | Zero |
| Prompt | istruzione di task | Bassa-Media | Minuti |
| Guide | regola AGENTS.md | Media | Minuti |
| Sensor | test automatizzato | Alta | Ore |
| Environment | permesso/schema/CI | Massima | Ore-Giorni |

## Build path: 7 giorni alla produzione

| Giorno | Build | Exit test |
|---|---|---|
| 1 | `AGENTS.md` con build/test/lint | l'agente esegue tutti e 3 |
| 2 | +3 regole da fallimenti | evita 3 anti-pattern |
| 3 | primo sensore computazionale | esegue test dopo ogni cambio |
| 4 | agentic loop + retry budget | retry poi escalation |
| 5 | checkpoint su filesystem | riprende dopo restart |
| 6 | permessi + budget di costo | non supera lo scope |
| 7 | logging strutturato + trip wire | il trip wire scatta su spike simulato |

**Scale gate** (espandi solo se tutti passano): completion ≥80% senza correzione manuale, nessun task oltre il budget, almeno 1 escalation corretta, checkpoint sopravvissuto a 1 restart, trip wire scattato su ≥1 anomalia simulata, permesso che ha bloccato ≥1 azione.

## Quando NON costruire un harness

Non giustifica l'overhead per: domande one-off, brainstorming creativo, conversazioni esplorative, task singoli. Il test: noteresti se l'agente producesse silenziosamente un risultato sbagliato? (→ serve sensore) Dovresti spiegare di nuovo lo stesso contesto? (→ serve memoria) Un errore avrebbe conseguenze esterne? (→ servono permessi).

## Relazione con il nostro harness (Claudia / OpenClaw)

Il playbook descrive esattamente ciò che già operiamo:

- **Guides** → la nostra `AGENTS.md` applica il ratchet (regole datate, pattern manifest, divieto di eseguire io stesso il lavoro dei subagenti).
- **Sensors** → cron watchdog (`check_flower_errors.py`, flower_seen_tasks.json) che notificano solo su nuovi errori.
- **Memory** → `memory/YYYY-MM-DD.md`, `MEMORY.md`, checkpoint su filesystem; recovery test implicito.
- **Permissions** → native approval gates, `DENY` su azioni distruttive, separazione input trusted/untrusted (contenuto esterno trattato come untrusted).
- **Observability** → log, trip wires su costo/errore, health scorecard.
- **Agentic loop** → delegazione a subagenti (MiMo) con retry/escalation, mai poll loop nel main thread.

Punti deboli da auditare (da verificare): trip wire esplicito su costo >2x media, sensor coverage test su ogni output critico, escalation packet strutturato, capability budget scritto per azione.

## Note di provenienza

Documento è una sintesi *indipendente* di materiale pubblico (Hashimoto, field report OpenAI Codex, Martin Fowler/Böckeler guides-and-sensors, Anthropic, LangChain, Cursor). Non ufficiale, diagrammi originali. Le raccomandazioni/template/pseudocode sono adattamento dell'autore, non specifiche ufficiali.

## Notes
<!-- openclaw:human:start -->
### Nel vault
- [DeepSeek Harness — "Everything is a Plugin"](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md) — stessa classe: l'harness come mole
- [LLM-as-a-Verifier — la verifica come asse di scaling](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md) — i sensori inferenziali come leva di scaling
- [Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md) — perché il punteggio non è del modello ma dell'harness
- [JCode — agente di coding super veloce](../syntheses/jcode-agente-di-coding-super-veloce.md) — agent di coding che vive di harness stretto
- [Prime Agent — self-improving RLM agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md) — self-improvement via ratchet
- [Webwright — browser agent Microsoft](../syntheses/webwright-microsoft-browser-agent.md) — agent autonomo come caso d'uso harness
- [Deep Agents from Scratch — LangChain course](deep-agents-from-scratch.md) — i pattern del loop (planning, offload, sub-agent) costruiti da zero; LangChain è una delle fonti della tabella di evidenza qui sopra
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [bb — The agent IDE that builds itself (GitHub get-bb/bb)](bb-agent-ide-github.md)
- [BRIX-IA](../entities/brix-ia.md)
- [Deep Agents from Scratch — LangChain course](deep-agents-from-scratch.md)
<!-- openclaw:wiki:related:end -->
