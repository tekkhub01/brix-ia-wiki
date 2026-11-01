---
pageType: synthesis
id: synthesis.decision-model-jev-e-l-ecosistema-open-source-laya-von-kev-jevlike
title: "Decision model: Jev e l'ecosistema open source (Laya, von, kev, jevlike)"
sourceIds:
  - source.wiki-jev-typesafe
  - source.wiki-jev-1-14-2026-10-16
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
  - text: "Benchmark indipendente (Eugene Pro AI, 30 task, 10 livelli): Laya locale
      risponde in ≤200 ms ma sbaglia su confidenza calibrata e azioni
      distruttive (casi 11, 16, 26, 27, 30); Jev cloud più preciso — conferma la
      lettura 'self-host con fine-tuning, non download diretto'."
    confidence: 0.8
    evidence:
      - kind: url
        sourceId: youtube:kCqNB4pg_5s
        note: "video 26:54 del 2026-10-02; dettagli nella sintesi 'Benchmark decision
          model: 30 task locale vs cloud'"
questions:
  - "Nessuna riproduzione indipendente dei benchmark Laya-vs-Jev: chi la fa?"
  - kev (decoder Qwen3.5 tiny) regge il confronto di latenza con gli encoder?
confidence: 0.8
status: active
updatedAt: 2026-10-22T15:10:18.376Z
publish: true
---

# Decision model: Jev e l'ecosistema open source (Laya, von, kev, jevlike)

## Notes
<!-- openclaw:human:start -->
**Che cos'è un decision model:** modello non autoregressivo che riceve stato + domande tipate e restituisce probabilità calibrate (choice/score) in pochi ms — non genera testo, decide. Categoria introdotta da Jev (TypeSafe); ecosistema open source mappato in questa pagina.

**Benchmark indipendente 30 task (locale vs cloud):** [[syntheses/benchmark-decision-model-30-task-locale-vs-cloud-eugene-pro-ai|Benchmark decision model: 30 task locale vs cloud (Eugene Pro AI)]] — Laya locale veloce ma meno calibrata; conferma la lettura self-host + fine-tuning.
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

## Aggiornamento 2026-10-16 — Jev 1.14: immagini, tipo box, long context
Fonte verificata: `sources/wiki-jev-1-14-2026-10-16.md` (blog + docs TypeSafe, 16/10).
- **jev-1.14.0** (14/10): miglioramenti ovunque, gains maggiori su multilingua. `jev-latest` passerà a 1.14 dopo ~1 settimana.
- **Immagini** (`TypeSafe-Danger-Zone-Images: true`): 1.13 "era multimodale da sempre". Assets referenziabili in state/instructions/criteria. PNG/JPEG, 280–1568 px, max 16 MiB. Ogni riferimento ripetuto riconta i token.
- **Tipo `box`** (solo 1.14): bounding box + confidence — prima primitiva non-decisionale.
- **Long context** (`TypeSafe-Danger-Zone-Long-Context: true`): 64k/32k → 262k per-request E per-question, stesso prezzo, più lento e meno accurato.
- **Prezzi confermati**: $0.042/Mtok input, output gratis; immagini allo stesso tariffario, ma la guida per stimare i token-immagine è "soon" → il calcolo community "$0.0001 a immagine" non è ufficiale.
- **Caveat TypeSafe**: tutto "danger zone", multimodale peggiore del testo puro, esplicitamente non production-ready.
- **Impatto sulla nostra decisione**: nessuna variazione — self-host resta la via. Da ri-valutare il pattern "dov'è X in immagine" solo quando i flag escono dal danger zone e la tokenizzazione immagini sarà documentata.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources


### Referenced By

- [Benchmark decision model: 30 task locale vs cloud (Eugene Pro AI)](benchmark-decision-model-30-task-locale-vs-cloud-eugene-pro-ai.md)
<!-- openclaw:wiki:related:end -->
