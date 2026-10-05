---
title: "Microsoft"
id: microsoft
pageType: entity
entityType: organization
sourceIds:
  - sources/webwright-microsoft-github.md
updatedAt: 2026-09-01T00:00:00Z
publish: true
---

# Microsoft

**Type:** organization — piattaforma cloud, agenti, ricerca
**Sito:** https://microsoft.com
**Rilevanza per questo vault:** presente in 22 pagine, quasi sempre come *piattaforma
di distribuzione altrui* (Azure, Foundry, Copilot) e due volte come autore di
qualcosa che questo vault studia davvero — Webwright e GraphRAG

## Prodotti

### Webwright

Browser agent open source (`github.com/microsoft/Webwright`), integrato come skill su
Claudia. I benchmark dichiarati dal repo:

| Benchmark | Webwright | Confronto dichiarato |
|---|---|---|
| Online-Mind2Web | **86,67%** | Claude Opus 4.6: 44,5% |
| Odysseys | **60,1%** | GPT-5.4 base: 33,5% |

**Nessuna di queste cifre è verificata da terzi**, e la pagina va letta tenendo conto
di un'ironia specifica: sono esattamente il tipo di numero — agente vs modello nudo —
che la tesi
[The Harness Is Half the Measurement](../topics/harness-vs-model.md)
mostra essere incomparabile. Un agente al 60,1% contro un modello "base" al 33,5% non
misura due modelli, misura un modello con harness contro lo stesso genere di modello
senza. Il confronto informativo — Webwright contro un altro *agente* — non è pubblicato.

### GraphRAG

Architettura di retrieval su grafo di entità e relazioni, ed è il contributo
Microsoft più solidamente coperto in questo vault: ha una
[pagina concetto dedicata](../concepts/graphrag.md) nel topic
llm-memory. Il claim per cui le community summary battono il retrieval vettoriale
"by a wide margin" resta però **senza numero**, tracciato in
[q-graphrag-global-query-margin](../questions/q-graphrag-global-query-margin.md).

### Azure, Microsoft Foundry, GitHub Copilot

Compaiono solo come destinazioni: [Anthropic](anthropic.md) distribuisce Claude anche
su Microsoft Foundry, JCode elenca Azure e Copilot fra i provider supportati,
[Alibaba](alibaba.md) cita Azure come alternativa. Nessuna analisi.

### Playwright MCP

Server [MCP](../concepts/mcp.md) per l'automazione browser,
raccomandato come companion nei Claude Code tips — uno dei cinque server che, nel
vault, dimostrano l'adozione del protocollo fuori dai framework di agenti.

## Perché ci interessa

Marginalmente come piattaforma — BRIX-IA lavora on-premise, e il cloud Microsoft è
per definizione l'opzione che il posizionamento locale rifiuta. Concretamente come
**fonte di software agentico open source**: Webwright gira su Claudia, GraphRAG è un
pilastro del topic llm-memory. È un attore che qui conta per quello che pubblica su
GitHub, non per quello che vende.

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [Webwright — Microsoft Browser Agent Skill](../sources/webwright-microsoft-github.md)
