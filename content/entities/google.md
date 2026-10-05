---
title: "Google"
id: google
pageType: entity
entityType: organization
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
  - sources/google-code-wiki-interactive-repo-documentation-nov-2025.md
  - sources/google-gemini-4-argon-announcement-2026-09-30.md
updatedAt: 2026-10-03T08:32:00Z
publish: true
---

# Google

**Type:** organization  
**Rilevanza per questo vault:** produce NotebookLM, il caso di studio più
citato del topic llm-memory, la famiglia Gemini che ne è il backbone, e Code Wiki
— l'implementazione industriale del pattern che questo vault stesso applica

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

**Aggiornamento 2026-09-30**: nuova frontier model **Gemini 4 Argon** — 1M output
token, rollout a fasi (prima trusted cyber defenders, poi API/Google AI Ultra),
SOTA dichiarati su DeepSWE v1.1 e Vals Index. Scheda:
[Gemini 4 Argon — il ritorno frontier di Google](../syntheses/gemini-4-argon-il-ritorno-frontier-di-google-rollout-a-fasi-1m-output-token.md).

### Context Caching (API)

Feature che conserva in RAM GPU embedding delle fonti e istruzioni di sistema
pre-processati, così le query successive sullo stesso notebook saltano la
ricomputazione: latenza −90%, costo inferiore.

### Code Wiki

Piattaforma annunciata il 13 novembre 2025 (public preview su `codewiki.google`)
che mantiene per ogni repository un wiki strutturato **rigenerato a ogni
cambiamento del codice**, e lo usa come base di conoscenza per una chat Gemini
iperlinkata ai file. Genera anche diagrammi di architettura, classi e sequenza
sempre allineati al codice. Annunciata un'estensione Gemini CLI per farlo girare
in locale sui repo privati.

**Analisi completa:**
[Google Code Wiki — la documentazione come wiki ricompilata](../syntheses/google-code-wiki-documentazione-viva-dei-repository.md)

> È lo stesso pattern di sintesi-a-write-time che questo vault attribuisce a
> [Karpathy](karpathy-andrej.md) e data ad aprile 2026 — spedito come prodotto
> cinque mesi prima. La sintesi registra la divergenza senza risolverla.

## Analisi tecnica

L'architettura ibrida di NotebookLM — fase di ingest, retrieval agentico,
generazione vincolata — è smontata nel topic wiki, non qui:

- [notebooklm](../concepts/notebooklm.md) — la scheda del prodotto come concetto
- [notebooklm-hybrid-stack](../topics/notebooklm-hybrid-stack.md) — le tecniche che compongono invece di competere

**Sources:**
- [LLM Memory & Context Evolution — Deep Research](../sources/llm-memory-context-evolution-2026.md)
- [Google Code Wiki — Interactive repo documentation](../sources/google-code-wiki-interactive-repo-documentation-nov-2025.md)
- [Google — Annuncio Gemini 4 Argon](../sources/google-gemini-4-argon-announcement-2026-09-30.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [Google Code Wiki — la documentazione come wiki ricompilata](../syntheses/google-code-wiki-documentazione-viva-dei-repository.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)

### Related Pages

- [Anthropic](anthropic.md)
- [Karpathy, Andrej](karpathy-andrej.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->
