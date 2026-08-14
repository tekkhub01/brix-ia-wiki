---
title: "LLM Wiki (Karpathy Pattern)"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-04-28
updated: 2026-08-12
verified: 2026-08-12
tags: [knowledge-management, agentic-memory, write-time-synthesis]
aliases: [LLM Wiki, Karpathy Pattern]
confidence: high
summary: "Karpathy's write-time synthesis pattern: compile sources into a persistent agent-maintained markdown wiki instead of retrieving per query. Three layers: immutable raw, LLM-owned wiki, human-owned schema."
volatility: hot
publish: true
---
# LLM Wiki (Karpathy Pattern)

**Type:** Knowledge management architecture  
**Proposer:** Andrej Karpathy — X post + [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), 2026-04-04  
**Core idea:** Abandon retrieval-at-query-time in favor of synthesis-at-write-time  
**Implementation:** Persistent Markdown filesystem with auto-maintained cross-links, summaries, indices  
**Reception:** ~16M views on the original post; gist passed 5k stars within days

## Three-layer architecture

Karpathy's gist is explicit about the layering, and the separation is the load-bearing part of the pattern:

| Layer | Owner | Rule |
|-------|-------|------|
| **Raw sources** | Human / ingest | Immutable. The agent reads but *never* writes here. |
| **The wiki** | LLM | Fully agent-owned: entity pages, summaries, cross-references. |
| **The schema** | Human | A config doc (`CLAUDE.md` / `AGENTS.md`) defining structure, conventions, workflows. |

The read-only `raw/` boundary is the single most-cited implementation rule in community write-ups — it is what keeps provenance intact when synthesis goes wrong.

## How it works

Instead of [[rag|RAG]] (retrieve → read → generate), the LLM Wiki uses three workflows:

1. **Ingest**: new source → agent reads it → discusses takeaways → updates the pages it touches (Karpathy's own figure: a single source typically touches **10–15 pages**) → appends a log entry
2. **Query**: agent reads `index.md` first, drills into relevant pages, synthesizes with citations — and files valuable answers back as new pages
3. **Lint**: periodic health check for contradictions, stale claims, orphan pages, missing cross-references

Two support files carry the pattern: **`index.md`** (content-oriented catalog of every page, grouped by category) and **`log.md`** (append-only, parseable, chronological record of ingests/queries/maintenance).

> "Traditional RAG rediscovers knowledge from scratch on every question." The LLM Wiki *compiles* knowledge once, then keeps it current. The LLM does not retrieve — it compiles.

Karpathy's stated rationale is an economic one, not an epistemic one: *"the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."* LLMs drive bookkeeping cost to ~zero; humans keep the analysis and the good questions.

## Key innovations

- **Write-time synthesis vs query-time retrieval**: Knowledge accumulates; no re-discovery per query
- **Managed note blocks** with semantic wikilinks (not just plain Markdown)
- **Automated linting** for graph health (contradictions, broken links, entropy)
- **Schema-driven updates**: Agents follow strict note templates to avoid chaos

## Pros & cons

**Pros:**
- No retrieval randomness; knowledge is composed, not fetched
- Persistent state that compounds over time
- Human-readable, editable knowledge base
- Full provenance via source linking

**Cons:**
- Build cost high upfront (needs synthesis agents)
- Over-linking can create entropic graph (spaghetti knowledge)
- Requires disciplined schema and linting
- Hybrid approaches (Wiki + [[graphrag|GraphRAG]]) still experimental

## Community implementations

Verified as of 2026-08-12:

- **[nvk/llm-wiki](https://github.com/nvk/llm-wiki)** — the most feature-complete extension. Parallel multi-agent research (5–10 agents fanning out across academic / technical / applied / news / contrarian angles), thesis-driven investigation that routes agents to *both* supporting and opposing evidence and re-weights round 2 toward the weaker side, idea→project promotion pipeline, session memory via redacted checkpoints. Isolated topic sub-wikis under `~/wiki/topics/`. Installs into Claude Code, Codex, OpenCode, or any agent via a portable `AGENTS.md`.
- **LLM Wiki agent skill** ([engineering-advanced-skills](https://alirezarezvani.github.io/claude-skills/skills/engineering/llm-wiki/)) — a faithful, minimal implementation of the base pattern. Ships `/wiki-init`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/wiki-log`; dual `CLAUDE.md` + `AGENTS.md` schemas; helper scripts use only the Python stdlib for cross-platform parity.
- **[ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki)** — framework for agents maintaining an Obsidian-backed digital brain.
- **Obsidian LLM Wiki MCP server** — exposes read/search/write over a vault so any MCP client can maintain it.
- **Obsidian + Claude Code** remains the canonical hand-rolled stack: open the vault in an agentic coding environment, hand it the gist, ask it to instantiate the pattern in place.

> Earlier revisions of this page listed `llmwiki` (Lucas Astorian) and an `obsidian-direct` OpenClaw bridge. Neither could be verified in the 2026-08 sweep — treat as unconfirmed until a source turns up.

## Position in evolution

LLM Wiki represents the shift from **retrieval-augmented** to **agentic memory**: the agent becomes the librarian that maintains the library, not just a visitor checking out books.


## Compounding: the first empirical numbers

The "does it compound or does it rot?" question got its first measurement in **Wen & Ku, *Knowledge Compounding: An Empirical Economic Analysis of Self-Evolving Knowledge Wikis under the Agentic ROI Framework*** ([arXiv 2604.11243](https://arxiv.org/abs/2604.11243), April 2026). It attacks the Agentic ROI framework's assumption that task costs are independent, and models cost as *decreasing* as the knowledge base grows.

Measured on a four-query run: **47K cumulative tokens under the compounding regime vs 305K on a matched RAG baseline — 84.6% saved.** Projected over 30 days: 53.7% saving at moderate topic concentration, 81.3% at high concentration.

Three mechanisms drive the reduction:
1. Ingestion cost is amortized across every later retrieval
2. High-quality answers are recycled back into synthesis pages
3. External search findings are folded into entity pages instead of being re-fetched

Their framing is the useful one: it reframes **LLM tokens from consumables into capital goods**. The caveat is in the numbers themselves — the saving scales with *topic concentration*. A wiki spread thin across unrelated domains amortizes nothing.

## Open research questions

- Hybrid Wiki + Graph: when to use each layer? (see [[graphrag|GraphRAG]] — the agentic-search benchmarks are now asking the same question from the other side)
- Cost of maintenance: how expensive is linting at scale, and does lint cost grow super-linearly with page count?
- Does the compounding result hold past the four-query horizon, and at what point does contradiction-resolution cost overtake ingest savings?

## See Also

- [[rag|RAG (Retrieval-Augmented Generation)]]
- [[graphrag|GraphRAG]]
- [[span-level-attribution]] — links here
- [[long-context-models]] — links here
- [[agentic-rag]] — links here
- [[structure-vs-iteration]] — synthesis drawing on this page
- [[grounding-across-architectures]] — synthesis drawing on this page
- [[memory-economics]] — synthesis drawing on this page

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
