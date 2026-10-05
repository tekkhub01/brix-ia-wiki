---
pageType: synthesis
id: synthesis.deepseek-harness-agent-harness-everything-is-a-plugin
title: DeepSeek Harness — Agent Harness "Everything is a Plugin"
sourceIds:
  - source.deepseek-harness-github
status: active
publish: true
updatedAt: 2026-08-17T14:32:14.384Z
---

# DeepSeek Harness — Agent Harness "Everything is a Plugin"

## Notes
<!-- openclaw:human:start -->
**Passata di armonizzazione 2026-08-26.** Fonte ingerita il 17/08 e rimasta
sospesa: nessuna entity per DeepSeek, blocco Related vuoto, nessun link in
entrata. Corretto `sourceIds` (mancava il prefisso `source.`, per questo il
Related non si popolava) e creata la scheda azienda.

**Nel corpus.** L'azienda è [DeepSeek](../entities/deepseek.md), che in questo
vault compare in tre ruoli insieme — fornitore dei modelli in produzione su
questo host, autore di questo harness, e soggetto dei benchmark di
[Artificial Analysis](../entities/artificial-analysis.md).

DSH entra nel **cluster agent-loop** già presente qui:
[Archon](../sources/archon-workflow-engine.md) come workflow engine,
[JCode](jcode-agente-di-coding-super-veloce.md) e
[Webwright](webwright-microsoft-browser-agent.md) come agenti verticali,
[Prime Agent](prime-agent-self-improving-rlm-agent-primeintellect-ai.md) come
loop auto-migliorante. DSH è l'unico dei cinque che dichiara come tesi
architetturale ciò che gli altri fanno di fatto: *tutto è un plugin*.

Il confronto che manca — e che è il motivo per cui la pagina resta interessante —
è **DSH vs OpenClaw**: stesso perimetro (modelli, tool, skill, sessioni, sandbox,
scheduling, UI), scelta opposta sul confine fra core e plugin. Nessuna fonte in
questo vault lo copre; da aprire come confronto quando ci sarà materiale di prima
mano invece di un annuncio.
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# DeepSeek Harness — Agent Harness "Everything is a Plugin"

## Cos'è
DeepSeek Harness (dsh) è un **harness per agenti AI** rilasciato da DeepSeek in developer preview il 2026-08-13, open source (licenza MIT, codice sorgente incluso). Principio dichiarato: *tutto è un plugin* — modelli, tool, skill, sessioni, sandbox, storage, loop, scheduling e la UI sono componenti intercambiabili e ricomponibili.

## Come funziona
- Architettura interna **Cordis**: permette di sostituire i componenti a piacimento.
- Schema: `qualunque modello + qualunque componente = agente pronto`.
- Sistema a plugin: un plugin può essere un modello, una sessione, uno skill, una sandbox o persino l'interfaccia.
- Avvio rapido: `npx @deepseek-ai/dsh web` (alternativa manuale: git clone + pnpm install + pnpm run build + pnpm dsh web). Richiede Node.js + pnpm.

## Verifica dati live (2026-08-17, 16:20 CEST)
Controllato via GitHub API e sito ufficiale: il post virale russo era sostanzialmente accurato, non fuffa.
- ⭐ **146.796 stelle** (created_at 2026-08-13) — il post diceva "130k in 3 giorni": confermato e già superato.
- 🍴 14.979 fork
- 🔌 Topic `dsh-plugin`: **6.576 repository** di plugin community (il post parlava di "6000 skill": confermato).
- Homepage ufficiale `deepseek.com/harness` (risponde 200, "Everything is a plugin").
- Org proprietaria: `deepseek-ai` (ufficiale).
- Nota: è un developer preview, non stable — aspettarsi bug e API che cambiano. `npx` esegue codice da npm (rischio supply-chain basso ma presente); per audit clonare il repo e leggere il codice.

## Rilevanza per BRIX-IA
Framework "harness" parallelo a OpenClaw + skill. Potenziale interesse per i membri tecnici della community; da monitorare per un confronto sul modello a plugin/agenti (DSH vs OpenClaw).

## Riferimenti
- GitHub: https://github.com/deepseek-ai/deepseek-harness
- Topic plugin community: https://github.com/topics/dsh-plugin
- Homepage ufficiale: https://deepseek.com/harness
- Lingua originale della segnalazione: russo (canale di aggregazione news AI)
- Data scoperta: 2026-08-17
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [deepseek harness github](../sources/deepseek-harness-github.md)

### Referenced By

- [Claude Code Tips (ykdojo) — le 5 skill più interessanti](claude-code-tips-ykdojo-le-5-skill-più-interessanti.md)
- [Deep Agents from Scratch — LangChain course](../sources/deep-agents-from-scratch.md)
- [DeepSeek](../entities/deepseek.md)
- [Due classifiche per lo stesso benchmark — perché un punteggio non è del modello](due-classifiche-per-lo-stesso-benchmark.md)
- [Harness Engineering — Agent = Model + Harness: The 6-Layer Production Playbook](../sources/harness-engineering-6-layer-playbook-2026.md)
- [Skill OpenClaw: progress-check (barre di avanzamento ASCII)](skill-openclaw-progress-check-barre-di-avanzamento-ascii.md)
<!-- openclaw:wiki:related:end -->
