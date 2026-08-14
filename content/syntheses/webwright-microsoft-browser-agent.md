---
pageType: synthesis
id: synthesis.webwright-microsoft-browser-agent
title: Webwright — Microsoft Browser Agent
sourceIds:
  - webwright-microsoft-github
status: active
updatedAt: 2026-06-06T12:46:17.140Z
publish: true
---

# Webwright — Microsoft Browser Agent

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Webwright — Microsoft Browser Agent

## Cos'è
Webwright è un progetto open source di Microsoft che funziona come **skill per agenti AI** (complementare al [LLM Wiki](../concepts/llm-wiki-karpathy.md) per l automazione web) per il controllo del browser. Rilasciato su GitHub: https://github.com/microsoft/Webwright

## Come funziona
A differenza degli agenti browser tradizionali (guarda pagina → predice click → esegue, ogni step = chiamata al modello), Webwright adotta un approccio diverso:

- L'agente **scrive codice Playwright completo** in blocco
- Lo esegue in terminale
- Legge i log e itera
- Il browser non è un ambiente ma uno **strumento** da avviare e chiudere

Vantaggi: più veloce, meno costoso, più affidabile rispetto al pattern step-by-step.

## Benchmark
- **Online-Mind2Web:** 86.67%
- **Odysseys:** 60.1%
- vs Opus 4.6: 44.5%
- vs GPT-5.4 base: 33.5%

## Relevanza per noi
La maggior parte dei siti non ha API pubbliche — solo interfacce web. Webwright apre agli agenti l'accesso a questo "resto del web". Potenziale integrazione come skill OpenClaw per browser automation.

## Riferimenti
- GitHub: https://github.com/microsoft/Webwright
- Requisiti: Python ≥3.10, Playwright/Chromium
- Backend supportati: OpenAI, Anthropic, OpenRouter
- Lingua originale della segnalazione: russo
- Data scoperta: 2026-06-06
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Webwright — Microsoft Browser Agent Skill](../sources/webwright-microsoft-github.md)
<!-- openclaw:wiki:related:end -->
