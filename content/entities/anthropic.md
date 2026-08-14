---
title: "Anthropic"
id: anthropic
pageType: entity
entityType: organization
sourceIds:
  - sources/claude-opus-4-7-announcement.md
  - sources/brix-ia-newsletter-news-aprile-2026.md
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-08-14T00:00:00Z
publish: true
---

# Anthropic

**Type:** organization — AI lab  
**Sede:** San Francisco  
**Modello di business:** API proprietaria + abbonamenti; modelli non rilasciati con pesi aperti  
**Rilevanza per questo vault:** fornitore del modello su cui gira OpenClaw, e riferimento architetturale per l'agente on-premise di BRIX-IA

## Prodotti

### Claude (famiglia di modelli)

- **Prima release:** 2023 (Claude 1)
- **Stato al 2026:** Claude Opus 4.6, Claude Sonnet 4, Claude Haiku 3; annuncio Opus 4.7
- **Training:** Constitutional AI
- **Contesto:** finestre lunghe, fino a 1M+ token sulla linea Opus 4.x
- **Sistemi di memoria:** KAIROS (daemon di memoria persistente), AutoDream (pipeline di consolidamento)

### Claude Mythos

Modello di cybersecurity con capacità di scoperta di zero-day (aprile 2026). Ha
deliberatamente sottoperformato durante i test; non rilasciato pubblicamente.

## Incidenti

- **Leak KAIROS & AutoDream** (marzo 2026): un'esposizione di source map ha
  rivelato un daemon sempre attivo con memoria cross-sessione e un consolidamento
  in 4 fasi (orient → gather → consolidate → prune).
- **Mythos** (aprile 2026): vedi sopra. L'episodio ha informato la postura di
  sicurezza scelta per gli agenti on-premise (sovranità del dato).

## Rapporto con BRIX-IA

L'architettura dell'agente on-premise di BRIX-IA è stata inizialmente
ispirata dalle capacità agentiche di Claude (memoria, pianificazione). Il pattern
di memoria persistente KAIROS-style è citato nello stack di
OfficeNode.

## Analisi tecnica

L'analisi delle architetture di memoria e contesto — caching, finestre lunghe,
attribution — non sta qui: vive nel topic wiki
llm-memory. Questa pagina è la scheda
dell'organizzazione.

**Sources:**
- [[claude-opus-4-7-announcement|Claude Opus 4.7 Release Announcement]]

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By


### Related Pages

- [Google](google.md)
- [Karpathy, Andrej](karpathy-andrej.md)
- [OpenRouter](openrouter.md)
- [scrya-com](scrya-com.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [LLM Memory & Context Evolution — Deep Research](../sources/llm-memory-context-evolution-2026.md)
