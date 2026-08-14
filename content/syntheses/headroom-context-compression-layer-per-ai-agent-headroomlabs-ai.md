---
pageType: synthesis
id: synthesis.headroom-context-compression-layer-per-ai-agent-headroomlabs-ai
title: Headroom — Context compression layer per AI agent (headroomlabs-ai)
sourceIds:
  - source.headroom-2026-08-04
  - https://github.com/headroomlabs-ai/headroom
status: active
updatedAt: 2026-08-14T14:42:31.360Z
publish: true
---

# Headroom — Context compression layer per AI agent (headroomlabs-ai)

## Notes
<!-- openclaw:human:start -->
### Collegamenti
- Prodotto da [Headroom Labs](../entities/headroom-labs.md)
- Terza leva sul costo del contesto, accanto a [context caching](../concepts/context-caching.md) (riusa il prefisso) e ai [modelli long-context](../concepts/long-context-models.md) (allargano la finestra). Headroom riduce ciò che entra
- I suoi numeri sono in unità ancora diverse dalle quattro già confrontate in [memory-economics](../topics/memory-economics.md)
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Headroom — Il layer di compressione del contesto per AI agent

**Repo:** https://github.com/headroomlabs-ai/headroom
**Docs:** https://docs.headroomlabs.ai/docs
**Linguaggio:** Rust · **License:** Apache-2.0 · **Stars:** 66,3k (verificato sul repo il 2026-08-14)

## Cos'è

Tool open-source (originariamente `chopratejas/headroom`) che **comprime tutto ciò che l'AI agent legge** — output di tool, log, RAG chunks, file e cronologia conversazione — *prima* che arrivi al LLM. Stesse risposte, frazione dei token.

**Risparmi dichiarati:**
- **15–20% di token in meno** per coding agent
- **60–95% di token in meno** su dati JSON

Esempi reali (tabella "Proof" del repo): code search 92%, SRE debugging 92%, GitHub issue triage 73%, codebase exploration 47%. L'accuratezza è preservata (GSM8K ±0.000, SQuAD v2 97%, BFCL 97%).

## Modalità di deployment

- **Libreria** — `compress(messages)` in Python o TypeScript, inline in qualunque app
- **Proxy** — `headroom proxy --port 8787`, zero modifiche al codice, qualunque linguaggio
- **Agent wrap** — `headroom wrap claude|codex|grok|copilot|cursor|...|openclaw` (un comando; undo con `headroom unwrap`). **Supporta anche OpenClaw**
- **MCP server** — tool `headroom_compress`, `headroom_retrieve`, `headroom_stats` per qualunque client MCP

## Architettura

`CacheAligner → ContentRouter → CCR`
- **ContentRouter** rileva il tipo di contenuto e seleziona il compressore giusto
- **SmartCrusher** (JSON), **CodeCompressor** (AST), **Kompress-v2-base** (testo, modello HF)
- **CacheAligner** rileva contenuti volatili che possono invalidare i prefissi KV-cache del provider (non riscrive i prompt)
- **CCR** (reversible): gli originali restano in cache locale; l'LLM chiama `headroom_retrieve` se serve un frammento

## Funzionalità chiave

- **Cross-agent memory** — store condiviso tra Claude, Codex, Gemini, Grok, auto-dedup
- **`headroom learn`** — mina le sessioni fallite e scrive correzioni in `CLAUDE.local.md` / `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` / `GROK.md`
- **Output token reduction** — taglia anche ciò che il modello *riscrive* (preamboli, codice ripetuto, thinking su passaggi routinari) via verbosity steering ed effort routing (Anthropic + OpenAI-compatible)
- **Reversible (CCR)** — nessun dato perso, retrieval on-demand

## Installazione

```bash
uv tool install --python 3.13 "headroom-ai[all]"   # CLI (global tool)
pip install "headroom-ai[all]"                      # Python, ships `headroom` CLI
npm install headroom-ai                             # solo TS SDK, no CLI
```
Richiede **Python 3.10+**. Extra opzionali: `[proxy] [mcp] [ml] [code] [memory] [vector] [relevance] [image] [agno] [langchain] [evals]`.

## Rilevanza

Strumento di **context compression** mature (Apache-2.0, molto attivo, ~66k stars). Utile per abbattere i costi token su pipeline lunghe (coding agent, RAG, tool-heavy workflows). Interessante per noi: **Headroom ha un wrapper ufficiale per OpenClaw** (`headroom wrap openclaw`), quindi è candidato diretto per ridurre il consumo token dei nostri agent.

## Provenienza

- Repo: https://github.com/headroomlabs-ai/headroom
- Segnalato il 2026-08-04, con video dimostrativo che avvolge la CLI di Claude Code e mostra dashboard real-time di compression savings / token saved / cache performance.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Headroom — segnalazione 2026-08-04](../sources/headroom-2026-08-04.md)

### Referenced By

- [Headroom Labs](../entities/headroom-labs.md)
<!-- openclaw:wiki:related:end -->
