---
pageType: synthesis
id: synthesis.qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram
title: Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)
sourceIds:
  - source.qwen3-8-flash-next-how-to-run-locally-unsloth
status: active
publish: true
updatedAt: 2026-08-27T09:04:30.686Z
---

# Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)

## Notes
<!-- openclaw:human:start -->
### Collegamenti nel vault
- [Alibaba](../entities/alibaba.md) — rilascia la famiglia Qwen
- [Unsloth](../entities/unsloth.md) — autore dei quant e della documentazione usata come fonte
- [Qwen3.8 su Unsloth — scala hardware](qwen3-8-unsloth-inferenza-locale.md) — il modello *diverso* con cui non va confuso
- [Hardware per inferenza locale domestica](hardware-per-inferenza-locale-domestica-presente-e-futuro.md) — le macchine che reggono i 75-112 GB richiesti
- [Esperimenti quantizzazione Gemma 4 12B](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md) — l'altra serie KLD/top-1 del vault, per confronto metodologico
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
Sintesi della documentazione Unsloth per **Qwen3.8-Flash-Next** (non confondere con Qwen3.8-27B: vedi [scala hardware Qwen3.8](qwen3-8-unsloth-inferenza-locale.md)). Qui il focus è: è un modello **frontier-size** che *può* girare in casa su memoria unificata/discreta ampia, senza GPU VRAM dedicata.

## Cos'è (dati fonte, da verificare indipendentemente)
- **Modello:** open-weight, **125B parametri MoE**, multimodale, architettura **Qwen4**
- **Contesto:** 262.144 token (262K)
- **Claim Unsloth:** "supera Claude-4.6-Opus (Max)" — **NON verificato** nel vault, trattato come affermazione del produttore
- **Claim Unsloth:** gira localmente su **75 GB RAM/unified memory, no GPU VRAM richiesta** — plausibile per il quant 1-bit, ma il vantaggio "RAM vs VRAM poco differente" è una caratteristica architetturale rivendicata, non misurata qui

## Scala memoria (tabella fonte — unità = memoria totale RAM+VRAM o unificata)
| 1-bit | 2-bit | 3-bit | 4-bit | 5-bit | 8-bit | BF16 |
|---|---|---|---|---|---|---|
| **75 GB** | 79 GB | 90 GB | 112 GB | 200 GB | 270 GB | 355 GB |

Il quant 1-bit è **più grande del solito** (75 GB vs i ~70 attesi per 125B) perché i nuovi layer **Ngram / PLE** (per-layer embeddings, tipo lookup table) non vengono quantizzati aggressivamente (minimo 4-bit). Costa più spazio, ma trattiene più accuratezza: il 1-bit **UD-IQ1_S (72,5 GB)** ritiene **80,2%** di top-1 (KLD 0,375). Si possono **offloadare Ngram/PLE su SSD via mmap** per risparmiare RAM/VRAM.

## Quantization analysis (tabella fonte)
| quant | size_gb | mean_kld | same_top_pct |
|---|---|---|---|
| UD-Q4_K_XL | 111,3 | 0,0447 | 93,5% |
| UD-IQ4_XS | 93,7 | 0,0792 | 91,1% |
| UD-Q3_K_XL | 90,0 | 0,0997 | 90,4% |
| UD-IQ3_XXS | 82,0 | 0,1565 | 87,6% |
| UD-Q2_K_XL | 78,9 | 0,2133 | 85,2% |
| UD-IQ1_M | 74,5 | 0,3022 | 82,4% |
| UD-IQ1_S | 72,5 | 0,3751 | 80,2% |

1-bit = **79% più piccolo** di BF16 (355 GB), ritiene 80% top-1. Confronto utile con la regola del vault (~0,6 GB/1B a Q4): qui a Q4 servono 112 GB per 125B → **0,9 GB/1B**, cioè *più* del tipico per via dei layer Ngram/PLE non compressi.

## Perché è rilevante per l'inferenza "domestica"
- È il primo caso nel vault di un modello **frontier-size (125B MoE)** che Unsloth dichiara eseguibile su **memoria unificata/discreta** (Mac, DGX Spark) senza VRAM GPU dedicata
- Abbassa la soglia: **96 GB unified** (Mac Studio M4 Max / M3 Ultra, o mini-PC Strix Halo/Gorgon Halo futuri) bastano per il quant 1-bit
- Si incastra con la [roadmap hardware domestica](hardware-per-inferenza-locale-domestica-presente-e-futuro.md): i Mac 128 GB e i mini-PC 192 GB (Gorgon Halo) diventano macchine frontier-locali

## Settings raccomandati (fonte)
Modello **hybrid thinking**; default `reasoning_effort=xhigh`.
| Param | Thinking | Instruct |
|---|---|---|
| temperature | 1.0 | 0.7 |
| top_p | 0.95 | 0.80 |
| top_k | 20 | 20 |
| presence_penalty | 0.0 | 1.5 |
| repetition_penalty | 1.0 | 1.0 |

`reasoning_effort`: xhigh (default) / medium / low / none. **Preserve Thinking** mantiene la traccia di ragionamento fra i turni (più token, più accuratezza su conversazioni lunghe).

## Caveat / domande aperte
1. I claim di superiorità su Claude-4.6-Opus e di "prestazioni RAM≈VRAM" sono **non verificati** nel vault — servirebbe un benchmark indipendente
2. Serve la **llama.cpp PR #27742** (specifica Unsloth) per l'esecuzione — non è mainline al momento della stesura
3. 125B MoE a 1-bit su sola RAM sarà lento (throughput CPU-bound) — la "frontier a casa" è realistica per qualità, meno per velocità
4. Discrepanza da segnalare: il vault aveva Qwen3.8-27B (17-19 GB Q4, 256K). Flash-Next è un modello *diverso* (125B, Qwen4, 262K), non un drop-in upgrade

## Riferimenti
- Sintesi esistente: [Qwen3.8 su Unsloth — scala hardware](qwen3-8-unsloth-inferenza-locale.md)
- Hardware domestica: [Hardware inferenza locale domestica](hardware-per-inferenza-locale-domestica-presente-e-futuro.md)
- Fonte: Unsloth Docs — Qwen3.8-Flash-Next (web)
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Qwen3.8-Flash-Next — How to Run Locally (Unsloth)](../sources/qwen3-8-flash-next-how-to-run-locally-unsloth.md)

### Referenced By

- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [Hardware per inferenza locale domestica — presente e futuro](hardware-per-inferenza-locale-domestica-presente-e-futuro.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)
- [Qwen3.8-Flash-Next — How to Run Locally (Unsloth)](../sources/qwen3-8-flash-next-how-to-run-locally-unsloth.md)
<!-- openclaw:wiki:related:end -->
