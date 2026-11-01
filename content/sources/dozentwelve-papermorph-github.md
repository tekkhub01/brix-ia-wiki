---
id: source.dozentwelve-papermorph-github
pageType: source
title: "Papermorph – PDF in web-book interattivo (GitHub)"
updatedAt: 2026-10-07T09:19:00Z
publish: true
---

# Papermorph

**Date:** ottobre 2026 (repo letto il 2026-10-07)
**Source URL:** https://github.com/DozenTwelve/Papermorph
**Author:** DozenTwelve
**License:** MIT
**Type:** Skill per Claude Code
**Introduced via:** richiesta PK (post video Telegram)

## Cos'è

Skill che trasforma un PDF (libro/dispensa) in una **web-book animata e interattiva**: piano del libro → storyboard → narrazione → animazioni e quiz → sito. Pipeline dichiarata: `PDF -> Book plan -> Storyboards -> Narration -> Animation & quizzes -> Web book`.

## Uso

```
npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code
/papermorph Turn /path/to/book.pdf into an animated interactive web book.
```

Bookshelf demo live: https://papermorph.diamonddoge.org/

## Stato e limiti

- **Oggi funziona solo con Opus 5.5**; niente modelli immagine, multilingua o BGM
- Roadmap: image model + storyboard per picture book interattivi e documentari umanistici; espansione dello scaffale (STEM → picture book → scienze sociali)
- È una skill, non un prodotto: qualità dell'output legata al modello; per libri lunghi i costi di generazione sono significativi
- Attenzione al copyright: trasformare libri altrui in web-book è distribuzione di derivati

## Collegamenti (audit 2026-10-22)

- Stesso batch (post video Telegram, 2026-10-07): [[sources/morluto-rea-github|REA – Reverse Engineer Anything]] · [[sources/anteloc-ldraw-nova-github|LDraw Nova – agenti LEGO]]
- Strumento affine PDF→output: [[syntheses/pdf-inspector-firecrawl|pdf-inspector (Firecrawl)]]

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [LDraw Nova – agenti che progettano set LEGO (GitHub)](anteloc-ldraw-nova-github.md)
- [REA – Reverse Engineer Anything (GitHub)](morluto-rea-github.md)
<!-- openclaw:wiki:related:end -->
