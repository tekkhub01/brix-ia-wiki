---
pageType: source
id: source.qwen3-8-flash-next-how-to-run-locally-unsloth
title: Qwen3.8-Flash-Next — How to Run Locally (Unsloth)
sourceType: local-file
sourcePath: https://unsloth.ai/docs/models/qwen3.8-next
ingestedAt: 2026-08-28T09:05:53.041Z
updatedAt: 2026-08-28T09:05:53.041Z
status: active
publish: true
date: 2026-08-28
url: https://unsloth.ai/docs/models/qwen3.8-next
tags: [qwen, unsloth, moe, quantization, gguf, local-inference, llama-cpp, unified-memory]
---

# Qwen3.8-Flash-Next — How to Run Locally (Unsloth)

## Source
- Type: `local-file`
- Origine: https://unsloth.ai/docs/models/qwen3.8-next
- Bytes: 12900
- Updated: 2026-08-28T09:05:53.041Z

## Content
## Qwen3.8-Flash-Next: How to Run Locally

Qwen3.8-Flash-Next is a new open-weight, **125B parameter** MoE multimodal model from Qwen. Built on the new Qwen4 architecture, it supports a 262K context window and advanced reasoning. The model outperforms Claude-4.6-Opus (Max) and can run locally on devices with **75GB RAM**/unified memory with no GPU VRAM required. To run the model, use our [GGUFs](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF) via llama.cpp or [Unsloth Desktop](https://unsloth.ai/docs/desktop). Thank you Qwen for day zero access.

**1-bit is 75GB** and uses 4-bit for the Ngram / PLE. This is **79% smaller** than BF16 (355GB), and retains a **top-1% accuracy of 80%**.

[Run Qwen3.8-Flash](https://unsloth.ai/pages/Ef8lrnBt1lmETOqIFCHj#run-qwen3.8-flash-next-in-unsloth)[Download Unsloth](https://unsloth.ai/download)

Qwen3.8-Flash can now run locally in [Unsloth Desktop](#run-qwen3.8-flash-next-in-unsloth)!

![4-bit Qwen3.8-Flash running in Unsloth](https://unsloth.ai/files/BllgxCChDC9PNkfUYyZk)

#### Usage Guide

Whether you run **Qwen3.8-Flash-Next** on a CPU with system RAM or on a GPU with VRAM may make relatively little difference. Its unique architecture allows inference using RAM or unified memory to achieve performance closer to that of GPU VRAM than is typical for other models. This makes it particularly well suited to Macs, NVIDIA DGX Spark systems, and other devices with large memory capacities.

You will need at least **75 GB of RAM or unified memory** to run the model. Its smallest 1-bit quantized version is larger than usual because of new Ngram layers or per layer embeddings which is like a lookup table. However, this also means the quantization is less aggressive, allowing the model to retain more of its original accuracy than more heavily quantized models. You can also offload the PLE / Ngram layer to SSD and use mmap which allows less usage of CPU and GPU VRAM.

##### Qwen3.8-Flash-Next Requirements:

The smallest quant works on 75GB RAM so it's best to have a 96GB RAM/unified memory device.\
**Table: Hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

<table><thead><tr><th>1-bit</th><th>2-bit</th><th>3-bit</th><th>4-bit</th><th width="128">5-bit</th><th>8-bit</th><th>BF16</th></tr></thead><tbody><tr><td>75 GB</td><td>79 GB</td><td>90 GB</td><td>112 GB</td><td>200 GB</td><td>270 GB</td><td>355 GB</td></tr></tbody></table>

#### Recommended Settings

Qwen3.8-Flash-Next is a **hybrid thinking** model with different default settings for thinking and non-thinking modes. Extra high is enabled by default so if you want shorter thinking traces, you can [adjust the thinking effort](#thinking--preserve-thinking):

| Parameter            | Thinking Mode | Instruct (non-thinking) Mode |
| -------------------- | ------------- | ---------------------------- |
| `temperature`        | 1.0           | 0.7                          |
| `top_p`              | 0.95          | 0.80                         |
| `top_k`              | 20            | 20                           |
| `min_p`              | 0.0           | 0.0                          |
| `presence_penalty`   | 0.0           | 1.5                          |
| `repetition_penalty` | 1.0           | 1.0                          |

* Context length = up to `262,144`
* Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`
* Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`

#### 💡 Thinking + Preserve Thinking

Qwen3.8-Flash-Next has **Preserve Thinking** which leaves the thinking trace from the previous conversation. This increases the number of tokens you use, but could increase accuracy in continued conversations. [Unsloth](#run-qwen3.8-in-unsloth-desktop) has 'Think' and Preserved Thinking toggles for Qwen3.8 (see right):

![](https://unsloth.ai/files/Iv7qED32vTUYwyLX62NB)

Qwen3.8-Flash-Next comes with support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost. These toggles are automatically enabled in Unsloth:

* `xhigh` (default): for complex tasks demanding thorough analysis
* `medium`: balancing accuracy and speed
* `low`: efficient reasoning optimizing for speed and cost
* none

To change[ thinking / reasoning](#how-to-enable-or-disable-reasoning-and-thinking) effort in `unsloth run` or `llama-server`, use `--chat-template-kwargs '{"reasoning_effort":"medium"}'`

If you're on **Windows** Powershell, use: `--chat-template-kwargs "{\"reasoning_effort\":\"medium\"}"`

Change `medium` to your desired reasoning level.

#### Quantization Analysis

We ran KLD for Qwen3.8-Flash quants, and show that 80% top-1% accuracy recovery is possible with 79% less disk space usage. The new architecture uses PLE / Ngrams, and these are not quantized that heavily (4-bit minimum) since they have random access pattern, and quantizing them heavily will damage the model.

<div>![](https://unsloth.ai/files/HbLMSAfr4mHGDG36tEQS) ![](https://unsloth.ai/files/trRPxrnr4rFkAZruewTh)</div>

| quant        | size\_gb | mean\_kld | same\_top\_pct |
| ------------ | -------- | --------- | -------------- |
| UD-Q4\_K\_XL | 111.3    | 0.044715  | 93.481         |
| UD-IQ4\_XS   | 93.7     | 0.079162  | 91.089         |
| UD-Q3\_K\_XL | 90       | 0.099694  | 90.387         |
| UD-IQ3\_XXS  | 82       | 0.156505  | 87.57          |
| UD-Q2\_K\_XL | 78.9     | 0.213343  | 85.163         |
| UD-IQ1\_M    | 74.5     | 0.302159  | 82.396         |
| UD-IQ1\_S    | 72.5     | 0.37514   | 80.239         |

### Run Qwen3.8-Flash-Next Guide

You can now run Qwen3.8-Flash-Next in Unsloth Desktop and llama.cpp. Feel free to change quantization type.

* Hugging Face: [Qwen3.8-Flash-Next-**GGUF**](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)
* ModelScope: [Qwen3.8-Flash-Next-GGUF](https://www.modelscope.cn/models/unsloth/Qwen3.8-Flash-Next-GGUF)

[Run in Unsloth Desktop](https://unsloth.ai/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-unsloth-desktop)[Run in llama.cpp](https://unsloth.ai/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-llama.cpp)

Qwen3.8-Flash-Next is now available to run locally in [Unsloth Desktop](#run-qwen3.8-flash-next-in-unsloth)!

#### 🦥 Run Qwen3.8-Flash-Next in Unsloth

Qwen3.8-Flash-Next now is able to run in [Unsloth Desktop](#run-qwen3.8-in-unsloth-desktop), an open-source UI app for local AI. **Unsloth automatically offloads to RAM and detects multiGPU setups**. With Unsloth Desktop, you can run models locally on **MacOS, Windows**, Linux and:

* Search, download, [run GGUFs](https://unsloth.ai/docs/new/studio#run-models-locally) and safetensor models
* [**Self-healing** tool calling](https://unsloth.ai/docs/new/studio/chat#auto-healing-tool-calling) + **web search**
* [**Code execution**](https://unsloth.ai/docs/desktop#code-execution) (Python, Bash)
* [Automatic inference](https://unsloth.ai/docs/desktop#feature-deep-dive) parameter tuning (temp, top-p, etc.)
* Fast CPU + GPU inference via MLX and llama.cpp
* [Train LLMs](https://unsloth.ai/docs/new/studio#no-code-training) 2x faster with 70% less VRAM
  

![](https://unsloth.ai/files/0xoUQOYpTX661nFuPLSL)

##### Install Unsloth

The easiest way to get started is by downloading the [Unsloth Desktop app](https://unsloth.ai/docs/desktop). Works on [macOS](https://unsloth.ai/docs/get-started/install/mac), [Windows](https://unsloth.ai/docs/get-started/install/windows-installation), and [Linux](https://unsloth.ai/docs/get-started/install/linux).

[Download Unsloth](https://unsloth.ai/download)

* <i class="fa-apple">:apple:</i> [Download for macOS](https://unsloth.ai/download/mac)
* <i class="fa-windows">:windows:</i> [Download for Windows](https://unsloth.ai/download/windows)
* <i class="fa-linux">:linux:</i> [Download for Linux](https://unsloth.ai/download/linux)

Or, if you prefer to install manually:

MacOS, Linux, WSL:

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

Windows PowerShell:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

##### Search and download Qwen3.8-Flash-Next

Go to [Unsloth Chat](https://unsloth.ai/docs/new/studio/chat) or Model hub and search for Qwen3.8-Flash in the search bar and download your desired model and quant.

![](https://unsloth.ai/files/D2hKNrTz4WevbfhUkqjD)

##### Run Qwen3.8-Flash-Next

Inference parameters should be auto-set when using Unsloth, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth inference guide](https://unsloth.ai/docs/new/studio/chat).

For example using Unsloth Desktop with the 397GB Qwen3.8 (-91% smaller) allows you to toggle thinking modes, allow inline canvas, web search and code execution and much more.

![](https://unsloth.ai/files/BllgxCChDC9PNkfUYyZk)

##### Serve Qwen3.8-Flash-Next with Unsloth API

You can use `unsloth run` command and serve Qwen3.8 via an API using `llama-server` runtime flags, including context sizing, GPU layers, threading, sampling, networking, and tool configuration. For more info see our [API docs](https://unsloth.ai/docs/basics/api) or [unsloth start](https://unsloth.ai/docs/integrations/unsloth-start).

```bash
unsloth run --model unsloth/Qwen3.8-Flash-Next-GGUF:UD-Q4_K_XL
```

##### Unsloth is now ready

You can also do many other things with Qwen3.8-Flash-Next via Unsloth Desktop like:

* **Connect tools:** [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex), [web search](https://unsloth.ai/docs/new/studio/chat#advanced-web-search), [MCP](https://unsloth.ai/docs/basics/mcp) and more
* **Train models:** Fine-tune text, diffusion, [embedding](https://unsloth.ai/docs/basics/embedding-finetuning), and more
* **Generate media:** Create and train [images](https://unsloth.ai/docs/basics/diffusion-image), video, [TTS](https://unsloth.ai/docs/basics/text-to-speech-tts-fine-tuning) locally

![](https://unsloth.ai/files/OdaMAEViRv35ZvHSFyRn)

#### Run Qwen3.8-Flash-Next in llama.cpp

Install the latest version of llama.cpp. You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

To run the model, you can do:

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-Flash-Next-GGUF \
    --local-dir unsloth/Qwen3.8-Flash-Next-GGFF \
    --include "*UD-Q4_K_XL*" # Use "*IQ2_XXS*" for 2-bit
```

Then to run it:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-Flash-Next-GGUF/UD-IQ1_S/Qwen3.8-Flash-Next-UD-Q4_K_XL-00001-of-00004.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

#### 📊 Benchmarks

For GGUF quantization benchmarks you can see above for our [quantization analysis](#quantization-analysis) or [Dynamic V3.0 article](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs).

<div>![](https://unsloth.ai/files/F1nnx6tFwiejoXJth3zZ) ![](https://unsloth.ai/files/0rP53jLSxT70vSR3sB1U)</div>

---

## Notes
<!-- openclaw:human:start -->
### Nel vault
- Sintesi: [Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)](../syntheses/qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md)
- [Alibaba](../entities/alibaba.md) — rilascia la famiglia Qwen · [Unsloth](../entities/unsloth.md) — autore dei quant e di questa documentazione
- Fonte sorella: [Qwen3.8 — How to Run Locally (Unsloth)](qwen3-8-how-to-run-locally-unsloth.md) — il modello **diverso** (27B) con cui non va confuso
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Alibaba](../entities/alibaba.md)
- [Qwen3.8-Flash-Next — MoE 125B locale a 75GB (unified/RAM)](../syntheses/qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md)
- [Unsloth](../entities/unsloth.md)
<!-- openclaw:wiki:related:end -->
