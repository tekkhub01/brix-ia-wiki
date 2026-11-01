---
pageType: synthesis
id: synthesis.google-sleep-framework-consolidamento-offline-dei-modelli-linguistici
title: "Google \"Sleep\" framework — consolidamento offline dei modelli linguistici: BABILong a 10M token"
sourceIds:
  - https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning
  - arxiv:Language-Models-Need-Sleep (Behrouz, Hashemi, Javanmard, Mirrokni)
  - telegram:brixia-newsletter/2026-11-01
claims:
  - text: "Google Research presenta il framework Sleep (blog 27/10/2026, Behrouz/Hashemi/Javanmard/Mirrokni; paper Language Models Need Sleep su arXiv da giugno 2026): ciclo wake/sleep in cui il modello smette di ricevere input e consolida la memoria di breve periodo nei parametri."
    status: supported
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning
        weight: 1
        note: blog ufficiale verificato via ricerca 2026-11-01
  - text: "Nella fase dreaming il modello genera da sé problemi di esercizio, seleziona i più utili e si addestra su quelli; capacità extra riservata in un MoE, teacher guida il trasferimento, poi reset dei parametri temporanei."
    status: supported
    confidence: 0.85
    evidence:
      - kind: web
        sourceId: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning
        weight: 1
  - text: "Su BABILong scaling quasi perfetto fino a 10M token, sopra GPT-4, GPT-4o-mini, Llama-8B+retrieval, RMT, ARMT e Titans. Attenzione all'interpretazione: è informazione compressa nei pesi (sleep-time consolidation), NON attenzione su un prompt da 10M token."
    status: supported
    confidence: 0.85
    evidence:
      - kind: web
        sourceId: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning
        weight: 1
        note: il blog dichiara "compress long-context information directly into parametric memory"; la precisone è confermata anche dalla stampa tecnica
  - text: "Altri risultati dichiarati: Qwen3-8B allenato con Sleep batte base e baseline su tre benchmark di matematica competitiva (16 sample/domanda); batte SEAL nell'incorporamento fattuale; traduzione continua di due lingue fuori pretraining con forgetting quasi zero; ragionamento few-shot su Llama-3.2-1B 80% vs 72,5% SEAL."
    status: reported
    confidence: 0.6
    evidence:
      - kind: web
        sourceId: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning
        weight: 0.7
        note: numeri auto-riportati dal team, nessuna riproduzione indipendente
questions:
  - Riproduzione indipendente dei risultati BABILong a 10M token: i claim long-context si riducono spesso sotto prompt diversi.
  - Il framework uscirà dal prototipo (API/prodotto Gemini) o resta ricerca?
  - Confronto diretto con la nostra memoria esterna (wiki + daily notes): se il consolidamento sta nel modello, metà dello stack di memoria si sposta nel fornitore.
status: active
publish: true
updatedAt: 2026-11-01T14:05:00Z
---

# Google "Sleep" framework — consolidamento offline dei modelli linguistici: BABILong a 10M token

## Notes
<!-- openclaw:human:start -->
Prototipo, non prodotto: da citare sempre come risultato auto-riportato.

Vedi anche: [[syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai|Headroom]] (comprime ciò che entra), [[syntheses/supermemory-motore-di-memoria-e-contesto-per-agenti-ai-valutazione|Supermemory]] (memoria esterna lato agente), AA Index v5. Copertura: newsletter #54 del 01-11-2026.
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
Google Research propone il **sonno per i LLM** (blog 27/10/2026): un ciclo in due fasi ispirato alla biologia. **Wake**: il modello interagisce e accumula informazioni temporanee. **Sleep**: smette di ricevere input, consolida in memoria parametrica di lungo periodo e nella fase **"dreaming"** genera da sé problemi di esercizio, seleziona i più utili e si addestra su quelli.

**Il numero che fa discutere**: quasi-perfetto su BABILong fino a **10 milioni di token**, sopra GPT-4 e Titans. Ma è una precisione decisiva: è conoscenza **compressa nei pesi**, non attenzione su un prompt da 10M token. È un risultato di *retention*, non di context window.

**Perché riguarda BRIX-IA**: è esattamente il problema che risolviamo a mano con memoria esterna e riscrittura delle note (wiki, daily notes, dreaming di memory-core). Se il consolidamento diventa una fase del modello invece che un'infrastruttura sopra il modello, metà del nostro stack di memoria si sposta dentro il fornitore.

## Contesto in vault
- Alternativa infrastrutturale lato agente: [[syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai|Headroom]] (comprime ciò che entra) e [[syntheses/supermemory-motore-di-memoria-e-contesto-per-agenti-ai-valutazione|Supermemory]]
- Tema concettuale: AA Index v5 (i task agentici già consumano ~90% dei token)
- Newsletter di copertura: #54 del 01-11-2026
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Anthropic S-1 — i primi numeri pubblici di un frontier lab: ticker ANT, $16,3 mld H1, utile operativo Q2](anthropic-s-1-i-primi-numeri-pubblici-di-un-frontier-lab-ticker-ant-16-3-mld-h1-utile-operativo-q2.md)
- [Gemini 4 Carbon — il frontier Google a accesso controllato: #1 AA v5, SOTA cybersecurity, rollout solo cyber defenders](gemini-4-carbon-il-frontier-google-a-accesso-controllato-1-aa-v5-sota-cybersecurity-rollout-solo-cyber-defenders.md)
- [Idol (Speridlabs) — una foto diventa oggetto 3D Gaussian splats in 19 secondi, Apache 2.0](idol-speridlabs-una-foto-diventa-oggetto-3d-gaussian-splats-in-19-secondi.md)
- [Kimi K3.1 Pro (Moonshot) — il frontier aperto in arrivo: 2,8T parametri, pesi annunciati per il 4 novembre](kimi-k3-1-pro-moonshot-il-frontier-aperto-in-arrivo-2-8t-parametri-pesi-annunciati-per-il-4-novembre.md)
<!-- openclaw:wiki:related:end -->
