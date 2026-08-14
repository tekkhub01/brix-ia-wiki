---
pageType: synthesis
id: synthesis.pdf-inspector-firecrawl
title: PDF Inspector (Firecrawl)
sourceIds:
  - https://github.com/firecrawl/pdf-inspector
status: active
updatedAt: 2026-08-03T08:02:29.385Z
publish: true
---

# PDF Inspector (Firecrawl)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# PDF Inspector (Firecrawl)

**GitHub:** https://github.com/firecrawl/pdf-inspector
**Crates.io:** https://crates.io/crates/pdf-inspector
**npm:** https://www.npmjs.com/package/@firecrawl/pdf-inspector
**PyPI:** https://pypi.org/project/pdf-inspector/
**Docs Python:** https://github.com/firecrawl/pdf-inspector/blob/main/docs/python.md

## Cos'è

Libreria Rust (veloce) per l'ispezione, classificazione ed estrazione testo da PDF. Rileva intelligentemente se un PDF è scansionato o basato su testo per abilitare smart routing e saltare l'OCR costosa — circa il 54% dei PDF non ne ha bisogno. Costruita da Firecrawl per gestire PDF testuali localmente in meno di 200ms.

## Funzionalità principali

- **Smart classification** — Distingue TextBased, Scanned, ImageBased, Mixed in ~10-50ms campionando i content stream. Ritorna un confidence score (0.0-1.0) e OCR routing per-pagina.
- **Text extraction** — Estrazione position-aware con font info, coordinate X/Y e reading order automatico multi-colonna.
- **Markdown conversion** — Heading H1-H4 (via font size ratios), liste (bullet/numbered/letter), code block (monospace detection), tabelle, bold/italic, URL linking, page breaks.
- **Table detection** — Dual-mode: rectangle-based (da PDF drawing ops) + heuristic (da allineamento testo). Gestisce tabelle finanziarie, footnote e continuazione across pages.
- **CID font support** — ToUnicode CMap decoding per Type0/Identity-H, UTF-16BE, UTF-8, Latin-1.
- **Multi-column layout** — Rilevamento colonne stile giornale, reading order sequenziale, supporto RTL.
- **Encoding issue detection** — Flagga encoding rotti per fallback a OCR.
- **Single document load** — Il documento è parsato una volta e condiviso tra detection ed extraction (no I/O ridondante).
- **Browser WebAssembly** — Stesso parser Rust in browser/Web Workers, CMaps embeddati, zero round-trip server.
- **Lightweight** — Pure Rust, nessun modello ML, nessun servizio esterno. Una sola dipendenza: `lopdf`.

## Bindings
Python, Node.js (napi), WebAssembly browser.

## Performance
Valutato su opendataloader-bench (200 PDF, OCR disabilitato, M4 Pro, 2026-07-31). Overall 0.875 / Reading Order 0.915 / Tables 0.814 / Headings 0.788 / Speed 0.470s (200 docs). Supera liteparse, opendataloader, pymupdf4llm e markitdown in qualità e velocità.

## Rilevanza
Alternativa local-first a PyMuPDF4LLM e MarkItDown per estrazione PDF→Markdown, senza OCR ed eseguita localmente. Utile per pipeline RAG/document-processing. Potenziale integrazione con le skill di estrazione PDF (es. `mineru`) per il routing smart scanned-vs-text (classifica prima di decidere se serve OCR).
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
