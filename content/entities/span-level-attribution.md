---
id: span-level-attribution
pageType: entity
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-08-12T00:00:00Z
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

- **FACTS Grounding** — enforces attribution at sentence/span level and uses a *consensus of multiple LLM judges* rather than a single grader. Each prompt pairs a request with a full document up to 32k tokens; every substantive claim must be supported by that context.
- **ALCE / ASQA / BioASQ / ExpertQA** — score citation quality on three separable axes: document-level correctness, **evidence span identification**, and claim-citation faithfulness.
- **[Explicit Evidence Grounding via Structured Inline Citation Generation](https://arxiv.org/html/2606.07130)** — inline structured citation emission, the direct descendant of the hidden-token scheme described above.

**The central empirical finding, and it validates the "Limits" section above:** models are broadly good at identifying the *right document* and materially worse at identifying the *precise supporting span within it*. Document-level attribution is largely solved; span-level is not.

Groundedness failure rates are non-trivial even at the frontier: on RAGTruth's ~18K labeled response chunks the median frontier model fails groundedness on **5–8%** of answers. The characteristic 2026 production failure mode is a high grounded-response score paired with a much lower claim-to-citation *alignment* rate — i.e. the citation exists and the source is real, but it does not actually support the specific sentence attached to it. Which is precisely the misattribution risk this page's Limits section flags.

**[Cited but Not Verified](https://arxiv.org/pdf/2605.06635)** applies this to deep-research agents specifically, and answers one of the open questions below from the negative direction: multi-source synthesis attribution is where parsing and verification of agent citations most often breaks down.

## Future research

- **Automatic chunk ID resolution**: instead of human-crafted span IDs, use dense retrieval to find supporting spans post-hoc
- **Citation precision vs recall trade-off**: strict attribution may reduce answer completeness
- **Multi-source synthesis**: how to attribute when answer combines 3–4 sources clearly? (partially characterized by *Cited but Not Verified*, not solved)
- **Closing the span gap**: why document-level retrieval succeeds where span-level localization fails, given the model has the document in context

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agentic RAG](agentic-rag.md)
- [Claude (Anthropic)](claude-anthropic.md)
- [Context Caching](context-caching.md)
- [GLM 5.1](glm-5.1.md)
- [GraphRAG](graphrag.md)
- [LLM Wiki (Karpathy Pattern)](llm-wiki-karpathy.md)
- [Long-Context Models](long-context-models.md)
- [NotebookLM (Google)](notebooklm.md)
- [Quantization](quantization.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
<!-- openclaw:wiki:related:end -->
