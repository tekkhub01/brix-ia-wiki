---
pageType: source
id: source.benchmark-open-weight-2026-08-21
title: "Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index"
sourceType: local-file
sourcePath: /tmp/benchmark-open-weight-2026-08-21.md
ingestedAt: 2026-08-24T07:45:39.139Z
updatedAt: 2026-08-24T07:45:39.139Z
status: active
publish: true
---

# Benchmark open-weight 2026-08-21 — Terminal-Bench 2.1 e AA Intelligence Index

## Source
- Type: `local-file`
- Path: `/tmp/benchmark-open-weight-2026-08-21.md`
- Bytes: 4940
- Updated: 2026-08-24T07:45:39.139Z

## Content
## Benchmark open-weight che scalano la classifica (Terminal-Bench 2.1 + Artificial Analysis Intelligence Index)

### Source
- Origine: forward Telegram da un canale russo di aggregazione news AI, ricevuto 2026-08-21 (orario originale 06:00 UTC), lingua originale russa.
- Ingerita da file locale `benchmark-open-weight-2026-08-21.md` il 2026-08-24.
- Conversazione Telegram PK (msg #19824 e #19826), sintesi e take tecnico di Claudia (#19825 e #19827).

### Contenuto (traduzione IT)
Due forward dello stesso giorno raccontano lo stesso fenomeno: i modelli open-weight — e i trucchi di inferenza — stanno raggiungendo i top-tier a una frazione del costo. “L'efficienza sta mangiando il premium.”

#### 1. Terminal-Bench 2.1 (post #19824)
Testo originale (RU, forward):
> В Стэнфорде нашли способ сделать ИИ-агентов умнее без дообучения. LLM-as-a-Verifier предлагает модели сгенерировать несколько вариантов ответа, а потом самой же их проверить и выбрать самый удачный. И, как оказалось, это действительно работает! В эксперименте с DeepSeek V4 Flash результат на Terminal-Bench 2.1 поднялся с 79% до 88% — это выше, чем у Claude Fable 5. И да, при этом, по расчётам авторов, такой подход оказался примерно в 11 раз дешевле Fable 5 на задачу. Сам фреймворк бесплатный и опенсорсный.

Riassunto (Claudia, #19825): niente fine-tuning — la LLM genera più varianti di risposta, poi si fa da sé il verificatore e sceglie la migliore. Su Terminal-Bench 2.1 con DeepSeek V4 Flash: 79% → 88% di success rate, battendo “Claude Fable 5”. Costo per task stimato ~11x inferiore a Fable 5 (nel grafico allegato il confronto diretto con OpenAI/Anthropic dice “4x cheaper”). Framework open-source e gratuito.

#### 2. Artificial Analysis Intelligence Index (post #19826)
Testo originale (RU, forward):
> А вот чем действительно хочется пользоваться, так это GLM-5.3: модель набрала 60 пунктов в Artificial Analysis Intelligence Index, сравнявшись с Kimi K3 и уступив Sol max всего 1 балл. Выходит, что новый GLM силён не только в кодинге, но и в целом как умная модель. На практике это ощущается примерно так же.

Riassunto (Claudia, #19827): GLM-5.3 (max) — 60 punti sull'Artificial Analysis Intelligence Index, in pareggio con Kimi K3 e a -1 dal vertice (“Sol max” a 63). Non solo coding: il post dice che regge anche come modello “intelligente” in generale. La classifica nel grafico: Claude Opus 5 (max) 63 in testa, poi Claude Fable 5 e GPT-5.6 Sol, GLM-5.3 (max) 60 (evidenziato) pari a Kimi K3, giù fino a Command A+ a 23. L'indice fonde 9 eval (GDPval-AA v2, GPQA Diamond, ecc.).

### Fatti verificati (ricerca web 2026-08-24)
- **Terminal-Bench 2.1 è REALE**: benchmark agentico open-source (Laude Institute, Stanford, community) che valuta capacità agentiche in un terminale containerizzato (SWE, sysadmin, data, training, security). La v2.1 corregge 28/89 task della v2.0 e introduce validazione continua. DeepSeek V4 serie esiste (V4-Flash-0731 = 82.7, V4-Pro-0813 = 87.9 su TB2.1).
- **Artificial Analysis Intelligence Index è REALE**: metrica unificata di artificialanalysis.ai. La v4.1.1 fonde 9 eval: GDPval-AA v2, τ³-Banking, Terminal-Bench v2.1, SciCode, AA-LCR, AA-Omniscience, Humanity's Last Exam, GPQA Diamond, CritPt. Pesi: Agents 34%, Coding 24%, Scientific Reasoning 24%, General 18%. Al 22 ago 2026 Claude Opus 5 guida lo snapshot pubblico al 63.0%.
- **CAVEAT — nomi modello NON verificati**: i nomi esatti e gli score citati nel forward (DeepSeek V4 Flash 79→88%, “Claude Fable 5”, GLM-5.3=60, Kimi K3=60, “Sol max”=63, GPT-5.6 Sol, Command A+ a 23) NON compaiono in ricerca web e suonano come snapshot di modelli futuri/placeholder. La struttura dei benchmark è verificata; i numeri specifici vanno trattati come non verificati.

### Il filo conduttore (take di Claudia)
- Post 1: stessa performance dei top model a 11x-4x meno costo (via verifica, non fine-tuning).
- Post 2: modelli open-weight entrano in top-3 di “intelligenza” (GLM, Kimi).
- Sintesi newsletter: “L'efficienza sta mangiando il premium — come ottenere performance da fascia alta spendendo da fascia bassa”. Tema portante prossima puntata BRIX-IA.

## Notes
<!-- openclaw:human:start -->
**Passata di armonizzazione 2026-08-26.**

*Attribuzione corretta il 26/08.* La pagina era intitolata al canale Telegram
che aveva girato i due post, e il titolo lasciava intendere che il benchmark
fosse suo. Non lo è: quel canale è un **aggregatore di news**, non l'autore. Terminal-Bench 2.1 è del Laude
Institute con Stanford e community; l'Intelligence Index è di
[Artificial Analysis](../entities/artificial-analysis.md). Il canale resta citato
solo come *tramite* della segnalazione, senza nome.

*Doppio ingest.* Lo stesso materiale è entrato due volte a due minuti di distanza
(la copia alle 07:43, questa alle 07:45). Questa è la canonica; la copia è stata cancellata il 26/08 dopo aver
riportato qui i due "take" che questa versione aveva perso:
- Post 1 — pattern self-consistency / verifier-as-judge incapsulato in un framework
  pulito; il rapporto qualità/prezzo su task agentici è sbilanciato a favore dei
  modelli cheap.
- Post 2 — la linea GLM di [Z.AI (Zhipu AI)](../entities/z-ai.md) è storicamente
  fra le più solide in open-weight; un modello di quel livello è direzionalmente
  plausibile.

*Il CAVEAT sopra è sbagliato in parte, e va letto con questa correzione.* La
verifica del 24/08 dichiara "non verificati" i **nomi** dei modelli oltre che i
numeri. I nomi però sono verificabili senza uscire da questa macchina:
`openclaw.json` di questo host configura in produzione `deepseek/deepseek-v4-flash`,
`deepseek/deepseek-v4-pro`, `openai/gpt-5.6-sol` e `anthropic/claude-sonnet-5`
(vedi [DeepSeek](../entities/deepseek.md) e [Anthropic](../entities/anthropic.md)),
e la riga precedente dello stesso blocco ammette già che "DeepSeek V4 serie esiste"
con gli score TB2.1 — contraddicendo la riga dopo. Claude Opus 5 e Claude Fable 5
sono la famiglia Claude 5 di Anthropic, non placeholder.

**Resta non verificato solo il numero**: 79→88% via LLM-as-a-Verifier, GLM-5.3=60,
Kimi K3=60, "Sol max"=63, Command A+=23. Divergenza registrata, non risolta, in
[q-verifier-uplift-vs-index-scores](../questions/q-verifier-uplift-vs-index-scores.md).
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Artificial Analysis](../entities/artificial-analysis.md)
- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](../syntheses/artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [DeepSeek](../entities/deepseek.md)
- [Z.AI (Zhipu AI)](../entities/z-ai.md)
<!-- openclaw:wiki:related:end -->
