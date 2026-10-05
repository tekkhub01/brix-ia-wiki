---
id: immich-project
pageType: source
title: "Immich — Self-hosted Photo/Video Management"
type: source
date: 2026-06-05
updatedAt: 2026-09-13T04:40:00Z
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

## Stato release (verifica web 2026-09-13)

- **v3.2.0** rilasciata il 2026-09-10 (GitHub releases); serie v3.x attiva dai rc di maggio.
- **v3.0.0** ha rimosso il supporto pgvecto.rs: chi arriva da <v1.133.0 deve fare la migrazione prima dell'upgrade (migration guide nei docs).
- Rilevante per un'installazione nuova (non ancora fatta): nessun vincolo di migrazione, partire da v3.2.0.

## Collegamenti (dreaming 2026-08-15)

- Stesso pattern self-hosted privacy-first di [Libre WebUI](libre-webui-github.md), dominio diverso
- Contesto operativo: [BRIX-IA](../entities/brix-ia.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Libre WebUI — Privacy-First Web Interface for Local AI](libre-webui-github.md)
<!-- openclaw:wiki:related:end -->
