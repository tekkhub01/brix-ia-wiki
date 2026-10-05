---
title: "What does a connected MCP server cost in context, per run?"
kind: question
status: proposed
priority: p2
created: 2026-09-01
updated: 2026-09-01
last_checked: 2026-09-01
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
