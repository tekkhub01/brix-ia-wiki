---
pageType: synthesis
id: synthesis.hardware-per-inferenza-locale-domestica-presente-e-futuro
title: Hardware per inferenza locale domestica — presente e futuro
sourceIds:
  - brix-ia-llm-locale-2026-guida-hardware-pmi
status: active
publish: true
updatedAt: 2026-08-27T09:01:16.748Z
---

# Hardware per inferenza locale domestica — presente e futuro

## Notes
<!-- openclaw:human:start -->
### Collegamenti nel vault
- [BRIX-IA](../entities/brix-ia.md) — destinataria della raccomandazione operativa
- [Qwen3.8 su Unsloth — scala hardware](qwen3-8-unsloth-inferenza-locale.md) — i modelli su cui si applicano queste fasce di VRAM
- [Qwen3.8-Flash-Next — MoE 125B a 75GB](qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md) — il caso frontier che alza l'asticella a 96-128 GB unified
- [Esperimenti quantizzazione Gemma 4 12B](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md) — verifica locale della regola ~0,6 GB/1B a Q4
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
Sintesi complementare alla [guida hardware PMI 2026](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md): qui il focus è l'uso **domestico** (casa, piccolo ufficio, hobbyist) e la **roadmap futura** (2026-2027), con enfasi su mini-PC e NPU oltre alle GPU da tavolo.

## Il principio fondamentale: VRAM / memoria unificata è tutto
Per l'inferenza LLM locale, la capacità di memoria (VRAM discreta o memoria unificata) è il fattore limitante #1. Regola pratica:
- ~0,6 GB per miliardo di parametri a Q4_K_M
- ~2 GB per miliardo a FP16

| Modello | VRAM @Q4 | VRAM @FP16 |
| 7B-14B | 8-12 GB | 14-28 GB |
| 27B-34B | 16-24 GB | 54-68 GB |
| 70B | 35-48 GB | 140 GB |
| 100B+ MoE | 24-60 GB | 200+ GB |

Shortage di memoria 2026 → i Mac con memoria preinstallata e le GPU usate (RTX 3090) sono i rapporti prezzo/GB migliori.

## Presente (disponibile ora)

### GPU discrete — massima flessibilità
- **RTX 5090** (32 GB GDDR7, Blackwell): singola GPU più veloce, gestisce 70B quantizzati. ~€2000+
- **RTX 4090** (24 GB): sweet spot storico, 30B-33B. Usata ~€1000
- **RTX 3090 usata** (24 GB): miglior rapporto VRAM/prezzo (~€500-700), 30B interi in VRAM
- **RTX 5060 Ti 16GB**: entry-level nuovo, 14B dense / 20B MoE
- **AMD Radeon AI Pro R9700** (32 GB), **Intel Arc Pro B70** (32 GB): alternative non-NVIDIA, ecosistemi ROCm/OpenVINO in maturazione

### Apple Silicon — memoria unificata come superpotere
- **Mac Mini M4 Pro 48GB** (~€1200): sweet spot domestico — 33B pieni, 70B degradata. Silenzioso, basso consumo
- **Mac Mini M4 16GB** (~€700): 7B-13B
- **M4 Max / M5 Max** (fino 128 GB): 70B+, 614 GB/s (M5)
- **M3 Ultra** (fino 256 GB, 800 GB/s): modelli frontier

Vantaggio: memoria unificata = niente overhead CPU↔GPU. Ottimizzato via MLX + llama.cpp.

### Mini-PC con NPU — la categoria "domestica" emergente
- **AMD Ryzen AI Max+ 395 (Strix Halo)**: 50 TOPS NPU + 128 GB LPDDR5X unificata, Radeon 8060S. Fino a ~200B parametri in memoria unificata
  - **ACEMAGIC M1A PRO+**, **Minisforum AI X1 Pro**, **Beelink GTR9 Pro**, **GEEKOM A9 Max**
- **Qualcomm Snapdragon X2 Elite**: 80-85 TOPS NPU, fino 128 GB — Windows on Arm maturo

NPU ≠ GPU: gli NPU eccellono per inferenza leggera/always-on (<13B), ma per modelli grandi serve GPU discreta o memoria unificata ampia.

### Il trigger di questa nota: Xiaomi entra nel segmento
Il messaggio originario citava i mini-PC AI Xiaomi. Xiaomi sta spingendo nel segmento con piattaforme XRING (SoC + acceleratore + NPU): segnale che i produttori consumer cinesi entrano nell'inferenza locale domestica. Da monitorare per disponibilità ed ecosistema software — per ora non un'alternativa matura in Occidente.

## Futuro (roadmap 2026-2027)

### NVIDIA
- **Rubin** (H2 2026): architettura successiva a Blackwell, efficienza inferenza migliorata
- **RTX Spark** (Grace Blackwell Spark): mini-PC Windows on Arm, 128 GB LPDDR5X unificata, atteso fine 2026

### Intel
- **Panther Lake** (Core Ultra 300, 2026): NPU ~50 TOPS, platform ~180 TOPS
- **Crescent Island**: acceleratore AI dedicato, cache maggiorate, FLOPS/watt ottimizzati

### AMD
- **Ryzen AI Max+ 495 (Gorgon Halo)** (Q3 2026): fino 192 GB memoria unificata
- **ROCm 7**: 3,5x inferenza vs ROCm 6

### Apple
- **M7** (fine 2027-2028, salta M6 Pro/Max): M7 Ultra progettata per ~1,5 TB memoria unificata, "drammaticamente superiore" per AI

## Raccomandazione operativa per BRIX-IA
- **Sweet spot domestico**: Mac Mini M4 Pro 48GB — silenzioso, zero driver, 33B a piena qualità
- **Budget/usato**: RTX 3090 24GB (~€600) — imbattibile per VRAM/€
- **Prototyping/Test**: Mini-PC AMD Strix Halo 128GB — 70B in memoria unificata senza GPU separata
- **Future-proof**: attendere Rubin (H2 2026) o Gorgon Halo (Q3 2026) per salti di capacità memoria

## Trend
1. Memoria = collo di bottiglia; shortage 2026 premia usato e Mac preconfigurati
2. NPU complementari alla GPU, non sostitutivi per LLM grandi
3. Mini-PC AI = compromesso forma-fattore/potenza; Strix Halo leader
4. Apple sfida il paradigma con memoria unificata
5. Produttori consumer (Xiaomi) entrano nell'inferenza locale domestica
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Come Usare un LLM in Locale nel 2026: Guida Hardware per PMI con Prezzi, Benchmark e 3 Fasce di Budget](../sources/brix-ia-llm-locale-2026-guida-hardware-pmi.md)

### Referenced By

- [BRIX-IA](../entities/brix-ia.md)
- [Claude Code Tips (ykdojo) — le 5 skill più interessanti](claude-code-tips-ykdojo-le-5-skill-più-interessanti.md)
- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant](../sources/l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant.md)
- [NVIDIA](../entities/nvidia.md)
- [Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)](qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md)
<!-- openclaw:wiki:related:end -->
