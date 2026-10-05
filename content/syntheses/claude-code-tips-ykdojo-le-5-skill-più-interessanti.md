---
pageType: synthesis
id: synthesis.claude-code-tips-ykdojo-le-5-skill-più-interessanti
title: Claude Code Tips (ykdojo) — le 5 skill più interessanti
sourceIds:
  - source.claude-code-tips-ykdojo-claude-code-tips
status: active
publish: true
updatedAt: 2026-08-27T09:40:10.769Z
---

# Claude Code Tips (ykdojo) — le 5 skill più interessanti

## Notes
<!-- openclaw:human:start -->
### Collegamenti nel vault
- [Anthropic](../entities/anthropic.md) — vendor di Claude Code; i costrutti del Tip 23 (skill/slash/plugin) sono suoi
- [DeepSeek Harness — everything is a plugin](deepseek-harness-agent-harness-everything-is-a-plugin.md) — stessa idea del plugin `dx`: capacità impacchettate, non hardcoded
- [Hermes Agent — skills hub (Nous Research)](hermes-agent-skills-hub-nous-research.md) — l'altro modello di distribuzione di skill già nel vault
- [Webwright — browser agent Microsoft](webwright-microsoft-browser-agent.md) — esempio di skill esterna integrata col pattern del Tip 23
- [Hardware per inferenza locale domestica](hardware-per-inferenza-locale-domestica-presente-e-futuro.md) — le macchine su cui far girare questi agenti
- [BRIX-IA](../entities/brix-ia.md) — stack interno a cui i 5 tip vengono mappati
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
Sintesi selettiva del repo [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) (tip per sfruttare Claude Code, dal base all'avanzato — **49 tip numerati** contati sul README il 28/08, mentre il titolo del repo dice ancora "45+": è il repo a sottostimarsi, divergenza registrata e non risolta). Il repo è una raccolta di **tip**, alcuni dei quali sono vere e proprie **skill** installabili (cartella `skills/`, es. `/handoff`, `/gha`) raggruppate nel plugin **`dx`** (Tip 44). Qui sotto le **5 più interessanti** dal punto di vista dell'agentic coding e dell'orchestrazione multi-agente che usiamo in BRIX-IA.

## Top 5 (per leva/non-ovvietà)

### 1. Tip 23 — CLAUDE.md vs Skills vs Slash Commands vs Plugins
Il modello mentale che tiene insieme tutto il resto. Distingue 4 livelli di configurazione/automazione:
- **CLAUDE.md** = istruzioni persistenti e contesto (cosa sei, come comportarti)
- **Skills** = capacità richiamabili on-demand (es. `/handoff`, `/gha`) — il nostro skill-system locale è lo stesso pattern
- **Slash Commands** = azioni pre-definite (`/compact`, `/copy`, `/remote-control`)
- **Plugins** = bundle di skill (il `dx` plugin impacchetta quelle del repo, no symlink)

**Perché interessa:** è la stessa architettura che abbiamo nel workspace (`SKILL.md` + `tool_search`). Utile per spiegare a PK come mappare le nostre skill sui costrutti nativi di Claude Code.

### 2. Tip 19 — Isolated environments per task rischiosi/lunghi
Eseguire Claude Code **dentro un container** (autore usa il preset [safeclaw](https://github.com/ykdojo/safeclaw)) con `--dangerously-skip-permissions` per sessioni autonome di ricerca/sperimentazione. Il container isola il filesystem e limita il blast radius.

**Perché interessa:** specchio esatto del nostro pattern orchestratore → delega a subagent isolati invece di eseguire noi stessi. La nota di sicurezza del repo è in linea con le nostre regole: mai eseguire operativo nel main thread, isolare ciò che è rischioso.

### 3. Tip 14 — Git worktrees per lavoro parallelo su branch
Un worktree = branch + directory dedicata. Permette di far girare **più istanze di Claude Code in parallelo** sullo stesso repo senza conflitti di working tree (es. main nel folder originale + feature-branch-1 in un folder nuovo).

**Perché interessa:** è il costrutto base per il multitasking agentico (la nostra regola "delega sempre, non eseguire mai" si appoggia su isolamento per-branch). Si combina con il Tip 32 (`--spawn=worktree`).

### 4. Tip 36 — Bash in background + subagent in background
- `Ctrl+B` sposta un comando bash lungo in background; Claude lo recupera dopo tramite `BashOutput`
- Si possono lanciare **subagent in background** per ricerca lunga o check periodici
- I subagent si customizzano: background vs foreground, e **modello** (Opus/Sonnet/Haiku a seconda della complessità; default Sonnet)
- Caso d'uso: codebase enorme → spawn di più subagent che analizzano parti diverse in parallelo

**Perché interessa:** è letteralmente il nostro pattern watchdog (mimo-flash in background per polling) e la regola "non bloccare la sessione principale con polling". Conferma che il pattern è una best practice consolidata, non una nostra eccentricità.

### 5. Tip 32 — Controllare Claude Code dal telefono (Remote Control)
`/remote-control` (o `/rc`) attacca il telefono a una sessione esistente; oppure `claude remote-control --spawn=worktree --capacity=N` per avviare **nuove** sessioni dal telefono, ciascuna col suo worktree. Si sposa con auto mode: kick off, vai via, ricontrolli da dovunque.

**Caveat di sicurezza (riportato dal repo):** chi prende il controllo della sessione ha di fatto accesso a tutto il computer → meglio disattivarlo quando non serve, **a meno che** non giri dentro un isolated environment (Tip 19), nel qual caso è comodissimo.

**Perché interessa:** remote orchestration + isolamento = combinazione che useremmo per far girare agenti BRIX-IA su macchine remote (es. LM Studio locale, server Xray) senza esporsi.

## Bonus non in top-5 ma rilevanti
- **Tip 8** — Compaction proattiva + **handoff document** (`HANDOFF.md`) per passare il contesto a un agente fresco: pattern che già applichiamo (write-test cycle, verify before spawn)
- **Tip 44** — Plugin `dx`: installa tutte le skill del repo in un colpo solo (no symlink)
- **Tip 47** — Usare GitHub come knowledge base (pattern wiki-as-source che rispecchia il nostro vault)

## Collegamenti con il nostro stack
- [Hardware inferenza locale domestica](hardware-per-inferenza-locale-domestica-presente-e-futuro.md) — i mini-PC/Apple sopra sono le macchine su cui girare questi agenti
- Pattern orchestratore (AGENTS.md): delega a subagent, isolation, no-polling-in-main-thread → validato dai Tip 19/36
- Skill system locale (`SKILL.md` + `tool_search`) ↔ Tip 23 (Skills vs Slash vs Plugins)

## Fonti
- Repo: ykdojo/claude-code-tips (48 tip) + cartella `skills/` + plugin `dx`
- safeclaw (preset container): https://github.com/ykdojo/safeclaw
- Docs Remote Control: https://code.claude.com/docs/en/remote-control
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Claude Code Tips (ykdojo/claude-code-tips)](../sources/claude-code-tips-ykdojo-claude-code-tips.md)

### Referenced By

- [Claude Code Tips (ykdojo/claude-code-tips)](../sources/claude-code-tips-ykdojo-claude-code-tips.md)
- [Skill OpenClaw: progress-check (barre di avanzamento ASCII)](skill-openclaw-progress-check-barre-di-avanzamento-ascii.md)
<!-- openclaw:wiki:related:end -->
