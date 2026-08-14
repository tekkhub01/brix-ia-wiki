---
id: libre-webui-github
pageType: source
updatedAt: 2026-03-10T00:00:00Z
publish: true
---

# Libre WebUI — Privacy-First Web Interface for Local AI

**Source:** https://github.com/libre-webui/libre-webui
**License:** Apache 2.0 (perpetual, guaranteed in charter)
**Author:** Kroonen AI + open-source community
**Type:** Open-source chat interface / Platform
**Category:** Local AI, privacy, self-hosted, web UI, Ollama integration

---

## Overview

The privacy-first, open-source chat interface for local and cloud AI.

**Core principle:** No telemetry. No tracking. No compromises.

Libre WebUI is a self-hosted chat interface that:
- Connects to **Ollama** for fully local AI
- Integrates with **OpenAI, Anthropic, Google** and 10+ cloud providers
- Runs everything from one clean, fast UI
- **Guarantees** conversations never leave your machine unless you choose

Built by **Kroonen AI** (professional services + governance) and open-source community.
**License:** Apache 2.0 forever (protected in charter — no bait-and-switch).

---

## Key Features

| Feature | Capability |
|---------|-----------|
| **💬 Streaming Chat** | Real-time responses, dark/light themes, mobile support |
| **🔌 Plugin System** | Any OpenAI-compatible API via simple JSON config (no code changes) |
| **📄 Document Chat (RAG)** | Upload PDFs, search + retrieve, chat with documents |
| **🎭 Personas** | Custom AI personalities with persistent memory |
| **🎨 Artifacts** | Live HTML, SVG, code preview in chat |
| **🖼️ Image Generation** | ComfyUI + Flux, DALL·E integration |
| **🔊 Text-to-Speech** | Qwen3-TTS, Kyutai, OpenAI voices (local or cloud) |
| **🤗 HuggingFace Hub** | Browse 1M+ models for chat, TTS, images, embeddings, STT |
| **🔐 Auth & SSO** | GitHub, HuggingFace OAuth/OIDC, role-based access |
| **🌍 25+ Languages** | Full i18n (Arabic to Vietnamese) |
| **🖥️ Desktop App** | Native Electron app (macOS, Windows, Linux) |
| **🤖 AI Agent Support** | **OpenClaw integration** — persistent agents with memory + tools |
| **🏢 Enterprise** | GDPR, HIPAA, SOC 2 compatible; AES-256-GCM encryption |

---

## Quick Start

### One-liner (local default)
```bash
npx libre-webui
```
Opens http://localhost:8080. Works immediately with Ollama.

### Docker (recommended)
```bash
# Default: bundles Ollama
docker-compose up -d

# With your existing Ollama
docker-compose -f docker-compose.external-ollama.yml up -d

# GPU support (NVIDIA)
docker-compose -f docker-compose.gpu.yml up -d
```

### Homebrew (macOS)
```bash
brew tap libre-webui/tap && brew install libre-webui
libre-webui

# Or install desktop app
brew install --cask libre-webui
```

### Kubernetes / Helm
```bash
helm install libre-webui oci://ghcr.io/libre-webui/charts/libre-webui
```

### Desktop App
Download from [GitHub Releases](https://github.com/libre-webui/libre-webui/releases) — macOS, Windows, Linux.

### Source (development)
```bash
git clone https://github.com/libre-webui/libre-webui
cd libre-webui
cp backend/.env.example backend/.env
npm install && npm run dev
```

---

## Configuration

Edit `backend/.env`:

```env
# Local AI (default, just install Ollama)
OLLAMA_BASE_URL=http://localhost:11434

# Cloud providers (optional, add only what you need)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
HUGGINGFACE_API_KEY=hf_...
```

### Add Any Provider in JSON
No code changes needed. Drop a config file:

```json
{
  "id": "my-provider",
  "name": "My Provider",
  "type": "completion",
  "endpoint": "https://api.example.com/v1/chat/completions",
  "auth": {
    "header": "Authorization",
    "prefix": "Bearer ",
    "key_env": "MY_API_KEY"
  },
  "model_map": ["model-a", "model-b"]
}
```

**Built-in plugins:** OpenAI, Anthropic, Google Gemini, Groq, Mistral, OpenRouter, HuggingFace, and more.

---

## Architecture

```
┌─────────────────────────────────────────────┐
│ Libre WebUI                                 │
├──────────────────┬──────────────────────────┤
│ React + TS       │ Express + SQLite         │
│ Frontend         │ Backend                  │
│ (Vite)           │ (AES-256 encryption)     │
├──────────────────┴──────────────────────────┤
│ Plugin Layer                                │
│ Ollama │ OpenAI │ Anthropic │ Google │ … │
├─────────────────────────────────────────────┤
│ Deployment                                  │
│ Electron (Desktop) │ Docker │ Kubernetes    │
└─────────────────────────────────────────────┘
```

### Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 + TypeScript, Vite, responsive, keyboard shortcuts |
| **Backend** | Express 5, SQLite with AES-256-GCM encryption, WebSocket streaming |
| **Plugins** | JSON config files — add any provider without code |
| **Desktop** | Electron with native macOS/Windows/Linux builds |

---

## Plugin Architecture

### Multi-Capability Plugins
Single config file can support:
- Chat completions
- Text-to-speech
- Image generation
- All in one provider entry

### Plugin Features
- Per-user variables
- Encrypted credential storage
- No code required (JSON only)
- Multi-provider support

**Example: OpenClaw Agent Plugin**
```json
{
  "id": "openclaw-agent",
  "name": "OpenClaw Agent",
  "type": "completion",
  "endpoint": "http://localhost:3000/v1/chat/completions",
  "auth": {
    "header": "Authorization",
    "prefix": "Bearer ",
    "key_env": "OPENCLAW_API_KEY"
  },
  "model_map": ["agent:main"]
}
```

📖 [Full plugin docs](https://github.com/libre-webui/libre-webui/blob/main/docs/08-PLUGIN_ARCHITECTURE.md)

---

## OpenClaw Agent Integration

Libre WebUI **natively supports AI agents** via OpenClaw plugin — turning chat into a full agent platform.

### Agent Capabilities

- **🧠 Persistent memory** — agents remember across sessions
- **🔧 Tool use** — file access, web search, code execution, device control
- **📅 Proactive actions** — scheduled tasks, reminders, heartbeat monitoring
- **🎙️ Voice messages** — agents generate + send audio via local TTS
- **🖼️ Image generation** — agents create images via ComfyUI, DALL·E
- **💬 Multi-channel** — same agent across Telegram, Discord, Signal, Nextcloud Talk
- **🔌 Plugin-powered** — configure via JSON, no code required

### Agent Brain Options
- **Local:** Claude, GPT, Gemini running locally
- **Cloud:** Same LLMs via cloud APIs
- **Hybrid:** Any combination, all through self-hosted interface

📖 [OpenClaw integration docs](https://github.com/libre-webui/libre-webui/blob/main/docs/31-OPENCLAW_INTEGRATION.md)

---

## Privacy & Ethics Charter

Libre WebUI has an **Ethical Charter** guaranteeing:

✅ **Apache 2.0 forever** — no bait-and-switch relicensing  
✅ **Zero telemetry** — no analytics, no tracking, no phone-home. Ever.  
✅ **Community governance** — transparent decisions, public roadmap  
✅ **No VC capture** — funded by community, for community  
✅ **Ethical use** — actively oppose surveillance + weapons applications  

[View Charter](https://github.com/libre-webui/libre-webui/blob/main/CHARTER.md)

---

## Enterprise & Professional Services

**Kroonen AI** provides professional deployment + compliance:

| Service | Description |
|---------|---|
| Custom Deployment | On-prem, cloud, air-gapped, Kubernetes |
| SSO Integration | Okta, Azure AD, SAML, LDAP |
| Custom Development | Integrations, white-labeling, plugins |
| Compliance | GDPR, HIPAA, SOC 2, FedRAMP |
| SLA Support | Priority response, dedicated channel |

📧 [enterprise@kroonen.ai](mailto:enterprise@kroonen.ai)

---

## Development & Contributing

### Getting Started
```bash
git clone https://github.com/libre-webui/libre-webui
cd libre-webui
npm install && npm run dev
```

### Contribution Process
1. Fork + clone
2. Branch off `dev`
3. Make changes
4. Open PR
5. One approving review from TSC → merged

### Ways to Contribute
- 🐛 Bug reports — open issues
- 💡 Feature ideas — discussions
- 🌍 Translations — help reach more languages
- 📖 Documentation — improve docs
- 🔌 Plugins — share provider configs

**Code of Conduct:** [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)

### Security
Found a vulnerability? Email [security@kroonen.ai](mailto:security@kroonen.ai)  
30-day coordinated disclosure policy.

---

## Use Cases

### 1. Local AI Chat (Privacy-First)
- Run Claude/Llama/Qwen locally via Ollama
- No cloud dependency
- Conversations never leave your machine

### 2. Multi-Provider Aggregation
- Fallback between OpenAI, Anthropic, Google
- Mix local + cloud in one UI
- Cost optimization (use cheap provider for simple tasks)

### 3. Enterprise RAG
- Upload internal documents
- Search + retrieve with local embeddings
- HIPAA/GDPR compliant

### 4. AI Agents Platform
- Run persistent agents with memory
- Agents access tools (file system, web, code execution)
- Multi-channel deployment (Telegram, Discord, etc.)

### 5. SME Internal Tool
- Self-hosted behind corporate firewall
- No external vendor lock-in
- Full data ownership

---

## Integration Ecosystem

### Connects With
- **Ollama** (local LLMs)
- **OpenAI, Anthropic, Google, Groq, Mistral** (cloud APIs)
- **HuggingFace Hub** (model discovery + inference)
- **ComfyUI, Flux** (image generation)
- **Qwen3-TTS, Kyutai** (text-to-speech)
- **OpenClaw** (AI agents)
- **Kubernetes, Docker, Electron** (deployment)

### Used By
- Enterprises (compliance-critical)
- Open-source communities
- Researchers (local model testing)
- SMEs (cost-conscious, privacy-first)

---

## Comparison with Alternatives

### vs. ChatGPT/Claude.ai
- ✅ Self-hosted, full control
- ✅ Privacy guaranteed
- ✅ Works offline (local models)
- ❌ Requires setup + maintenance

### vs. Ollama Web UI
- ✅ Much more polished UI
- ✅ Multi-provider support (not just Ollama)
- ✅ Document RAG built-in
- ✅ AI agents + OpenClaw integration

### vs. Open WebUI
- ✅ Cleaner architecture
- ✅ Better plugin system
- ✅ OpenClaw-native (agents)
- ✅ Ethical charter (no license tricks)

---

## Links

| Resource | URL |
|----------|-----|
| **Website** | https://librewebui.org |
| **Docs** | https://docs.librewebui.org |
| **GitHub** | https://github.com/libre-webui/libre-webui |
| **GitLab** | https://git.kroonen.ai/libre-webui/libre-webui |
| **HuggingFace** | https://huggingface.co/libre-webui |
| **Twitter** | @librewebui |
| **Mastodon** | @librewebui@fosstodon.org |
| **Sponsor** | https://github.com/sponsors/libre-webui |

---

## Categories
Local AI, privacy, open-source, self-hosted, web UI, Ollama, chat interface, AI agents, OpenClaw, plugin architecture, document RAG, multi-provider, ethics, charter

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
