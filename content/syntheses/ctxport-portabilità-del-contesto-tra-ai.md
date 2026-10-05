---
pageType: synthesis
id: synthesis.ctxport-portabilità-del-contesto-tra-ai
title: CtxPort — portabilità del contesto tra AI
sourceIds:
  - source.ctxport-nicepkg-github
confidence: 0.92
status: active
publish: true
updatedAt: 2026-08-23T08:37:34.976Z
---

# CtxPort — portabilità del contesto tra AI

## Notes
<!-- openclaw:human:start -->
**Passata di armonizzazione 2026-08-26.** La pagina era una diade sigillata:
citava solo la propria fonte e nessuna pagina la citava. Collegata al corpus qui
sotto; corretto anche `sourceIds`, che era scritto senza il prefisso `source.` e
per questo non produceva nessun blocco Related.

**Nel corpus.** L'autore è [nicepkg](../entities/nicepkg.md). CtxPort sta
all'estremo opposto di
[Headroom](headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md):
Headroom **comprime** il contesto dentro l'agente per farcelo stare, CtxPort lo
**estrae** e lo porta su un altro agente. Stesso vincolo — la finestra come
risorsa scarsa — due mosse opposte; vale la pena tenerle vicine invece di
sceglierne una, perché rispondono a domande diverse (durata vs portabilità).

Il flusso "genero sul modello economico, verifico sul premium" che questa pagina
propone come rilevanza è esattamente il pattern misurato — e non ancora
verificato nei numeri — in
[Artificial Analysis Intelligence Index e i suoi 9 benchmark](artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
e in [DeepSeek](../entities/deepseek.md). CtxPort è il tubo che lo rende
praticabile a mano.

Nota di formato: il Context Bundle è **Markdown con frontmatter**, cioè già la
forma che questo vault ingerisce. È la scorciatoia più corta fra una
conversazione e una fonte con la sua provenienza.
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# CtxPort — portabilità del contesto tra AI

## Cos'è
CtxPort è un'estensione browser open-source (MIT, Chrome MV3) che copia intere conversazioni da servizi AI in un "Context Bundle" — un documento Markdown strutturato con frontmatter — pronto da incollare in un altro AI, nei propri appunti o in una PR. Repository: https://github.com/nicepkg/ctxport

## Come funziona
- Navighi su una piattaforma supportata (ChatGPT, Claude, Gemini, DeepSeek, Grok, Doubao, GitHub)
- Clicchi il pulsante di copia CtxPort che appare nella chat (o premi Alt+Shift+C)
- Incolli il Context Bundle ovunque ti serva

Tutto il parsing avviene nel browser: zero upload, 100% locale, nessun account, funziona offline.

## Formati di export
| Formato | Cosa contiene | Ideale per |
|---|---|---|
| Full | Conversazione completa | Trasferimento di contesto tra AI |
| User Only | Solo i tuoi messaggi (prompt) | Riusare i prompt in un altro AI |
| Code Only | Solo i blocchi di codice con linguaggio | Estrarre snippet di implementazione |
| Compact | Messaggi condensati in un paragrafo | Condivisione rapida in chat/email |

Ogni bundle include frontmatter (source, url, title, date, nodes, format) che dice a qualsiasi tool ricevente da dove arriva, quando e quanto è lungo.

## Piattaforme supportate
ChatGPT, Claude, Gemini, DeepSeek, Grok, Doubao (豆包), GitHub Issues & PRs

## Funzionalità chiave
- In-Chat Copy Button
- Sidebar List Copy (copi dalle conversazioni nella sidebar senza aprirle — utile per raccoglierne 5 per un brief di progetto)
- Keyboard Shortcut Alt+Shift+C
- Multiple Formats (Full, User Only, Code Only, Compact)

## Stato (2026-08-23)
- Chrome Web Store release: in arrivo
- Firefox support: in arrivo
- Context Bundle import (incolla un bundle per ripristinare il contesto): in sviluppo
- Batch export (selezioni multiple conversazioni): in sviluppo

## Relevanza per noi
È il "tubo" pratico che mancava al discorso di oggi su efficienza AI: i modelli economici (DeepSeek, GLM, Kimi) stanno raggiungendo i top-tier, e CtxPort permette di spostare il lavoro da uno all'altro senza ricopiare a mano. Flusso concreto: generi su un modello cheap, porti il contesto su uno premium solo per verificare (LLM-as-a-Verifier), e risparmi sul serio. Utile anche per rimbalzare tra i limiti degli account free.

## Riferimenti
- GitHub: https://github.com/nicepkg/ctxport
- Docs: https://ctxport.xiaominglab.com/
- Licenza: MIT
- Scoperto: 2026-08-23 (forward Telegram da un canale di aggregazione news AI del 2026-08-21, lingua originale russo)
- Non confondere con "Context Portal (ConPort)", un MCP server database-backed — progetto diverso.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [ctxport nicepkg github](../sources/ctxport-nicepkg-github.md)

### Referenced By

- [Artificial Analysis Intelligence Index e i suoi 9 benchmark](artificial-analysis-intelligence-index-e-i-suoi-9-benchmark.md)
- [nicepkg](../entities/nicepkg.md)
<!-- openclaw:wiki:related:end -->
