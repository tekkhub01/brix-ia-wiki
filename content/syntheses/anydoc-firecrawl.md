---
pageType: synthesis
id: synthesis.anydoc-firecrawl
title: anydoc (Firecrawl)
sourceIds:
  - https://github.com/firecrawl/anydoc
status: active
updatedAt: 2026-08-10T10:05:33.000Z
publish: true
---

# anydoc (Firecrawl)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# anydoc (Firecrawl)

**GitHub:** https://github.com/firecrawl/anydoc
**Homepage/Demo:** https://firecrawl.github.io/anydoc/
**npm:** https://www.npmjs.com/package/@firecrawl/anydoc
**PyPI:** https://pypi.org/project/firecrawl-anydoc/
**Crates.io:** https://crates.io/crates/anydoc
**License:** MIT
**Linguaggio:** Rust (bindings Node.js, Python, WebAssembly, Rust)

## Cos'è

Libreria Rust (velocissima) che converte documenti — Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV e PDF — in Markdown pulito (GitHub-Flavored). Obiettivo: trasformare qualsiasi documento da ufficio in Markdown "LLM-ready" in millisecondi a singola cifra, con un output coerente indipendentemente dal formato in ingresso. Alimenta [Firecrawl Parse](https://firecrawl.dev/parse).

## Funzionalità principali

- **Conversione multi-formato** — DOCX, PPTX, XLSX, ODT, RTF, EPUB, CSV, PDF → Markdown pulito, con un unico formato di output.
- **Auto-detect del formato** — `toMarkdownBytes(bytes)` rileva il formato dal contenuto; i formati senza firma (es. CSV) richiedono di specificarlo esplicitamente.
- **Modello documento intermedio** — `toDocument(...)` espone il document model con asset embedded (immagini, ecc.) prima della conversione in Markdown.
- **Local-first** — Esegue in locale (CLI/Node/Python/Rust) o nel browser via WebAssembly; la demo gira interamente client-side, i file non lasciano la macchina.
- **Agent Skill** — Si installa come Agent Skill (`npx skills add firecrawl/anydoc`); insegna all'agente a convertire documenti via CLI. Compatibile con Claude Code, Codex, Cursor, OpenCode.
- **Niente OCR integrato (importante per progetti OCR)** — anydoc legge il testo nativo nei PDF; per le pagine scansionate/immagine che non riesce a leggere da solo, serve l'API hostata Firecrawl Parse (che aggiunge i modelli OCR di Firecrawl). In locale anydoc non fa OCR.

## Quick start

```bash
# CLI (npx scarica il binario prebuilt al primo run)
npx @firecrawl/anydoc report.docx            # Markdown su stdout
npx @firecrawl/anydoc slides.pptx -o out.md  # su file
npx @firecrawl/anydoc - --format csv < data.csv

# Python
pip install firecrawl-anydoc
import anydoc; md = anydoc.to_markdown("report.docx")

# Node.js
npm install @firecrawl/anydoc
import { toMarkdown } from '@firecrawl/anydoc'
```

## Rilevanza

Alternativa local-first e multi-formato a PyMuPDF4LLM / MarkItDown per il document-processing, ma copre anche DOCX/PPTX/XLSX/ODT/EPUB/RTF/CSV (non solo PDF). Utile come layer di pre-processing unificato prima della RAG o dell'estrazione dati.

Per i **progetti OCR**: anydoc gestisce i documenti nativi (testo) → Markdown in locale e gratis; per i PDF scansionati serve comunque un motore OCR. Combinazione suggerita:
- `pdf-inspector` per classificare scanned-vs-text (routing smart, evita OCR inutile ~54% dei casi);
- anydoc per la conversione text-based in Markdown;
- OCR (modelli Firecrawl Parse via API, oppure motore locale) solo sulle pagine scansionate.

Da testare se può sostituire/affiancare MinerU sui progetti OCR correnti.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Firecrawl](../entities/firecrawl.md)
- [PDF Inspector (Firecrawl)](pdf-inspector-firecrawl.md)
<!-- openclaw:wiki:related:end -->
