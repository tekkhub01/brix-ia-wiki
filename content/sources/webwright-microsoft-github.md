---
id: webwright-microsoft-github
pageType: source
updatedAt: 2026-06-06T00:00:00Z
publish: true
---

# Webwright — Microsoft Browser Agent Skill

**Source:** https://github.com/microsoft/Webwright
**Author:** Microsoft
**Type:** Open-source AI agent skill / browser automation framework
**Category:** Browser agents, AI automation, Playwright, agentic coding

---

## Overview

Webwright è una skill open source di Microsoft per agenti AI che abilita il controllo programmatico del browser tramite codice Playwright.

A differenza degli agenti browser tradizionali che funzionano step-by-step (guarda → predici click → esegui), Webwright adotta un approccio "write-and-execute": l'agente scrive interi script Playwright, li esegue in terminale, legge i log e itera.

## Architettura

- L'agente non interagisce con il DOM in tempo reale
- Scrive codice Playwright completo come farebbe un developer
- Esegue il codice in un terminale sandbox
- Analizza l'output e itera fino al completamento
- Il browser è uno strumento da avviare/chiudere, non un ambiente permanente

## Benchmark

| Benchmark | Webwright | Opus 4.6 | GPT-5.4 base |
|---|---|---|---|
| Online-Mind2Web | 86.67% | 44.5% | — |
| Odysseys | 60.1% | — | 33.5% |

## Requisiti

- Python ≥ 3.10
- Playwright / Chromium
- Backend supportati: OpenAI, Anthropic, OpenRouter

## Rilevanza

Solo una minima parte dei siti web espone API pubbliche. La maggior parte dell'interazione digitale avviene tramite interfacce web. Webwright apre agli agenti AI l'accesso a questo "web restante" senza necessità di API dedicate.

## Riferimenti

- GitHub: https://github.com/microsoft/Webwright
- Scoperto tramite: INCUBE.AI (Telegram), 2026-06-06
- Lingua originale: russo

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

<!-- openclaw:wiki:related:end -->
