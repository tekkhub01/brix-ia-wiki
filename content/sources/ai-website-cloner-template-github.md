---
id: ai-website-cloner-template-github
pageType: source
updatedAt: 2026-09-13T04:40:00Z
publish: true
---

# AI Website Cloner Template

**Source:** https://github.com/JCodesMore/ai-website-cloner-template
**Author:** JCodesMore
**License:** MIT
**Type:** Open-source template / Framework
**Category:** Web development, AI coding agents, reverse engineering, Next.js

---

## Overview

A reusable template for reverse-engineering any website into a clean, modern Next.js codebase using AI coding agents.

**Core concept:** Point at a URL → AI agent inspects site → extracts design tokens + assets → writes component specs → dispatches parallel builders → reconstructs every section in modern Next.js

**Recommended:** Claude Code with Opus 4.6+ (but supports 11+ different AI coding agents)

---

## Key Features

### 1. Multi-Agent Support
Works with:
- **Claude Code** (recommended, Opus 4.6)
- Codex CLI
- OpenCode
- GitHub Copilot
- Cursor
- Windsurf
- Gemini CLI
- Cline
- Roo Code
- Continue
- Amazon Q
- Augment Code
- Aider

Each agent reads `AGENTS.md` for unified instructions.

### 2. Tech Stack
- **Next.js 16** — App Router, React 19, TypeScript strict
- **shadcn/ui** — Radix primitives + Tailwind CSS v4
- **Tailwind CSS v4** — OKLCH design tokens
- **Lucide React** — icons (replaced by extracted SVGs)
- **Node.js 24+** required

### 3. Multi-Phase Pipeline

#### Reconnaissance
- Screenshots of target website
- Design token extraction (colors, fonts, spacing)
- Interaction sweep (scroll, click, hover, responsive states)

#### Foundation Phase
- Update fonts globally
- Extract colors into design system
- Download all images/videos/assets

#### Component Specs
- Detailed specification files written automatically
- Located: `docs/research/components/`
- Include:
  - Exact computed CSS values (`getComputedStyle()`)
  - State behaviors (hover, active, disabled, etc.)
  - Multi-state content variations
  - Responsive breakpoints
  - Asset paths (no guessing)

#### Parallel Build Phase
- Dispatches **builder agents** in git worktrees
- **One agent per section/component** (parallelized)
- Each receives full spec inline (computed values, interactions, responsive rules)
- No ambiguity or iteration loops

#### Assembly & QA
- Merges worktrees together
- Wires up the page
- Runs visual diff against original site
- Validates correctness

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/JCodesMore/ai-website-cloner-template.git my-clone
cd my-clone

# 2. Install
npm install

# 3. Start agent (Claude Code recommended)
claude --chrome

# 4. Run the skill
/clone-website https://example.com

# 5. Customize (optional)
# Agent will rebuild site, then you can modify further
```

---

## Usage Scenarios

### 1. Platform Migration
- Rebuild site owned by you from WordPress/Webflow/Squarespace
- Modernize to Next.js stack
- Retain design fidelity

### 2. Lost Source Code
- Site is live but repo is gone
- Original developer left
- Legacy stack no longer supported
- **Solution:** Extract code back in modern format

### 3. Learning / Deconstruction
- Understand how production sites implement layouts, animations, responsive behavior
- Work with real production code
- Extract design system patterns

### 4. Rapid Prototyping
- Quickly clone a competitor or reference site
- Use as starting point for customization

---

## What NOT to Use This For

### ⛔ Phishing / Impersonation
- Must not be used for deceptive purposes
- Must not violate law

### ⛔ Design Theft
- Logos, brand assets, original copy belong to owners
- Do not pass off someone's design as your own

### ⛔ Terms of Service Violations
- Some sites explicitly prohibit scraping/reproduction
- Check ToS first before cloning

---

## Project Structure

```
my-clone/
├── src/
│   ├── app/                    # Next.js routes
│   ├── components/             # React components (rebuilt)
│   ├── ui/                     # shadcn/ui primitives
│   ├── icons.tsx               # Extracted SVG icons
│   ├── lib/utils.ts            # cn() utility
│   ├── types/                  # TypeScript interfaces
│   └── hooks/                  # Custom React hooks
├── public/
│   ├── images/                 # Downloaded images
│   ├── videos/                 # Downloaded videos
│   └── seo/                    # Favicons, OG images
├── docs/
│   ├── research/               # Extraction output
│   └── design-references/      # Screenshots
├── scripts/
│   ├── sync-agent-rules.sh     # Regenerate agent instructions
│   └── sync-skills.mjs         # Regenerate /clone-website
├── AGENTS.md                   # Single source of truth (instructions)
├── CLAUDE.md                   # Claude Code config
└── GEMINI.md                   # Gemini CLI config
```

---

## Commands

```bash
npm run dev           # Start dev server (port 3000)
npm run build         # Production build
npm run lint          # ESLint
npm run typecheck     # TypeScript check
npm run check         # lint + typecheck + build

# Docker
docker compose up app --build  # Build & run
docker compose up dev --build  # Dev mode (port 3001)
```

---

## Architecture: Source of Truth Pattern

Two files power all platform support. Edit once, regenerate for all agents:

| What | Source of Truth | Sync Command |
|------|---|---|
| Project instructions | `AGENTS.md` | `bash scripts/sync-agent-rules.sh` |
| `/clone-website` skill | `.claude/skills/clone-website/SKILL.md` | `node scripts/sync-skills.mjs` |

**Pattern:** Agents read source files natively (Claude Code reads `AGENTS.md` + `CLAUDE.md` directly). Sync scripts regenerate platform-specific copies for other agents.

---

## Key Insights

### 1. Specification-Driven Parallel Building
- Each component builder receives **exact computed CSS** from the original
- `getComputedStyle()` values extracted during reconnaissance
- No approximation or style guessing
- Reduces iteration loops dramatically

### 2. Design System Extraction
- Colors, fonts, spacing automatically extracted
- Stored in Tailwind config (OKLCH tokens)
- Applied globally
- Enables consistent design scaling

### 3. Asset Management
- Images, videos, SVGs downloaded automatically
- Organized in `public/`
- SVG icons extracted and converted to components
- No broken links

### 4. Agent Agnostic
- Single `AGENTS.md` source of truth
- Works with 11+ different AI coding agents
- No lock-in to one platform
- Sync scripts keep all platforms in sync

---

## Integration with OpenClaw/Claude Code

**Recommended setup:** Claude Code (Opus 4.6) in OpenClaw environment
- Full browser inspection
- Chrome automation
- Parallel worktree builders
- Git operations
- File I/O

**Workflow:**
1. Load template into Claude Code workspace
2. Point `/clone-website` at target URL
3. Agent reconstructs entire site in Next.js
4. Test locally with `npm run dev`
5. Modify/customize as needed

---

## Relationships & Dependencies

### Depends on
- **AI Coding Agent** (Claude Code, Cursor, etc.)
- **Next.js 16** ecosystem
- **shadcn/ui** component library

### Integrates with
- Git (worktree-based parallel building)
- Tailwind CSS (design system extraction)
- Radix UI (primitives)

### Related Tools
- Claude Design (visual handoff from prototype)
- Claude Code (implementation)
- shadcn/ui (component library)
- **[Startupa.ge - Platform for Founders, Investors & Talent](../syntheses/startupa-ge-platform-for-founders-investors-talent.md)** — Template utile per creare piattaforme di startup simili
- **[Impeccable.style - AI Design Tool](../syntheses/impeccable-style-ai-design-tool.md)** — Tool complementare per il design workflow

---

## Use Case: SME Website Modernization

**Scenario:** Small business built site on Webflow 5 years ago, now wants to own the codebase.

**Workflow:**
1. Clone template
2. Run `/clone-website https://their-website.webflow.io`
3. Agent extracts design system, components, content structure
4. Outputs modern Next.js codebase in ~30 minutes
5. SME can now:
   - Host on Vercel/own servers
   - Customize components freely
   - Integrate with backend
   - Version control everything

**Value:**
- Frees from platform lock-in
- Retains design fidelity
- Modern, maintainable codebase
- Full source code ownership

---

## Categories
AI coding agents, web development, Next.js, reverse engineering, design systems, parallel building, open source, template, Claude Code

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Introducing Claude Design by Anthropic Labs](anthropic-claude-design-labs.md)
- [Startupa.ge - Platform for Founders, Investors & Talent](../syntheses/startupa-ge-platform-for-founders-investors-talent.md)
<!-- openclaw:wiki:related:end -->
