---
title: "Should the structure of a run live in the workflow engine or in the agent's own scaffolding?"
kind: question
status: proposed
priority: p1
created: 2026-09-01
updated: 2026-09-01
last_checked: 2026-09-01
tags: [question, gap, harness, agentic-loop, workflows]
summary: "Archon encodes the sequence in YAML owned by the engineer; Deep Agents builds the same capabilities inside the agent as planning, offloading and delegation. The vault holds no evidence comparing them."
confidence: medium
origin: "2026-09-01, writing the agentic-loop concept: the two sources answer the same question in opposite ways and neither cites the other"
publish: true
---

# Should the structure of a run live in the workflow engine or in the agent's own scaffolding?

## Why Track This

| Source | Where structure lives |
|---|---|
| [Archon](../sources/archon-workflow-engine.md) | Outside the model: a YAML DAG (plan → implement → validate → review → PR), deterministic nodes mixed with AI nodes. *"When you ask an AI agent to 'fix this bug', the outcome depends on the model's mood."* |
| [Deep Agents from Scratch](../sources/deep-agents-from-scratch.md) | Inside the model's loop: TODO list with task state, context offloaded to a virtual filesystem, sub-agent delegation, parallel specialists. |

The choice determines what happens when the model gets better. If structure is
external, a stronger model fills the same slots better. If structure is internal,
a stronger model may reorganize the work itself — and the external scaffold
becomes the ceiling.

## Current State

Not compared anywhere in this vault. Note that OpenClaw already takes the second
position by default (delegation to sub-agents, context on files), so this is not
an academic question here: it is a description of a choice already made without
the comparison having been run.

## Next Action

Not resolvable by reading. The honest first step is smaller: write down which of
the two shapes each agent-cluster source in this vault actually implements
(Archon, DSH, JCode, Prime Agent, Webwright, Deep Agents), which is a
classification pass over material already ingested. A distribution across six
systems is weak evidence but it is evidence, and it costs one afternoon.
