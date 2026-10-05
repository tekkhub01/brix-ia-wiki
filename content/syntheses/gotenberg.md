---
pageType: synthesis
id: synthesis.gotenberg
title: Gotenberg
sourceIds:
  - https://gotenberg.dev/
status: active
updatedAt: 2026-09-13T04:40:00Z
publish: true
---

# Gotenberg

## Notes
<!-- openclaw:human:start -->
### Collegamenti (dreaming 2026-08-15)
- Stessa catena documentale, lato rendering: [anydoc](anydoc-firecrawl.md) e [PDF Inspector](pdf-inspector-firecrawl.md)
- Entrambi di [Firecrawl](../entities/firecrawl.md)

<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Gotenberg

**Sito:** https://gotenberg.dev/
**GitHub:** https://github.com/gotenberg/gotenberg
**Docker Hub:** https://hub.docker.com/r/gotenberg/gotenberg
**Documentazione:** https://gotenberg.dev/docs/getting-started/introduction

## Stato release (verifica web 2026-09-13)

- Ultima release: **v8.37.0** (2026-09-11). Serie v8.x attiva; roadmap **v9.0.0** già aperta come issue (#1484).
- **Sicurezza:** advisory GO-2026-5080 — lettura PDF arbitraria via `stampExpression`/`watermarkExpression` nelle rotte merge/split/convert; patchata nelle release di agosto. Rilasci recenti irrigidiscono anche l'SSRF: i file OOXML/RTF/ODF caricati possono incorporare URL esterni che LibreOffice risolveva sotto i filtri Go — ora ogni fetch in uscita da LibreOffice passa da un forward proxy in-process (`gotenberg.DecideOutbound`). Se si usa Gotenberg con upload non fidati, aggiornare ad almeno v8.36/v8.37.

## Cos'è

Gotenberg è un'API Docker-based per convertire documenti in PDF. Usa Chromium headless e LibreOffice sotto il cofano, gestendo automaticamente font, JS e rendering. Supportato da arm64, amd64, armhf, i386, ppc64le.

## Funzionalità principali

### Web → PDF (Chromium)
- Conversione di URL, template HTML e Markdown in PDF
- Attesa per network idle, espressioni JS o selettori DOM prima del rendering (utile per SPA)
- Controllo rete: cookies, HTTP headers personalizzati, gestione errori HTTP
- Screenshot di URL e HTML

### Office → PDF (LibreOffice)
- Conversione di Word (.docx), Excel (.xlsx), PowerPoint (.pptx) e 100+ formati
- Page ranges specifiche
- PDF/A e PDF/UA compliance (standard archivio)

### Operazioni PDF (QPDF, pdfcpu, ExifTool)
- Merge, split, rotate, flatten form fields
- Watermark, stamp, encrypt (user/owner password)
- Leggere/scrivere metadata e bookmarks
- Embed attachments

### Cloud Native — Zero-Transfer Pipelines
- **Direct Fetch:** Gotenberg scarica il file direttamente da S3 Presigned GET URL
- **Auto Upload:** Gotenberg carica il risultato su S3 Presigned PUT URL
- **Webhook Events:** notifiche JSON su completamento/fallimento
- Vantaggio: il server orchestra, Gotenberg fa il lavoro pesante — risparmio banda

## Utilizzo base

```bash
# Avvio container
docker run --rm -p 3000:3000 gotenberg/gotenberg:8

# URL → PDF
curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://example.com \
  -o output.pdf

# HTML → PDF
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@documento.html \
  -o output.pdf

# DOCX → PDF
curl --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@documento.docx \
  -o output.pdf

# Merge PDF
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@doc1.pdf \
  --form files=@doc2.pdf \
  -o merged.pdf
```

## Cloud Native Pipeline (S3)

```bash
curl --request POST http://localhost:3000/forms/libreoffice/convert \
  --form 'downloadFrom=[{"url": "https://my-bucket.s3.amazonaws.com/file.docx?Start=..."}]' \
  --header 'Gotenberg-Webhook-Url: https://my-bucket.s3.amazonaws.com/out.pdf?Start=...' \
  --header 'Gotenberg-Webhook-Method: PUT' \
  --header 'Gotenberg-Webhook-Events-Url: https://my-api.com/events'
```

## Rilevanza

Gotenberg è adottato da migliaia di aziende in produzione e da progetti open-source notabili. Può sostituire/supportare il pattern attuale di conversione PDF via LibreOffice headless (skill `docx2pdf`), offrendo in più Chromium per rendering HTML/URL e pipeline S3.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [anydoc (Firecrawl)](anydoc-firecrawl.md)
- [Firecrawl](../entities/firecrawl.md)
- [PDF Inspector (Firecrawl)](pdf-inspector-firecrawl.md)
<!-- openclaw:wiki:related:end -->
