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

## Temi

I quattro saggi trasversali. Se hai tempo per leggere una cosa sola,
parti da qui: mettono a confronto le architetture invece di descriverle
una per una.

- [[memory-economics|L'economia della memoria LLM]] — recupero,
  compilazione e caching, e quando ciascuno conviene
- [[structure-vs-iteration|Struttura contro iterazione]] — quando la
  conoscenza compilata ripaga il suo costo
- [[grounding-across-architectures|Grounding e modi di fallimento]] —
  come sbagliano le diverse architetture di memoria
- [[notebooklm-hybrid-stack|NotebookLM come caso di studio]] — lo stack
  ibrido nella pratica

## Concetti

[[rag|RAG]] · [[agentic-rag|Agentic RAG]] · [[graphrag|GraphRAG]] ·
[[llm-wiki-karpathy|LLM Wiki]] · [[context-caching|Context caching]] ·
[[long-context-models|Modelli long-context]] ·
[[span-level-attribution|Attribuzione span-level]] ·
[[quantization|Quantizzazione]] · [[notebooklm|NotebookLM]]

## Chi le costruisce

Aziende e persone, con i loro prodotti dentro la pagina di chi li rilascia —
Claude sta in Anthropic, GLM 5.1 in Z.AI, RotorQuant in scrya-com.

[[anthropic|Anthropic]] · [[google|Google]] · [[z-ai|Z.AI]] ·
[[openrouter|OpenRouter]] · [[firecrawl|Firecrawl]] ·
[[nous-research|Nous Research]] · [[prime-intellect|Prime Intellect]] ·
[[headroom-labs|Headroom Labs]] · [[scrya-com|scrya-com]] ·
[[karpathy-andrej|Andrej Karpathy]]

## Strumenti

Ogni pagina in `syntheses/` è un tool che abbiamo installato e usato, non
una scheda prodotto: cosa fa, dove si rompe, se vale il tempo.

## Domande aperte

Le cose che **non** sappiamo, tenute in evidenza invece che nascoste.
Ogni pagina in `questions/` è una domanda con il motivo per cui vale la
pena tracciarla. Se hai una risposta o un dato, è il posto migliore da
cui contribuire.

## Come è fatta

Tre layer, separati apposta:

| Layer | Chi lo scrive | Regola |
|---|---|---|
| Fonti | ingest umano | immutabili, mai riscritte |
| Wiki | agente LLM | concetti, temi e sintesi, cross-linkati |
| Schema | umano | convenzioni e workflow |

Le pagine in `sources/` sono note attribuite sul materiale di partenza,
non copie: il testo integrale sta al link originale citato in ciascuna.

---

*Community BRIX-IA · [brix-ia.com](https://brix-ia.com)*
