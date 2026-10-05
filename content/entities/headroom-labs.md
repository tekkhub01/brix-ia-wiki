---
title: "Headroom Labs"
id: headroom-labs
pageType: entity
entityType: organization
sourceIds:
  - sources/headroom-2026-08-04.md
updatedAt: 2026-09-13T05:00:00Z
publish: true
---

# Headroom Labs

**Type:** organization — tooling per AI agent
**GitHub:** https://github.com/headroomlabs-ai
**Docs:** https://docs.headroomlabs.ai/docs
**Rilevanza per questo vault:** produce Headroom, che attacca il costo del
contesto dal lato opposto rispetto al caching

## Prodotti

### Headroom

Layer di compressione che riduce tutto ciò che l'agente legge — output di tool,
log, chunk RAG, file, cronologia — *prima* che arrivi al modello. Rust, licenza
Apache-2.0, 66,3k stelle (verificato sul repo il 2026-08-14).

Risparmi dichiarati dal progetto: **15–20% di token** negli agent di coding,
**fino al 60–95% su JSON**.

Tre proprietà lo rendono adottabile:

- gira in locale come **libreria, proxy o MCP server**
- processa separatamente codice, testo e dati strutturati
- **gli originali non vengono distrutti**: restano in cache locale e l'agente può
  richiedere indietro il frammento che gli serve

Quest'ultimo punto è quello che lo distingue da una compressione con perdita: la
riduzione è sul percorso di lettura, non sull'archivio.

Analisi completa: [Headroom — Context compression layer](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md)

### Novità (verifica 2026-09-13)

Il progetto ha esteso la compressione lato **output** (verbosity steering ed effort routing gestiti dal proxy) e aggiunto statistiche token/costo per sessione in chiaro. Le cifre del vault (15–20% coding, 60–95% JSON) sono già quelle "ristrette" — nessuna correzione necessaria.

## Perché ci interessa

È la terza strada sul costo del contesto, accanto alle due che il topic wiki già
tratta: [context caching](../concepts/context-caching.md)
riusa il prefisso senza ricalcolarlo, i
[modelli long-context](../concepts/long-context-models.md)
allargano la finestra. Headroom invece riduce ciò che entra. Le tre leve si
compongono e non si escludono — e nessuna delle tre è misurata nelle stesse unità,
che è il problema aperto in
[memory-economics](../topics/memory-economics.md).

**Sources:**
- [Headroom — segnalazione 2026-08-04](../sources/headroom-2026-08-04.md)

## Collegamenti (dreaming 2026-08-15)

- Comprimere la KV cache è l'altra leva sulla stessa voce di costo: [quantization](../concepts/quantization.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Headroom — Context compression layer per AI agent (headroomlabs-ai)](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md)
- [nicepkg](nicepkg.md)
<!-- openclaw:wiki:related:end -->
