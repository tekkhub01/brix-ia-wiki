---
pageType: synthesis
id: synthesis.decision-model-jev-e-l-ecosistema-open-source-laya-von-kev-jevlike
title: "Decision model: Jev e l'ecosistema open source (Laya, von, kev, jevlike)"
sourceIds:
  - source.wiki-jev-typesafe
claims:
  - text: "Laya: 421M ModernBERT-large, Apache 2.0, p50 32.8ms vs Jev 236-276ms;
      zero-shot 0.362, 0.766 solo fine-tuned"
    confidence: 0.85
    evidence:
      - kind: web
        path: https://huggingface.co/convaiinnovations/laya
        note: model card ufficiale
      - kind: web
        path: https://aiweekly.co/alerts/convai-ships-laya-a-421m-modernbert-decision-model-apache-20
        note: sintesi con numeri
  - text: von sub-15ms, kev su Qwen3.5, jevlike come libreria di training,
      CUA-S1-FORMS 706K parametri specialista form
    confidence: 0.8
    evidence:
      - kind: web
        path: https://github.com/wfzyx/von
      - kind: web
        path: https://github.com/jaredpalmer/kev
      - kind: web
        path: https://github.com/yibie/awesome-jev
        note: lista curata, verificata 22/09
  - text: "Demo minecraft-agent: Astra planner + Jev controller, 8'43\", <$1, open
      source"
    confidence: 0.95
    evidence:
      - kind: web
        path: https://github.com/rmalde/minecraft-agent
      - kind: web
        path: https://x.com/rronak_/status/2101544156757950697
questions:
  - "Nessuna riproduzione indipendente dei benchmark Laya-vs-Jev: chi la fa?"
  - kev (decoder Qwen3.5 tiny) regge il confronto di latenza con gli encoder?
confidence: 0.8
status: active
updatedAt: 2026-09-22T12:20:01.498Z
publish: true
---

# Decision model: Jev e l'ecosistema open source (Laya, von, kev, jevlike)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Decision model: Jev e l'ecosistema open source

**Aggiornamento 2026-09-22** — stato dell'arte verificato su fonti primarie. Fonte della ricerca originale: `sources/wiki-jev-typesafe.md` (20-21/09).

## Jev (TypeSafe AI) — promemoria
API chiusa, nessun paper/weights/dataset. Decision model non autoregressivo: stato + domande tipate → probabilità calibrate (choice/score/noul) in 70-500 ms. Pricing ~$0.042/M input, output gratis.

## Le alternative open source (verificate 22/09)
| Progetto | Cosa | Numeri chiave |
|---|---|---|
| **Laya** (Convai/NandakishorM) — huggingface.co/convaiinnovations/laya | Replica diretta: ModernBERT-large 421M, Apache 2.0, 3 checkpoint (EN, multilingue, typed-decisions), router linguistico integrato | p50 32.8 ms su T4 vs 236-276 ms di Jev dichiarato; ⚠️ zero-shot typed-decisions 0.362 (quasi casuale), 0.766 solo con fine-tuning; multilingue MASSIVE macro-avg 0.227 → copertura senza accuratezza |
| **laya-mlx** (aac6fef) / **laya-GGUF** (mys) | Port community: MLX per Apple Silicon (no PyTorch), GGUF via ggmlc (4/8/16-bit, NON llama.cpp) | Stessi pesi upstream, runtime nativi |
| **von** (github.com/wfzyx/von) | Decision model sub-15 ms, non autoregressivo, drop-in locale | Il più veloce dichiarato della famiglia |
| **jevlike** (github.com/vinnylarouge/jevlike) | Libreria di TRAINING per costruire jev-like propri (N opzioni → N probabilità in un pass) | Base usata da CUA-S1-FORMS |
| **CUA-S1-FORMS** | Specialistissimo: 706K parametri, 2.8 MB, scorer FILL/CHECK/CLICK/SKIP su form | 99.7% sul suo eval vs 83.6% di Jev — specialista in casa sua, non vittoria generale |
| **kev** (github.com/jaredpalmer/kev, 21/09) | Famiglia tiny jev-like costruita **sopra Qwen3.5**, allenabile e eseguibile in proprio | Terza via: decoder piccoli invece di encoder |
| **awesome-jev** (github.com/yibie) | Lista curata di progetti/integrazioni su Jev | Mappa dell'ecosistema |

## Demo di riferimento (20/09)
**github.com/rmalde/minecraft-agent** — Ronak Malde: GPT-6 Astra pianificatore (1 chiamata/15 s) + Jev controllore + 11 righe di codice per i reflex = Ender Dragon battuto in 8'43", <$1 ($0.96 Astra + $0.01 Jev). È il caso di scuola del pattern "jev engineering": LLM scrive, decision model decide, codice esegue. Il pianificatore scriveva anche nuove regole per Jev dopo i fallimenti (self-improvement senza retraining).

## Lettura operativa (conferma decisione PK 21/09)
- La categoria è legittima, il prodotto chiuso non serve: **self-host resta la via**.
- CANDIDATO 1: Laya fine-tunato (serve GPU ~1 GB VRAM) per triage email gaia@ e routing report FF — ma i numeri zero-shot sono quasi casuali: il valore sta nel fine-tuning, non nel download.
- CANDIDATO 2: jevlike o kev per addestrare un decisore nostro sui dati nostri (pipeline FF/Xray).
- Da tenere d'occhio: CUA-S1-FORMS dimostra che uno specialista da 2.8 MB batte Jev sul suo terreno → per task stretti (smistamento PDF, routing) il modello piccolo dedicato è la scelta giusta.

**Caveat**: tutti i benchmark cross-prodotto (Laya vs Jev) sono auto-riportati dalle parti in causa; a oggi nessuna riproduzione indipendente.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

<!-- openclaw:wiki:related:end -->
