---
title: "Agentic Loop"
category: concept
sources: [harness-engineering-6-layer-playbook-2026, loop-engineering-complete-guide-huashu, archon-workflow-engine, deep-agents-from-scratch]
created: 2026-09-01
updated: 2026-09-01
verified: 2026-09-01
tags: [agents, agentic-loop, control-flow, reliability]
aliases: [Agentic Loop, Agent Loop, ReAct Loop]
confidence: high
summary: "Plan → execute → verify → adjust, repeated under explicit bounds. The bounds are the engineering: without a retry ceiling and a cost budget an agent does not fail, it grinds. Escalation is a designed exit, not a defect."
volatility: warm
publish: true
---
# Agentic Loop

**Type:** control-flow pattern
**Position:** layer 3 of the [[harness]] — the part that decides what happens next
**Lineage:** ReAct (reason + act) → planning with explicit task state → delegation to sub-agents

## The loop

```
plan ──> execute ──> verify ──> adjust ──┐
  ^                                      │
  └──────────────────────────────────────┘
```

The shape is old; what makes it an engineering object rather than a slogan is that every arrow needs a stopping rule. A loop without bounds does not fail cleanly — it spends.

## Bounds

The [6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md) proposes concrete ceilings, offered as defaults to be tuned rather than as measured optima:

| Bound | Suggested default |
|---|---|
| Retries per step | 3 |
| Wall clock per task | 30 min |
| Tokens per task | 100K |
| Cost per task | $5 |
| Tool calls per task | 50 |

**Escalation is not failure.** Hitting a bound and handing back a structured account of what was attempted is the designed exit. The failure mode the bounds exist to prevent is the silent one: an agent looping on the same broken approach, paying for each turn.

## The five moves of one turn

[Loop Engineering](../sources/loop-engineering-complete-guide-huashu.md) decomposes a turn into five moves, arguing that dropping any one leaves the loop either unable to turn or spinning in place:

1. **Discovery** — the turn finds its own work, rather than being fed a task.
2. **Handoff** — the work moves to the agent that does it, in an isolated workspace. *"Two agents writing the same file is the exact same headache as two engineers committing to the same lines."*
3. **Verification** — a second agent, with different instructions and sometimes a different model, reviews the output. *"The hard part of a loop isn't the loop itself, it's putting something inside it that can say no."*
4. **Persistence** — state is written outside the conversation. *"The agent forgets, the repo doesn't."*
5. **Scheduling** — the turn recurs without a human starting it.

Moves 1 and 5 are properly *loop* engineering, one floor above the harness; 2–4 are the harness itself. The boundary matters because the failure modes differ: a bad harness produces a wrong result, a bad loop produces a wrong result many times while nobody is watching.

## Determinism as an alternative to instruction

Two sources in this vault attack loop reliability from opposite ends:

- **[Archon](../sources/archon-workflow-engine.md)** encodes the process as a YAML workflow — plan → implement → validate → review → PR — so the *sequence* is owned by the engineer and only the *content* of each step is left to the model. Its framing: *"when you ask an AI agent to 'fix this bug', the outcome depends on the model's mood."* Isolated git worktrees per run; deterministic nodes (bash, tests, git) mixed with AI nodes.
- **[Deep Agents from Scratch](../sources/deep-agents-from-scratch.md)** (LangChain) builds the same capabilities inside the agent instead: a TODO list with task state, context offloaded to a virtual filesystem, delegation to sub-agents, parallel specialists.

These are the two available answers to the same question — *where does structure live, in the runner or in the model's own scaffolding* — and the vault holds no evidence comparing them. See [q-workflow-vs-agent-structure](../questions/q-workflow-vs-agent-structure.md).

## Self-improvement

[Prime Agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md) closes the loop one level higher: the agent modifies its own scaffolding between runs. This is the [[guides-and-sensors|ratchet]] applied automatically rather than by a human noticing a repeated failure — with the corresponding risk that a regression is also ratcheted in. No measurement of that risk exists in this vault.

## Relation to context

Every turn of the loop consumes window. The two mitigations both appear in this vault as products rather than as measured techniques: offloading context to files (Deep Agents, and the OpenClaw orchestrator by default) and compressing it in place ([Headroom](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md)). The economics of that choice belong to the sibling topic — see [The Economics of LLM Memory](../topics/memory-economics.md).

## See Also

- [[harness]] — the enclosing structure
- [[guides-and-sensors]] — what "verify" actually runs
- [[mcp|MCP]] — how "execute" reaches a tool

## Sources

- [Harness Engineering — the 6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md)
- [Loop Engineering — The Complete Guide](../sources/loop-engineering-complete-guide-huashu.md)
- [Archon — workflow engine for AI coding agents](../sources/archon-workflow-engine.md)
- [Deep Agents from Scratch — LangChain course](../sources/deep-agents-from-scratch.md)
