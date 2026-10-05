---
pageType: source
id: source.deepseek-harness-github
title: deepseek harness github
sourceType: local-file
sourcePath: /tmp/deepseek-harness-github.md
ingestedAt: 2026-08-17T14:30:16.444Z
updatedAt: 2026-08-17T14:30:16.444Z
status: active
publish: true
---

# deepseek harness github

## Source
- Type: `local-file`
- Path: `/tmp/deepseek-harness-github.md`
- Bytes: 1918
- Updated: 2026-08-17T14:30:16.444Z

## Content
## DeepSeek Harness — Annuncio e verifica (GitHub)

**Source:** https://github.com/deepseek-ai/deepseek-harness
**Author:** DeepSeek (org deepseek-ai) + segnalazione via canale Telegram di aggregazione news AI (russo)
**Type:** Agent harness open source (developer preview)
**Category:** AI agents, plugin architecture, agent frameworks

---

### Claim originale (canale Telegram di news AI, 2026-08-17 13:01 UTC, russo)
- "Creiamo agenti AI dal nulla con DeepSeek: la neuronet ha lanciato l'ambiente agentico Harness, ora il repo in piu rapida crescita su GitHub."
- "In 3 giorni il progetto ha superato 130.000 stelle."
- Feature chiave: un plugin puo essere TUTTO (modelli, sessioni, skill, sandbox, persino la UI). Architettura su Cordis. Schema: qualunque modello + qualunque componente = agente pronto.
- Community: 6000 skill pronte. Topic: https://github.com/topics/dsh-plugin
- Install: git clone https://github.com/deepseek-ai/deepseek-harness -> cd deepseek-harness -> pnpm install -> pnpm run build -> pnpm dsh web
- Landing: https://deepseek.com/harness/en/ (quick-start npx @deepseek-ai/dsh web)

### Verifica live (Claudia, GitHub API + sito ufficiale, 2026-08-17 16:20 CEST)
- Repo deepseek-ai/deepseek-harness: pubblico, org ufficiale deepseek-ai, licenza MIT, codice sorgente incluso.
- 146.796 stelle (created_at 2026-08-13T11:56:32Z) — claim "130k in 3 giorni" confermato e superato.
- 14.979 fork
- Topic dsh-plugin: 6.576 repository community (claim "6000 skill" confermato).
- Homepage deepseek.com/harness risponde 200 ("Everything is a plugin").
- Nota: developer preview, non stable. npx esegue codice da npm (rischio supply-chain basso ma presente).

### Riferimenti
- GitHub: https://github.com/deepseek-ai/deepseek-harness
- Topic plugin: https://github.com/topics/dsh-plugin
- Homepage: https://deepseek.com/harness

## Notes
<!-- openclaw:human:start -->

### Update 2026-10-05 — desktop macOS/Windows (verifica via GitHub API)

Segnalazione INCUBE.AI (canale Telegram russo, 4/10): "DeepSeek ha rilasciato Harness per
macOS e Windows — alternativa aperta a Claude Code e Codex; l'agente può crearsi plugin da
solo in chat". Verificato alla fonte:

- **Sì, desktop macOS/Windows reale**: release `dsh-v0.2.0-rc.2` (29/9) integra il comando
  `dsh` nell'app desktop (gestione plugin senza installare Node/pnpm); fix dedicati su porte
  Windows riservate, sandbox PowerShell con diagnosi/riparazione permessi autorizzata,
  firma Node per macOS Intel. Ultima release `dsh-v0.2.1-alpha.1` (3/10) — **ancora alpha**.
- **Sì, self-creation di plugin**: `v0.2.1-alpha.1` aggiunge l'ingresso "fai creare il plugin
  all'agente" nella pagina di gestione plugin (bozza + esecuzione solo dopo invio richiesta).
  Nella stessa release: layer di compatibilità **sperimentale con Claude Code Mods** —
  dichiarato esplicitamente come verifica che le Mods siano un sottoinsieme del plugin API,
  non compatibilità reale. Lettura onesta: DeepSeek sta mappando il terreno, non promettendo
  migrazione.
- **No, "alternativa a Claude Code/Codex" è impreciso**: Harness resta provider-agnostic
  ("qualunque modello"), gira su account DeepSeek ma non sostituisce quelle CLI — le ospita
  affiancate: Orca lo lista tra i ~35 agenti che pilota. È un concorrente della *superficie*
  (desktop agent con workspace/file/terminal), non del motore.
- **Numeri**: 243.732 stelle (da 146.796 al 17/8 — +97k in ~7 settimane), push attivo 3/10.
- Contesto vault: è il filone desktop dell'architettura "Everything is a Plugin" già
  documentato nella sintesi collegata; per il confronto a tre con bb e Orca →
  [bb-agent-ide-github](bb-agent-ide-github.md) e [orca-ade-github](orca-ade-github.md).
  **Definizione formale delle Claude Code Mods ora in vault** (5/10):
  [claude-code-mods-docs-2026-10-05](claude-code-mods-docs-2026-10-05.md) — è il superset
  che il layer di compatibilità di DeepSeek dichiara di voler contenere.

<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [bb — The agent IDE that builds itself (GitHub get-bb/bb)](bb-agent-ide-github.md)
- [Claude Code Mods — plugin per personalizzare interfaccia e tool call (docs ufficiali)](claude-code-mods-docs-2026-10-05.md)
- [DeepSeek](../entities/deepseek.md)
- [DeepSeek Harness — Agent Harness "Everything is a Plugin"](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md)
- [Orca ADE — agente di orchestrazione per flotte di agenti paralleli (GitHub stablyai/orca)](orca-ade-github.md)
<!-- openclaw:wiki:related:end -->
