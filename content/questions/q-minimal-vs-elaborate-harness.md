---
title: "Does harness complexity stop paying, and where?"
kind: question
status: partially-answered
priority: p0
created: 2026-09-01
updated: 2026-09-13
last_checked: 2026-09-13
tags: [question, gap, harness, benchmarks]
summary: "On Terminal-Bench 3.0 the minimal harness (mini-SWE-agent) beats the commercial agents, while the 6-layer playbook argues for six layers. Both cannot be general advice."
confidence: medium
origin: "2026-09-01, opening the harness topic: the playbook and the TB3.0 leaderboard point in opposite directions and neither cites the other"
publish: true
---

# Does harness complexity stop paying, and where?

## Why Track This

Two claims in this vault, neither aware of the other:

| Source | Claim |
|---|---|
| [6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md) | Six layers, built over seven days, with a scale gate before expanding. More harness, more reliability. |
| [Due classifiche](../syntheses/due-classifiche-per-lo-stesso-benchmark.md) | On Terminal-Bench 3.0 the top entry is `mini-SWE-agent` — the *minimal* harness — ahead of commercial agents. |

This is the central practical question of the whole topic. If harness effort has a
knee past which it degrades performance, then "build a harness" is bad advice
without a stopping rule, and [[harness-vs-model]] needs the qualification that
what is worth tens of points is harness *design*, not harness *quantity*.

## Classification run 2026-09-13 (dreaming sweep)

Read the `DefaultAgent` class (~190 lines, `src/minisweagent/agents/default.py`,
main branch) and the `mini.yaml` config, against the playbook's six layers:

| Layer | mini | Evidence |
|---|---|---|
| Guides | **minimal** | one system line + a recommended-workflow prompt; no ratchet, no dated rules from failures |
| Sensors | **weak** | no external validators; format-error parsing with max-3-consecutive exit is the only mechanical check; verification is *instructed* in the prompt (write repro script, run it), not enforced |
| Agentic loop | **yes** | query→execute→observe with explicit bounds: `step_limit`, `cost_limit` (default $3), `wall_time_limit_seconds`, 3 consecutive format errors |
| Memory | **none** | linear message history, trajectory saved to JSON per run; nothing persists across runs |
| Permissions | **delegated to environment** | every action in a fresh `subprocess.run`, swappable for docker/singularity/bubblewrap — the sandbox *is* the permission layer |
| Observability | **partial** | trajectory + cost/call stats serialized every step; no trip wires, no scorecard |

So mini is **strong sensors-and-permissions by environment, weak guides/memory/observability** —
reading 3 (different objectives) is supported: on a bounded benchmark the
environment sandbox substitutes for most of what the playbook's elaborate layers
buy in production. What it does *not* have is anything that improves run N+1 from
run N's failures — the ratchet is absent by design ("put the language model, not
the scaffold, in the middle of our attention"). The contradiction dissolves
conditionally; the open remainder is whether any benchmark measures *unattended
completion across sessions*, which none here does. Not fully closed: needs a
longitudinal or production-ops source to settle the general claim.

## Original framing (2026-09-01)

Three readings fit, and nothing here separated them:

1. **Benchmark artifact.** TB 3.0 tasks may reward short, direct tool use, so a
   thin harness wins there and nowhere else.
2. **Real knee.** Each added layer adds prompt surface and failure modes; past
   some point the marginal layer costs more than it prevents.
3. **Different objectives.** The playbook optimizes for unattended reliability in
   production, the leaderboard for score on bounded tasks. Both correct, neither
   general — which would mean the benchmark cannot settle the playbook's claim at all.

Reading 3 is the most likely and the least examined: nothing in this vault measures
a harness on *unattended completion rate*, which is the metric the playbook says
actually matters.

## Next Action

~~Cheapest discriminator: read the `mini-SWE-agent` scaffold and classify what it
does and does not implement against the playbook's six layers.~~ **Done 2026-09-13**
(see classification above — reading 3 supported, contradiction largely dissolved).
Remaining to close fully: a source that measures unattended completion *across*
sessions (the ratchet's metric), which no benchmark in this vault provides.
