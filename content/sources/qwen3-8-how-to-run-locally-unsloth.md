---
pageType: source
id: source.qwen3-8-how-to-run-locally-unsloth
title: Qwen3.8 — How to Run Locally (Unsloth)
sourceType: local-file
sourcePath: /tmp/qwen3.8-unsloth.md
ingestedAt: 2026-08-15T06:04:25.611Z
updatedAt: 2026-08-15T06:04:25.611Z
status: active
publish: true
date: 2026-08-15
tags: [quantization, gguf, nvfp4, mtp, local-inference, qwen, unsloth, llama-cpp, vllm]
url: https://unsloth.ai/docs/models/qwen3.8
---

# Qwen3.8 — How to Run Locally (Unsloth)

## Source
- Type: `local-file`
- Path: `/tmp/qwen3.8-unsloth.md`
- Origine: https://unsloth.ai/docs/models/qwen3.8 (documentazione Unsloth, pubblicata su GitBook)
- Bytes: 24944
- Updated: 2026-08-15T06:04:25.611Z

> **Nota di resa (2026-08-15).** Il contenuto era incapsulato in un fence
> ```` ```text ````, quindi l'intera pagina renderizzava come blocco di codice —
> stesso difetto corretto il 2026-08-14 sulle cinque fonti di agosto. Il corpo è
> stato promosso a pagina; i blocchi di codice reali (build llama.cpp, download
> HF, `vllm serve`, la GET `?ask=`) sono preservati. Rimossi i soli tag di layout
> GitBook (`{% raw %}{% columns %}{% endraw %}`, `{% raw %}{% step %}{% endraw %}`
> e simili), che non sono contenuto. Il testo della fonte non è stato alterato.

## Content
> For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://unsloth.ai/docs/models/qwen3.8.md).

Qwen3.8 is Qwen’s new model family, featuring Qwen3.8-**27B**, Qwen3.8-**2.4T-A95B** and Qwen3.8-**Max**. Qwen3.8-27B has **vision** and reasoning capabilities, a **256K context** window, and runs locally on **17GB RAM/VRAM** setups. Qwen3.8 excels at agentic coding, vision and chat tasks, and can now run via Unsloth GGUFs, NVFP4 and [Unsloth Desktop](#run-qwen3.8-in-unsloth-desktop). Qwen3.8-2.4T-A95B is a 2.4T parameter (95B active) model with rivaling GPT-5.6 Sol.

<a href="https://unsloth.ai/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-guide" class="button primary">Run Qwen3.8 Guide</a><a href="https://unsloth.ai/download" class="button primary">Download Unsloth</a>

Qwen3.8 GGUFs use Unsloth Dynamic V3.0 (preview) for SOTA quant performance. Thank you Qwen for day zero access. Unsloth quants also include:

* **Developer Role Support** for agentic tools like Codex
* [MTP enabled](https://unsloth.ai/docs/models/mtp.md) for fast inference
* **Tool calling:** Improved parsing nested objects to make tools succeed more

Full-precision Qwen3.8-2.4T-A95B requires 4.9TB of storage and 1-bit [Unsloth](https://github.com/unslothai/unsloth) Dynamic GGUFs takes **397GB (91% smaller)**, and larger IQ1\_S takes 508GB.

<figure><img src="/files/NwjKvtloQ6F3q7EZ5Oqn" alt=""><figcaption><p>Dynamic 4-bit Qwen3.8-27B in Unsloth Desktop</p></figcaption></figure>

Unsloth quants:

* [Qwen3.8-**27B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)
* [Qwen3.8-27B-**NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4)
* [Qwen3.8-**2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)

### :gear: Usage Guide

#### Qwen3.8-27B Requirements:

Qwen3.8-**27B** 4-bit quants will work on most devices 17-19GB VRAM like RTX 5080, 4090 or a Mac with 24GB RAM.\
**Table: Hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

<table><thead><tr><th>2-bit</th><th>3-bit</th><th>4-bit</th><th width="128">6-bit</th><th>8-bit</th><th>BF16</th></tr></thead><tbody><tr><td>11-13 GB</td><td>13-16 GB</td><td>17-19 GB</td><td>24 GB</td><td>31 GB</td><td>56 GB</td></tr></tbody></table>

#### Qwen3.8-**2.4T** Requirements:

| Dynamic 1-bit XXXS | Dynamic 1-bit Standard | Dynamic 2-bit | Q8\_0  | BF16 (Lossless) |
| ------------------ | ---------------------- | ------------- | ------ | --------------- |
| 397GB              | 508GB                  | 657 GB        | 2.6 TB | 4.9 TB          |

### Recommended Settings

#### Qwen3.8-**27B Settings:**

Qwen3.8-27B is a **hybrid thinking** model with different default settings for thinking and non-thinking modes:

| Parameter            | Thinking Mode | Instruct (non-thinking) Mode |
| -------------------- | ------------- | ---------------------------- |
| `temperature`        | 1.0           | 0.7                          |
| `top_p`              | 0.95          | 0.80                         |
| `top_k`              | 20            | 20                           |
| `min_p`              | 0.0           | 0.0                          |
| `presence_penalty`   | 0.0           | 1.5                          |
| `repetition_penalty` | 1.0           | 1.0                          |

* **Maximum context window:** `262,144` (can be extended to 1M via YaRN)
* Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`
* Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`

#### Qwen3.8-**2.4T Settings:**

Qwen3.8-2.4T is **thinking-only**, while Qwen3.8-Max is hybrid.

| Default                 |
| ----------------------- |
| temperature = 1.0       |
| top\_p = 0.95           |
| top\_k = 20             |
| min\_p = 0.0            |
| presence\_penalty = 0.0 |

* Context length = up to `1,010,000`
* `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`

If the model fits, you will get \~20 tokens/s generation when using B200s and >120 tokens / s throughput. Best rule of thumb: RAM+VRAM ≈ the quant size; otherwise it’ll still work, just much slower due to disk offloading.

### 💡 Thinking + Preserve Thinking

Qwen3.8 has **Preserve Thinking** which leaves the thinking trace from the previous conversation. This increases the number of tokens you use, but could increase accuracy in continued conversations. [Unsloth](#run-qwen3.8-in-unsloth-desktop) has 'Think' and Preserved Thinking toggles for Qwen3.8 (see right):

<figure><img src="/files/Iv7qED32vTUYwyLX62NB" alt=""><figcaption></figcaption></figure>

Qwen3.8-27B comes with support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost. These toggles are automatically enabled in Unsloth:

* `xhigh` (default): for complex tasks demanding thorough analysis
* `medium`: balancing accuracy and speed
* `low`: efficient reasoning optimizing for speed and cost
* none

## Run Qwen3.8 Guide

You can now run Qwen3.8 in llama.cpp and Unsloth Desktop. For the large Qwen3.8-2.T model, we will be utilizing the 397GB `IQ1_XXXS` quant (named Q1\_0) for best results in terms of accessibility and accuracy and it will require at least 450GB RAM. Feel free to change quantization type. GGUF: [**Qwen3.8-GGUF**](https://huggingface.co/unsloth/Kimi-K3-GGUF)

<a href="https://unsloth.ai/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-unsloth-desktop" class="button primary">Run in Unsloth Desktop</a><a href="https://unsloth.ai/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-llama.cpp" class="button secondary">Run in llama.cpp</a><a href="https://unsloth.ai/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-llama.cpp" class="button secondary">NVFP4 Guide</a>

### 🦥 Run Qwen3.8 in Unsloth Desktop

Qwen3.8 can run in [Unsloth Desktop](#run-qwen3.8-in-unsloth-desktop), an open-source UI app for local AI. **Unsloth automatically offloads to RAM and detects multiGPU setups**. With Unsloth Desktop, you can run models locally on **MacOS, Windows**, Linux and:

* Search, download, [run GGUFs](https://unsloth.ai/docs/new/studio.md#run-models-locally) and safetensor models
* [**Self-healing** tool calling](https://unsloth.ai/docs/new/studio/chat.md#auto-healing-tool-calling) + **web search**
* [**Code execution**](https://unsloth.ai/docs/desktop.md#code-execution) (Python, Bash)
* [Automatic inference](https://unsloth.ai/docs/desktop#feature-deep-dive) parameter tuning (temp, top-p, etc.)
* Fast CPU + GPU inference via MLX and llama.cpp
* [Train LLMs](https://unsloth.ai/docs/new/studio.md#no-code-training) 2x faster with 70% less VRAM

<figure><img src="/files/0xoUQOYpTX661nFuPLSL" alt=""><figcaption></figcaption></figure>

#### Install Unsloth

The easiest way to get started is by downloading the [Unsloth Desktop app](https://unsloth.ai/docs/desktop.md). Works on [macOS](https://unsloth.ai/docs/get-started/install/mac.md), [Windows](https://unsloth.ai/docs/get-started/install/windows-installation.md), and [Linux](https://unsloth.ai/docs/get-started/install/linux.md).

<a href="https://unsloth.ai/download" class="button primary" data-icon="down-to-bracket">Download Unsloth</a>

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

#### Search and download Qwen3.8

Go to [Unsloth Chat](https://unsloth.ai/docs/new/studio/chat.md) or Model hub and search for Qwen3.8 in the search bar and download your desired model and quant.

<figure><img src="/files/5UXWLhOCIWtTLwtKQVE0" alt=""><figcaption></figcaption></figure>

#### Run Qwen3.8

Inference parameters should be auto-set when using Unsloth, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth inference guide](https://unsloth.ai/docs/new/studio/chat.md).

For example using Unsloth Desktop with the 397GB Qwen3.8 (-91% smaller) allows you to toggle thinking modes, allow inline canvas, web search and code execution and much more.

<figure><img src="/files/drgfSklC2kZpGDsn1gGe" alt="" width="563"><figcaption><p>Dynamic 1-bit 397GB 91% smaller GGUF of Qwen3.8 2.4T in Unsloth Desktop</p></figcaption></figure>

### Qwen3.8-2.4T-A95B New 1-bit data-types

We extended IQ1\_S in llama.cpp which is 1.5625 bits per weight to 1.1875 bpw by reducing the number of entries in the codebook - we found this works well for large models, and can still retain a lot of accuracy - we also found these new data-types to be fine for post training quantization (PTQ) without the need for QAT or QAD (quantization aware training / distillation)

Due to naming issues, we used TQ2\_0, TQ1\_0 and Q1\_0 otherwise it won't pop up in the HF repo.

<table><thead><tr><th>Dtype</th><th width="147.60000610351562">Naming</th><th width="114.39996337890625" align="right">BPW</th><th width="106.20001220703125" align="right"># entries</th><th width="113.413330078125" align="right">Index bits</th><th width="106.4000244140625" align="right">Block</th></tr></thead><tbody><tr><td>IQ1_S</td><td>IQ1_S</td><td align="right"><strong>1.5625</strong></td><td align="right">2048</td><td align="right">11</td><td align="right">50 B</td></tr><tr><td>UD-IQ1_XS</td><td>TQ2_0</td><td align="right">1.4375</td><td align="right">1024</td><td align="right">10</td><td align="right">46 B</td></tr><tr><td>UD-IQ1_XXS</td><td>TQ1_0</td><td align="right">1.3125</td><td align="right">512</td><td align="right">9</td><td align="right">42 B</td></tr><tr><td>UD-IQ1_XXXS</td><td>Q1_0</td><td align="right"><strong>1.1875</strong></td><td align="right">256</td><td align="right">8</td><td align="right">38 B</td></tr></tbody></table>

We are still running benchmarks for the new data-types, but for other large models, we get **good results without any QAT / QAD**:

| Dtype        |     GiB |      PPL |      KLD |  top-p |
| ------------ | ------: | -------: | -------: | -----: |
| IQ1\_S       | 553.204 | 2.578876 | 0.564553 | 78.882 |
| UD-IQ1\_XS   | 513.583 | 2.931261 | 0.690161 | 75.726 |
| UD-IQ1\_XXS  | 473.961 | 3.540383 | 0.876007 | 71.284 |
| UD-IQ1\_XXXS | 434.340 | 4.488796 | 1.109944 | 66.257 |

### :llama: Run Qwen3.8 in llama.cpp

We need to use the specific IQ1\_XXXS branch [here](https://github.com/unslothai/llama.cpp/pull/61). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone --branch iq1-narrow https://github.com/unslothai/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

If you just want to run the standard `IQ1_S` and other quants, then compile llama.cpp normally:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Download the model via (after installing `pip install huggingface_hub`). You can choose `Q1_0` for `IQ1_XXXS` or other quantized versions like `Q8_0` . If downloads get stuck, see: [Hugging Face Hub, XET debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md)

**Qwen3.8-27B:**

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-27B-GGUF \
    --local-dir unsloth/Qwen3.8-27B-GGUF \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q3_K_XL*" for 3-bit
```

**Qwen3.8-2.4T:**

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --local-dir unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --include "*Q1_0*" # Use "*IQ2_XXS*" for 2-bit
```

To run the model in llama-cli, follow the code snippets below:\
Remember to [change settings](#recommended-settings) according to your use-case.

**Qwen3.8-27B:**

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-27B-GGUF/Qwen3.8-27B-UD-Q4_K_XL.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

**Qwen3.8-2.4T:**

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-2.4T-A95B-GGUF/UD-Q1_0/Qwen3.8-2.4T-A95B-UD-Q1_0-00001-of-00010.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

To run the general UD-IQ1\_S you can do:

**Qwen3.8-2.4T:**

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --local-dir unsloth/Qwen3.8-2.4T-A95B-GGFF \
    --include "*IQ1_S*" # Use "*IQ2_XXS*" for 2-bit
```

Then to run it:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-2.4T-A95B-GGUF/UD-IQ1_S/Qwen3.8-2.4T-A95B-UD-IQ1_S-00001-of-00012.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

### ⚡️NVFP4

Like Qwen3.6, we’re also releasing new [dynamic NVFP4 Qwen3.8](https://unsloth.ai/docs/basics/nvfp4.md)-27B quants that run **\~1.5× faster** than BF16 checkpoints, with **better performance** and comparable file sizes. Run Qwen3.8-27B NVFP4 **1.5x faster** on **24GB VRAM.** We also added **FP8 KV cache calibration** for 2x longer context lengths! NVFP4 requires NVIDIA's Blackwell GPUs like RTX 50X, DGX Spark (see [#dgx-spark-with-nvfp4-quants](#dgx-spark-with-nvfp4-quants "mention")), B200, B300 GPUs. For older GPUs, our GGUFs work well! You can run NVFP4 quants in [vLLM](#vllm) and [SGLang](#sglang).

* [Qwen3.8-27B-**NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4) quant

<table><thead><tr><th width="90" align="right">batch</th><th width="114.5999755859375" align="right">BF16 total tok/s</th><th width="122.60003662109375" align="right">NVFP4 total tok/s</th><th width="122" align="right">speedup</th><th width="137.4000244140625" align="right">BF16 per-user</th><th align="right">NVFP4 per-user</th></tr></thead><tbody><tr><td align="right">1</td><td align="right">89.8</td><td align="right"><strong>133.7</strong></td><td align="right">1.49x</td><td align="right">89.8</td><td align="right"><strong>133.7</strong></td></tr><tr><td align="right">8</td><td align="right">649.4</td><td align="right"><strong>938.8</strong></td><td align="right">1.45x</td><td align="right">81.2</td><td align="right"><strong>117.3</strong></td></tr><tr><td align="right">32</td><td align="right">1983.0</td><td align="right"><strong>2787.0</strong></td><td align="right">1.41x</td><td align="right">62.0</td><td align="right"><strong>87.1</strong></td></tr><tr><td align="right">64</td><td align="right">3048.5</td><td align="right"><strong>4407.2</strong></td><td align="right">1.45x</td><td align="right">47.6</td><td align="right"><strong>68.9</strong></td></tr></tbody></table>

See below for previous benchmarks conducted for Qwen3.6 as well comparing to other NVFP4 implementations which use 16bit activations vs our NVFP4 activations:

<figure><img src="/files/6X0DPBb8ijDqd6cGk4sH" alt="" width="563"><figcaption></figcaption></figure>

All benchmarks use 1x B200 128 concurrency. Higher concurrency can boost 35B to 17,561 tokens / s.&#x20;

For accuracy benchmarks we ran KLD and Top-1% agreement over Code, Chat and many domains. NVFP4 is consistency 92% to 97% accuracy recovery vs BF16

| corpus            |      KLD mean | top-1 agreement |
| ----------------- | ------------: | --------------: |
| zh                |       0.01628 |          93.55% |
| code              |       0.02600 |          96.68% |
| refgen            |       0.03993 |          94.46% |
| chat              |       0.05818 |          92.15% |
| ja / ko / ru / es | 0.0124-0.0155 |          94-95% |

For accuracy benchmarks For Qwen 3.6, we conducted MMLU-Pro, AIME 2025, GPQA for FP8, BF16, NVIDIA's NVFP4 and our NVFP4s - we show our faster quants do similarly on all:

<figure><img src="/files/95OLTU6BPWYWYNmsJidJ" alt=""><figcaption></figcaption></figure>

For more information, you can read our [Dynamic NVFP4 quants blog](https://unsloth.ai/docs/basics/nvfp4.md).

To run NVFP4 quants, see below for commands to run Qwen3.8-27B in [vLLM](https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide.md) or [SGLang](https://unsloth.ai/docs/basics/inference-and-deployment/sglang-guide.md):

#### **vLLM:**

To install vLLM in a separate venv:

```bash
uv venv unsloth-nvfp4-env --python 3.13
source unsloth-nvfp4-env/bin/activate
uv pip install "vllm>=0.25.0" "flashinfer-python>=0.6.13" "nvidia-cutlass-dsl>=4.5.2" \
    --torch-backend=auto
```

Then to serve the 27B variant:

```shell
vllm serve unsloth/Qwen3.8-27B-NVFP4
```

To enable MTP / speculative decoding (faster decode but somewhat less throughput), use:

```bash
vllm serve unsloth/Qwen3.8-27B-NVFP4
    --speculative-config '{"method": "mtp", "num_speculative_tokens": 2}'
```

If you get Torchcodec issues, be sure to do the below then relaunch vllm.

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

#### **SGLang:**

Install SGLang then run:

```bash
python -m sglang.launch_server --model-path unsloth/Qwen3.8-27B-NVFP4 --speculative-algorithm NEXTN \
     --speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4
```

### :exploding\_head:Quantization Analysis

We ran top-1% and KLD for Qwen3.8 GGUFs, and we retain 82.5% accuracy (IQ2\_XXS 9GB) whilst being 83.5% smaller (BF16 54.7GB).

NVFP4 quants are 1.5x faster than BF16 and retains 92 to 97% top-1% accuracy.

More benchmarks coming soon!

<figure><img src="/files/DbbbfANlugzdDgNt28za" alt=""><figcaption></figcaption></figure>

### 📊 Benchmarks

#### Qwen3.8-**27B**

See further below for table benchmarks:

<div><figure><img src="/files/RpY0LAnu8jPDxMFOXDOm" alt=""><figcaption></figcaption></figure> <figure><img src="/files/vJHpGT8GqDUWtvpxhRnQ" alt=""><figcaption></figcaption></figure></div>

#### Text Performance

|                                                      | Qwen3.8-27B                  | Qwen3.6-27B          | Qwen3.7-Plus         | Muse Glimmer-30B | Opus4.6 Max |
| ---------------------------------------------------- | ---------------------------- | -------------------- | -------------------- | ---------------- | ----------- |
| Coding                                               |                              |                      |                      |                  |             |
| Agentic terminal codingTerminal Bench 2.1 (Terminus) | 73.0                         | 63.4                 | 64.0                 | 51.7             | **78.2**    |
| Agentic codingSWE-bench Pro                          | **61.7**                     | 53.5                 | 57.6                 | 51.2             | 53.4        |
| Repo-level code generationNL2Repo-Bench              | 42.3                         | 36.2                 | 41.1                 | --               | **47.6**    |
| Agentic codingDeepSWE 1.1                            | **42.2**                     | 13.3                 | 14.2                 | --               | --          |
| Software engineeringQwenSWEBench                     | **79.0**                     | 49.3                 | 59.2                 | --               | 63.8        |
| Agent                                                |                              |                      |                      |                  |             |
| Long-horizon office workCoWorkBench                  | **70.7**                     | 61.0                 | 65.1                 | --               | 68.2        |
| Professional job tasksJobBench                       | **33.4**                     | 21.8                 | 27.6                 | --               | --          |
| Frontier agentic tasksAgents' Last Exam              | Pass\@1**20.4**Score**42.9** | Pass\@110.6Score27.3 | Pass\@113.2Score33.6 | --               | --          |
| General                                              |                              |                      |                      |                  |             |
| Instruction followingIFBench                         | **79.5**                     | 69.1                 | 79.1                 | 77.0             | 62.5        |
| Scientific reasoningGPQA Diamond                     | 89.2                         | 87.8                 | 90.3                 | 83.5             | **91.3**    |
| Multidisciplinary reasoningHLE                       | 30.8                         | 24.0                 | 34.7                 | 22.0             | **40.0**    |
| Competitive codingLiveCodeBench v6                   | **90.3**                     | 83.9                 | 89.6                 | --               | 88.8        |

1. SWE-bench Pro: Except for Opus4.6 Max, which uses the officially reported score, all models are evaluated with the Claude Code harness at temp=1.0, top\_p=0.95, and a 256K context window. Problematic tasks were corrected, and all baseline models were re-evaluated on the refined benchmark.
2. NL2Repo-Bench: Evaluated with the Claude Code harness. To prevent reward hacking, we disable Bash commands that attempt to access the specific repository, such as pip download, pip install, and git clone.
3. DeepSWE 1.1: Evaluated with the Claude Code harness at temp=1.0, top\_p=0.95, and a 256K context window.
4. QwenSWEBench: In-house coding benchmark for evaluating models' software engineering capabilities. Evaluated with the Claude Code harness. Reporting avg\@3 with an 8-hour timeout, max\_tokens=32,768, temperature=1.0, and a 256K context window.
5. CoWorkBench: In-house cowork benchmark for evaluating long-horizon tasks across computer science, finance, law, medical, and other productivity domains.
6. HLE: Judged by GPT-4o.
7. The best result in each row is shown in bold.
8. Empty cells (--) indicate that results are not yet available or not applicable.

#### Qwen3.8-**2.4T-A95B**

<figure><img src="/files/rUwPDAu4KgLzJCPv1VSJ" alt=""><figcaption></figcaption></figure>

---

## Agent Instructions (GitBook)
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://unsloth.ai/docs/models/qwen3.8.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

## Notes
<!-- openclaw:human:start -->
### Collegamenti (dreaming 2026-08-15)
- Sintesi di questa fonte: [Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale](../syntheses/qwen3-8-unsloth-inferenza-locale.md)
- Modello di [Alibaba](../entities/alibaba.md), quantizzato da [Unsloth](../entities/unsloth.md)
- L'argomento: [quantization](../concepts/quantization.md)
- Secondo corpus sulle stesse tecniche: [Esperimenti Quantizzazione Gemma 4 12B](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)

<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Alibaba](../entities/alibaba.md)
- [Qwen3.8 su Unsloth — la scala hardware dell'inferenza locale](../syntheses/qwen3-8-unsloth-inferenza-locale.md)
- [Qwen3.8-Flash-Next — How to Run Locally (Unsloth)](qwen3-8-flash-next-how-to-run-locally-unsloth.md)
- [Unsloth](../entities/unsloth.md)
<!-- openclaw:wiki:related:end -->
