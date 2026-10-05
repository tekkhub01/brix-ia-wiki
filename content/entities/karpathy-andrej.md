---
title: "Karpathy, Andrej"
id: karpathy-andrej
pageType: entity
entityType: person
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
  - sources/karpathy-llm-wiki-original-gist.md
updatedAt: 2026-09-13T05:00:00Z
publish: true
---

# Karpathy, Andrej

**Type:** person — ricercatore AI  
**Rilevanza per questo vault:** propone il pattern LLM Wiki, cioè l'architettura
su cui è costruito questo vault

## Contributo tracciato qui

**Formati di output per capire gli LLM** — post su X, 2 ottobre 2026 ([scheda](../syntheses/karpathy-formati-di-output-per-capire-gli-llm-asd-ste100-diagrammi-html-video.md)): ASD-STE100 all'80%, diagrammi, HTML interattivo, video stile 3Blue1Brown.

**LLM Wiki** — post su X + [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f),
4 aprile 2026. Propone di abbandonare il retrieval al momento della query in
favore della sintesi al momento della scrittura: un filesystem Markdown
persistente con cross-link, riassunti e indici mantenuti da un agente.

Il post ha raccolto ~16M visualizzazioni e il gist ha superato le 5k stelle in
pochi giorni.

La sua motivazione dichiarata è economica, non epistemica: *"la parte tediosa nel
mantenere una knowledge base non è leggere o pensare — è la contabilità."* Gli
LLM portano il costo di contabilità vicino a zero; agli umani restano l'analisi e
le buone domande.

## Stato della fonte

✅ **Il gist è ingerito** (2026-09-13): [Karpathy — LLM Wiki (original gist)](../sources/karpathy-llm-wiki-original-gist.md).
Le citazioni sopra e l'architettura a tre layer sono verificate **verbatim** contro
il testo primario. Restano di seconda mano solo i numeri di engagement (~16M
visualizzazioni, 5k stelle): non sono nel testo del gist.

## Novità (verifica 2026-09-13)

- Il pattern LLM Wiki è ora citato anche fuori dal vault come base del "knowledge compounding" di Wen & Ku (arXiv 2604.11243, Qing Claw): [fonte ingerita 2026-09-13](../sources/wen-ku-knowledge-compounding-under-the-agentic-roi-framework-arxiv-2604-11243.md).
- Talk a Sequoia AI Ascent 2026 ("From Vibe Coding to Agentic Engineering", con Stephanie Zhan): riassunto pubblicato sul suo blog (karpathy.bearblog.dev/sequoia-ascent-2026). Tema: "mai più indietro come programmatore" — coerente col filone harness/agent-loop del vault.
- Una notizia di startuphub.ai (giugno 2026) lo darebbe **approdato ad Anthropic** a dirigere il training. Fonte singola, aggregatore, non verificata: non incorporated nei claim.

## Analisi

Il pattern in sé — architettura a tre layer, workflow, pro e contro, numeri sul
compounding — è trattato nel topic wiki:
[llm-wiki-karpathy](../concepts/llm-wiki-karpathy.md).
Questa pagina è la scheda della persona.

## Background

Ricercatore AI noto per il lavoro su reti neurali e per un'ampia produzione
divulgativa. *Nota: background generale, non tratto dalle fonti di questo vault —
da confermare in fase di ingest del gist.*

**Sources:**
- [LLM Memory & Context Evolution — Deep Research](../sources/llm-memory-context-evolution-2026.md)
- [Karpathy — LLM Wiki (original gist)](../sources/karpathy-llm-wiki-original-gist.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Google](google.md)
- [OpenAI](openai.md)

### Related Pages

- [Anthropic](anthropic.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->
