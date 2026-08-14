---
id: context-caching
pageType: entity
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-08-12T00:00:00Z
publish: true
---
# Context Caching

**Type:** LLM inference optimization technique  
**Introduced:** 2024–2025 (Gemini API, OpenAI, Anthropic)  
**Purpose:** Avoid recomputing embeddings/attention for static prompt prefixes across repeated queries

## Mechanism

Instead of re-processing the same long system prompt + document chunks on every query:

1. **Initial call**: system prompt + static context → processed → cached in GPU memory (KV cache + embedding layers)
2. **Subsequent calls**: only new user query tokens computed; cached prefix re-used from memory
3. Cache invalidated when underlying sources change

**The one invariant everything else follows from: caching is a *prefix match*.** A single byte changed anywhere in the prefix invalidates every cache point at or after that position. Render order on the Anthropic API is `tools` → `system` → `messages`, so a breakpoint on the last system block covers tools + system together.

## Economics (Anthropic, verified 2026-08)

| | Multiplier vs base input |
|---|---|
| Cache **read** | ~0.1× |
| Cache **write**, 5-minute TTL | 1.25× |
| Cache **write**, 1-hour TTL | 2× |

Break-even therefore depends on TTL: **two** requests with the 5-minute TTL (1.25 + 0.1 = 1.35 vs 2.0 uncached), but **three** with the 1-hour TTL (2.0 + 0.2 = 2.2 vs 3.0). The 1h TTL buys survival across gaps in bursty traffic at the cost of needing more reads to pay for itself.

Max 4 `cache_control` breakpoints per request.

## Footgun: the minimum cacheable prefix is not monotonic

Below the minimum, caching silently does nothing — no error, just `cache_creation_input_tokens: 0`:

| Model | Minimum |
|---|---|
| Claude Opus 5, Fable 5, Mythos 5 | 512 tokens |
| Opus 4.8, Sonnet 5, Sonnet 4.6/4.5 | 1024 tokens |
| Opus 4.7, Haiku 3.5 | 2048 tokens |
| Opus 4.6, Opus 4.5, Haiku 4.5 | 4096 tokens |

**It gets *worse* on older models, not better** — a 3K-token prompt caches on Opus 5 and Sonnet 4.5 and silently does not on Opus 4.6 or Haiku 4.5. Anything routing across a model mix needs to check per-model, not assume a floor.

## Invalidation hierarchy

Not every change costs everything. Three tiers, and a change only invalidates its own tier and below:

- **Tool definitions or model switch** → destroys tools + system + messages caches
- **System prompt content** → keeps tools, destroys system + messages
- **Message content, `tool_choice`, images, thinking on/off** → keeps tools + system

So toggling `tool_choice` or thinking per-request is cheap; changing the tool list mid-conversation is not. Two escape hatches exist: `tool_addition`/`tool_removal` blocks (Claude Opus 5, beta) change the tool set without invalidating, and mid-conversation `{"role": "system"}` messages inject operator context without touching the cached top-level system prompt. Model switching has no escape hatch — caches are model-scoped.

## Silent invalidators to grep for

`datetime.now()` / `Date.now()` in a system prompt; `uuid4()` early in content; `json.dumps()` without `sort_keys=True`; iterating a `set`; session or user IDs interpolated into the system prompt; conditional system sections. Each one makes the prefix unique per request, so the cache write is paid every time and never read. The tell is `cache_read_input_tokens` stuck at zero across identical-looking requests.

## Trade-offs

- Cache storage expensive (GPU RAM); limited capacity
- Cache eviction policies matter (LRU, TTL)
- Works best when source set stable (not changing every query)
- Only 20 content blocks of lookback per breakpoint — long agentic turns that add more than that per turn silently stop matching
- Concurrent requests with the same prefix all miss: the entry is only readable once the first response *starts streaming*. Fan-out patterns should send one request, await first token, then fire the rest
- Cloud-only (Google Gemini, Anthropic, OpenAI); on-premise implementations rare

## Relevance to local deployment

For on-premise LLM (GLM 5.1 + vLLM/KTransformers), similar techniques exist:
- **vLLM PagedAttention** caches KV across requests (but not named "context caching")
- **KTransformers** offloads KV cache to CPU/GPU split
- Custom implementation possible: precompute document embeddings once, reuse across queries with prefix caching

## Related entries

- [[notebooklm|NotebookLM]] — prominent example using Context Caching
- [[quantization|Quantization]] — complementary optimization (reduces size of cached tensors)
- [[long-context-models|Long-Context Models]] — benefit most from caching

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Long-Context Models](long-context-models.md)

### Related Pages

- [Agentic RAG](agentic-rag.md)
- [Claude (Anthropic)](claude-anthropic.md)
- [GLM 5.1](glm-5.1.md)
- [GraphRAG](graphrag.md)
- [LLM Wiki (Karpathy Pattern)](llm-wiki-karpathy.md)
- [NotebookLM (Google)](notebooklm.md)
- [Quantization](quantization.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
- [Span-Level Attribution](span-level-attribution.md)
<!-- openclaw:wiki:related:end -->
