---
title: "Google"
id: google
pageType: entity
entityType: organization
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-08-14T00:00:00Z
publish: true
---

# Google

**Type:** organization  
**Rilevanza per questo vault:** produce NotebookLM, il caso di studio più
citato del topic llm-memory, e la famiglia Gemini che ne è il backbone

## Prodotti

### NotebookLM

Prodotto di RAG agentico source-grounded, team Gemini. Lancio 2024 in preview
pubblica, iterato 2025–2026. Posizionamento: "il tuo assistente di ricerca
personale" — centrato sulle fonti, non sulla chat.

Tre elementi lo rendono interessante come sistema funzionante e non come demo:
unità di retrieval grandi (pagine, non frasi), context caching che azzera il
costo di re-embedding per query, e citazioni inline a livello di span.

### Gemini

Backbone di NotebookLM. Registrato come Gemini 1.5 Pro / Flash con finestra da
2M token.

> Backbone registrato ma **non ri-verificato**: la cifra risale al 2026-04-28 e
> la linea Gemini è nel frattempo avanzata. Trattare come storica.

### Context Caching (API)

Feature che conserva in RAM GPU embedding delle fonti e istruzioni di sistema
pre-processati, così le query successive sullo stesso notebook saltano la
ricomputazione: latenza −90%, costo inferiore.

## Analisi tecnica

L'architettura ibrida di NotebookLM — fase di ingest, retrieval agentico,
generazione vincolata — è smontata nel topic wiki, non qui:

- [notebooklm](../concepts/notebooklm.md) — la scheda del prodotto come concetto
- [notebooklm-hybrid-stack](../topics/notebooklm-hybrid-stack.md) — le tecniche che compongono invece di competere

**Sources:**
- [[llm-memory-context-evolution-2026|LLM Memory & Context Evolution — Deep Research]]

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Anthropic](anthropic.md)
- [Karpathy, Andrej](karpathy-andrej.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->
