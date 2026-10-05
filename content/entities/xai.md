---
title: "xAI"
id: xai
pageType: entity
entityType: organization
sourceIds:
  - sources/x-for-you-feed-algorithm-xai-org-x-algorithm.md
updatedAt: 2026-10-04T04:00:00Z
publish: true
---

# xAI

**Type:** organization — laboratorio AI, proprietario della piattaforma X
**Repository pubblico:** https://github.com/xai-org
**Rilevanza per questo vault:** è finora l'unica azienda qui dentro ad aver
pubblicato il codice di un sistema di raccomandazione in produzione, pesi
inclusi — un livello di apertura che nessun altro sistema censito in questo vault
raggiunge

## Prodotti

### X — feed "For You"

Il sistema che decide cosa un utente vede nel feed. Ad agosto 2026 il core è
open-source in [`xai-org/x-algorithm`](https://github.com/xai-org/x-algorithm),
licenza Apache-2.0: pipeline di ranking, filtri, configurazioni dei modelli e —
il punto che ha fatto notizia — i **pesi dei segnali**.

Componenti principali, tutti nel repo:

| Sistema | Ruolo |
|---|---|
| `home-mixer/` | costruisce il feed: stage della pipeline, pesi, chiamate agli altri servizi |
| `thunder/` | candidate source in-network: post recenti di chi segui, tenuti in memoria |
| `phoenix/` | retrieval out-of-network **e** modello di ranking (training in JAX, serving in Rust) |
| `simclusters/` | seconda sorgente out-of-network, per similarità di cluster |
| `vm-ranker/` | riordino finale con determinantal point process, per diversità |
| `visibility-filtering/` | decide se un post è mostrabile: allow / interstitial / drop |
| `grox/` | classificatori su testo e media dei post (spam, adulti, violenza) |
| `botmaker/`, `scarecrow/` | motore di regole e applicazione delle label sugli eventi |
| `agatha/`, `bdsm/`, `user-cred-v2/` | scoring degli account: reazioni ricevute, comportamento inautentico, PageRank sul grafo dei follow |

**Analisi completa:**
[Il feed "For You" di X in chiaro](../syntheses/x-algorithm-for-you-feed-xai.md)

### Grok

Modello e assistente di xAI. In questo vault compare finora solo di riflesso,
come uno degli agenti CLI che
[Headroom](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md)
dichiara di poter avvolgere (`headroom wrap grok`, memoria cross-agent con file
`GROK.md`). Nessuna fonte diretta ancora ingerita.

> **Aggiornamento 2026-10-04 (seconda mano, da verificare alla fonte):** xAI ha
> rilasciato **Grok 4.7** il 21 settembre — contesto 500k, input testo+immagine,
> pricing $2/$0.50/$6 per M token (Releasebot, 30/9). Grok 5 (MoE ~6T parametri su
> Colossus 2) ancora in training senza data annunciata; le fonti parlano anche di
> 4.8/4.9 davanti a Grok 5 (felloai.com, geotoolbox.ai, fine set). Nota: gli stessi
> aggregator riportano il nome "SpaceXAI" anche nel titolo di x.ai/news — possibile
> riclassificazione/merge societario non ancora registrato nel vault, da verificare.

## Perché ci interessa

Non per il prodotto — per il **precedente**. Il repo è l'unico caso nel vault in
cui si può leggere il codice che decide una distribuzione, invece di dedurlo dai
suoi effetti. Due conseguenze concrete:

1. **Le affermazioni sui pesi diventano verificabili.** Il repo corregge nei
   propri commenti al codice il mito che circola sui numeri (vedi la sintesi):
   una fonte che documenta come *non* va letta è più utile di una che si limita a
   pubblicare i valori.
2. **Trasparenza come architettura, non come comunicato.** Il codice è affiancato
   da uno strumento — *Under the Hood* — che mostra a ciascuno le label applicate
   al proprio account. Codice pubblico più output verificabili sul proprio caso:
   è lo stesso schema di provenienza che questo vault applica alle proprie
   affermazioni.

**Sources:**
- [X For You Feed Algorithm (xai-org/x-algorithm)](../sources/x-for-you-feed-algorithm-xai-org-x-algorithm.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Headroom — Context compression layer per AI agent (headroomlabs-ai)](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md)
- [Il feed "For You" di X in chiaro — architettura, pesi, filtri](../syntheses/x-algorithm-for-you-feed-xai.md)
- [X For You Feed Algorithm (xai-org/x-algorithm)](../sources/x-for-you-feed-algorithm-xai-org-x-algorithm.md)
<!-- openclaw:wiki:related:end -->
