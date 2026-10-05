---
pageType: synthesis
id: synthesis.karpathy-formati-di-output-per-capire-gli-llm-asd-ste100-diagrammi-html-video
title: Karpathy — formati di output per capire gli LLM (ASD-STE100, diagrammi,
  HTML, video)
sourceIds:
  - karpathy-x-post-formati-output-llm-2026-10-02
confidence: 0.9
status: active
updatedAt: 2026-10-03T07:14:17.522Z
publish: true
---

# Karpathy — formati di output per capire gli LLM (ASD-STE100, diagrammi, HTML, video)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Immagine dal post

![Infografica ASD-STE100 (Simplified Technical English)](../_attachments/karpathy-asd-ste100-infographic-2026-10-03.jpg)

*Infografica di sintesi dello standard ASD-STE100: struttura del documento, anatomia della frase (procedurale/sicurezza/descrittiva), verbi approvati vs non approvati, esempi di dizionario, limiti delle regole di scrittura, timeline storica.*

## Il post originale

Andrej Karpathy, X, 2 ottobre 2026: https://x.com/karpathy/status/2105819303471976479

Tesi: passeremo sempre più tempo a **capire gli output** degli LLM, più che a generarli. Quattro formati in ordine di efficacia:

1. **Testo in ASD-STE100** — Simplified Technical English (standard aviation, ~900 parole approvate, frasi ≤20-25 parole, active voice). Karpathy usa la versione ammorbidita: "80% of the way to ASD-STE100".
2. **Diagrammi/immagini** — al posto del testo dove la struttura visiva è più rapida da decodificare.
3. **Pagine HTML interattive** — visualizzazioni e animazioni on-demand sul tema specifico.
4. **Video spiegatori personalizzati** — "fai un video stile 3Blue1Brown su X" + narrazione ElevenLabs. Il più promettente secondo lui.

## Contesto e caveat

- L'idea STE+LLM circolava già da fine luglio 2026 (Andrew Carr, Pieter Levels con Claude); Karpathy ha dato reach.
- Sono nati skill/repo: `JAICHANGPARK/ASD-STE100`, `danyuchn/asd-ste100-skill`, `prithivrajmu/asd-ste100`, `AminBlg/SimpleEnglish`.
- **Tradeoff misurato**: con STE strict le spiegazioni perdono ~47% dei fatti tecnici (test Ghinda, ago 2026); con "80%" ~8,5%. Da qui la versione ammorbidita di Karpathy.
- Lo standard esiste solo per l'inglese; esiste un "Italiano Tecnico Semplificato" di ricerca, non certificato.
- ASD-STE100 Issue 9 (gen 2025) scaricabile gratis: https://www.asd-ste100.org/STE_downloads.html

## Applicazione pratica in BRIX-IA

Questi trucchi sono già usabili on-demand: spiegazioni "in stile STE all'80%", diagrammi Mermaid, pagine HTML interattive (skill `md2html`), video (pipeline Remotion/generazione). Candidabile come skill dedicata se PK lo usa spesso.

*Aggiunta dal thread Telegram del 3/10/2026 (post INCUBE.AI in russo + verifica fonte originale).*
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Karpathy — X post sui formati di output per capire gli LLM (2/10/2026)](../sources/karpathy-x-post-formati-output-llm-2026-10-02.md)

### Referenced By

- [Karpathy, Andrej](../entities/karpathy-andrej.md)
<!-- openclaw:wiki:related:end -->
