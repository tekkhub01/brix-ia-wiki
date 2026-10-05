---
id: source.codegraph-2026-05-26
pageType: source
title: CodeGraph — Pre-indexed code knowledge graph
updatedAt: 2026-09-13T04:40:00Z
publish: true
---

# CodeGraph — Pre-indexed code knowledge graph

**Date:** 2026-05-26  
**Source URL:** https://colbymchenry.github.io/codegraph/  
**GitHub:** https://github.com/colbymchenry/codegraph  
**Author:** Colby McHenry  
**Introduced via:** Tips AI | IT & AI Telegram channel (forwarded by PK)

## Description

CodeGraph is a local-first, pre-indexed code knowledge graph for AI coding agents. It scans a codebase once, builds a queryable graph of symbols, callers, callees and relationships using Tree-sitter AST parsing, and exposes it to agents via an MCP server.

## Key features

- **Tree-sitter parsing** across 20+ languages (TS, JS, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, ObjC, Swift, Kotlin, Dart, Lua, Svelte, etc.)
- **MCP server** exposes graph to Claude Code, Cursor, Codex, opencode, Hermes Agent, Gemini CLI, AntiGravity IDE
- **Impact analysis** — trace callers, callees, impact radius before changing code
- **Full-text search** (FTS5) across entire codebase
- **Auto-sync** via native OS file watchers (FSEvents/inotify/ReadDirectoryChangesW) with debounced updates
- **Framework-aware routing** — recognizes 14 web frameworks
- **100% local** — no data leaves the machine
- **Bundled runtime** — no Node.js required, single binary via curl/npx

## Installation

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

# Windows (PowerShell)
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex

# Via npm
npx @colbymchenry/codegraph
npm i -g @colbymchenry/codegraph
```

## Usage

```bash
cd your-project
codegraph init -i   # interactive setup with agent auto-config
codegraph serve --mcp   # launch MCP server for agents
codegraph uninstall     # remove from all configured agents
```

## Benchmark results (v0.9.4, 2026-05-24)

Tested on 7 real-world codebases with Claude Opus 4.7:

| Codebase | Language | Cost ↓ | Tokens ↓ | Time ↓ | Tool calls ↓ |
|----------|----------|--------|----------|--------|-------------|
| VS Code | TS (~10k files) | 26% | 78% | 52% | 85% |
| Excalidraw | TS (~640 files) | 52% | 90% | 73% | 96% |
| Django | Python (~3k) | 12% | 36% | 19% | 53% |
| Tokio | Rust (~790) | 82% | 86% | 71% | 92% |
| OkHttp | Java (~645) | 2% | 13% | 31% | 45% |
| Gin | Go (~110) | 21% | 34% | 27% | 40% |
| Alamofire | Swift (~110) | 47% | 64% | 48% | 83% |

**Average:** 35% cheaper · 57% fewer tokens · 46% faster · 71% fewer tool calls

## Star history

~23K GitHub stars as of late May 2026, with a viral spike in May.

## Notes

- Gains scale with codebase size (larger repos = bigger savings)
- On small repos (~100 files) native search is already cheap, margin narrows
- v0.9.4 as of 2026-05-24
- License: NOT explicitly stated yet (likely MIT or similar)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [CodeGraph — Pre-indexed code knowledge graph](../syntheses/codegraph-pre-indexed-code-knowledge-graph.md)
<!-- openclaw:wiki:related:end -->
