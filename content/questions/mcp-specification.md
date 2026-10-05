---
title: "MCP specification (Model Context Protocol)"
kind: ingest-candidate
status: ingested
priority: p0
created: 2026-09-01
updated: 2026-09-13
sources: [https://modelcontextprotocol.io]
last_checked: 2026-09-13
tags: [ingest, source, harness, protocol]
summary: "Seven sources here use MCP and none defines it; the concept page is written from observed usage rather than from the spec, and is flagged as the weakest in the topic."
confidence: high
origin: "2026-09-01, writing the mcp concept page without a primary source"
publish: true
---

# MCP specification (Model Context Protocol)

## Why Track This

The highest ratio of load-bearing to unverified in the topic. MCP is the tool
surface of every harness described here, five projects in this vault ship an MCP
server, and [[mcp]] is written entirely from how those five use it. Any claim on
that page about what the protocol *requires* is currently an inference from
examples.

## Current State

**Ingested 2026-09-13** (dreaming sweep): the official documentation set for spec
version **2026-07-28** (intro, architecture, server-concepts, versioning) is now at
[sources/model-context-protocol-specification-documentation-2026-07-28](../sources/model-context-protocol-specification-documentation-2026-07-28.md).
The three verification targets from Next Action resolved as follows:

- **Transport and lifecycle**: two transports — stdio (local, one client) and
  Streamable HTTP (remote, many clients, OAuth-recommended auth). The protocol is
  **stateless**: every request carries version + capabilities in `_meta`; a
  mandatory `server/discover` RPC replaces the old handshake.
- **Are tool definitions sent up front?** Yes — clients discover primitives via
  `*/list` (`tools/list`) before `tools/call`. The listing is dynamic and
  change-notifiable, which confirms the concept page's inference: an eager client
  pays the full tool-definition cost before the first action, so lazy loading is a
  client-side mitigation of a real protocol behavior, not a protocol feature.
- **Trust boundaries**: the spec places consent on the **client/application**, not
  the protocol — tools "may require user consent prior to execution", and the
  normative list is UI display, approval dialogs, pre-approval settings, activity
  logs. Elicitation (server asking the user via `elicitation/create`) is the
  in-protocol mechanism. Sampling and Logging as client features are **deprecated**
  as of 2026-07-28.

Concept page `mcp` re-verified against these; its confidence note updated.

## Next Action

Ingest the specification into `raw/`, then re-verify three specific things the
concept page asserts from usage: the transport and lifecycle, whether tool
definitions must be sent up front (which is what the lazy-loading mitigation
implies), and what the protocol says, if anything, about trust boundaries.
