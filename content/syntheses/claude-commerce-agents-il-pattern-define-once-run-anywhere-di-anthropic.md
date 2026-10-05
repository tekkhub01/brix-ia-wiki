---
pageType: synthesis
id: synthesis.claude-commerce-agents-il-pattern-define-once-run-anywhere-di-anthropic
title: Claude Commerce Agents — il pattern define-once, run-anywhere di Anthropic
sourceIds:
  - source.anthropic-commerce-agents-github
status: active
updatedAt: 2026-09-04T11:11:44.854Z
publish: true
---

# Claude Commerce Agents — il pattern define-once, run-anywhere di Anthropic

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Claude Commerce Agents — il pattern define-once, run-anywhere di Anthropic

## Cos'è

Blueprint di riferimento (Apache 2.0, settembre 2026) di [Anthropic](../entities/anthropic.md) per costruire agenti di commercio su Claude: uno **shopping agent** embedded nello store (ricerca → confronto → piano → carrello → checkout) e un **merchant agent** per il back-office (analisi vendite, listing, scorte, pricing, campagne). Non è un prodotto: è un template da forkare — il repo non è mantenuto e non accetta contributi.

## Il pattern architetturale

Il punto chiave: ogni agente è definito **una sola volta** — prompt, skills (5 flussi a ruolo), contratti tool, gate — e gira su **tre runtime**:

- **Messages API** — il loop di riferimento, implementato dall'app host
- **Agent SDK** — l'SDK esegue il loop, stesso prompt/skills/tool
- **Managed Agents** — agente hostato che chiama il tuo MCP server

```
[Definizione: prompt + skills + tool contracts + gates]
     ├── runtime Messages API
     ├── runtime Agent SDK
     └── runtime Managed Agents (MCP)
```

## Modello di sicurezza

- **Niente write live**: il checkout passa la mano all'app host (il modello non vede mai l'URL); ogni modifica del merchant è *staged* e aspetta l'approvazione umana
- **Gate dentro la tool call**: fencing, provenance gates, cap, validazione memoria, approval gate — attivi su tutti e tre i runtime
- **Backend disaccoppiati**: `StorefrontBackend` / `MerchantBackend` chiamano i sistemi server-side con le credenziali dell'host; il modello legge solo il risultato
- **Switch `enable_*`**: un sistema che l'azienda non ha si spegne — tool, righe di prompt e regole di grounding vengono rimossi su tutti i path

## Perché è interessante

1. **Define once, run anywhere** — è il pattern che Anthropic sta imponendo per l'agentic commerce: stessa definizione, tre modi di eseguire
2. **Human-in-the-loop sui write** — staged changes + approval gate come standard di riferimento per agenti che toccano sistemi live
3. **Backend come interfaccia** — ordine dei passi e credenziali li applica il backend, non il modello
4. **Plugin Claude Code** — `/scaffold-commerce-agent` scaffolda un agente su questi pacchetti contro i tuoi sistemi (o ne revisiona uno esistente)

## Rilevanza per BRIX-IA

Il pattern è trasferibile a flussi non-commerce: un "merchant agent" che fa digest su dati gestionali interni con write staged e gated. Gli switch `enable_*` sono un design pulito per integrazioni parziali (sistemi mancanti → tool e prompt lines rimossi, non stub).

## Provenienza

- [Fonte: repo GitHub anthropics/commerce-agents](../sources/anthropic-commerce-agents-github.md)
- [Anthropic](../entities/anthropic.md)
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Claude Commerce Agents — Anthropic reference blueprint (GitHub)](../sources/anthropic-commerce-agents-github.md)

### Referenced By

- [Anthropic](../entities/anthropic.md)
<!-- openclaw:wiki:related:end -->
