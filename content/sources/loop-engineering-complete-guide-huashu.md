---
id: loop-engineering-complete-guide-huashu
pageType: source
updatedAt: 2026-09-13T05:00:00Z
verified: 2026-09-13
claims: []
links: []
publish: true
---

# Loop Engineering — The Complete Guide

> Verifica sweep 2026-09-13: fonte ri-legata al tema harness del vault; nessuna
> novità che la smentisca. Resta un riferimento di giugno 2026.

**Source:** PDF by HuaShu (花叔)
**Version:** v260615 (June 2026)
**Author:** HuaShu (花叔)
**Type:** Technical Book / Engineering Guide
**Origin:** Inspired by Addy Osmani (Google Chrome), Peter Steinberger (OpenClaw), Boris Cherny (Anthropic)

---

## What It Is

Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger
> "I don't prompt Claude anymore. I have loops running that prompt Claude. My job is to write loops." — Boris Cherny
> "Loop engineering sits one floor above the harness." — Addy Osmani

Three people, same realization, same week (June 2026).

---

## The Four-Layer Stack

| Layer | What it minds | Core question |
|-------|--------------|---------------|
| **Prompt Engineering** | Writing one good prompt | What should I tell the model |
| **Context Engineering** | What goes in the window right now | What to retrieve, summarize, clear out |
| **Harness Engineering** | Arming a single run | Which tools, what actions, what counts as done |
| **Loop Engineering** | Scheduling on top of the harness | How to make it run itself over and over |

Each layer up, scope gets one size bigger. Each fails in a different way. The higher the layer, the farther you are from the scene, the longer mistakes pile up.

---

## The Five Moves of One Loop

Every turn of a loop has exactly five moves. Drop any one and the loop won't turn, or it'll spin in place.

### 1. Discovery
Find this turn's work on its own. The loop figures out "what should this turn do" rather than you feeding work to it.

Key: trigger a `$skill-name`, not a wall of instructions pasted into a cron job nobody will update.

### 2. Handoff
Move the task from scheduling to the agent that does the work. Each finding gets its own isolated worktree so parallel agents don't step on each other.

> "Two agents writing the same file is the exact same headache as two engineers committing to the same lines."

### 3. Verification
A second sub-agent — with different instructions, sometimes a different model — reviews the work. The agent that wrote the code is too soft grading its own homework.

> "The hard part of a loop isn't the loop itself, it's putting something inside it that can say no."

### 4. Persistence
Write state outside the conversation. Open PR, update ticket, write to markdown file. Without persistence, every turn is like opening its eyes for the first time.

> "The agent forgets, the repo doesn't."

### 5. Scheduling
Make it turn automatically, round after round. Automation is what makes a loop a real loop — not just one run you did once by hand.

---

## Six Parts: What a Loop Is Built From

| Part | What it is | Maps to move |
|------|-----------|-------------|
| **Automations** | Runs automatically off a schedule/trigger | Scheduling |
| **Worktrees** | Isolated working directories for parallel agents | Handoff |
| **Skills** | Permanent project knowledge (SKILL.md), paying off intent debt | Discovery |
| **Connectors** | MCP hookup to external systems (issue tracker, DB, Slack) | Persistence / Discovery |
| **Sub-agents** | Generator separated from judge/verifier | Verification |
| **Memory** | Persistent state on disk crossing conversation boundaries | Persistence |

> "Automation is what makes a loop an actual loop and not just one run you did once."
> "A loop that can only see the filesystem is a tiny loop."

---

## Generator and Evaluator — Why an AI Can't Grade Its Own Code

This is the hardest part of building a loop.

> "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work — even when, to a human observer, the quality is obviously mediocre." — Prithvi Rajasekaran, Anthropic

**Key insight:** Tuning a standalone evaluator to be skeptical is far more tractable than making a generator critical of its own work. The problem is structural, not a matter of prompt wording.

The evaluator should **act**, not just read. Use Playwright MCP to click buttons, take screenshots, inspect the DOM. Judge behavior, not intent.

### Maker-Checker Principle (productized as `/goal`)

| Who decides "done" | Problem / advantage |
|-------------------|-------------------|
| Agent self-grades | Carries self-persuasion, tends to praise itself |
| `/goal` fresh model each turn | No baggage, can only look at objective conditions |

After each turn, a small fast model checks whether the condition holds. If not, another turn starts. Completion is decided by a fresh model, not the one doing the work.

> "A loop with no real check is just an agent nodding at itself over and over."

---

## Real Loop Example: Addy Osmani's Morning Triage

1. Automation kicks off in the morning
2. Triage skill reads yesterday's CI failures, open issues, recent commits
3. Writes results to markdown file or Linear board
4. For each finding: opens isolated worktree
5. Sub-agent 1 drafts the fix; Sub-agent 2 reviews against skills and tests
6. Connector opens PR and updates ticket
7. Anything it can't handle → human inbox
8. State file persists for next day's pickup

---

## The Costs

- **Verification Debt:** Accumulated when loop runs without proper checks
- **Comprehension Rot:** When loops run long enough that nobody understands the full flow
- **Token Blowout:** Unbounded loops consuming context and tokens exponentially

---

## Relationship to OpenClaw

This framework maps directly onto OpenClaw's architecture:
- **Skills** (SKILL.md, AGENTS.md, tools) = the skills layer
- **Sub-agents** (mimo agent delegation) = generator/evaluator split
- **Memory** (MEMORY.md, daily notes, Obsidian) = persistence outside context window
- **Cron/automations** = scheduling layer
- **Worktrees** = git worktree for agent parallelism

Gaps to fill:
- Systematic evaluator for autonomous tasks (`/goal`-style stop condition)
- Discovery loop that finds work independently instead of waiting for input

---

## Categories
Loop Engineering, AI agents, agent orchestration, automation, Addy Osmani, HuaShu, Peter Steinberger, Boris Cherny, harness engineering, Claude Code, OpenClaw

## Collegamenti (dreaming 2026-08-15)

- [Archon](archon-workflow-engine.md) è questa tesi resa eseguibile: workflow YAML deterministici invece di prompt
- [Prime Agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md) è il grado successivo: il loop che riscrive se stesso
- Altri agenti del cluster: [JCode](../syntheses/jcode-agente-di-coding-super-veloce.md), [Webwright](../syntheses/webwright-microsoft-browser-agent.md)
- Boris Cherny lavora in [Anthropic](../entities/anthropic.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Archon — Open-source workflow engine for AI coding agents](archon-workflow-engine.md)
- [JCode — Agente di coding super-veloce](../syntheses/jcode-agente-di-coding-super-veloce.md)
- [Prime Agent — Self-Improving RLM Agent (PrimeIntellect-ai)](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md)
- [Webwright — Microsoft Browser Agent](../syntheses/webwright-microsoft-browser-agent.md)
<!-- openclaw:wiki:related:end -->
