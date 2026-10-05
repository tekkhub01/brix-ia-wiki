---
title: "Span-Level Attribution"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md, sources/the-facts-grounding-leaderboard-jacovi-et-al-arxiv-2501-03200.md, sources/ragtruth-a-hallucination-corpus-wu-et-al-arxiv-2401-00396.md, sources/cited-but-not-verified-abs.md]
created: 2026-04-28
updated: 2026-10-04
verified: 2026-10-04
tags: [grounding, citations, evaluation]
aliases: [Span-Level Attribution, Citation Grounding]
confidence: high
summary: "Forcing per-sentence source citations to make generation auditable. Document-level attribution is largely solved; precise span localization is not."
volatility: warm
publish: true
---
# Span-Level Attribution

**Type:** Grounding technique for LLM outputs  
**Also called:** Citation grounding, evidence-based generation  
**Used in:** [[notebooklm|NotebookLM]], some [[agentic-rag|Agentic RAG]] systems, research prototypes

## Core idea

Force the LLM to attach a source identifier (chunk ID, span range, or document coordinate) to **every sentence** it generates. The system can then:
- Verify the claim exists in the cited source
- Highlight the exact source text for user inspection
- Discard sentences without valid citations

## How it works (technical)

During text generation, the model is prompted to emit special hidden tokens (not shown to user) interleaved with normal text:

```
<sentence>The capital of France is Paris.</sentence>
<span id="chunk_42" start="120" end="135"/>
<sentence>Paris is known for the Eiffel Tower.</sentence>
<span id="chunk_17" start="45" end="67"/>
```

UI layer reads these markers and creates clickable footnotes linking to original PDF locations.

## Why it matters

- **Reduces hallucinations**: model cannot invent facts without citing a source; if source doesn't support claim, citation fails → sentence dropped
- **Auditability**: every fact traceable to exact document + character offset
- **Trust**: user sees provenance inline (like academic citations but per-sentence)

## Limits

- Model can still misattribute (cite wrong chunk)
- Does not prevent cherry-picking (only citing supportive spans, ignoring contradictory ones)
- Requires retrieval to be recall-rich enough to actually contain answer
- Adds overhead to generation (hidden tokens, post-processing validation)

## Implementation patterns

1. **Constraint prompting** ("Answer only from sources; each sentence must cite")
2. **Post-generation verification**: generate first, then retrieve supporting spans; reject unsupported sentences
3. **Reward models** during training to enforce citation behavior
4. **Deterministic decoder constraints** (not yet mainstream) to force citation tokens

## Relation to RAG family

- Classic [[rag|RAG]]: provides context but no forced attribution
- [[agentic-rag|Agentic RAG]]: validator agent can enforce span-level checks before final answer
- [[notebooklm|NotebookLM]]: first product to ship this at scale (Gemini-based)
- [[llm-wiki-karpathy|LLM Wiki]]: provenance inherent (notes directly link to source documents; synthesis traceable via edit history)

## Benchmarks and measured performance (2026)

- **FACTS Grounding** ([Jacovi et al., arXiv 2501.03200](../sources/the-facts-grounding-leaderboard-jacovi-et-al-arxiv-2501-03200.md), Google DeepMind) — each prompt pairs a request with a full document up to **32k tokens**, requiring a long-form response fully grounded in that document. Judging is automated and two-phase: (1) responses that don't fulfil the request are disqualified outright, (2) surviving responses are judged on groundedness. The final factuality score is an **aggregate of multiple judge models** (multi-judge consensus, chosen via held-out test-set prompt selection) to mitigate evaluation bias; public + private splits guard leaderboard integrity.
- **RAGTruth** ([Wu et al., arXiv 2401.00396](../sources/ragtruth-a-hallucination-corpus-wu-et-al-arxiv-2401-00396.md), ACL 2024) — the corpus behind the failure-rate figures below: **nearly 18,000 naturally generated RAG responses** (not "chunks" — the unit is the response), manually annotated at case *and word* level with hallucination intensity. Its headline transferable finding: a small LLM fine-tuned on RAGTruth matches prompt-based GPT-4-level hallucination detection.
- **ALCE / ASQA / BioASQ / ExpertQA** — score citation quality on three separable axes: document-level correctness, **evidence span identification**, and claim-citation faithfulness.
- **[Explicit Evidence Grounding via Structured Inline Citation Generation](https://arxiv.org/html/2606.07130)** — inline structured citation emission, the direct descendant of the hidden-token scheme described above.

**The central empirical finding, and it validates the "Limits" section above:** models are broadly good at identifying the *right document* and materially worse at identifying the *precise supporting span within it*. Document-level attribution is largely solved; span-level is not.

Groundedness failure rates are non-trivial even at the frontier: on RAGTruth's ~18K labeled responses the median frontier model fails groundedness on **5–8%** of answers (the corpus itself is now in the vault; this specific percentage is still secondhand — it is not in the abstract, it is in the paper's benchmark tables). The characteristic 2026 production failure mode is a high grounded-response score paired with a much lower claim-to-citation *alignment* rate — i.e. the citation exists and the source is real, but it does not actually support the specific sentence attached to it. Which is precisely the misattribution risk this page's Limits section flags.

**[Cited but Not Verified](../sources/cited-but-not-verified-abs.md)** (Onweller et al., arXiv 2605.06635 — abstract in vault dal 2026-10-04) applies this to deep-research agents specifically, and now with its primary source: the framework scores citations on three axes (**Link Works / Relevant Content / Fact Check**), and the shape of the failure is exactly this page's thesis — frontier models pass link validity at **94%+** and relevance at **80%+** while factual accuracy sits at **39–77%**. The paper's own ablation adds the depth effect the corpus carried secondhand: Fact Check accuracy **drops ~42%** as tool calls scale from 2 to 150 — "more retrieval does not produce more accurate citations" is the authors' conclusion, not an inference. Fewer than half of open-source models produce cited reports at all in one-shot: attribution is a trained capability, not a formatting instruction.

## Future research

- **Automatic chunk ID resolution**: instead of human-crafted span IDs, use dense retrieval to find supporting spans post-hoc
- **Citation precision vs recall trade-off**: strict attribution may reduce answer completeness
- **Multi-source synthesis**: how to attribute when answer combines 3–4 sources clearly? (partially characterized by *Cited but Not Verified*, not solved)
- **Closing the span gap**: why document-level retrieval succeeds where span-level localization fails, given the model has the document in context

## See Also

- [[agentic-rag|Agentic RAG]]
- [[rag|RAG (Retrieval-Augmented Generation)]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[notebooklm]] — links here
- [[grounding-across-architectures]] — synthesis drawing on this page
- [[notebooklm-hybrid-stack]] — synthesis drawing on this page

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
