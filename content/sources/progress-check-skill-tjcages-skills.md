---
pageType: source
id: source.progress-check-skill-tjcages-skills
title: progress-check — skill (tjcages/skills)
sourceType: local-file
sourcePath: https://github.com/tjcages/skills/tree/main/progress-check/skills/progress-check
ingestedAt: 2026-08-28T09:05:59.722Z
updatedAt: 2026-08-28T09:05:59.722Z
status: active
publish: true
date: 2026-08-28
url: https://github.com/tjcages/skills/tree/main/progress-check/skills/progress-check
tags: [openclaw, claude-code, skills, agent-ux, progress]
name: progress-check
license: MIT
metadata:
  version: 1.0.1
description: Give sparse, evidence-based progress updates for long-running agent
  tasks and projects. Use when work will take more than 15 minutes, spans
  multiple milestones, involves delegated agents, or when the user asks for
  progress bars, status cadence, fewer updates, or a global cross-agent progress
  rule. Not for short answers or tasks with no meaningful intermediate state.
---

# progress-check — skill (tjcages/skills)

## Source
- Type: `local-file`
- Origine: https://github.com/tjcages/skills/tree/main/progress-check/skills/progress-check
- Bytes: 3369
- Updated: 2026-08-28T09:05:59.722Z

## Content
## Progress Check

Full method: [METHODOLOGY.md](https://github.com/tjcages/skills/blob/main/progress-check/skills/progress-check/METHODOLOGY.md). Chat shape:
[RESPONSE.md](https://github.com/tjcages/skills/blob/main/progress-check/skills/progress-check/RESPONSE.md). Examples: [EXAMPLES.md](https://github.com/tjcages/skills/blob/main/progress-check/skills/progress-check/EXAMPLES.md).

### Choose the mode

- **Report progress:** default for qualifying long-running work.
- **Install globally:** only when the user asks to persist this behavior across
  agents or projects.

### Report progress

1. Define a small set of observable milestones before estimating a percentage.
   Weight by work and risk, not elapsed time.
2. Send one baseline update after scope is understood.
3. Send a routine update only when at least 30 minutes have passed **and** one
   of these is true: a milestone completed, verified progress rose by at least
   10 percentage points, or the next action materially changed.
4. Report a new blocker immediately when the user can act on it. Report
   completion immediately.
5. Never repeat an unchanged bar or send a routine “still working” message.

Keep each update to at most three short items: completed evidence, current
work, and next step or blocker. End with exactly one overall bar styled as
inline code on its own line:

`Performance rollout  [██████████████████░░] 90%`

Use one pair of backticks for inline-code styling. Do not indent the line by
four spaces and do not use a fenced code block; both create a separate block
that interfaces may label or make copyable.

- Replace the label with a short task-specific label.
- Use 20 cells: `█` completed and `░` remaining.
- Round down to the nearest 5% unless completion evidence supports 100%.
- Show only the overall bar unless the user requests subtask bars.
- In multi-agent work, only the coordinator shows the overall bar.
- The progress line is the final content in the update. End immediately after
  it with no note, recap, or closer.

### Install globally

Prefer installing this skill globally through the available Agent Skills CLI
so one source works across supported agents:

```bash
npx skills add tjcages/skills --skill progress-check -g --agent '*'
```

If the user explicitly requests native always-on instructions instead:

1. Detect each installed agent's documented user-level instruction mechanism.
2. Merge the progress rules without overwriting existing instructions.
3. Make the change idempotent and avoid repository-level instruction files.
4. If an agent supports only UI-managed rules, give the exact settings location
   and a copy-ready block instead of inventing a file path.
5. Verify each changed target and state whether a new session is required.

Do not claim an unsupported agent was configured. Do not modify unrelated
preferences.

## Notes
<!-- openclaw:human:start -->
### Nel vault
- Sintesi: [Skill OpenClaw: progress-check (barre di avanzamento ASCII)](../syntheses/skill-openclaw-progress-check-barre-di-avanzamento-ascii.md) — dove sono registrati i due claim del forward Telegram che questa fonte **non** conferma
- [Claude Code Tips (ykdojo/claude-code-tips)](claude-code-tips-ykdojo-claude-code-tips.md) — stesso meccanismo di distribuzione delle skill
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Claude Code Tips (ykdojo/claude-code-tips)](claude-code-tips-ykdojo-claude-code-tips.md)
- [Skill OpenClaw: progress-check (barre di avanzamento ASCII)](../syntheses/skill-openclaw-progress-check-barre-di-avanzamento-ascii.md)
<!-- openclaw:wiki:related:end -->
