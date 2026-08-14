---
id: source.archon-workflow-engine
pageType: source
title: Archon — Open-source workflow engine for AI coding agents
updatedAt: 2026-06-10T07:20:00Z
publish: true
---

# Archon — Open-source workflow engine for AI coding agents

**Date:** 2026-06-10  
**Source URL:** https://archon.diy/docs/  
**GitHub:** https://github.com/coleam00/archon  
**Author:** coleam00 (Colby McHenry?)  
**Introduced via:** PK request

## Description

Archon is a workflow engine for AI coding agents. It lets you define development processes as YAML workflows — planning, implementation, validation, code review, PR creation — and run them reliably across all your projects. Think of it as "Dockerfiles for AI coding workflows" or "n8n for software development".

The core problem it solves: when you ask an AI agent to "fix this bug", the outcome depends on the model's mood. It might skip planning, forget tests, or ignore your PR template. Archon makes this deterministic by encoding your dev process as a workflow — the AI fills in intelligence at each step, but the structure is owned by you.

## Key features

- **Deterministic workflows** — Same workflow, same sequence, every time. Plan → implement → validate → review → PR
- **Isolated worktrees** — Every run gets its own git worktree. Run 5 fixes in parallel with no conflicts
- **Fire and forget** — Kick off a workflow, come back to a finished PR with review comments
- **Composable nodes** — Mix deterministic nodes (bash, tests, git ops) with AI nodes (planning, code gen, review)
- **Portable** — Workflows defined in `.archon/workflows/`, committed to repo. Work from CLI, Web UI, Slack, Telegram, GitHub
- **Web dashboard** — Chat interface, workflow builder (visual DAG editor), execution monitoring
- **Multi-platform adapters** — Telegram (5 min setup), Slack, Discord, GitHub Webhooks
- **19 built-in workflows** — From idea-to-PR to adversarial development to multi-agent code review

## Architecture

```
Platform Adapters (Web UI, CLI, Telegram, Slack, Discord, GitHub)
         │
         ▼
    Orchestrator (Message Routing & Context Management)
         │
    ┌────┴────┐
    ▼         ▼
Command    Workflow        AI Assistant Clients
Handler    Executor        (Claude / Codex / Pi)
(Slash)    (YAML)
    │         │
    └─────────┘
         │
         ▼
SQLite / PostgreSQL (12 tables)
```

## Workflows (19 built-in)

| Workflow | Description |
|---|---|
| `archon-assist` | General Q&A, debugging, exploration |
| `archon-fix-github-issue` | Classify → investigate → plan → implement → validate → PR → review → self-fix |
| `archon-idea-to-pr` | Feature idea → plan → implement → validate → PR → 5 parallel reviews → self-fix |
| `archon-piv-loop` | Plan-Implement-Validate loop with human review |
| `archon-adversarial-dev` | Build complete app from scratch using adversarial development |
| `archon-smart-pr-review` | Classify PR complexity → targeted review agents → synthesize |
| `archon-comprehensive-pr-review` | Multi-agent PR review (5 parallel reviewers) with auto-fixes |
| `archon-architect` | Architectural sweep, complexity reduction, codebase health |
| `archon-refactor-safely` | Safe refactoring with type-check hooks and behavior verification |
| `archon-interactive-prd` | Create PRD through guided conversation |
| `archon-ralph-dag` | PRD implementation loop — iterate through stories |
| `archon-workflow-builder` | Generate new workflow YAML for your project |
| `archon-resolve-conflicts` | Detect merge conflicts → analyze → resolve → validate → commit |

## Workflow YAML example

```yaml
# .archon/workflows/build-feature.yaml
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"

  - id: implement
    depends_on: [plan]
    loop:
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
      fresh_context: true

  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"  # Deterministic - no AI

  - id: review
    depends_on: [run-tests]
    prompt: "Review all changes against the plan. Fix any issues."

  - id: approve
    depends_on: [review]
    loop:
      prompt: "Present the changes for review. Address any feedback."
      until: APPROVED
      interactive: true  # Pauses for human input

  - id: create-pr
    depends_on: [approve]
    prompt: "Push changes and create a pull request"
```

## Installation

```bash
# Quick install CLI (macOS/Linux)
curl -fsSL https://archon.diy/install | bash

# Homebrew
brew install coleam00/archon/archon

# Full setup (clone + wizard)
git clone https://github.com/coleam00/archon
cd Archon
bun install
claude  # Then say "Set up Archon"
```

**Prerequisites:** Bun, Claude Code, GitHub CLI

## Tech stack

- **Runtime:** Bun
- **Database:** SQLite / PostgreSQL (12 tables)
- **AI assistants:** Claude Code, Codex, Pi
- **Web UI:** Built-in dashboard with chat, workflow builder, execution monitoring
- **Docs:** https://archon.diy/docs/ (includes `/llms.txt` for AI tools)

## Relation to OpenClaw

Archon is complementary to OpenClaw — while OpenClaw is a personal AI assistant platform with messaging, memory, and tool integration, Archon focuses specifically on structured AI coding workflows. They could potentially be used together: OpenClaw as the orchestration layer and Archon for deterministic dev workflows.

## Notes

- The original Python-based Archon (task management + RAG) is preserved on `archive/v1-task-management-rag` branch
- Telemetry is opt-in and anonymous (workflow names for bundled only, "custom" for yours)
- Docs designed for both humans and AI (`/llms.txt`, `/llms-full.txt`, `/llms-small.txt`)

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
