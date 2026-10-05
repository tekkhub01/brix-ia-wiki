---
title: "The Harness Is Half the Measurement"
category: topic
sources: [due-classifiche-per-lo-stesso-benchmark, harness-engineering-6-layer-playbook-2026, llm-as-a-verifier-arxiv-2607-05391, verifica-leaderboard-benchmark-2026-08-26]
created: 2026-09-01
updated: 2026-09-13
verified: 2026-09-13
tags: [benchmarks, harness, evaluation, methodology]
aliases: [Harness vs Model, The Harness Is Half the Measurement]
confidence: high
summary: "Four independent results in this vault say the same thing: a published agent score measures a model-and-harness pair, not a model. The practical consequence is that a bare model name attached to an agent benchmark number is an incomplete citation."
volatility: warm
publish: true
---
# The Harness Is Half the Measurement

**Type:** synthesis — what no single concept page in this topic states
**Claim:** on agentic benchmarks, the [[harness]] contributes a share of the score comparable to, and sometimes larger than, the difference between model generations. A score reported against a model name alone is therefore under-specified.

## The four results

These were ingested separately, from four teams, and did not cite each other.

**1. The same benchmark has two public leaderboards with different winners.** Terminal-Bench v2.1 tops out at 83.8% on the official `tbench.ai` board and 89.5% on Artificial Analysis. Inside the official board, the same model is worth up to 3.4 points more or less depending on which agent runs it. Source: [Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md), built by reading both primary leaderboards directly.

**2. Changing only the harness moved GAIA by 43.64 points.** Claude Sonnet 4.5 held fixed, 30.91% → 74.55%. Source: the [6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md), reporting Masood. A same-model swing of 44 points is larger than several adjacent model generations put together.

**3. A verifier wrapper is worth nine points without touching the weights.** [LLM-as-a-Verifier](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md) (arXiv 2607.05391, Stanford Scaling Intelligence Lab). This is the proof by contradiction: if something bolted on outside the model moves the number, the number was never the model's alone.

**4. On Terminal-Bench 3.0 the minimal harness wins.** `mini-SWE-agent` sits above the commercial agents. Whatever the elaborate harnesses are buying, on that benchmark it is not the top score.

## Why this is not merely "benchmarks are noisy"

Noise is symmetric and shrinks with repetition. This is neither: it is a systematic, reproducible offset attributable to a named component that the reported figure omits. Two consequences follow, and they are different in kind:

- **For reading published numbers.** A row saying *"model X: 84%"* on an agentic benchmark is missing a column. The vault already applies this rule in practice — the [verification pass](../sources/verifica-leaderboard-benchmark-2026-08-26.md) of 2026-08-26 records agent *and* model *and* reasoning effort for every row precisely because the triple is the unit, not the model.
- **For spending.** If the harness is worth tens of points, harness work competes directly with model upgrades for the same budget — and it is the cheaper of the two, since it does not recur per token. This is the practical thesis of the [[harness]] page and the reason [[guides-and-sensors|the ratchet]] pays.

## What would falsify it

The claim is strong enough to be worth stating as refutable:

- If the GAIA and Terminal-Bench harness effects turn out to be artifacts of tasks with unusually long tool-use chains, the effect would be real but bounded to a benchmark family rather than general.
- If minimal harnesses keep winning as benchmarks get harder, the claim survives but inverts in its practical advice: the lesson would be that *harness design* matters, not *harness quantity* — which the Terminal-Bench 3.0 result already hints at and no source here settles. Tracked as [q-minimal-vs-elaborate-harness](../questions/q-minimal-vs-elaborate-harness.md), **partially answered 2026-09-13**: the mini-SWE-agent scaffold classified against the playbook's six layers shows the sandbox substituting for the elaborate layers on bounded benchmarks, while the ratchet (layer 1) is absent by design.

## A caution about this vault's own evidence

Result 2 comes from an independent synthesis, not a controlled study, and its four rows are four different setups never run against each other. Results 1 and 4 rest on leaderboards this vault read directly and are the strongest. Result 3 is a peer-reviewed paper, with the caveat recorded on its own page that the k in its sampling is 5, so the cost per task is five generations plus verification.

The convergence is what carries the claim — four methods, one direction — not any single row.

## See Also

- [[harness]] — the object being argued about
- [[agentic-loop]] — where most of the harness effect is spent
- [[guides-and-sensors]] — the cheapest place to buy some of it back

## Sources

- [Due classifiche per lo stesso benchmark](../syntheses/due-classifiche-per-lo-stesso-benchmark.md)
- [Harness Engineering — the 6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md)
- [LLM-as-a-Verifier (arXiv 2607.05391)](../sources/llm-as-a-verifier-arxiv-2607-05391.md)
- [Verifica sulle fonti primarie dei benchmark](../sources/verifica-leaderboard-benchmark-2026-08-26.md)
- [bb — The agent IDE that builds itself](../sources/bb-agent-ide-github.md) — un harness che si auto-costruisce: qui il confine model/harness diventa una variabile del prodotto
