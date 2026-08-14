---
title: BRIX-IA Wiki
publish: true
---

# BRIX-IA Wiki

Knowledge base della community BRIX-IA su LLM, agenti e infrastruttura AI.

Non è un blog e non è un archivio di link. È una wiki **compilata**: ogni
fonte che entra viene letta, sintetizzata e fusa nelle pagine che tocca,
seguendo il [[llm-wiki-karpathy|pattern LLM Wiki]] di Andrej Karpathy. Le
pagine non invecchiano in fondo a un feed — vengono aggiornate sul posto.

## Da dove partire

**Architetture di memoria e retrieval**
[[rag|RAG]] · [[agentic-rag|Agentic RAG]] · [[graphrag|GraphRAG]] ·
[[context-caching|Context caching]] · [[long-context-models|Modelli long-context]] ·
[[span-level-attribution|Attribuzione span-level]]

**Modelli e inferenza**
[[claude-anthropic|Claude]] · [[glm-5.1|GLM 5.1]] · [[openrouter|OpenRouter]] ·
[[quantization|Quantizzazione]] · [[rotorquant|RotorQuant]]

**Strumenti provati sul campo**
Ogni pagina in `syntheses/` è un tool che abbiamo installato e usato, non
una scheda prodotto: cosa fa, dove si rompe, se vale il tempo.

## Come è fatta

Tre layer, separati apposta:

| Layer | Chi lo scrive | Regola |
|---|---|---|
| Fonti | ingest umano | immutabili, mai riscritte |
| Wiki | agente LLM | pagine entità e sintesi, cross-linkate |
| Schema | umano | convenzioni e workflow |

Il layer delle fonti resta privato: qui pubblichiamo il **livello di
sintesi**, non le copie del materiale di partenza.

---

*Community BRIX-IA · [brix-ia.com](https://brix-ia.com)*
