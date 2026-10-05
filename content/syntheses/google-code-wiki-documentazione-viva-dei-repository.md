---
pageType: synthesis
id: synthesis.google-code-wiki-documentazione-viva-dei-repository
title: Google Code Wiki — la documentazione come wiki ricompilata
sourceIds:
  - source.google-code-wiki-interactive-repo-documentation-nov-2025
claims:
  - text: Code Wiki mantiene per ogni repository un wiki strutturato che viene
      rigenerato a ogni cambiamento del codice, e usa quel wiki come base di
      conoscenza per una chat Gemini.
    confidence: 0.9
    evidence:
      - kind: url
        sourceId: source.google-code-wiki-interactive-repo-documentation-nov-2025
        confidence: 0.9
        note: annuncio ufficiale Google Developers Blog, 2025-11-13
  - text: Code Wiki (nov 2025) implementa la sintesi-a-write-time su codice cinque
      mesi prima del post di Karpathy (apr 2026) che in questo vault è registrato
      come origine del pattern LLM-wiki.
    confidence: 0.75
    evidence:
      - kind: url
        sourceId: source.google-code-wiki-interactive-repo-documentation-nov-2025
        confidence: 0.9
        note: data di pubblicazione dell'annuncio
confidence: 0.85
status: active
updatedAt: 2026-08-26T00:00:00Z
publish: true
---

# Google Code Wiki — la documentazione come wiki ricompilata

## Notes
<!-- openclaw:human:start -->
Pagina scritta nella passata di armonizzazione del 2026-08-26. La fonte era
ferma dal 17/08 senza sintesi, senza entity e senza un solo link in entrata.
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Cos'è

**Code Wiki** è una piattaforma di [Google](../entities/google.md) — annunciata
sul Developers Blog il **13 novembre 2025**, in public preview su
`codewiki.google` — che mantiene per ogni repository un **wiki strutturato e
continuamente aggiornato**, al posto di file di documentazione statici.

Tre proprietà dichiarate:

| Proprietà | Cosa significa in pratica |
|---|---|
| Automatica e sempre aggiornata | scansiona l'intera codebase e **rigenera** la documentazione dopo ogni cambiamento |
| Context-aware | il wiki *intero e corrente* è la base di conoscenza di una chat Gemini integrata: non parli con un modello generico, ma con uno che conosce il repo da capo a fondo |
| Integrata e azionabile | ogni sezione e ogni risposta è iperlinkata ai file e alle definizioni che cita; genera anche diagrammi di architettura, classi e sequenza sempre allineati al codice |

In arrivo (dichiarato): un'estensione **Gemini CLI** per far girare lo stesso
sistema in locale sui repo privati — il caso, dice l'annuncio, dove la
documentazione manca di più, perché "l'autore originale del codice potrebbe non
essere più disponibile".

## Il punto che emerge incrociando le fonti

Questo vault registra il pattern "wiki compilata da un LLM" come **pattern di
Karpathy**, datato al post e al gist del **4 aprile 2026**
([LLM Wiki (Karpathy Pattern)](../concepts/llm-wiki-karpathy.md)):
abbandonare il retrieval a query-time in favore della **sintesi a write-time**,
su tre strati — raw immutabile, wiki di proprietà dell'LLM, schema di proprietà
dell'umano.

Code Wiki spedisce esattamente quel meccanismo — sorgenti immutabili (il codice),
wiki rigenerata dall'LLM, agente che risponde *dalla wiki* e non dalle sorgenti —
**cinque mesi prima**, come prodotto pubblico. La differenza non è l'idea: è
l'ambito. Karpathy generalizza il pattern a qualsiasi corpus e lo lascia a chi
legge; Google lo restringe a un corpus dove il layer "raw" ha una proprietà rara —
il codice è **verificabile in modo automatico e cambia con un evento discreto**
(il commit) che può fare da trigger della ricompilazione.

Vale la pena registrarlo senza risolverlo: non c'è evidenza in nessuna delle due
fonti che l'una conosca l'altra. Il pattern sembra essere stato inventato due
volte perché il vincolo — finestre di contesto che non reggono un repository —
era lo stesso per entrambi.

## Code Wiki, CodeGraph e questo vault

Tre risposte alla stessa domanda ("come faccio a non far rileggere il codice
all'agente a ogni sessione?"), che divergono su *cosa* si pre-compila:

| Sistema | Cosa produce | Dove gira | A chi parla |
|---|---|---|---|
| **Code Wiki** (Google) | prosa + diagrammi, iperlinkati al codice | hosted (locale "in arrivo" via Gemini CLI) | umani, e una chat Gemini |
| [**CodeGraph**](codegraph-pre-indexed-code-knowledge-graph.md) | knowledge graph di simboli, chiamanti, chiamati (Tree-sitter → SQLite) | 100% locale | agenti, via MCP |
| **Questo vault** | pagine Markdown con claim, provenienza, link | locale | agenti e umani |

La divergenza interessante è fra le prime due. CodeGraph misura il proprio valore
in **token risparmiati** (−57%, −71% di tool call): pre-compila la *struttura*,
che un agente sa già interrogare. Code Wiki pre-compila la *spiegazione*, che un
agente dovrebbe altrimenti generare — e il costo di generarla non compare
nell'annuncio. Sono ottimizzazioni di due voci di spesa diverse, e nessuna delle
due fonti confronta la propria con l'altra.

## Perché ci interessa

1. **Il trigger di ricompilazione.** È la cosa che a questo vault manca: qui la
   ricompilazione è un gesto umano ("armonizza la wiki"), là è un evento del
   sistema. Il sintomo si vede a occhio: questa stessa fonte è rimasta sospesa
   nove giorni — ingerita il 17/08, senza sintesi né link fino al 26/08 — perché
   nessun commit la reclamava.
2. **Il precedente industriale.** Se il pattern che regge questo vault ha una
   implementazione Google in public preview, la domanda "vale la pena mantenerlo
   a mano?" ha una risposta empirica là fuori, non solo un'intuizione qui dentro.
3. **Il caso repo privati.** L'estensione Gemini CLI annunciata copre esattamente
   lo scenario [BRIX-IA](../entities/brix-ia.md): codice interno, autore non più
   disponibile, onboarding lento.

## Riferimenti

- Annuncio: [Introducing Code Wiki](https://developers.googleblog.com/introducing-code-wiki-accelerating-your-code-understanding/) — Google Developers Blog, 2025-11-13
- Prodotto: `codewiki.google` (public preview)
- Autori dell'annuncio: Fergus Hurley, Pedro Rodriguez, Rafael Marques (Google Cloud, Developer & Experiences), Omar Shams (Google Research)
- Segnalata via forward Telegram da un canale di aggregazione news AI il 2026-08-17, ingerita lo stesso giorno
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Google Code Wiki — Interactive repo documentation (Nov 2025)](../sources/google-code-wiki-interactive-repo-documentation-nov-2025.md)

### Referenced By

- [Google](../entities/google.md)
<!-- openclaw:wiki:related:end -->
