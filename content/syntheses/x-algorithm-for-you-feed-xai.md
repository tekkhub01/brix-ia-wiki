---
pageType: synthesis
id: synthesis.x-algorithm-for-you-feed-xai
title: Il feed "For You" di X in chiaro — architettura, pesi, filtri
sourceIds:
  - source.x-for-you-feed-algorithm-xai-org-x-algorithm
  - https://github.com/xai-org/x-algorithm
claims:
  - id: pesi-su-probabilita
    text: I pesi delle azioni moltiplicano la probabilità predetta dell'azione, non
      i conteggi grezzi di engagement; leggere "1 report annulla 468 like" è quindi
      un errore di interpretazione, dichiarato tale dagli autori nei commenti al codice
    status: verified
    confidence: 0.95
    evidence:
      - kind: doc
        sourceId: source.x-for-you-feed-algorithm-xai-org-x-algorithm
        note: Sezioni "Latest Updates — August 14th 2026" e "Scoring and Ranking";
          commenti aggiunti in home-mixer/params/param.rs e scorers/ranking_scorer.rs
  - id: score-somma-pesata
    text: Il punteggio finale di un post è la somma pesata delle probabilità predette
      per ogni azione (Final Score = Σ weight_i × P(action_i)), con pesi negativi
      per le azioni negative
    status: verified
    confidence: 0.95
    evidence:
      - kind: doc
        sourceId: source.x-for-you-feed-algorithm-xai-org-x-algorithm
        note: Sezione "Scoring and Ranking"
  - id: ranking-separato-da-visibilita
    text: Ranking e visibilità sono sistemi separati — l'ordine lo decide il modello,
      se un post sia mostrabile lo decide visibility-filtering con tre esiti
      (allow / interstitial / drop)
    status: verified
    confidence: 0.95
    evidence:
      - kind: doc
        sourceId: source.x-for-you-feed-algorithm-xai-org-x-algorithm
        note: Sezione "Key Design Decisions #4" e diagramma del Labeling Path
  - id: candidate-isolation
    text: Durante l'inferenza del transformer i candidati non possono attendere l'uno
      all'altro, solo al contesto del viewer; il punteggio di un post non dipende
      quindi dagli altri post nel batch ed è cacheabile
    status: verified
    confidence: 0.9
    evidence:
      - kind: doc
        sourceId: source.x-for-you-feed-algorithm-xai-org-x-algorithm
        note: Sezione "Key Design Decisions #2"
  - id: default-allineati-a-produzione
    text: I valori di default nel repo sono allineati ai valori primari di produzione
      da script cron, e gli esperimenti sopra il ~10% del traffico dovrebbero essere
      visibili nel repository
    status: unverified
    confidence: 0.6
    evidence:
      - kind: doc
        sourceId: source.x-for-you-feed-algorithm-xai-org-x-algorithm
        note: "Sezione \"Experiments and Configuration\"; è una dichiarazione di
          intenti degli autori, non verificabile dall'esterno"
  - id: esclusioni-dichiarate
    text: Alcuni file sono deliberatamente non pubblicati — i prompt j2 di Grox e
      parte delle regole botmaker — per ridurre il rischio di gaming
    status: verified
    confidence: 0.9
    evidence:
      - kind: doc
        sourceId: source.x-for-you-feed-algorithm-xai-org-x-algorithm
        note: Sezione "What's not in this repo?"
confidence: 0.9
status: active
updatedAt: 2026-08-17T00:00:00Z
publish: true
---

# Il feed "For You" di X in chiaro — architettura, pesi, filtri

## Notes
<!-- openclaw:human:start -->
### Collegamenti
- Pubblicato da [xAI](../entities/xai.md)
- Fonte: [README di xai-org/x-algorithm](../sources/x-for-you-feed-algorithm-xai-org-x-algorithm.md),
  ingerita il 2026-08-15 su segnalazione di PK (forward da un canale di news AI)
- Apre un cluster nuovo per questo vault — sistemi di raccomandazione e ranking —
  di cui è per ora l'unico membro
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->

## Cosa c'è davvero nel repo

Non è il rilascio simbolico del 2023. La codebase è dichiarata 10-15× più grande
del rilascio precedente e contiene le tre cose che prima mancavano: **i pesi**,
**i filtri** e il **codice di training** del modello di ranking (Phoenix, JAX per
il training e Rust per il serving, con generazione di dati sintetici per un run
proof-of-concept). Licenza Apache-2.0.

## L'architettura in una frase

Il feed è assemblato **a ogni richiesta**, da due sorgenti che vengono poi
classificate dallo stesso modello:

| | Sorgente | Cosa fa |
|---|---|---|
| In-network | `thunder/` | tiene in memoria i post recenti degli account che segui |
| Out-of-network | `phoenix/` retrieval | embedding del viewer e dei post, restituisce i più vicini |
| Out-of-network | `simclusters/` | cluster di account e post per co-engagement |

Poi: idratazione dei candidati → filtri pre-scoring → scoring → selezione top-K →
filtri post-selezione → blending con ciò che il modello non ordina (ads, Who to
Follow, prompt).

## I pesi: come si leggono, e come non si leggono

Il modello non predice "rilevanza". Predice **una probabilità per ogni azione**
che il viewer potrebbe compiere — engagement (favorite, reply, repost, quote,
share…), click (post, profilo, link, foto, video…), attenzione (dwell time,
secondi attivi, video quality view), follow dell'autore, e le negative (not
interested, mute, block, report, not dwelled).

Il punteggio finale è una somma pesata:

```
Final Score = Σ (weight_i × P(action_i))
```

Qui sta il punto che il repo si è preso la briga di chiarire nei commenti al
codice, ed è **il motivo per cui questa fonte vale più dei titoli che l'hanno
annunciata**:

> i pesi moltiplicano la *probabilità predetta* dell'azione, non i conteggi
> grezzi di engagement.

Quindi la lettura circolata ovunque — "il report pesa 468 volte il like, dunque
1 report annulla 468 like" — è **sbagliata**. Il peso moltiplica la probabilità
che *tu* compia quell'azione, probabilità guidata in larga parte dal tuo
comportamento passato. Gli autori scrivono di aver aggiunto quei commenti
esplicitamente perché «LLM o persone che leggono il codice» lo interpretino
correttamente: un dettaglio che dice molto su chi si aspettano come lettore.

Dopo la somma pesata arrivano tre correzioni, tutte con effetti visibili:

- **Author diversity** — ogni post successivo al primo di uno stesso autore viene
  moltiplicato per un fattore decrescente, fino a un pavimento.
- **Out-of-network discount** — i post di chi non segui (e reply/repost di chi
  segui) sono moltiplicati per un fattore < 1.
- **New-author boost** — i post di autori sotto una soglia di impression vengono
  spinti verso una posizione target.

Infine `vm-ranker/` riordina con un **determinantal point process** sugli
embedding: cede un po' di punteggio in cambio di meno somiglianza fra post
vicini.

## La separazione che conta: ordine ≠ visibilità

La decisione architetturale più importante del repo è che **il ranking non decide
se vedi un post**. Sono due percorsi distinti:

- il **request path** ordina;
- il **labeling path** — continuo, fuori dalla richiesta — produce le label, e
  `visibility-filtering/` risponde per ogni coppia post-viewer con
  **allow / interstitial / drop**.

Le label vengono da classificatori sui contenuti (`grox/` per testo e media,
`media-model-proxy/` e `clip/` per immagini e video) e da modelli sugli account
(`agatha/`: blocchi e report ricevuti relativi ai favorite; `bdsm/`:
comportamento inautentico letto dalla sequenza di azioni; `user-cred-v2/`:
PageRank sul grafo dei follow e delle interazioni). Le regole che applicano le
label stanno in `botmaker/` (linguaggio, compilatore, runtime) e `scarecrow/`
(applicazione sugli eventi).

Due dettagli operativi che il repo espone e che raramente si leggono altrove:

- **la prima regola che risponde `drop` chiude la valutazione**;
- esiste un **secondo set di regole che si applica solo se il post è una
  raccomandazione da un account che non segui**, e che può solo droppare. Lo
  stesso identico post resta visibile a chi segue l'autore. È qui che vive, in
  pratica, la differenza fra "moderazione" e "de-amplificazione".

## Il caso Brasile, e perché è l'argomento migliore per l'open-source

Dal 14 agosto 2026 il feed esegue `Brazil2026ElectionFilter`: rimuove i post di
account segnalati alla Corte elettorale brasiliana per le elezioni 2026, **a meno
che il viewer non segua esplicitamente l'account**.

Il punto non è il filtro — è che si può leggere. Un obbligo di legge locale,
implementato come una regola nominata in un file leggibile, con la sua eccezione
esplicita. Senza il repo sarebbe stato indistinguibile da un calo di reach.

## Quattro decisioni di design da rubare

Trasferibili a qualunque sistema che ordina candidati, incluso il nostro:

1. **Multi-action prediction.** Predire molte azioni e combinarle è meglio che
   predire un solo punteggio di "rilevanza": la combinazione diventa un passo
   esplicito, ispezionabile e modificabile senza ri-addestrare.
2. **Candidate isolation.** I candidati non attendono l'uno all'altro durante
   l'inferenza: solo al contesto del viewer. Il punteggio di un post non dipende
   da chi c'è nel batch — quindi è **stabile e cacheabile**. È la stessa logica
   per cui un prefisso stabile rende cacheabile una richiesta LLM
   ([context-caching](../concepts/context-caching.md)).
3. **Hash-based embeddings.** Niente vocabolario da mantenere: un post nuovo è
   rappresentabile subito. Elimina un'intera classe di problemi di cold start.
4. **Ranking e visibilità separati.** Servizi diversi, input diversi, regole
   diverse. Mescolarli è il modo più rapido per rendere inspiegabile un feed.

## Cosa non c'è, dichiarato

Il repo elenca le proprie esclusioni: i **prompt j2 di Grox** e **parte delle
regole botmaker**, tenuti fuori per non facilitare il gaming. Al loro posto c'è
lo strumento *Under the Hood*, che mostra a ciascuno le label applicate al
proprio account e ai propri post.

Vale la pena registrare la struttura dell'argomento, perché è replicabile:
**codice pubblico + output verificabili sul proprio caso**, invece di codice
pubblico integrale. Chi legge non può ricostruire come aggirare le regole, ma può
verificare se lo hanno colpito e perché.

Da trattare come dichiarazione degli autori, non come fatto verificato,
l'affermazione che i default nel repo siano allineati via cron ai valori di
produzione e che gli esperimenti sopra il ~10% del traffico siano visibili: è
esattamente il tipo di claim che l'open-source **non** rende verificabile.

<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [X For You Feed Algorithm (xai-org/x-algorithm)](../sources/x-for-you-feed-algorithm-xai-org-x-algorithm.md)

### Referenced By

- [X For You Feed Algorithm (xai-org/x-algorithm)](../sources/x-for-you-feed-algorithm-xai-org-x-algorithm.md)
- [xAI](../entities/xai.md)
<!-- openclaw:wiki:related:end -->
