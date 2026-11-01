---
id: source.anteloc-ldraw-nova-github
pageType: source
title: "LDraw Nova – agenti che progettano set LEGO (GitHub)"
updatedAt: 2026-10-07T09:19:00Z
publish: true
---

# LDraw Nova

**Date:** ottobre 2026 (repo letto il 2026-10-07, v0.6.0)
**Source URL:** https://github.com/anteloc/ldraw-nova
**Author:** anteloc
**Type:** Web app + agent tooling (Docker)
**Introduced via:** richiesta PK (post video Telegram)

## Cos'è

Toolkit che dà a un agente AI il compito di **progettare modelli LEGO costruibili** scrivendo in LDraw (linguaggio "assembly" per CAD di mattoncini). Si dà un'idea, si guida l'agente, si ottiene:

- sorgente LDraw + viewer 3D / player / **VR interattivo (Meta Quest 3)**
- file **glTF `.glb` editabile in Blender** (metainfo come Custom Properties)
- chat history e thinking process dell'agente

## Architettura

- Costruito con **Astra e Opus 5.5**
- La ricerca semantica dei pezzi passa da **jev-rerank** (stesso autore), reranking con **Jev System One** di TypeSafe: senza `TYPESAFE_API_KEY` si degrada a FTS, con modelli peggiori
- Richiede due repo sibling alla stessa tag (`ldraw-nova` + `ldraw-nova-docker`), build Docker ~5 GB di disco

## Note

- Il claim "migliaia di dettagli combinati come un ingegnere LEGO" va ridimensionato: l'autore stesso dice che i modelli generati **non sono mai risultati pienamente corretti** — serve revisione umana
- Nessun login: esporlo solo su rete fidata
- L'angolo interessante è il pattern: usare un DSL geometrico esistente (LDraw) come "linguaggio di programmazione" per agenti che progettano oggetti fisici

## Collegamenti (audit 2026-10-22)

- Stesso batch (post video Telegram, 2026-10-07): [[sources/morluto-rea-github|REA]] · [[sources/dozentwelve-papermorph-github|Papermorph]]

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Papermorph – PDF in web-book interattivo (GitHub)](dozentwelve-papermorph-github.md)
- [REA – Reverse Engineer Anything (GitHub)](morluto-rea-github.md)
<!-- openclaw:wiki:related:end -->
