---
title: "What does a connected MCP server cost in context, per run?"
kind: question
status: partially-answered
priority: p2
created: 2026-09-01
updated: 2026-11-01
last_checked: 2026-11-01
tags: [question, gap, harness, mcp, context]
summary: "Tool definitions occupy window before any work happens. Lazy loading is documented as the mitigation, which implies the tax is real, but no source here measures it."
confidence: medium
origin: "2026-09-01, writing the mcp concept page"
publish: true
---

# What does a connected MCP server cost in context, per run?

## Why Track This

The [Claude Code tips](../sources/claude-code-tips-ykdojo-claude-code-tips.md)
source documents lazy loading of MCP tool definitions as a context-saving measure.
A mitigation implies a cost, and the cost is paid on *every* run of a harness with
many servers connected — which makes it a standing tax rather than a one-off.

If the figure is small, this is a non-issue and the page should say so. If it is
large, "which servers are connected" becomes a harness design decision on par with
which model to use, and it interacts directly with the compression/offloading
economics in the sibling topic.

## Next Action

Directly measurable on this machine and not worth a research pass: count the tokens
of the tool definitions advertised by the MCP servers currently configured in
OpenClaw, with and without lazy loading. One measurement, locally, closes it.

## Resolution pass (2026-11-01, eleventh sweep — partially-answered)

The tax is real and now has published orders of magnitude (all secondhand,
practitioner/vendor sources):

- **Per tool**: a typical tool definition runs **100–500 tokens** (MindStudio);
  a measured footprint of **~1,000 tokens/tool/session** was filed as a spec
  concern (modelcontextprotocol discussion #2812, May 2026 — definitions cost
  5–15× a type-only schema because of descriptions).
- **Per server**: GitHub MCP ~40 tools ≈ **12k tokens** before the prompt
  (MCP Playground); a 3-server stack (GitHub+Slack+Sentry) measured **55k
  tokens** of tool definitions pre-first-message, another setup **143k**
  (Apideck, Mar 2026, via Roadie).
- **Per turn, not per session**: definitions reload into every message
  (MindStudio) — the tax is recurring, which is what makes lazy loading the
  standard mitigation.
- **The sharper comparison**: Scalekit's 75-run CLI-vs-MCP benchmark — MCP cost
  **4–32× more tokens per operation** than the equivalent CLI (repo language
  detection: 1,365 vs 44,026 tokens). Bigger windows shrink the percentage,
  not the multiplier.

**What this settles:** "which servers are connected" is confirmed as a harness
design decision — the vault's hypothesis in *Why Track This* is supported by
multiple independent measurements.

**What stays open:** the local number for *this* machine (OpenClaw's configured
servers, with/without lazy loading) is still unmeasured — one session of
token-counting closes the record entirely.
