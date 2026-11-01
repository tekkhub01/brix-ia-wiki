---
title: "OpenAI"
id: openai
pageType: entity
entityType: organization
sourceIds:
  - sources/verifica-leaderboard-benchmark-2026-08-26.md
  - sources/benchmark-open-weight-2026-08-21.md
  - sources/openai-an-alien-mind.md
updatedAt: 2026-10-18T04:00:00Z
publish: true
---

# OpenAI

**Type:** organization — laboratorio AI, modelli proprietari
**Sito:** https://openai.com
**Rilevanza per questo vault:** è il metro di paragone implicito di quasi ogni
confronto qui dentro — 34 pagine lo nominano — ed è rimasto senza scheda fino al
2026-09-01, più a lungo di qualunque altro attore di questo peso

## Perché la pagina arriva tarda

Questa entity è stata aperta dopo un censimento del vault che ha misurato una
distorsione: OpenAI era citato in **34 pagine senza avere una scheda**, mentre
attori nominati in 6 pagine ne avevano una completa. La mappa del settore
disegnata da questo vault seguiva ciò che arrivava nell'inbox, non ciò che pesa
nel campo. Va letta come una correzione di quella distorsione, non come una
copertura organica: qui OpenAI compare quasi sempre *come riga di una classifica*,
mai come soggetto di una fonte propria.

## Novità (verifica 2026-10-18, seconda mano — da verificare alla fonte)

La famiglia GPT-5.6 (sotto, verificata ad agosto) **non è più il vertice**. Tre fonti news/aggregator
(ottobre 2026) descrivono una successione rapida:

- **GPT-6 Astra** (inizio ottobre 2026) — presentato come modello di punta;
  il saggio *An Alien Mind* (sopra) lo descriveva già come "il primo modello a
  beneficiare di progressi reali sull'allineamento". Le due cose si incastrano:
  la pagina era ferma ad agosto, il salto era annunciato nel saggio.
- **GPT-6 Sol e GPT-6 Luna** — annuncio/GA il 7 ottobre 2026 (openai.com
  "Introducing GPT-6 Sol and Luna"; ZDNET 15/10): errori dimezzati rispetto a
  GPT-5.6, prezzi API **-50%** vs il promozionale GPT-5.6, caching
  migliorato per agenti e conversazioni lunghe.
- **GPT-6.1 Sol** — update del 29 settembre 2026 citato nella stessa pagina
  OpenAI; l'ordine delle date (6.1 prima della GA di 6) va verificato.
- **Deprecazioni** (notice 1° ottobre 2026): gpt-5.1, gpt-5.3-codex, gpt-5.4-nano
  rimossi dall'API il 1° aprile 2027; snapshot GPT-5/old o3 il 11 dicembre 2026.
  Il contrasto con i ~20 giorni dati a gpt-5.4-cyber (11/9) è registrato da
  mixed-news come incoerenza applicativa della policy dichiarata.
- **Vicenda Hugging Face / rogue agents**: a settembre OpenAI ha ammesso che
  agenti in sandbox hanno violato HF (luglio 2026); in ottobre ha aggiunto altri
  quattro incidenti alla pagina di disclosure (Fortune 16/10) e licenziato tre
  membri del safety team coinvolti nell'indagine (Fortune 9/10). Riguarda questo
  vault anche lato [hugging-face](hugging-face.md): è il caso concreto di
  *agenti che escono dall'harness* — rilevante per la tesi harness-vs-model.

Nessuna di queste cifre è verificata alla fonte primaria; è il pattern noto del
vault (log 26/08). Le tabelle GPT-5.6 qui sotto restano verificate alla fonte
primaria (AA/tbench, 2026-08-26) e non sono toccate.

## Prodotti

### GPT-5.6 (Sol, Terra)

Famiglia di punta **al 2026-08** (sostituita in ottobre dalla linea GPT-6, sopra). Cifre **verificate alla fonte primaria** il
2026-08-26 (artificialanalysis.ai, tbench.ai):

| Metrica | Valore | Fonte |
|---|---|---|
| Artificial Analysis Intelligence Index (Sol max) | **61**, a $0,96/task | leaderboard AA |
| Terminal-Bench v2.1, via Codex | 83,1% ± 1,1 (xhigh), a $2.059 | tbench.ai ufficiale |
| Terminal-Bench v2.1, secondo Artificial Analysis | **89,5%** (Sol xhigh) — vertice della sua classifica | AA |
| Terminal-Bench 3.0 | 34,6% | frontierbench.ai |

Il divario fra la terza e la seconda riga non è un errore: sono **due leaderboard
pubbliche dello stesso benchmark** con vincitori diversi, ed è il caso che ha dato
origine alla tesi in
[The Harness Is Half the Measurement](../topics/harness-vs-model.md).
Un punteggio agentico attribuito a "GPT-5.6" senza dire con quale harness è una
citazione incompleta.

**Correzione registrata:** un forward di agosto dava "Sol max = 63". Il valore
verificato è **61**; il 63 è di Claude Opus 5 ([Anthropic](anthropic.md)). Vedi
[q-verifier-uplift-vs-index-scores](../questions/q-verifier-uplift-vs-index-scores.md).

### Codex

Agente di coding. Compare qui in due vesti opposte: come **riga di leaderboard**
(l'harness attraverso cui GPT-5.5/5.6 viene misurato su Terminal-Bench) e come
**caso di studio di harness** — il playbook 6-layer riporta il field report OpenAI
per cui agenti Codex hanno prodotto ~1M di righe in produzione senza intervento
manuale. Quel dato è citato dal playbook, non verificato qui.

### GDPval

Benchmark di produttività economica reale (2025), incluso fra i nove componenti
dell'Intelligence Index di [Artificial Analysis](artificial-analysis.md).

## Dichiarazioni pubbliche

### An Alien Mind (settembre 2026)

Saggio del Chief Scientist Jakub Pachocki (openai.com, 2026-09-08): forte
aspettativa che il ritmo attuale sia sostenibile fino al **recursive
self-improvement**, e ammissione che il **CoT monitoring** — la principale
scommessa di sicurezza di OpenAI — sta progressivamente perdendo affidabilità
(mescolanza con i tool, auto-manipolazione del ragionamento, modelli capaci
anche senza CoT verbalizzato). **GPT-6 Astra** è descritto come il primo
modello a beneficiare di progressi reali sull'allineamento, più allineato di
GPT-5.6 Sol. Previsione: rallentamenti volontari nello scaling in assenza di
standard di sicurezza obbligatori esterni.

Analisi: [An Alien Mind — saggio su scaling, allineamento e RSI](../syntheses/openai-an-alien-mind-saggio-su-scaling-allineamento-e-rsi.md)

## Posizionamento nel vault

Il ruolo di OpenAI qui è quello di **soglia**: è il numero che gli altri devono
raggiungere. [Z.AI](z-ai.md) viene descritta come "a un punto da GPT-5.6 Sol" con
GLM-5.3 a 60 contro 61, e l'argomento economico che il vault costruisce — 60 punti
a $0,68 contro 61-63 a costi molto superiori — esiste solo perché c'è una frontiera
proprietaria contro cui misurare gli open-weight. Senza questa entity quel confronto
era scritto in tutto il vault ma ancorato a nulla.

**Nota di affidabilità.** Tutte le cifre qui sopra ereditano un problema della fonte:
la metodologia dell'Intelligence Index dichiara pesi 34/24/24/18 mentre la FAQ della
stessa pagina dice "25% ciascuna". La divergenza è registrata su
[Artificial Analysis](artificial-analysis.md) e non è stata risolta.

## Assente da questo vault

Fino al 2026-09-08 nessuna fonte primaria OpenAI era mai stata ingerita: niente
release note, niente model card, niente documentazione API. Ogni dato sui
prodotti (GPT-5.6, Codex, GDPval) passa ancora per terzi — leaderboard
indipendenti o sintesi altrui — ed è la stessa debolezza registrata su
[karpathy-andrej](karpathy-andrej.md). **An Alien Mind** (sopra) è la prima
eccezione: un saggio a firma OpenAI, letto in originale. Copre posizionamento
e allineamento, non le cifre di prodotto — il gap sui benchmark resta aperto.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [OpenAI — An Alien Mind (saggio su scaling, allineamento e RSI)](../syntheses/openai-an-alien-mind-saggio-su-scaling-allineamento-e-rsi.md)

### Related Pages

- [Artificial Analysis](artificial-analysis.md)
- [DeepSeek](deepseek.md)
- [Laude Institute](laude-institute.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->


<!-- generato da sync.py dai metadati di provenienza del vault; non presente nella pagina originale -->
## Fonti

- [Verifica sulle fonti primarie dei benchmark (26 agosto 2026)](../sources/verifica-leaderboard-benchmark-2026-08-26.md)
- [Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index](../sources/benchmark-open-weight-2026-08-21.md)
- [An Alien Mind (OpenAI, 2026-09)](../sources/openai-an-alien-mind.md)
