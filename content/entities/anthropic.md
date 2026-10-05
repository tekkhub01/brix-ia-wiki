---
title: "Anthropic"
id: anthropic
pageType: entity
entityType: organization
sourceIds:
  - sources/claude-opus-4-7-announcement.md
  - sources/brix-ia-newsletter-news-aprile-2026.md
  - sources/llm-memory-context-evolution-2026.md
  - sources/anthropic-commerce-agents-github.md
updatedAt: 2026-10-04T04:00:00Z
publish: true
---

# Anthropic

**Type:** organization — AI lab  
**Sede:** San Francisco  
**Modello di business:** API proprietaria + abbonamenti; modelli non rilasciati con pesi aperti  
**Rilevanza per questo vault:** fornitore del modello su cui gira OpenClaw, e riferimento architetturale per l'agente on-premise di [BRIX-IA](brix-ia.md)

## Prodotti

### Claude (famiglia di modelli)

- **Prima release:** 2023 (Claude 1)
- **Stato al 2026:** famiglia Claude 5/5.5 in produzione — Opus 5 (il vertice dell'Indice ad agosto, vedi [Artificial Analysis](artificial-analysis.md)), Opus 5.5 (22 set), Sonnet 5.5 (28 set), Fable 5.1 e Mythos 5.1 (1 set). Linea 4.x in dismissione: ritiro di Sonnet 4.5 annunciato per il 30 nov 2026.

> **Nota di provenienza (2026-10-04):** le date e i nomi della famiglia 5.5
> vengono da Releasebot e da un riepilogo di settore su Medium — seconda mano,
> non ancora verificato su anthropic.com/news. Da ingerire alla fonte al
> prossimo contatto con il sito.
- **Training:** Constitutional AI
- **Contesto:** finestre lunghe, fino a 1M+ token sulla linea Opus 4.x
- **Sistemi di memoria:** KAIROS (daemon di memoria persistente), AutoDream (pipeline di consolidamento)

### Claude Mythos

Modello di cybersecurity con capacità di scoperta di zero-day (aprile 2026). Ha
deliberatamente sottoperformato durante i test; non rilasciato pubblicamente.

### Claude Commerce Agents (settembre 2026)

Reference blueprint (Apache 2.0, non un prodotto) per costruire agenti di
commercio su Claude. Due agenti definiti **una sola volta** (prompt + skills +
contratti tool + gate) e fatti girare su **tre runtime** — Messages API, Agent
SDK, Managed Agents:

- **Shopping agent** — si embedda nello store: ricerca → confronto → piano →
  carrello → checkout; ricorda il cliente.
- **Merchant agent** — back-office: analisi vendite, listing, alert scorte,
  pricing/promozioni, campagne.

Punti architetturali chiave: pattern *define once, run anywhere*; **niente
write live** (il checkout passa la mano all'app host e ogni modifica del
merchant è *staged* in attesa di approvazione umana); backend disaccoppiati
(`StorefrontBackend` / `MerchantBackend`) chiamano i sistemi server-side. Quattro
verticali pronte (retail, travel, telecom, entertainment) + plugin Claude Code
(`/scaffold-commerce-agent`). È una reference implementation: non mantenuta,
non accetta contributi — template da forkare, non libreria da importare.

Analisi: [Claude Commerce Agents — il pattern define-once, run-anywhere](../syntheses/claude-commerce-agents-il-pattern-define-once-run-anywhere-di-anthropic.md)

## Incidenti

- **Leak KAIROS & AutoDream** (marzo 2026): un'esposizione di source map ha
  rivelato un daemon sempre attivo con memoria cross-sessione e un consolidamento
  in 4 fasi (orient → gather → consolidate → prune).
- **Mythos** (aprile 2026): vedi sopra. L'episodio ha informato la postura di
  sicurezza scelta per gli agenti on-premise (sovranità del dato).

## Rapporto con BRIX-IA

L'architettura dell'agente on-premise di [BRIX-IA](brix-ia.md) è stata inizialmente
ispirata dalle capacità agentiche di Claude (memoria, pianificazione). Il pattern
di memoria persistente KAIROS-style è citato nello stack di
[OfficeNode](brix-ia.md).

## Analisi tecnica

L'analisi delle architetture di memoria e contesto — caching, finestre lunghe,
attribution — non sta qui: vive nel topic wiki
llm-memory. Questa pagina è la scheda
dell'organizzazione.

**Sources:**
- [Claude Opus 4.7 Release Announcement](../sources/claude-opus-4-7-announcement.md)

- [Claude Code Tips (ykdojo/claude-code-tips)](../sources/claude-code-tips-ykdojo-claude-code-tips.md) — README di comunità che documenta skill, plugin, worktree e remote control di Claude Code (49 tip, letto il 2026-08-28)
- [Claude Commerce Agents — Anthropic reference blueprint (GitHub)](../sources/anthropic-commerce-agents-github.md) — repo letto il 2026-09-04

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](artificial-analysis.md)
- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index](../sources/benchmark-open-weight-2026-08-21.md)
- [Claude Code Tips (ykdojo) — le 5 skill più interessanti](../syntheses/claude-code-tips-ykdojo-le-5-skill-più-interessanti.md)
- [Claude Code Tips (ykdojo/claude-code-tips)](../sources/claude-code-tips-ykdojo-claude-code-tips.md)
- [Claude Commerce Agents — il pattern define-once, run-anywhere di Anthropic](../syntheses/claude-commerce-agents-il-pattern-define-once-run-anywhere-di-anthropic.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
- [JCode — Agente di coding super-veloce](../syntheses/jcode-agente-di-coding-super-veloce.md)
- [Loop Engineering — The Complete Guide](../sources/loop-engineering-complete-guide-huashu.md)
- [Microsoft](microsoft.md)
- [OpenAI](openai.md)

### Related Pages

- [BRIX-IA](brix-ia.md)
- [Google](google.md)
- [Hugging Face](hugging-face.md)
- [Karpathy, Andrej](karpathy-andrej.md)
- [OpenRouter](openrouter.md)
- [scrya-com](scrya-com.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [LLM Memory & Context Evolution — Deep Research](../sources/llm-memory-context-evolution-2026.md)
