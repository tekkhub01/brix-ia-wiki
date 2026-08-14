---
id: claude-opus-4-7-announcement
pageType: source
updatedAt: 2026-04-07T00:00:00Z
publish: true
---

# Claude Opus 4.7 Release Announcement

**Source:** https://www.anthropic.com/news/claude-opus-4-7
**Date:** April 2026
**Author:** Anthropic
**Type:** Product announcement / Release notes

---

## Overview

Claude Opus 4.7 is now generally available. It represents a notable improvement over Opus 4.6 in advanced software engineering, with particular gains on the most difficult tasks.

### Key Features

- **Advanced coding:** Better at complex, long-running tasks with rigor and consistency
- **Vision improvements:** Accepts images up to 2,576 pixels on the long edge (~3.75 megapixels), 3.75x more than prior Claude models
- **Instruction following:** Substantially better at following instructions literally
- **Memory:** Better at using file system-based memory across multi-session work

### Performance Highlights

- **Software Engineering:** Handles complex coding work previously needing close supervision
- **Vision:** Tasteful and creative on professional tasks (interfaces, slides, docs)
- **Benchmarks:** Better results than Opus 4.6 across multiple benchmarks
- **Finance Agent:** State-of-the-art on finance domain evaluations
- **Real-world work:** More effective as a finance analyst, producing rigorous analyses and professional presentations

### Effort Levels

Introduces **xhigh** ("extra high") effort level between high and max, for finer control over reasoning vs. latency tradeoff.

### Safety & Alignment

- Similar safety profile to Opus 4.6
- Improvements on honesty and resistance to prompt injection attacks
- Modestly weaker on some measures (e.g., harm-reduction advice on controlled substances)
- Assessment: "largely well-aligned and trustworthy, though not fully ideal in its behavior"

### Pricing & Availability

- **Cost:** $5 per million input tokens, $25 per million output tokens (same as Opus 4.6)
- **Available:** Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry
- **API model:** `claude-opus-4-7`

### Technical Changes for Migration

1. **Tokenizer update:** Same input → 1.0–1.35× more tokens (depending on content type)
2. **Higher thinking at xhigh/max effort:** More output tokens on agentic workflows
3. **Mitigation:** Use effort parameter, task budgets, or conciseness prompts

### Early Testing Feedback

Positive feedback from:
- Stripe (financial platforms, accelerated development velocity)
- Cursor (51% improvement on coding benchmark vs. Opus 4.6)
- Notion (14% improvement on multi-step workflows, fewer tool errors)
- Databricks (21% fewer errors on document reasoning)
- Many others (see full article for detailed quotes)

### Cybersecurity Safeguards

- Includes safeguards that automatically detect and block high-risk cybersecurity requests
- Security professionals can apply for **Cyber Verification Program** for legitimate use cases (vulnerability research, penetration testing, red-teaming)

---

## Additional Launches

- **Task budgets (beta):** API feature for guiding Claude's token spend on long-running tasks
- **/ultrareview command:** Claude Code dedicated review session for bug/design issue detection
- **Auto mode (Max users):** Claude makes decisions autonomously with fewer interruptions

---

## Key Insight

Opus 4.7 is positioned as a step-change improvement for agentic, long-running, and complex tasks rather than general capability—Mythos Preview remains the most capable model, but 4.7 shows better practical performance on real-world workflows.

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Anthropic](../entities/anthropic.md)
<!-- openclaw:wiki:related:end -->
