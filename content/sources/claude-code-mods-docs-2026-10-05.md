---
pageType: source
id: source.claude-code-mods-docs-2026-10-05
title: "Claude Code Mods — plugin per personalizzare interfaccia e tool call (docs ufficiali)"
sourceType: web
url: https://code.claude.com/docs/en/plugins/mods/overview
date: 2026-10-05
tags: [source, harness, claude-code, plugins, anthropic]
ingestedAt: 2026-10-05T12:41:00Z
updatedAt: 2026-10-05T12:41:00Z
status: active
publish: true
---

# Claude Code Mods — la superficie dell'harness diventa estendibile

**Source:** https://code.claude.com/docs/en/plugins/mods/overview (docs ufficiali, fetch 2026-10-05)
**Annuncio:** post X @ClaudeDevs 2105721434807083061 (secondo mano, via INCUBE.AI 5/10 — non verificato il tweet, verificata la documentazione)
**Richiede:** Claude Code **v2.1.287+**, attive di default

## Cosa sono

Un **mod è un plugin che cambia come Claude Code appare e si comporta**: handler di eventi in
JavaScript/TypeScript che girano **dentro il processo di Claude Code** — questa è la differenza
dai settings hooks (comandi shell / HTTP / prompt che girano fuori) e da MCP server (processi
esterni che danno tool). Il handler viene chiamato su un evento (tool call, prompt inviato,
parte dell'interfaccia disegnata) e può **osservare, riscrivere o prendere in carico** l'evento.

Cinque capacità dichiarate:
1. **Disegnare interfaccia** — un pannello accanto al transcript o una banda sopra il prompt,
   con tab, bottoni, campi testo (il claim della segnalazione "mini-giochi sopra la finestra
   del prompt" ricade qui: la banda sopra il prompt è una primitive ufficiale).
2. **Ridisegnare l'interfaccia propria di Claude Code** — riga di tool call, spinner, dialoghi.
3. **Intervenire su tool call o richieste** — trattenere una tool call per fare una domanda,
   rispondere senza eseguire il tool, instradare una richiesta a un modello diverso.
4. **Comandi che eseguono codice proprio**, senza turno di Claude, anche mentre Claude lavora.
5. **Dati condivisi tra hook** — stato nel modulo (es. contatore tool call mostrato nello spinner).

## Il punto di sicurezza (la parte che il post Telegram non dice)

Il docs hanno un warning esplicito e dettagliato: **"A mod is code that runs with your
permissions"**. Una volta caricato, un mod può: leggere/scrivere file ovunque possa il tuo
utente, avviare processi, fare richieste di rete; **leggere i tuoi segreti** (variabili
d'ambiente e settings file, incluse API key); vedere ogni prompt e ogni tool call; **riscrivere
prompt e tool call, inviare prompt spacciandoli per tuoi, mandare messaggi ad altre tue
sessioni**; **approvare tool call senza chiedertelo** — incluse quelle che una regola `ask`
avrebbe mostrato o che un tuo `PreToolUse` hook aveva bloccato (può arrivare ad approvare
quanto una regola `deny` rifiuta, con dettagli nella pagina admin); consumare il tuo piano.
**Non sono sandboxati**: se attivi il sandboxing di Claude Code, i processi avviati dal mod
girano fuori dal sandbox. Unico confine durevole: il mod può ridisegnare quasi tutto tranne
**il permission prompt** — non può cambiare cosa mostra a te.

Mitigazioni previste: `claude plugin validate <dir>` elenca `hooks:` e `calls:` **senza eseguire**
(il vincolo che rende l'audit possibile: un hook può agire sul mondo solo via mods API),
`--safe-mode`, `disableAllHooks`, e per le organizzazioni `allowManagedModsOnly`.

## Dove girano

Terminal e Code tab di Desktop: hook + disegno. VS Code chat panel, `claude -p`, Agent SDK,
cloud session: **hook sì, disegno no**. WSL: niente plugin. Un mod che disegna può rilevare
l'ambiente e degradare a testo.

## Sample ufficiali (anthropics/claude-code-playground, claude-code/mods)

- `token-weather` — forecast della context window sopra il prompt
- `blast-radius` — **trattiene comandi rischiosi (`rm -rf`, force push) e mostra cosa cambierebbe**,
  con procedi/annulla: è il pattern guard del punto 3 applicato alla sicurezza
- `replay-theater` — `/replay` che ripercorre le modifiche file dell'ultimo turno
Condivisione "as-is", senza supporto.

## Rilevanza per il vault

È la risposta di Anthropic al filone "harness come prodotto" documentato in questo vault, vista
dal lato opposto rispetto a [bb](bb-agent-ide-github.md) e
[DeepSeek Harness](deepseek-harness-github.md): lì l'harness si estende costruendo (bb) o con
plugin propri (Harness "everything is a plugin"); qui **la superficie dell'harness ufficiale
diventa essa stessa un'API** — UI, tool call routing e modello per-request sono riscrivibili.

Chiude un anello aperto il 5/10: DeepSeek ha aggiunto il 3/10 un layer di compatibilità
sperimentale "Claude Code Mods" dichiarando di voler verificare che le Mods siano **un sottoinsieme
del proprio plugin API**. Ora la definizione del superset è in vault: il claim di DeepSeek è
verificabile — le capacità 1–5 sopra sono tutte riscrivibilità in-process dell'host, che un
modello "plugin = tutto" (modelli, sessioni, sandbox, UI) può in principio contenere; il punto
di attrito è il confine di sicurezza (il permission prompt non ridisegnabile, `validate`
statico) che Harness non dichiara equivalente.

Per [harness-vs-model](../topics/harness-vs-model.md): i mods cambiano
l'harness *a runtime e per-utente* — un benchmark "Claude Code" corso con mods diversi non è
lo stesso harness. Ricade nel problema delle [due classifiche](../syntheses/due-classifiche-per-lo-stesso-benchmark.md).

## Ecosistema community (ricercato il 5/10)

- **[awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods)** —
  catalogo indipendente di **1.744 mod pubblici** scansionati da GitHub (scan 4/10), con
  l'output di `claude plugin validate` per ciascuno: cosa può leggere/scrivere/eseguire/inviare
  in rete. È la risposta pratica al problema dei permessi: browse su mods.aidojo.si.
- **Mod ufficiali built-in**: Anthropic usa i mod per features proprie (/diff, supporto
  AGENTS.md) — la superficie pubblica e quella interna sono lo stesso meccanismo.
- **`next-steps`** (marketplace `anthropics/claude-plugins-community`) — suggerisce cosa fare
  dopo ogni turno, incluso scegliere skill e comandi.
- Mod community notevoli (per stelle/capacità): **token-optimizer** (alexgreensh, 2.5k —
  "ghost tokens", sopravvivenza alla compaction), **ctx-handoff-mod** (cablate — handoff
  automatico a conversazione fresca a soglia di contesto), **claude-flightdeck** (scasella —
  dashboard live contesto/costo — **codice analizzato il 5/10: osservatore puro**, ogni hook
  passa l'evento invariato, zero rete/processi/file, redaction credenziali in `redact()`, MIT,
  il miglior candidato da provare per primo), **prismantis** (reply tematizzate con tabelle/grafici),
  **terminal-browser** (zenbu-labs — browser nel terminale), **claude-pokemon-mod** (il
  "gioco sopra il prompt" del post russo è un mod reale), **glass** (look da desktop-app).
  **OneWave-AI/claude-code-mods**: 10 mod MIT con 155 test, orientati guardrail.
- Annuncio: post @ClaudeDevs 1/10 (non 5/10 — la segnalazione INCUBE era in ritardo di 4
  giorni); Boris Cherny: "non c'è motivo per cui l'esperienza di Claude di tutti debba
  essere identica".

## Riferimenti

- Docs: https://code.claude.com/docs/en/plugins/mods/overview (più le pagine /interface, /events, /api, /admin, /create)
- Playground: https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods
- Annuncio: https://x.com/ClaudeDevs/status/2105721434807083061 (secondo mano)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [deepseek harness github](deepseek-harness-github.md)
<!-- openclaw:wiki:related:end -->
