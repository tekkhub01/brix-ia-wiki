---
pageType: source
id: source.lost-in-the-middle-abs
title: "Lost in the Middle: How Language Models Use Long Contexts (Liu et al., arXiv 2307.03172)"
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/lost-in-the-middle-abs.md
ingestedAt: 2026-10-04T04:26:33.294Z
updatedAt: 2026-10-04T04:26:33.294Z
status: active
date: 2023-07-06
tags: [source, llm-memory, ingest, long-context]
url: https://arxiv.org/abs/2307.03172
publish: true
---

# Lost in the Middle: How Language Models Use Long Contexts

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/lost-in-the-middle-abs.md`
- Bytes: 1966
- Updated: 2026-10-04T04:26:33.294Z

## Content

## Lost in the Middle: How Language Models Use Long Contexts

Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang. arXiv:2307.03172, v1 2023-07-06.
URL: https://arxiv.org/abs/2307.03172

### Abstract (verbatim, arXiv abs page, fetched 2026-10-04)

While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how models use their input context and provides new evaluation protocols for future long-context language models.

### Key facts for the corpus

- The **U-shaped positional curve** is the finding: performance highest at beginning or end of context, significantly degraded in the middle — "**even for explicitly long-context models**". A bigger window does not imply the content is used well; this is the caveat [long-context-models](../concepts/long-context-models.md) was missing.
- Two task families: multi-document QA and key-value retrieval. Both are about *locating* relevant information, not reasoning over it — the failure is attention/placement, not capability.
- Date: July 2023, pre-dating the 1M-token tier the page describes. The finding is about models of its time; whether it persists at 1M is an open empirical question the page should state, not assume away.

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
