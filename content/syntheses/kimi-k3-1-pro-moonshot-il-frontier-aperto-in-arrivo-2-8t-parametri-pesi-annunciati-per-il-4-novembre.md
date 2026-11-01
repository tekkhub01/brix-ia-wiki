---
pageType: synthesis
id: synthesis.kimi-k3-1-pro-moonshot-il-frontier-aperto-in-arrivo-2-8t-parametri-pesi-annunciati-per-il-4-novembre
title: "Kimi K3.1 Pro (Moonshot) — il frontier aperto in arrivo: 2,8T parametri,
  pesi annunciati per il 4 novembre"
sourceIds:
  - https://huggingface.co/moonshotai/Kimi-K3
  - https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5
  - telegram:brixia-newsletter/2026-11-01
claims:
  - text: "Kimi K3.1 Pro: MoE 2,8T parametri, KDA + Attention Residuals, visione
      nativa, contesto 1M token, thinking sempre attivo con reasoning_effort;
      famiglia K3 primo open 3T-class (luglio 2026)."
    status: supported
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://huggingface.co/moonshotai/Kimi-K3
        weight: 1
        note: model card HF verificata 2026-11-01
  - text: Sull'AA Index v5 Kimi K3.1 Pro è il migliore open weights a 46, con gap di
      12 punti dal leader (Opus 5.5 a 58); tra i pesi pubblicati DeepSeek V4.1
      Flash/GLM-5.3 a 32.
    status: supported
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5
        weight: 1
        note: articolo ufficiale AA via web_fetch 2026-10-30
  - text: "La newsletter #54 riporta 55 punti e 4° posto su 215 per K3.1 Pro: da
      riconciliare con il 46 della sintesi AA v5."
    status: unverified
    confidence: 0.4
    evidence:
      - kind: secondary
        sourceId: telegram:brixia-newsletter/2026-11-01
        weight: 0.3
        note: "cifra della bozza newsletter #54, in conflitto con il 46 verificato
          sull'articolo AA: potrebbe essere un altro effort setting o variante"
  - text: Pesi aperti annunciati per il 4 novembre 2026; licenza non ancora
      confermata; Moonshot ha documentato la rimozione deliberata di dati di
      attacco cibernetico dal training.
    status: reported
    confidence: 0.7
    evidence:
      - kind: web
        sourceId: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5
        weight: 0.7
questions:
  - "Riconciliare 55 (newsletter #54) vs 46 (verifica AA 30/10): quale
    versione/effort del punteggio è il 55?"
  - I pesi del 4/11 escono davvero? Con quale licenza (Apache? modificata?)
  - Kimi K3.1 Pro ha una valutazione AA v5 con pesi pubblicati dopo il rilascio
    del 4/11?
status: active
publish: true
updatedAt: 2026-11-01T13:53:18.018Z
---

# Kimi K3.1 Pro (Moonshot) — il frontier aperto in arrivo: 2,8T parametri, pesi annunciati per il 4 novembre

## Notes
<!-- openclaw:human:start -->
- Indice: AA Index v5 (K3.1 Pro a 46 verificato) · Chiuso competitor: [[syntheses/gemini-4-carbon-il-frontier-google-a-accesso-controllato-1-aa-v5-sota-cybersecurity-rollout-solo-cyber-defenders|Gemini 4 Carbon]] · Copertura: newsletter #54
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
Moonshot AI rilascia **Kimi K3.1 Pro** (23/10/2026): MoE da **2,8 trilioni di parametri**, contesto 1M token, prezzo API circa la metà di Claude Opus 5.5. Il punto non è il punteggio: è la data annunciata per i **pesi aperti, 4 novembre** — quando escono, il gap tra miglior modello aperto e miglior chiuso si riduce drasticamente.

## Cosa è
- Upgrade della famiglia K3 (primo open 3T-class, luglio 2026) orientato a ricerca finanziaria, modellazione 3D e coding
- Model card HF: `moonshotai/Kimi-K3` — 2,8T parametri, Kimi Delta Attention (KDA) + Attention Residuals, visione nativa, contesto 1M
- Thinking sempre attivo con `reasoning_effort` low/high/max
- Usato come base per modelli USA (Thinking Machines Inkling, Cursor Composer 2 — Wikipedia)

## Il punto sulla classifica (⚠️ da riconciliare)
La newsletter #54 riportava **55 punti, 4° su 215** sull'AA Intelligence Index v5. La sintesi vault verificata il 30/10 sull'articolo ufficiale AA indica **Kimi K3.1 Pro a 46** (pesi non pubblicati) con gap di 12 punti dal leader. Numeri incompatibili: o il 55 include un effort setting diverso, o si riferisce a un'altra variante. Regola già in vault: punteggio AA senza versione/effort/data non è usabile.

## Nota di cautela
Moonshot ha documentato di aver **rimosso deliberatamente dati di attacco cibernetico** dal training — primo laboratorio aperto a dichiararlo. Licenza dei pesi del 4/11 non ancora confermata.

## Lettura BRIX-IA
Se i pesi escono come annunciato, l'assunto "l'open source insegue di due anni" è finito. Per un'infrastruttura self-hosted diventa realistico un frontier locale per i carichi sensibili — con il caveat che 2,8T parametri sono da inference host, non workstation.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Anthropic S-1 — i primi numeri pubblici di un frontier lab: ticker ANT, $16,3 mld H1, utile operativo Q2](anthropic-s-1-i-primi-numeri-pubblici-di-un-frontier-lab-ticker-ant-16-3-mld-h1-utile-operativo-q2.md)
- [Gemini 4 Carbon — il frontier Google a accesso controllato: #1 AA v5, SOTA cybersecurity, rollout solo cyber defenders](gemini-4-carbon-il-frontier-google-a-accesso-controllato-1-aa-v5-sota-cybersecurity-rollout-solo-cyber-defenders.md)
- [Google "Sleep" framework — consolidamento offline dei modelli linguistici: BABILong a 10M token](google-sleep-framework-consolidamento-offline-dei-modelli-linguistici.md)
- [Idol (Speridlabs) — una foto diventa oggetto 3D Gaussian splats in 19 secondi, Apache 2.0](idol-speridlabs-una-foto-diventa-oggetto-3d-gaussian-splats-in-19-secondi.md)
<!-- openclaw:wiki:related:end -->
