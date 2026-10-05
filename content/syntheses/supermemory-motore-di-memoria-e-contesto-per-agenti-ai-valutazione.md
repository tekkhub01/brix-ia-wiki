---
pageType: synthesis
id: synthesis.supermemory-motore-di-memoria-e-contesto-per-agenti-ai-valutazione
title: Supermemory — motore di memoria e contesto per agenti AI (valutazione)
sourceIds:
  - source.supermemory-fonti-verificate-2026-09-11
claims:
  - id: bench
    text: "Claim di #1 su LongMemEval, LoCoMo e ConvoMem con 95% Recall@15, 99.4%
      context reduction, profile ~50ms — numeri auto-dichiarati nel paper, non
      replicati indipendentemente"
    status: vendor-claimed
    confidence: 0.7
    evidence:
      - kind: source
        sourceId: source.supermemory-fonti-verificate-2026-09-11
        weight: 1
        note: README repo GitHub
  - id: selfhost
    text: "Self-hosted: singolo binario zero-config, graph engine embedded (nessun
      DB esterno), API server su localhost:6767, stessa API della piattaforma
      cloud"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: source
        sourceId: source.supermemory-fonti-verificate-2026-09-11
        weight: 1
        note: docs/self-hosting/overview
  - id: offline
    text: "Gira fully offline: LLM via endpoint OpenAI-compatible (Ollama/LM
      Studio/vLLM/llama.cpp), embeddings ONNX locali di default
      (bge-base-en-v1.5, 768d, inglese-only)"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: source
        sourceId: source.supermemory-fonti-verificate-2026-09-11
        weight: 1
        note: docs/self-hosting/embeddings
  - id: arch
    text: L'LLM configurato lavora sul write path (estrazione fatti, contraddizioni,
      decay); il read path è deterministico (vettori + graph traversal, nessun
      LLM)
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: source
        sourceId: source.supermemory-fonti-verificate-2026-09-11
        weight: 1
        note: "docs self-hosting: 'LLM keys power extraction and summarization'"
  - id: gaps
    text: Self-hosted rinuncia a connector (Drive/Gmail/Notion/OneDrive/GitHub) e
      MCP; qualità estrazione dipende dal modello fornito, non dai modelli
      proprietari cloud
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: source
        sourceId: source.supermemory-fonti-verificate-2026-09-11
        weight: 1
        note: tabella self-hosted vs platform nei docs
questions:
  - Quale modello embedding multilingue (bge-m3?) usare per memoria in italiano,
    e con quali dimensioni — da fissare prima di popolare il vector store
  - Reggerebbe il confronto con Mem0/Zep/Cognee/Graphiti su LongMemEval in una
    valutazione indipendente?
  - Integrabile come backend del memory stack OpenClaw, o resta un layer
    parallelo?
confidence: 0.85
status: draft
updatedAt: 2026-09-11T10:26:45.167Z
publish: true
---

# Supermemory — motore di memoria e contesto per agenti AI (valutazione)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Supermemory — valutazione strumento

> **Categoria:** AI memory / context engine · **Stato:** valutato, non testato · **Data valutazione:** 2026-09-11
> **Repo:** https://github.com/supermemoryai/supermemory · **Docs:** https://supermemory.ai/docs · **Licenza:** open source (self-host gratuito)

## 1. Cos'è
Layer di memoria e contesto per agenti AI: estrae automaticamente fatti dalle conversazioni, mantiene user profile, gestisce aggiornamenti temporali, contraddizioni e "forgetting" di info scadute. Include RAG ibrido, processazione file multi-modale (PDF, OCR immagini, trascrizione video, chunking AST-aware del codice) e connector verso Google Drive, Gmail, Notion, OneDrive, GitHub. SDK npm e pypi.

## 2. Claim benchmark (da verificare)
- #1 dichiarato su **LongMemEval**, **LoCoMo**, **ConvoMem**
- **95% Recall@15** con **99.4% context reduction**, user profile in **~50ms**
- ⚠️ Numeri auto-pubblicizzati nel loro research paper, non replicati da terzi. Trattare come marketing finché non c'è valutazione indipendente.

## 3. Architettura — i due percorsi
```
WRITE: conversazione grezza → [LLM: estrazione fatti, contraddizioni, decay] → grafo + vettori
READ:  query agente → [embeddings + graph traversal] → contesto   ← nessun LLM, deterministico
```
Punto chiave: l'LLM configurato **non serve alla ricerca** ma alla scrittura. Il valore del prodotto sta nella pipeline di estrazione/mantenimento automatica. Alternativa: estrazione lato agente e Supermemory solo come storage via `/v3/documents` — ma a quel punto decay/dedup/contraddizioni vanno reimplementati nel prompt dell'agente.

## 4. Self-hosting
- **Un binario, zero config**: `curl -fsSL https://supermemory.ai/install | bash` oppure `npx supermemory local`
- **Graph engine embedded** (nessun Neo4j/Postgres da provisionare), creato al primo boot
- API key generata automaticamente; server su `http://localhost:6767`, **stessa API del cloud** (`/v3/documents`, `/v4/search`, `/v4/profile`, spaces)
- Plugin per Claude Code / Codex / OpenCode puntabili in locale con `SUPERMEMORY_API_URL`
- **Cosa perde rispetto al cloud:** connector, MCP, modelli proprietari di estrazione (qualità benchmark)

### Modelli configurabili
| Livello | Opzioni |
|---|---|
| LLM (estrazione) | OpenAI, Anthropic, Gemini, Groq, o **qualsiasi endpoint OpenAI-compatible** → Ollama, LM Studio, vLLM, llama.cpp. Doc suggerisce `gpt-oss:20b` per uso locale |
| Embeddings | Default **ONNX locale** `Xenova/bge-base-en-v1.5` (768d, **inglese-only**), oppure OpenAI/Gemini, o Ollama/compatibile via `SUPERMEMORY_EMBEDDING_BASE_URL` |

Config env: `SUPERMEMORY_EMBEDDING_PROVIDER`, `SUPERMEMORY_EMBEDDING_MODEL`, `SUPERMEMORY_EMBEDDING_DIMENSIONS`, `SUPERMEMORY_EMBEDDING_BASE_URL`, `OPENAI_BASE_URL/API_KEY/MODEL`. Tuning workers: `SUPERMEMORY_LOCAL_EMBEDDING_POOL_SIZE`, `..._WASM_THREADS`.

### Vincoli tecnici rilevanti
- **Dimensioni embedding bloccate all'inizio**: il vector store non migra dopo il populate → scegliere il modello multilingue PRIMA di popolare
- Default embedding locale **debole su italiano**: serve modello multilingue (candidato: `bge-m3` via Ollama)
- Al primo boot in TTY chiede una LLM key **obbligatoria**; con Ollama la key è finta → flusso fully offline possibile (dati mai fuori dalla macchina)

## 5. Rilevanza per il nostro setup
- **Buco attuale:** MEMORY.md + daily notes + wiki gestiti a mano; contraddizioni e decay non risolti automaticamente
- **Cosa guadagnerebbe:** manutenzione automatica di fatti/contraddizioni/scadenza con grafo locale
- **Asset disponibili sul server:** Ollama → pipeline 100% on-box: graph embedded + embedding multilingue + LLM locale
- **Posizione presa:** engine completo (estrazione automatica con LLM locale), non solo-storage — è l'unico modo di guadagnare la gestione automatica delle contraddizioni

## 6. Checklist per confrontare strumenti simili
Criteri da riusare nella ricerca dei prossimi candidati (Mem0, Zep, Cognee, Graphiti, Letta/memGPT, ecc.):
1. **Self-host reale** vs cloud-only; effort di setup (DB esterni richiesti?)
2. **LLM agnostico** (endpoint OpenAI-compatible) o lock-in provider
3. **Graph + vector ibridi** o solo vettoriale
4. **Gestione contraddizioni/decay** automatica (write path) o appannaggio dell'agente
5. **Embeddings multilingue** supportati e migrazione dimensioni
6. **Benchmark indipendenti** (LongMemEval/LoCoMo/ConvoMem) replicati da terzi
7. API e integrazioni (MCP, SDK, plugin per coding agent)
8. Licenza e limiti della versione free

## 7. Prossimi passi
- [ ] Verificare modelli embedding multilingue già presenti in Ollama sul server
- [ ] Test locale: popolarlo con sessioni finte IT/EN, misurare qualità estrazione/contraddizioni
- [ ] Confronto diretto con almeno un'alternativa (Mem0 o Zep/Cognee) sulla stessa checklist

---
*Fonte primaria: Supermemory — fonti verificate 2026 09 11 (repo README + docs self-hosting, verificate il 2026-09-11).*
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

<!-- openclaw:wiki:related:end -->
