---
pageType: source
id: source.self-rag-asai-et-al-arxiv-2310-11511-abstract
title: Self-RAG (Asai et al., arXiv 2310.11511) — abstract
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/self-rag-abs.md
ingestedAt: 2026-10-11T04:05:41.420Z
updatedAt: 2026-10-11T04:05:41.420Z
status: active
date: 2023-10-17
tags: [source, llm-memory, ingest, rag]
url: https://arxiv.org/abs/2310.11511
publish: true
---

# Self-RAG (Asai et al., arXiv 2310.11511) — abstract

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/self-rag-abs.md`
- Bytes: 3469
- Updated: 2026-10-11T04:05:41.420Z

## Content

## Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

Asai, Wu, Wang, Sil, Hajishirzi. arXiv:2310.11511, v1 2023-10-17.
URL: https://arxiv.org/abs/2310.11511

### Abstract (verbatim, arXiv abs page, fetched 2026-10-11)

Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate. Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation. We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (Self-RAG) that enhances an LM's quality and factuality through retrieval and self-reflection. Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its own generations using special tokens, called reflection tokens. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. Experiments show that Self-RAG (7B and 13B parameters) significantly outperforms state-of-the-art LLMs and retrieval-augmented models on a diverse set of tasks. Specifically, Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models.

### Key facts for the corpus

- **The mechanism [agentic-rag](../concepts/agentic-rag.md) describes without attribution has a name and a date.** The page's "validator agent that cross-checks the answer against retrieved spans and demands citations" is, in its original academic form, Self-RAG's **reflection tokens**: a single LM trained to emit special tokens that retrieve on demand (`Retrieve`), judge whether retrieved passages are relevant (`ISREL`), whether its own generation is supported by them (`ISSUP`), and whether it is useful (`ISUSE`). "Critique through self-reflection" is literally the paper's subtitle.
- **Self-RAG is a trained single model, not an agent loop.** The critique is internalized in the generator via special tokens, not delegated to a separate validator agent. Agentic RAG (2026 wave) externalizes the same check into a second model in the loop. The lineage is: Self-RAG (2023, reflection tokens) → agentic validation (2026, separate verifier step).
- **The motivation matches the corpus's own argument against blind retrieval**: "indiscriminately retrieving and incorporating a fixed number of retrieved passages... diminishes LM versatility" — the same reasoning behind adaptive/agentic retrieval in [agentic-rag](../concepts/agentic-rag.md).
- **Measured claim available**: 7B/13B Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on open-domain QA, reasoning and fact verification, with significant gains in factuality and citation accuracy for long-form generation. (Headline numbers are in the paper body, not the abstract; do not cite specific scores from this source.)
- Date: October 2023 — the academic precursor, ~2.5 years before the agentic-GraphRAG wave the corpus describes.


## Notes
<!-- openclaw:human:start -->

### Collegamenti (audit 2026-10-22)
- Concetto di riferimento: [[topics/llm-memory/wiki/concepts/rag|RAG]] e [[topics/llm-memory/wiki/concepts/agentic-rag|Agentic RAG]] — Self-RAG è il classico pattern di recupero autodeterminato
- Applicazione nostra: Architettura retrieval stratificata
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
