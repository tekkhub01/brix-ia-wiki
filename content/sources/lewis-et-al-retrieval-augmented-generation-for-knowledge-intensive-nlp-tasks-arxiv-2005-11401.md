---
pageType: source
id: source.lewis-et-al-retrieval-augmented-generation-for-knowledge-intensive-nlp-tasks-arxiv-2005-11401
title: "Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (arXiv 2005.11401)"
sourceType: web
sourcePath: https://arxiv.org/abs/2005.11401
url: https://arxiv.org/abs/2005.11401
ingestedAt: 2026-09-13T06:33:36.566Z
updatedAt: 2026-09-13T06:33:36.566Z
status: active
publish: true
date: 2020-05-22
tags: [rag, retrieval, paper, arxiv, llm-memory]
---

# Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (arXiv 2005.11401)

## Source
- Type: `web` — arXiv abstract page, fetched 2026-09-13 (dreaming sweep)
- URL: https://arxiv.org/abs/2005.11401
- Ingestita come abstract + nota di lettura: il paper integrale non è richiesto dalle pagine del corpus, che citano il solo framework. Chiusura di lewis-rag-original

### Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**arXiv:** 2005.11401
**Authors:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela (Facebook AI Research et al.)
**Published:** 2020-05-22 (v1)

### Abstract

Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

### Why this matters for this vault

This is the origin paper of the entire llm-memory topic — named in the first lines of the `rag` concept page and never linked until now. Two points the corpus states loosely and the paper fixes precisely:

1. **RAG was defined as parametric + non-parametric memory in one model**, fine-tuned jointly — not as the 2023+ production pattern "frozen LLM + retrieved chunks in the prompt". The modern pipeline described in [rag](../concepts/rag.md) is retrieval-*augmented* inference, a descendant that the paper itself anticipates only in the RAG-sequence vs RAG-token distinction.
2. **Provenance and knowledge-updating were stated as open problems in 2020** — the same two axes the LLM Wiki and attribution pages in this vault treat as 2026 concerns. The topic's current frontiers are the paper's own unfinished agenda.


## Notes
<!-- openclaw:human:start -->
- Grounds the origin-paper claim of [RAG (concept)](../concepts/rag.md); link written relative-markdown per the cross-tree footgun rule.
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
