---
pageType: source
id: source.ragtruth-a-hallucination-corpus-wu-et-al-arxiv-2401-00396
title: "RAGTruth: A Hallucination Corpus (Wu et al., arXiv 2401.00396)"
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/ragtruth-hallucination-corpus-abs.md
ingestedAt: 2026-09-27T04:06:41.534Z
updatedAt: 2026-09-27T04:06:41.534Z
status: active
date: 2023-12-31
tags: [source, llm-memory, ingest]
url: https://arxiv.org/abs/2401.00396
publish: true
---

# RAGTruth: A Hallucination Corpus (Wu et al., arXiv 2401.00396)

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/ragtruth-hallucination-corpus-abs.md`
- Bytes: 2035
- Updated: 2026-09-27T04:06:41.534Z

## Content
### RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models

Wu et al. arXiv:2401.00396, v1 31 Dec 2023, v2 17 May 2024 (ACL 2024).
URL: https://arxiv.org/abs/2401.00396

### Abstract (verbatim, arXiv abs page, fetched 2026-09-27)

Retrieval-augmented generation (RAG) has become a main technique for alleviating hallucinations in large language models (LLMs). Despite the integration of RAG, LLMs may still present unsupported or contradictory claims to the retrieved contents. In order to develop effective hallucination prevention strategies under RAG, it is important to create benchmark datasets that can measure the extent of hallucination. This paper presents RAGTruth, a corpus tailored for analyzing word-level hallucinations in various domains and tasks within the standard RAG frameworks for LLM applications. RAGTruth comprises nearly 18,000 naturally generated responses from diverse LLMs using RAG. These responses have undergone meticulous manual annotations at both the individual cases and word levels, incorporating evaluations of hallucination intensity. We not only benchmark hallucination frequencies across different LLMs, but also critically assess the effectiveness of several existing hallucination detection methodologies. Furthermore, we show that using a high-quality dataset such as RAGTruth, it is possible to finetune a relatively small LLM and achieve a competitive level of performance in hallucination detection when compared to the existing prompt-based approaches using state-of-the-art large language models such as GPT-4.

### Key facts for the corpus

- Verifies [span-level-attribution](../concepts/span-level-attribution.md)'s "~18K labeled response chunks": the corpus is **nearly 18,000 naturally generated RAG responses**, manually annotated at case AND word level with hallucination intensity. The page's "response chunks" wording is imprecise — they are responses, annotated at word level.
- The "5–8% median frontier failure" figure is NOT in the abstract: remains secondhand, flagged.


## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
