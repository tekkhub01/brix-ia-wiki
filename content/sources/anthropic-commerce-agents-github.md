---
id: source.anthropic-commerce-agents-github
pageType: source
title: "Claude Commerce Agents — Anthropic reference blueprint (GitHub)"
updatedAt: 2026-09-04T00:00:00Z
publish: true
---

# Claude Commerce Agents — Anthropic reference blueprint (GitHub)

**Date:** settembre 2026 (repo letto il 2026-09-04)  
**Source URL:** https://github.com/anthropics/commerce-agents  
**Author:** Anthropic  
**Type:** Reference implementation (Apache 2.0) — non è un prodotto  
**Introduced via:** richiesta PK (post video INCUBE.AI, tradotto e ripubblicato su Telegram)

## Cos'è

Due agenti di commercio costruiti su Claude, definiti **una sola volta** (prompt + skills + contratti tool + gate) e fatti girare su **tre runtime**: Messages API (loop di riferimento), Agent SDK, Managed Agents (agente hostato che chiama il tuo MCP server).

## I due agenti

| Agente | Ruolo | Flussi |
|---|---|---|
| **Shopping agent** | Si embedda nello store: ricerca, confronto, piano, carrello, checkout, policy; ricorda quello che il cliente gli dice | 5 skills (`shopping-agent/skills/`) |
| **Merchant agent** | Back-office: analisi vendite, listing, alert scorte/ordini, pricing/promozioni, campagne | 5 skills (`merchant-agent/skills/`) |

## Modello di sicurezza (la parte che conta)

- **Niente write live**: il checkout passa la mano all'app host (il modello non vede mai l'URL); ogni modifica del merchant è *staged* e aspetta l'approvazione umana
- **Gate dentro la tool call**: fencing, provenance gates, cap, validazione memoria, approval gate — attivi su tutti e tre i runtime
- **Backend disaccoppiati**: `StorefrontBackend` / `MerchantBackend` chiamano i sistemi server-side con le credenziali dell'host; il modello legge solo il risultato
- **Integrazioni target**: analytics (Snowflake, BigQuery, Databricks, Amplitude), finanza (Stripe, Square, PayPal, QuickBooks), delivery (Slack, Google Drive, Gmail)

## Le quattro verticali pronte

Retail, travel, telecom ed entertainment — ognuna con storefront + admin portal, tutte su dati fittizi (ACME). Python 3.11+ e Node 22:

```bash
git clone https://github.com/anthropics/commerce-agents.git && cd commerce-agents
pip install -r requirements.txt && cp .env.example .env   # aggiungi ANTHROPIC_API_KEY
python scripts/run_demo.py retail                        # API :8000 + storefront :3000
```

## Il plugin per Claude Code

```bash
claude plugin marketplace add anthropics/commerce-agents
claude plugin install commerce-builder@claude-commerce-agents
/scaffold-commerce-agent a shopping assistant for our store
```

`/add-commerce-flow`, `/author-commerce-evals` e `/review-commerce-agent` completano il ciclo.

## Punti architetturali chiave

1. **Define once, run anywhere** — lo stesso agente (prompt/skills/tool/gate) su tre runtime
2. **Human-in-the-loop sui write** — staged changes + approval gate come standard di riferimento
3. **Backend come interfaccia** — il modello non tocca mai i sistemi: passa dai metodi del backend, che applicano ordine dei passi e credenziali
4. **Reference, non dipendenza** — Apache 2.0, non mantenuta, non accetta contributi: template da forkare, non libreria da importare
5. **Switch `enable_*`** — un sistema che l'azienda non ha si spegne: ne vengono rimossi tool, righe di prompt e regole di grounding su tutti i path

## Note

- Repo di riferimento: non mantenuto, non accetta contributi
- Gli esempi non hanno autenticazione e gli MCP server bindano su loopback
- `docs/safety.md` elenca ogni regola applicata con modulo e path; `docs/backends.md` guida il mapping dei sistemi; `docs/deployment.md` copre Vertex AI, Bedrock, Foundry e gateway

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Anthropic](../entities/anthropic.md)
- [Claude Commerce Agents — il pattern define-once, run-anywhere di Anthropic](../syntheses/claude-commerce-agents-il-pattern-define-once-run-anywhere-di-anthropic.md)
<!-- openclaw:wiki:related:end -->
