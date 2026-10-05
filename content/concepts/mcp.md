---
title: "MCP (Model Context Protocol)"
category: concept
sources: [model-context-protocol-specification-documentation-2026-07-28, claude-code-tips-ykdojo-claude-code-tips, codegraph-2026-05-26, headroom-2026-08-04]
created: 2026-09-01
updated: 2026-09-13
verified: 2026-09-13
tags: [agents, tools, protocol, interoperability]
aliases: [MCP, Model Context Protocol, MCP server]
confidence: high
summary: "The standard wire format by which a harness exposes tools to a model. Its practical effect in this vault is visible without the spec: five unrelated tools ship an MCP server as their agent-facing surface, which is what a successful interop standard looks like from the outside."
volatility: hot
publish: true
---
# MCP (Model Context Protocol)

**Type:** interoperability protocol
**Position:** the tool-delivery surface of a [[harness]] — how the "execute" step of the [[agentic-loop]] reaches something outside the model
**Introduced:** Anthropic, late 2024; by 2026 adopted across competing agent runtimes

## Confidence note

**The specification is ingested as of 2026-09-13** — version 2026-07-28, the current revision: [Model Context Protocol — Specification Documentation](../sources/model-context-protocol-specification-documentation-2026-07-28.md). The mechanics below were written from observed usage and are now re-verified against it; where the spec adds or corrects something, that is stated inline. The candidate [mcp-specification](../questions/mcp-specification.md) is closed.

## The problem it solves

Before a standard, every agent runtime defined its own tool-calling format, so a tool built for one agent had to be rewritten for the next. MCP fixes the shape of three things — how a server advertises the tools it offers, how the client calls one, and how the result comes back — so that a tool is written once and any compliant client can use it.

**What the spec adds** (2026-07-28): MCP is formally **stateless** — every request carries the protocol version and capabilities in its `_meta` field, and a mandatory `server/discover` RPC (versions, capabilities, identity in one call) replaces the older initialization handshake. Two transports: **stdio** for local one-client servers, **Streamable HTTP** for remote many-client ones, with OAuth recommended for auth. Versioning is date-based (`YYYY-MM-DD`), bumped only on breaking changes.

The evidence that this worked is indirect but strong, and it is visible entirely inside this vault: five unrelated projects, none of which are agent frameworks, chose an MCP server as their agent-facing interface.

| Tool | What its MCP server exposes |
|---|---|
| [CodeGraph](../syntheses/codegraph-pre-indexed-code-knowledge-graph.md) | a symbol/caller/callee graph, to *"Claude Code, Cursor, Codex, opencode, Hermes Agent, Gemini CLI"* |
| [Headroom](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md) | `headroom_compress`, `headroom_retrieve`, `headroom_stats` |
| [icons0.dev](../syntheses/icons0-dev-icon-search-engine-con-mcp-server.md) | icon search and install |
| Obsidian LLM Wiki server | read/search/write over a vault, *"so any MCP client can maintain it"* |
| Playwright MCP | browser automation |

CodeGraph's own list is the point: one server, six clients from five competing vendors. That list is the reason this page sits in the harness topic rather than in a tooling note — MCP is the seam that lets the harness layer be swapped without rewriting the tools underneath it.

## Deployment shapes

CodeGraph documents the three forms a tool can take, which generalize: **library** (linked into the process), **proxy**, or **MCP server** (a separate process the agent talks to). The third is what makes the tool reusable across runtimes; the first is faster and gives up that portability.

Servers are configured per scope — the [Claude Code tips](../sources/claude-code-tips-ykdojo-claude-code-tips.md) source documents user, project and local scopes, plus a `/mcp` command to inspect what is connected.

**What the spec confirms:** the lazy-loading premise is normatively right. Clients discover primitives via `*/list` methods (`tools/list` before `tools/call`), listings are dynamic and change-notifiable — so an eager client does pay the full tool-definition surface before the first action. Lazy loading is a client-side mitigation of real protocol behavior, not a protocol feature.

## The context cost

Every connected server spends window on its tool definitions before the agent has done anything. The mitigation named in this vault is **lazy loading** — *"only loads MCP tool definitions when needed, saves context"* — which reframes MCP from a pure interoperability question into a [context budget](../topics/memory-economics.md) question: connecting servers is not free, and a harness with many servers pays a standing tax on every run.

No source here measures that tax; the spec neither requires nor forbids eager listing, leaving the cost to client design. See [q-mcp-context-tax](../questions/q-mcp-context-tax.md).

## Security surface

**What the spec says about trust:** consent lives in the *application*, not the protocol. Tools "may require user consent prior to execution" and the normative menu is displaying available tools, per-execution approval dialogs, pre-approval settings for safe operations, and activity logs; `elicitation/create` is the one in-protocol mechanism for a server to ask the user anything. Notably, **Sampling** (server borrowing the client's model) and **Logging** as client features are **deprecated as of 2026-07-28** — the protocol is narrowing toward server-exposes-capability, client-owns-the-model.

An MCP server is code the agent invokes, frequently fetched at run time. The vault records the general form of this concern on the DeepSeek Harness page — *"`npx` esegue codice da npm (rischio supply-chain basso ma presente); per audit clonare il repo e leggere il codice"* — which applies to any `npx`-launched MCP server. The connected server is also a route by which untrusted content enters the run, which is the boundary layer 5 of the [[harness]] exists to police.

## See Also

- [[harness]] — the enclosing structure
- [[agentic-loop]] — the step MCP serves

## Sources

- [MCP Specification Documentation, version 2026-07-28](../sources/model-context-protocol-specification-documentation-2026-07-28.md) — the primary source, ingested 2026-09-13
- [Claude Code Tips (ykdojo)](../sources/claude-code-tips-ykdojo-claude-code-tips.md)
- [CodeGraph — pre-indexed code knowledge graph](../sources/codegraph-2026-05-26.md)
- [Headroom — context compression layer](../sources/headroom-2026-08-04.md)
