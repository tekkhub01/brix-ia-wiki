---
title: "Firecrawl"
id: firecrawl
pageType: entity
entityType: organization
sourceIds:
  - sources/pdf-inspector-2026-08-09.md
updatedAt: 2026-09-13T05:00:00Z
publish: true
---

# Firecrawl

**Type:** organization — tooling per document processing e web data
**GitHub:** https://github.com/firecrawl
**Prodotto commerciale:** Firecrawl Parse — https://firecrawl.dev/parse
**Rilevanza per questo vault:** produce due librerie Rust che stanno a monte di
qualunque pipeline documentale, incluse le nostre

La costante nei loro rilasci è la stessa: **Rust, local-first, nessuna
dipendenza di rete sul percorso veloce**, con binding per Node, Python e
WebAssembly. È ciò che li rende adottabili in un contesto on-premise.

## Prodotti

### anydoc

Converte Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV e PDF in Markdown
GitHub-Flavored pulito, con output coerente qualunque sia il formato in ingresso.
Licenza MIT. Espone anche un modello documento intermedio con gli asset embedded,
prima della conversione. Gira in locale o nel browser via WebAssembly — nella
demo i file non lasciano la macchina.

Analisi completa: [anydoc (Firecrawl)](../syntheses/anydoc-firecrawl.md)

### PDF Inspector

Inverte l'ordine della pipeline PDF: prima classifica il documento, poi decide
quali pagine hanno davvero bisogno di OCR. Il dato che regge la tesi è che circa
il **54% dei PDF non ne ha bisogno**, e l'OCR è di norma la fase più costosa.

```
prima:  PDF → OCR di tutte le pagine → parsing
dopo:   PDF → classificazione → estrazione nativa → OCR solo delle pagine complesse
```

Analisi completa: [PDF Inspector (Firecrawl)](../syntheses/pdf-inspector-firecrawl.md)

### Novità (verifica 2026-09-13)

La piattaforma commerciale si è allargata oltre le due librerie Rust tracciate qui: endpoint **Agent** (ricerca web autonoma da prompt), **/interact** (scrape + azioni sulla pagina), **Firecrawl Index / Developer Index** (claim: scraping fino a 5× più veloce con opt-in), Java SDK community. Trazione dichiarata: $14.5M Series A (Nexus Venture Partners), 350k+ developer, 48k+ stelle GitHub. Non cambia il perimetro di interesse del vault (anydoc e PDF Inspector restano il lato on-premise).

## Perché ci interessa

Entrambi risolvono lo stesso problema che affrontiamo con MinerU e Gotenberg:
portare documenti eterogenei a Markdown utilizzabile da un LLM senza mandarli a
un servizio esterno. PDF Inspector in particolare è complementare, non
alternativo: decide *cosa* mandare all'OCR, non lo sostituisce.

**Sources:**
- [PDF Inspector — segnalazione 2026-08-09](../sources/pdf-inspector-2026-08-09.md)

## Collegamenti (dreaming 2026-08-15)

- Stessa catena documentale, lato rendering: [Gotenberg](../syntheses/gotenberg.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Gotenberg](../syntheses/gotenberg.md)
- [PDF Inspector (Firecrawl)](../syntheses/pdf-inspector-firecrawl.md)
<!-- openclaw:wiki:related:end -->
