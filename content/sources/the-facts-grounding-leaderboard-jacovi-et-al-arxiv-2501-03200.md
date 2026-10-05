---
pageType: source
id: source.the-facts-grounding-leaderboard-jacovi-et-al-arxiv-2501-03200
title: The FACTS Grounding Leaderboard (Jacovi et al., arXiv 2501.03200)
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/facts-grounding-leaderboard-abs.md
ingestedAt: 2026-09-27T04:06:34.660Z
updatedAt: 2026-09-27T04:06:34.660Z
status: active
date: 2025-01-06
tags: [source, llm-memory, ingest]
url: https://arxiv.org/abs/2501.03200
publish: true
---

# The FACTS Grounding Leaderboard (Jacovi et al., arXiv 2501.03200)

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/facts-grounding-leaderboard-abs.md`
- Bytes: 1800
- Updated: 2026-09-27T04:06:34.660Z

## Content
### The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input

Jacovi et al. (Google DeepMind). arXiv:2501.03200, 2025-01-06.
URL: https://arxiv.org/abs/2501.03200

### Abstract (verbatim, arXiv abs page, fetched 2026-09-27)

We introduce FACTS Grounding, an online leaderboard and associated benchmark that evaluates language models' ability to generate text that is factually accurate with respect to given context in the user prompt. In our benchmark, each prompt includes a user request and a full document, with a maximum length of 32k tokens, requiring long-form responses. The long-form responses are required to be fully grounded in the provided context document while fulfilling the user request. Models are evaluated using automated judge models in two phases: (1) responses are disqualified if they do not fulfill the user request; (2) they are judged as accurate if the response is fully grounded in the provided document. The automated judge models were comprehensively evaluated against a held-out test-set to pick the best prompt template, and the final factuality score is an aggregate of multiple judge models to mitigate evaluation bias. The FACTS Grounding leaderboard will be actively maintained over time, and contains both public and private splits to allow for external participation while guarding the integrity of the leaderboard.

### Key facts for the corpus

- Confirms and sharpens [span-level-attribution](../concepts/span-level-attribution.md)'s one-liner: 32k-token document cap, long-form responses, two-phase automated judging (instruction-following disqualification first, then groundedness), **aggregate of multiple judge models** (multi-judge consensus) chosen via held-out test-set prompt selection, public+private splits, hosted at kaggle.com/facts-leaderboard.


## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
