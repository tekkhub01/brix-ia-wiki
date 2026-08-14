---
pageType: synthesis
id: synthesis.impeccable-style-ai-design-tool
title: Impeccable.style - AI Design Tool
sourceIds:
  - web_fetch:https://impeccable.style/
status: active
updatedAt: 2026-05-19T14:32:30.657Z
publish: true
---

# Impeccable.style - AI Design Tool

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Impeccable.style

Tool CLI per design AI che offre un "upgrade mancante" per le capacità di design di Anthropic.

### Descrizione
Impeccable è uno strumento progettato per migliorare il flusso di lavoro del design AI, con particolare attenzione alla coerenza del brand, alla generazione di risorse e all'interazione con gli agenti AI.

### Funzionalità principali

#### Live Mode
- Iterazione diretta nel browser su elementi UI
- Preservazione dell'identità del brand per default
- Varianti in linea con il brand esistente
- Supporta Vite, Next.js, SvelteKit, Astro, Nuxt
- Rilevamento e patch CSP per app con Content-Security-Policy stretta
- Survive disconnects con session journal

#### Detector
- Rileva monocultura design (font overused)
- Controlli di contrasto su elementi stilizzati e bottoni
- Flag strutturali AI: eroi italic-serif display, hero eyebrow chips
- Body text viewport edge detection
- Risoluzione OKLCH e CSS-var

#### Critique e Polish
- Snapshot persistente per ogni target
- Score, P0/P1 counts e report completo
- Polish come superset di normalizzazione
- Triage cosmetico vs funzionale

#### Design System
- **PRODUCT.md**: memoria condivisa del design (audience, brand personality, anti-references)
- **DESIGN.md**: generazione spec-compliant in formato Google Stitch
- Registri brand vs product separati

#### Asset Generation
- **Codex asset producer agent**: produce risorse raster pulite da mock approvati
- Preserva silhouette, palette, illuminazione, materiale
- Rimuove UI text e chrome pre-renderizzati

### Comandi principali
- `/impeccable live` - Live mode per iterazione UI
- `/impeccable critique` - Analisi design con snapshot persistente
- `/impeccable polish` - Allineamento al design system
- `/impeccable teach` - Crea PRODUCT.md
- `/impeccable document` - Genera DESIGN.md spec-compliant
- `/impeccable shape` - Draft toolkilt brand come immagini reali
- `/impeccable craft` - Mock-to-code verso implementazione

### Informazioni
- **URL**: https://impeccable.style/
- **Data acquisizione**: 2026-05-19
- **Repository**: <https://github.com/pbakaus/impeccable>

### Note
Tool progettato per agenti AI come Codex e Claude Code. Supporta framework moderni (React/TSX, Vite, Next.js, SvelteKit, Astro, Nuxt).

## Collegamenti

### Entità correlate nella wiki
- **[[sources/anthropic-claude-design-labs]]** - Impeccable è un tool per design AI simile alle funzionalità di Claude Design
- **agenti fisici ai mercato 2026 deep research** - Impeccable opera nel domaine degli agenti AI per design
- **[[sources/llm-memory-context-evolution-2026]]** - LIVE mode di Impeccable utilizza pattern di caching e session journal
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [AI Website Cloner Template](../sources/ai-website-cloner-template-github.md)
- [Introducing Claude Design by Anthropic Labs](../sources/anthropic-claude-design-labs.md)
<!-- openclaw:wiki:related:end -->
