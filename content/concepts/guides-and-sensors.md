---
title: "Guides and Sensors"
category: concept
sources: [harness-engineering-6-layer-playbook-2026, claude-code-tips-ykdojo-claude-code-tips, progress-check-skill-tjcages-skills]
created: 2026-09-01
updated: 2026-09-01
verified: 2026-09-01
tags: [agents, harness, guides, sensors, verification, ratchet]
aliases: [Guides and Sensors, Feedforward and Feedback, Ratchet Principle]
confidence: high
summary: "The two halves of the steering loop: guides are rules given before acting, sensors are checks applied after. The ratchet converts each observed failure into whichever of the two prevents its whole class from recurring."
volatility: warm
publish: true
---
# Guides and Sensors

**Type:** control pattern
**Position:** layers 1 and 2 of the [[harness]] — feedforward and feedback around the [[agentic-loop]]
**Attribution:** the guides/sensors framing is credited by the [playbook](../sources/harness-engineering-6-layer-playbook-2026.md) to Martin Fowler and Birgitta Böckeler; the ratchet to Mitchell Hashimoto

## The pair

- **Guides (feedforward)** — rules the agent reads before acting: `AGENTS.md`, `CLAUDE.md`, `.cursorrules`. The playbook's standard: every line should be a past failure converted into permanent prevention, and each rule should be verifiable, dated, and traceable to a failure that actually happened. A guide file that accumulates untested advice is not a harness component, it is decoration.
- **Sensors (feedback)** — checks applied to what was produced. Ordering matters: deterministic, fast and free first (linters, tests, validators), with LLM-as-judge reserved for semantic checks that cannot be coded, because it is slow, costly and non-deterministic. The stronger form is *self-verification*: the agent runs the sensors itself and acts on the results, rather than waiting for a human to run them.

## The ratchet

The mechanism that fills both, in one direction only:

1. the agent fails →
2. identify the *class* of failure, not the instance →
3. choose the strongest layer that can prevent the class →
4. encode the fix →
5. verify it prevents recurrence →
6. watch for regressions.

> A prompt patch fixes one conversation. A guide rule fixes every future run. An environment constraint makes the error structurally impossible.

**Lauren Tan's rule (Cursor)**: when a human reviewer writes the same comment three or more times, that comment stops being feedback and becomes a structural constraint — a guide, and then a sensor that blocks the output.

## The reliability ladder

Where to place a fix, ordered by how reliably it holds:

| Layer | Example | Reliability | Cost to build |
|---|---|---|---|
| Memory | a correction in chat | Low | Zero |
| Prompt | a task instruction | Low–Medium | Minutes |
| Guide | a rule in `AGENTS.md` | Medium | Minutes |
| Sensor | an automated test | High | Hours |
| Environment | permission / schema / CI | Highest | Hours–Days |

The ladder is the practical content of the ratchet: a fix that stays at the top two rows will be re-litigated; the same fix pushed down two rows stops being a matter of the model's cooperation.

**Reliability here is a claim about mechanism, not a measurement.** No study in this vault quantifies the recurrence rate at each rung.

## How this vault's own harness scores

The [playbook](../sources/harness-engineering-6-layer-playbook-2026.md) is applied to the OpenClaw/Claudia stack on its own source page. The parts already operating: guides carrying dated rules and named footguns, cron watchdogs that notify only on *new* errors, filesystem memory with checkpoints, approval gates with `DENY` on destructive actions, and delegation to sub-agents with retry and escalation.

The gaps the same page lists as unverified — an explicit trip wire at 2× average cost, sensor coverage on every critical output, a structured escalation packet, and a written capability budget per action — are open work, not claims.

A worked example of the ratchet in this vault: `AGENTS.md` carries a rule that generated blocks must never be hand-edited, dated and traced to the run on 2026-08-15 where hand-written content inside `openclaw:wiki:related` markers was silently discarded by the next compile. That is step 4 of the ratchet applied to a real observed failure — and the reason a further class of that failure surfaced anyway is that no *sensor* enforces the rule, only a guide.

## Sensors as a product category

Two sources in this vault are sensors sold as tools rather than described as a pattern: the [progress-check skill](../sources/progress-check-skill-tjcages-skills.md), which gates a progress report on observable milestones (and on at least 30 minutes elapsed — the vault's synthesis of it originally got this backwards, corrected 2026-08-28), and the verification wrapper measured in [LLM-as-a-Verifier](../syntheses/llm-as-a-verifier-la-verifica-come-asse-di-scaling.md), which is a sensor expensive enough to change the score by nine points.

## See Also

- [[harness]] — the enclosing structure
- [[agentic-loop]] — what the sensors gate
- [[harness-vs-model]] — synthesis: sensors as part of the measured object

## Sources

- [Harness Engineering — the 6-layer playbook](../sources/harness-engineering-6-layer-playbook-2026.md)
- [Claude Code Tips (ykdojo)](../sources/claude-code-tips-ykdojo-claude-code-tips.md)
- [progress-check — skill (tjcages/skills)](../sources/progress-check-skill-tjcages-skills.md)
