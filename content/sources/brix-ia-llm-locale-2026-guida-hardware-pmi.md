---
id: brix-ia-llm-locale-2026-guida-hardware-pmi
pageType: source
updatedAt: 2026-09-13T04:40:00Z
publish: true
---

# Come Usare un LLM in Locale nel 2026: Guida Hardware per PMI con Prezzi, Benchmark e 3 Fasce di Budget

**Source:** https://brix-ia.com/blog/llm-locale-2026-guida-hardware-pmi-prezzi-benchmark/
**Author:** BRIX-IA
**Date:** 2026
**Type:** Detailed guide with benchmarks, hardware comparison, and procurement strategies for SMEs
**Internal Reference:** Peter K., Fondatore BRIX-IA

---

## Executive Summary

The real bottleneck in local LLM inference is **memory bandwidth**, not TFLOPS. Choice of hardware matters dramatically: wrong choice = 4 tokens/second; right choice = 80+ tokens/second on same model.

### Key Insight
GPU power is marketing noise. What matters:
- **Unified memory architecture** (same pool for CPU+GPU)
- **High bandwidth memory** (273 GB/s GB10 vs. 32 GB/s PCIe bottleneck)
- **Model architecture** (Mixture of Experts = 3-5x speedup vs. dense models)

---

## 1. The Real Problem: Not Compute Power, Memory Bandwidth

### The Physics

When an LLM generates a token, it reads all model parameters from memory **once per token**:
- 70B param model in Q4: ~40 GB
- GB10 bandwidth: 273 GB/s → ~6-7 tok/s theoretical max
- Ryzen AI entry: 89 GB/s → ~2.2 tok/s max
- Speed scales **linearly with bandwidth**, not TFLOPS

### Example: RTX 5090 Bottleneck

- RTX 5090 alone: €3.000-3.500
- Full rig: €5.000+ (CPU, RAM, motherboard)
- PCIe bus: ~32 GB/s real throughput
- Penalty when model exceeds VRAM: 30x slowdown
- **Result:** Less flexible, worse context window than GB10 at €3.900

### The Kickstarter Fallacy: Tiiny AI Pocket Lab

Claimed: 40 tok/s on 120B parameters, 200 GB/s bandwidth
Reality: 200 GB/s + 120B INT4 (60 GB) = max 3.3 tok/s theoretical
Only plausible explanation: marketing counts total parameters, not active (Mixture of Experts trick)

---

## 2. Hardware Timeline: From CUDA Silos to Unified Memory

### 2007-2020: CUDA Dominance & PCIe Bottleneck

- CUDA locks the ecosystem (AlexNet 2012)
- GPU + CPU separate, connected by slow PCIe corridor
- VRAM~1000 GB/s internal, but only 32 GB/s across PCIe = 30x penalty

### 2020: Apple M1 Unified Memory (5 years ahead)

- Unified RAM pool for CPU+GPU
- No PCIe bottleneck
- Problem: No CUDA, useless for serious AI work
- 546 GB/s on Mac Studio M4 Max (best single-machine bandwidth today)

### 2024: AMD Ryzen AI Max+ (democratizing the solution)

- HBM memory soldered directly to processor
- No PCIe, no latency
- 89-256 GB/s bandwidth
- Windows + Linux, ROCm + Ollama work
- Price: ~€999-1.200

### 2025: NVIDIA GB10 Grace Blackwell (finally, CUDA + unified memory)

- 128 GB LPDDR5X unified at 273 GB/s
- ARM Grace CPU + Blackwell GPU via NVLink-C2C
- Native CUDA support
- Only consumer device with both unified memory AND CUDA
- Price: €3.900-4.200
- Problem: Qwen 70B dense only 4.7 tok/s (need MoE models)

---

## 3. Benchmark Comparison: GB10 vs RTX 4090 vs Mac Studio M4 Max

### GB10 vs RTX 4090 Performance Reality

| Hardware | Qwen 70B (Q4) | Qwen 35B-A3B MoE | Context 16K | Cost (IT) |
|----------|---|---|---|---|
| **GB10** | 4.7 tok/s | 82-102 tok/s | 47 tok/s | €3.900 |
| **RTX 4090 single** | 8-12 tok/s (VRAM limit) | 24-28 tok/s | Hits VRAM wall | €5.000 rig |
| **2x RTX 4090** | N/A (doesn't fit) | 15-20 tok/s | ~80 tok/s | €5.500 |
| **Mac Studio M4 Max** | ~8 tok/s | ~60 tok/s | ~40 tok/s (Mac optimized) | €3.999 |

### The Ryzen AI Max+ Reality

- Geekom A9 Max: €1.281
- 128 GB LPDDR5X, 89-256 GB/s
- Qwen 35B-A3B MoE: 15-18 tok/s
- Qwen 70B Q4: 2.2 tok/s (slow)
- **Sweet spot:** MoE 14B-35B models only

### The Cluster Advantage: Two GB10 Connected

- 256 GB unified memory distributed
- CUDA + 10GbE networking natively
- Qwen 235B-A22B MoE: interactive speed
- Infrastructure most powerful for local use today
- Price: ~€8.000

---

## 4. Mixture of Experts (MoE): The Game Changer

### How MoE Works

- Total parameters: 235 billion
- Active per token: 22 billion
- Router selects 2-4 experts per token
- Same speedup on hardware that would do 4.7 tok/s on dense 70B → 27 tok/s on MoE 235B

### MoE Models Dominating in 2026

60%+ of new open-source models use MoE:
- DeepSeek-R1
- Kimi K2
- Qwen 3.5
- Llama-4 Scout

### Performance Jump: Dense vs MoE on GB10

| Model | Total Params | Active Params | GB10 Performance |
|-------|---|---|---|
| Llama 70B (dense) | 70B | 70B | 4.7 tok/s |
| Qwen 34B (dense) | 34B | 34B | 61 tok/s |
| Qwen 35B-A3B (MoE) | 35B | 3.3B | **82-102 tok/s** |
| Qwen 122B-A10B (MoE) | 122B | 10B | 27-29 tok/s |
| Qwen 235B-A22B (MoE) | 235B | 22B | Interactive speed |

---

## 5. Long Context & RAG: The Real-World Benchmark

### The Hidden Performance Cliff

Marketing benchmarks at 512 tokens. Real workloads (RAG, contract analysis, multi-step agents) operate at 16K-128K tokens. KV cache scaling is brutal:

| Setup | 512 tokens | 16K tokens | 128K tokens |
|-------|---|---|---|
| GB10 — Qwen 35B-A3B | 167 tok/s | 47 tok/s | 7.6 tok/s |
| GB10 — Llama 70B dense | 4.7 tok/s | 4.2 tok/s | 3 tok/s |
| Ryzen AI Max+ — Qwen 35B | 55 tok/s | 15 tok/s | 2.5 tok/s |
| 2x RTX 4090 — Qwen 122B | 380 tok/s (batch) | 80 tok/s | VRAM limit |

### Real-World Rule

For RAG/conversational agents: actual context 16K-32K. On that range, GB10 + MoE = **3-5x superior** to Ryzen AI entry-level.

---

## 6. FPGA & ASIC: Beyond GPU

### FPGA: Full Flexibility, High Complexity

- AMD Xilinx Alveo, Intel Agilex
- Deterministic latency, exotic quantization (1-bit, 2-bit) possible
- Requires VHDL/HLS programming — not accessible
- Use case: embedded, edge, specific implementations

### ASIC: Maximum Efficiency, Zero Flexibility

| Chip | Maker | Focus | Notes |
|------|-------|-------|-------|
| TPU v6 Trillium | Google | Cloud training+inference | GCP only |
| Trainium 2 | AWS | Cloud training | EC2 only |
| Groq LPU | Groq | Ultra-fast inference | 500+ tok/s on 70B, cloud |
| **Tenstorrent n300S** | **Tenstorrent** | **Local inference** | **$1.400, buyable** |
| Cerebras WSE-3 | Cerebras | Wafer-scale training | Data center only |

**Key:** Groq proved SRAM on-chip instead of DRAM external = 500+ tok/s possible. Tenstorrent n300S is the only ASIC at consumer prices.

---

## 7. Budget Decision Matrix

### €1.000-1.500: Single Node Entry

| Hardware | Price | Model | Performance | Notes |
|----------|-------|-------|---|---|
| 2x Ryzen 780M mini PC cluster | €1.140 | Qwen 9B-14B | 20-30 tok/s agg. | DIY Linux, no CUDA, Exo/llama.cpp |
| Geekom A9 Max (128GB) | €1.281 | Qwen 35B-A3B Q4 | 15-18 tok/s | Plug-and-play, ROCm, no CUDA |
| Mac Mini M4 Pro 24GB | €1.499 | Qwen 14B | 30 tok/s | 40W power, best TCO, no training |

### €3.000-5.000: Serious Single Node

| Hardware | Price | Model | Performance | Notes |
|----------|-------|-------|---|---|
| RTX 4090 rig | €4.000-4.500 | Qwen 35B-A3B AWQ | 24-28 tok/s | CUDA native, training, PCIe bottleneck on 70B |
| **ASUS Ascent GX10 / Dell GB10** | **€3.916** | **Qwen 35B-A3B NVFP4** | **82-102 tok/s** | **Unified memory, CUDA, 128K context fluent** |

**Winner for this budget:** GB10. Dense models at 4.7 tok/s don't justify the hardware.

### >€5.000: Cluster/Production

| Hardware | Price | Performance | Use Case |
|----------|-------|---|---|
| 2x RTX 4090 cluster | €5.000-6.500 | Qwen 122B-A10B: 15-20 tok/s | Multi-user vLLM, 25ms latency, tensor parallelism |
| **2x GB10 cluster (Blackwell)** | **€8.000** | **Qwen 235B-A22B: interactive** | **256 GB unified, 10GbE native, most powerful local setup today** |
| 3x GB10 cluster | €12.000 | DeepSeek-R1 671B: 10-15 tok/s | Enterprise RAG, long documents, custom inference |

---

## 8. Budget Mini PC: Ryzen 780M Low-Cost Approach

### What to Look For

Reference: Ryzen 7 7840HS, Radeon 780M (RDNA 3), DDR5 5600MHz RAM

- **Qwen 9B Q4:** 10-15 tok/s — readable speech speed, usable for chat
- **Qwen 14B Q4:** 7-10 tok/s — still interactive for non-critical tasks
- **Qwen 35B-A3B Q4 (MoE):** 12-18 tok/s per node

Examples: Thomson W3, Geekom A7 Pro, Minisforum UM890 Pro

### What NOT to Buy

Minisforum UM690L (Ryzen 9 6900HX) — looks better on paper, worse for AI:
- Radeon 680M RDNA 2 (3.3 TFLOPS vs. 8+ for 780M)
- DDR4 4800MHz max (vs. DDR5 5600MHz)
- -16% tok/s despite "Ryzen 9" in the name

### Cluster Setup (2 nodes, no switch needed)

- Auto-MDI/MDIX support in modern NICs: just a straight Cat6a cable
- Node 1: 10.0.0.1, Node 2: 10.0.0.2
- Internet via integrated Wi-Fi
- Switch needed only from 3 nodes onward

| Config | Cost | RAM | Models | Aggregated tok/s |
|--------|------|-----|--------|---|
| 2x Ryzen 780M (32GB) | €800-1.000 | 64GB | Qwen 9B-14B | 20-30 |
| 2x Ryzen 780M (96GB) | €1.200-1.600 | 192GB | Qwen 35B-A3B MoE | 25-40 |
| 4x Ryzen AI Max+ (64GB) | €4.400 | 256GB | Qwen 122B-A10B MoE | 65 |

---

## 9. Professional AI Rack: Dual GB10 Cluster

### Why Two GB10 Change Everything

- 256 GB unified memory at 273 GB/s per node
- Qwen 122B-A10B fits with margin: 27-29 tok/s per node
- CUDA native, vLLM distributed, TensorRT-LLM out-of-the-box
- 10GbE + 2× 200GbE (ConnectX-7): 4-8x faster than consumer mini PCs
- Qwen 235B-A22B MoE: interactive speed on 256 GB total

### Network Setup

Dual GB10 over 10GbE direct (no switch needed at 2 nodes). Switch (e.g., MikroTik CRS309, €200) only from 3 nodes onward.

| Config | Cost | RAM | Top Model | Performance |
|--------|------|-----|-----------|---|
| 1x GB10 | €3.900 | 128GB | Qwen 35B-A3B NVFP4 | 82-102 tok/s |
| 2x GB10 cluster | €8.000 | 256GB | Qwen 235B-A22B MoE | Interactive |
| 3x GB10 cluster | €12.000 | 384GB | DeepSeek-R1 671B | 10-15 tok/s |

---

## 10. Future of Local AI: 2027 and Beyond

### ASIC Becomes Accessible

- Tenstorrent n300S: already buyable at ~$1.400
- Groq demonstrated 500+ tok/s on 70B achievable
- GPU paradigm could shift within 18 months

### MoE Becomes the Standard

- Dense 70B+ models → niche
- Kimi K2: 1.2 trillion parameters, only billions active per token

### Cluster Mini PCs Mature

- Exo maturation + Ryzen AI NPU improvements
- Cluster latency <100ms achievable (threshold for interactive use)

### Unified Memory as Commodity

- AMD scales, Intel follows
- GB10 vs. Ryzen AI gap narrows by 2027

---

## 11. Conclusion: The Two Rules

In 2026, running powerful LLMs locally is accessible for any SME. Wrong hardware choice (seduced by inflated TFLOPS) turns serious investment into 4 tok/s disappointment.

**Two simple rules:**
1. Look at **memory bandwidth**, not TFLOPS
2. Check if memory is **unified** (good) or separate GPU/CPU (bad)

Then pick the right price tier from the decision matrix.

---

## Source Verification

- Benchmarks: internal testing + cited papers + vendor official specs
- Hardware costs: Amazon IT, senetic.it, geekom.it (April 2026 EUR pricing)
- Bandwidth specs: NVIDIA, AMD, Apple official datasheets
- Framework: Exo (peer-to-peer open source), vLLM, llama.cpp, MLX

---

## Key Quotes from Author

> "Quando ho visto il Tiiny AI dichiarare 40 token/s su 120B parametri con 200 GB/s di bandwidth, ho fatto i conti su un foglio. Non tornano. La fisica non mente. Il problema dell'AI locale non è mai stata la potenza di calcolo — è sempre stata la bandwidth. E chi non lo dice chiaramente ha qualcosa da nascondere."
>
> — Peter K., Fondatore BRIX-IA

---

**Categories:** AI Infrastructure, Hardware Procurement, Local LLMs, SME Guides, MoE Models, Bandwidth Optimization, Benchmarking

## Collegamenti (dreaming 2026-08-15)

- Scala per bit aggiornata al 2026-08: [Qwen3.8 su Unsloth](../syntheses/qwen3-8-unsloth-inferenza-locale.md)
- I quant su cui poggiano le stime: [Unsloth](../entities/unsloth.md); i modelli: [Alibaba](../entities/alibaba.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Alibaba](../entities/alibaba.md)
- [BRIX-IA](../entities/brix-ia.md)
- [Hardware per inferenza locale domestica — presente e futuro](../syntheses/hardware-per-inferenza-locale-domestica-presente-e-futuro.md)
- [Libre WebUI — Privacy-First Web Interface for Local AI](libre-webui-github.md)
- [NVIDIA](../entities/nvidia.md)
- [Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale](../syntheses/qwen3-8-unsloth-inferenza-locale.md)
- [Unsloth](../entities/unsloth.md)
<!-- openclaw:wiki:related:end -->
