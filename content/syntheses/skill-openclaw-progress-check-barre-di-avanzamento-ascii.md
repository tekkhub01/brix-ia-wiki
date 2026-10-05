---
pageType: synthesis
id: synthesis.skill-openclaw-progress-check-barre-di-avanzamento-ascii
title: "Skill OpenClaw: progress-check (barre di avanzamento ASCII)"
sourceIds:
  - source.progress-check-skill-tjcages-skills
confidence: 0.6
status: tip
publish: true
updatedAt: 2026-08-27T15:07:22.103Z
---

# Skill OpenClaw: progress-check (barre di avanzamento ASCII)

## Notes
<!-- openclaw:human:start -->
### Collegamenti nel vault
- [Claude Code Tips (ykdojo) — le 5 skill più interessanti](claude-code-tips-ykdojo-le-5-skill-più-interessanti.md) — stesso ecosistema `npx skills add` e stessa distinzione skill/plugin del Tip 23
- [Hermes Agent — skills hub (Nous Research)](hermes-agent-skills-hub-nous-research.md) — l'altro canale di distribuzione di skill censito nel vault
- [DeepSeek Harness — everything is a plugin](deepseek-harness-agent-harness-everything-is-a-plugin.md) — la capacità come plugin installabile invece che cablata nell'agente
- [BRIX-IA](../entities/brix-ia.md) — l'agente su cui la skill andrebbe eventualmente installata
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
Tip di comunità (inoltrato da @tips_ai su Telegram, 2026-08-27) su uno skill OpenClaw esterno.

**Cosa fa:** aggiunge barre di avanzamento ASCII all'output dell'agente, aggiornate man mano che il task procede.

**Cosa dice davvero la fonte** (SKILL.md, letta il 28/08 — due claim del forward Telegram non reggono):
- Non parla di "3–7 checkpoint": dice *"define a small set of observable milestones before estimating a percentage"*, pesate **per lavoro e rischio, non per tempo trascorso**. Il numero 3–7 non compare nella fonte ed è verosimilmente del forward, non della skill
- Non è vero che il tempo non conta: l'aggiornamento di routine parte **solo dopo almeno 30 minuti** *e* in più deve valere una fra — milestone completata, progresso verificato salito di ≥10 punti percentuali, oppure prossima azione cambiata in modo sostanziale. Il tempo è condizione **necessaria ma non sufficiente**, non è escluso
- Regole di output: massimo tre voci per aggiornamento (evidenza completata, lavoro corrente, prossimo passo o blocco), **una sola barra complessiva**; mai ripetere una barra invariata né mandare "still working"; nel multi-agente la barra la mostra **solo il coordinatore**

**Installazione:**
```shell
# forma globale, quella documentata nella fonte
npx skills add tjcages/skills --skill progress-check -g --agent '*'
```
(il forward riportava la variante senza `-g --agent '*'`; la fonte documenta solo l'installazione globale)

**Sorgente / repo:** https://github.com/tjcages/skills/tree/main/progress-check/skills/progress-check

Fonte primaria ora nel vault e claim verificati contro di essa (28/08); la skill resta **non testata** su questo ambiente. Utile come ispirazione per dare feedback di progresso strutturato all'utente invece di spin lunghi e opachi.
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [progress-check — skill (tjcages/skills)](../sources/progress-check-skill-tjcages-skills.md)

### Referenced By

- [progress-check — skill (tjcages/skills)](../sources/progress-check-skill-tjcages-skills.md)
<!-- openclaw:wiki:related:end -->
