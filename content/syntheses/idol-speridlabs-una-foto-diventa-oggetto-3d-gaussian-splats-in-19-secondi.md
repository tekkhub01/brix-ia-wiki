---
pageType: synthesis
id: synthesis.idol-speridlabs-una-foto-diventa-oggetto-3d-gaussian-splats-in-19-secondi
title: "Idol (Speridlabs) — una foto diventa oggetto 3D Gaussian splats in 19 secondi, Apache 2.0"
sourceIds:
  - https://speridlabs.com/research/idol
  - telegram:brixia-newsletter/2026-11-01
claims:
  - text: "Idol (Speridlabs, progetto guidato da Alejandro Cañada, rilascio 28/10/2026): da una singola immagine — foto, render o immagine generata — produce un oggetto 3D completo di Gaussian splats, incluse le facce mai mostrate dalla foto. Codice e pesi Apache 2.0, modello su Hugging Face con demo gratuita ZeroGPU."
    status: supported
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://speridlabs.com/research/idol
        weight: 1
        note: pagina ufficiale + model card HF, verificati 2026-10-31 per la newsletter #54
  - text: "Numeri consumer: generatore 0,66B parametri, picco 7,2 GB VRAM per richiesta; 19,1 s su RTX 4090 (3,4 s B300, 46 s su 3080); dettaglio regolabile da 32.768 a 1.048.576 Gaussians per oggetto."
    status: supported
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://speridlabs.com/research/idol
        weight: 1
  - text: "Vince nel confronto diretto contro TripoSplat e TRELLIS su DINOv2/CLIP/sharpness a parità di step."
    status: reported
    confidence: 0.6
    evidence:
      - kind: web
        sourceId: https://speridlabs.com/research/idol
        weight: 0.6
        note: confronto pubblicato dai maintainers, non indipendente
  - text: "Due limiti tecnici: l'output è un .ply di 3DGS, non una mesh (ok visualizzazione e game prop, da convertire per CAD/animazione); la pipeline completa pesa ~1,8B parametri in GPU perché usa anche DINOv3 di Meta, il VAE di FLUX.2-dev e BiRefNet."
    status: supported
    confidence: 0.85
    evidence:
      - kind: web
        sourceId: https://speridlabs.com/research/idol
        weight: 0.8
        note: componenti dichiarati; verificato anche via ArtRealmAI e repo
  - text: "Il nome è Idol, non IDLE: la trascrizione del video di lancio lo trascrive IDLE, citarlo così lo rende irreperibile."
    status: supported
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://speridlabs.com/research/idol
        weight: 1
        note: citazione ufficiale Cañada & Garabito, 2026
questions:
  - Qualità reale su oggetti con superfici speculari/trasparenti (vetro, metallo): i benchmark DINOv2/CLIP non la catturano.
  - Converting 3DGS → mesh usabile (per CAD o animazione): quale pipeline regge?
  - Angolo BRIX-IA da testare: foto prodotto in galleria → oggetto 3D ruotabile per catalogo e-commerce/configuratori — prova pratica con una foto reale.
status: active
publish: true
updatedAt: 2026-11-01T14:05:00Z
---

# Idol (Speridlabs) — una foto diventa oggetto 3D Gaussian splats in 19 secondi, Apache 2.0

## Notes
<!-- openclaw:human:start -->
Il pezzo open source più "provalo oggi" della settimana #54. Attenzione al nome: Idol, non IDLE.

Vedi anche: Spark X2 (on-device, altra fascia). Copertura: newsletter #54 del 01-11-2026; copertina video scena 5 (news54-video).
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
**Idol** di **Speridlabs** (28/10/2026, Apache 2.0): una singola immagine diventa un oggetto 3D completo di **Gaussian splats**, comprese le facce che la foto non ha mai mostrato. Il generatore è da **0,66B parametri con picco di 7,2 GB VRAM**: gira su qualsiasi GPU consumer da 8 GB. **19,1 secondi su RTX 4090**, dettaglio regolabile fino a 1M Gaussians.

Onestà tecniche: l'output è un **.ply di 3DGS, non una mesh** — perfetto per visualizzazione e game prop, da convertire se serve CAD/animazione. E sotto il cofano la pipeline reale pesa ~1,8B parametri (DINOv3 + VAE FLUX.2-dev + BiRefNet).

**Lettura BRIX-IA**: il 3D per cataloghi, presentazioni e configuratori smette di essere un appalto: una foto del prodotto e hai un oggetto ruotabile in venti secondi su GPU consumer. Apache 2.0 significa che ci si può costruire sopra un servizio.

## Contesto in vault
- Generazione 3D/asset: Spark X2 (on-device, altra fascia)
- Newsletter di copertura: #54 del 01-11-2026; copertina video scena 5 (news54-video)
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Anthropic S-1 — i primi numeri pubblici di un frontier lab: ticker ANT, $16,3 mld H1, utile operativo Q2](anthropic-s-1-i-primi-numeri-pubblici-di-un-frontier-lab-ticker-ant-16-3-mld-h1-utile-operativo-q2.md)
- [Gemini 4 Carbon — il frontier Google a accesso controllato: #1 AA v5, SOTA cybersecurity, rollout solo cyber defenders](gemini-4-carbon-il-frontier-google-a-accesso-controllato-1-aa-v5-sota-cybersecurity-rollout-solo-cyber-defenders.md)
- [Google "Sleep" framework — consolidamento offline dei modelli linguistici: BABILong a 10M token](google-sleep-framework-consolidamento-offline-dei-modelli-linguistici.md)
- [Kimi K3.1 Pro (Moonshot) — il frontier aperto in arrivo: 2,8T parametri, pesi annunciati per il 4 novembre](kimi-k3-1-pro-moonshot-il-frontier-aperto-in-arrivo-2-8t-parametri-pesi-annunciati-per-il-4-novembre.md)
<!-- openclaw:wiki:related:end -->
