---
id: immich-project
pageType: source
title: "Immich — Self-hosted Photo/Video Management"
type: source
date: 2026-06-05
updatedAt: 2026-06-05T00:00:00Z
tags: [progetto, self-hosted, foto, video, privacy, open-source]
url: https://immich.app/
publish: true
---

# Immich — Self-hosted Photo/Video Management

**Sito:** https://immich.app/
**Documentazione:** https://docs.immich.app/
**Repository:** https://github.com/immich-app/immich
**Sviluppatore:** FUTO
**Licenza:** Open Source

---

## Descrizione

Immich è un'applicazione self-hosted open-source per la gestione di foto e video. Alternativa privacy-first a Google Photos, permette di:

- **Backup automatico** foto e video da smartphone (Android/iOS)
- **Galleria** con visualizzazione timeline e album
- **Ricerca intelligente** con riconoscimento facciale e oggetti (ML)
- **Mappe** con geolocalizzazione foto
- **Condivisione** con link pubblici o con utenti specifici
- **Supporto RAW** e formati professionali
- **API REST** per integrazioni

## Architettura

- **Server:** Docker (compose) con PostgreSQL, Redis, microservizi ML
- **Client:** App Android/iOS + web app
- **Storage:** filesystem locale o S3-compatible

## Requisiti Server

- Docker e Docker Compose
- Minimo 2 GB RAM (consigliati 4+ GB per ML)
- Storage variabile in base alla libreria

## Note progetto

- **Data inserimento:** 2026-06-05
- **Motivazione:** Peter ha condiviso il link come progetto da valutare/installare
- **Stato:** Da valutare — possibile installazione su brix-ia-linux

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
