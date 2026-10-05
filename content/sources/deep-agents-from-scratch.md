---
pageType: source
id: source.deep-agents-from-scratch
title: Deep Agents from Scratch — LangChain course
sourceType: local-file
sourcePath: https://github.com/langchain-ai/deep-agents-from-scratch
ingestedAt: 2026-09-01T13:57:28.173Z
updatedAt: 2026-09-01T13:57:28.173Z
status: active
publish: true
date: 2026-09-01
url: https://github.com/langchain-ai/deep-agents-from-scratch
tags: [ai-agents, langgraph, react, sub-agents, research-agent, course]
---

# Deep Agents from Scratch — LangChain course

## Source
- Type: `local-file`
- Origine: https://github.com/langchain-ai/deep-agents-from-scratch
- Autore: LangChain (langchain-ai), licenza MIT
- Provenienza: forward Telegram (canale INCUBE.AI), inviato da PK il 2026-09-01
- Updated: 2026-09-01T13:57:28.173Z

## Content

Corso di LangChain per costruire agenti AI avanzati "from scratch" su LangGraph.
5 notebook che fanno crescere progressivamente la complessità dell'agente:
da un semplice ciclo ReAct a un research-agent completo.

### Pattern affrontati
- **ReAct base**: reasoning + action (loop pensiero/azione)
- **Planning**: TODO list con stati delle task
- **Context offloading**: spostare il contesto su una virtual filesystem (scrivi/recupera)
- **File I/O**: lettura, scrittura e editing di file
- **Sub-agent delegation**: delegare task a sub-agent
- **Parallel specialized agents**: agenti specializzati che lavorano in parallelo

### Interesse / rilevanza (nota Claudia)
I pattern descritti (task planning, context offloading su filesystem virtuale,
sub-agent delegation, parallel specialized agents) rispecchiano esattamente
l'architettura che Claudia usa già nell'orchestratore OpenClaw:
- delega a sub-agent MiMo / mimo-flash per le pipeline lunghe
- spostamento del contesto su file invece di tenerlo tutto nel prompt

Differenza: loro lo ricostruiscono da zero su LangGraph, noi lo abbiamo "gratis"
nell'orchestratore. Utile come riferimento per capire *cosa* succede sotto il cofano
e per un eventuale confronto LangGraph Deep Agents vs OpenClaw/Claudia.

### Quickstart (dal README)
- Prerequisiti: Python 3.11+, [`uv`](https://github.com/astral-sh/uv)
- Installazione: istruzioni nel [README del repo](https://github.com/langchain-ai/deep-agents-from-scratch#readme)

### Diagramma (dal README)
LLM interagisce con 4 tool: Plan, Offload Context (Write/Retrieve),
Sub-Agent, Custom Tools / MCP.

### Link esterni
- Repo: https://github.com/langchain-ai/deep-agents-from-scratch
- Canale Telegram origine: https://t.me/+jqUKtk2A-LxlMWQ6 (INCUBE.AI)

## Notes
<!-- openclaw:human:start -->
### Nel vault
- [Harness Engineering — Agent = Model + Harness: The 6-Layer Production Playbook](harness-engineering-6-layer-playbook-2026.md) — stesso oggetto dall'altro lato: qui i pattern del loop (planning, offload, sub-agent), lì l'ambiente che li rende affidabili; LangChain compare nella sua tabella di evidenza harness
- [DeepSeek Harness — "Everything is a Plugin"](../syntheses/deepseek-harness-agent-harness-everything-is-a-plugin.md) — implementazione alternativa degli stessi pattern agent-loop, a plugin invece che a notebook
- [Prime Agent — self-improving RLM agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md) — research-agent completo, il punto d'arrivo a cui i 5 notebook tendono
- [BRIX-IA](../entities/brix-ia.md) — stack interno dove questi pattern (delega a sub-agent, contesto su file) sono già operativi nell'orchestratore OpenClaw
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Harness Engineering — Agent = Model + Harness: The 6-Layer Production Playbook](harness-engineering-6-layer-playbook-2026.md)
<!-- openclaw:wiki:related:end -->
