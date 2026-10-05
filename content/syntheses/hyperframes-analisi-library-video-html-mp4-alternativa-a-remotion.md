---
pageType: synthesis
id: synthesis.hyperframes-analisi-library-video-html-mp4-alternativa-a-remotion
title: HyperFrames — analisi library video HTML→MP4 (alternativa a Remotion)
sourceIds:
  - github:heygen-com/hyperframes
  - docs:hyperframes-introduction
claims:
  - id: hf-1
    text: HyperFrames è un framework open-source di HeyGen che trasforma HTML/CSS +
      animazioni seekable in video MP4 deterministici; released come OSS, repo
      heygen-com/hyperframes, npm package hyperframes.
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: github:heygen-com/hyperframes
        path: https://github.com/heygen-com/hyperframes
        weight: 0.9
        note: README fetch 2026-10-01
  - id: hf-2
    text: "Modello d'uso: CLI (npx hyperframes) oppure 21 skill installabili per
      coding agents (Claude Code, Codex, Cursor, Gemini CLI) che insegnano il
      loop plan → HTML → anima → media → lint → preview → render."
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: github:heygen-com/hyperframes
        weight: 0.9
        note: "README: plugin/skills install"
  - id: hf-3
    text: Il rendering è deterministico (stessa HTML = stesso video,
      frame-by-frame), a differenza dei modelli video generativi.
    confidence: 0.85
    evidence:
      - kind: web
        sourceId: docs:hyperframes-introduction
        path: https://hyperframes.heygen.com/introduction
        weight: 0.8
  - id: hf-4
    text: "Per il nostro stack è un'alternativa diretta alla skill
      remotion-chat-dialog (React/Remotion → ffmpeg): stesso pattern
      browser-headless→video, ma authoring HTML+CSS puro senza JSX, con catalogo
      block pronti (data-chart, title card) e playground su hyperframes.dev."
    confidence: 0.8
    evidence:
      - kind: memory
        path: ~/.openclaw/skills/remotion-chat-dialog/SKILL.md
        weight: 0.7
        note: pipeline esistente Remotion→mp4
      - kind: web
        sourceId: github:heygen-com/hyperframes
        weight: 0.8
  - id: hf-5
    text: "Candidati d'uso interni: cover animate newsletter BRIX-IA, conversione
      carousel LinkedIn→video, grafiche animate per le schede azioni di
      analisi-quotata; tutto self-hosted senza abbonamento HeyGen."
    confidence: 0.6
    evidence:
      - kind: memory
        path: MEMORY.md
        weight: 0.5
        note: pipeline esistenti che oggi usano immagini statiche/HeyGen
  - id: hf-6
    text: "Non ancora testato sul server: adozione da decidere dopo un test render
      (title card animata ~10s). Node-based, headless, compatibile con
      l'ambiente attuale."
    status: open
    confidence: 0.7
    evidence:
      - kind: session
        path: chat 2026-10-01
        weight: 0.6
        note: proposta di test non ancora eseguita
contradictions: []
questions:
  - HyperFrames regge font/emoji e rendering CJK headless sul nostro server come
    la pipeline Remotion attuale?
  - La licenza OSS consente uso commerciale self-hosted senza limiti (verificare
    LICENSE)?
  - Performance render 4K vs Remotion su hardware nostro?
confidence: 0.75
status: draft
updatedAt: 2026-10-01T09:34:42.664Z
publish: true
---

# HyperFrames — analisi library video HTML→MP4 (alternativa a Remotion)

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
## Sintesi

**HyperFrames** (HeyGen, open-source — github.com/heygen-com/hyperframes) è un framework che trasforma **HTML/CSS + animazioni seekable in video MP4 deterministici**. Tagline: "Write HTML. Render video. Built for agents" — è progettato perché siano agenti AI a scrivere la composition e renderizzarla.

## Come funziona

- **CLI**: `npx hyperframes` (init, lint, preview, render)
- **Skill per coding agents**: 21 skill (Claude Code, Codex, Cursor, Gemini CLI) che insegnano il loop di produzione: brief → HTML valido → animazioni → media → lint → preview → render
- **Determinismo**: stessa HTML = stesso video, frame per frame (niente "lottery" dei modelli generativi)
- **Ecosistema**: playground (hyperframes.dev), catalogo block pronti (data-chart, title card, ecc.), docs su hyperframes.heygen.com

## Confronto con Remotion (nostro stack attuale)

| Aspetto | Remotion (skill `remotion-chat-dialog`) | HyperFrames |
|---|---|---|
| Authoring | React/JSX + `useCurrentFrame()` | HTML/CSS puro con timeline seekable |
| Rendering | headless browser → ffmpeg | analogo (browser headless → MP4) |
| Agent-friendliness | richiede scrivere JSX | pensato esplicitamente per agenti (skill + lint) |
| Componenti pronti | nessun catalogo | catalogo block (chart, title card…) |
| Maturità | consolidato, lo usiamo da tempo | appena open-source, da validare |

È concettualmente la **stessa architettura che abbiamo già adottato** (HTML→video via Playwright/ffmpeg, come anche la skill `genera-video-3d`), generalizzata e con formato di authoring più semplice.

## Candidati d'uso per noi

1. **Video BRIX-IA**: cover animate newsletter, conversione carousel LinkedIn → video
2. **Schede azioni `analisi-quotata`**: grafiche animate sui dati (EMA, fondamentali) invece di PNG statici
3. **Sostituzione/semplificazione della pipeline Remotion** per i dialoghi chat

Tutto self-hosted, senza abbonamento HeyGen.

## Stato e prossimi passi

- ❓ **Non ancora testato sul server.** Proposta: test render di una title card animata BRIX-IA ~10s per giudicare qualità e performance prima di decidere l'adozione.
- Da verificare: licenza (uso commerciale), font/emoji headless, resa 4K su hardware nostro.

---
*Fonti: repo GitHub e docs ufficiali (fetch 2026-10-01), skill locali remotion-chat-dialog, analisi sessione chat 2026-10-01.*
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
