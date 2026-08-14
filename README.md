# BRIX-IA Wiki

Sito pubblico della knowledge base della community BRIX-IA, generato con
[Quartz 5](https://github.com/jackyzha0/quartz).

## Come funziona

Il contenuto **non si edita qui**. La source of truth è un vault privato
sulla macchina BRIX-IA (`~/.openclaw/wiki`), mantenuto dal plugin
`memory-wiki` di OpenClaw secondo il pattern LLM Wiki di Karpathy.

```
~/.openclaw/wiki          vault privato — sources, entities, syntheses
      │
      │  ./sync.py        copia SOLO le pagine con `publish: true`
      ▼
   content/               generato, non editare a mano
      │
      │  npx quartz build
      ▼
   public/                sito statico → Cloudflare Pages
```

## Il gate di pubblicazione

Una pagina finisce online **solo** se ha `publish: true` nel frontmatter.
Il controllo è a due livelli, di proposito:

1. **`sync.py`** — non copia i file privati, quindi non vengono nemmeno
   committati. Questo è il livello che conta: il repo è pubblico, e un
   file committato è leggibile su GitHub anche se escluso dal build.
2. **`@quartz-community/explicit-publish`** — seconda cintura lato build.

`sync.py` fa anche due cose che il filtro da solo non copre:

- **neutralizza i link** verso pagine non pubblicate, convertendoli in
  testo semplice. Altrimenti resterebbero link morti che, per giunta,
  rivelano il titolo di pagine che abbiamo deciso di non pubblicare;
- avvisa a video di ogni link neutralizzato, così le omissioni restano
  visibili invece di sparire in silenzio.

⚠️ **I file non-markdown (immagini, PDF) vengono emessi sempre**, filtro o
no — è un comportamento documentato di Quartz. Per questo
`quartz.config.yaml` ha `ignorePatterns` sulle estensioni binarie. Se
aggiungi allegati, verifica lì prima di pubblicare.

⚠️ Escludere un file **non redige la prosa**: se una pagina pubblicata
_nomina_ un argomento privato, il testo resta. Il filtro lavora sui file,
non sui contenuti.

## Uso

```bash
./sync.py --dry-run    # cosa verrebbe pubblicato, senza scrivere
./sync.py              # rigenera content/
npx quartz build --serve   # anteprima su localhost:8080
```

## Deploy — self-host (attivo)

Servito da nginx dietro il Cloudflare Tunnel e il Tailscale Funnel già in
uso sulla macchina:

- https://share.transizione-digital.it/wiki/
- https://brix-ia-linux.tail216abe.ts.net:10000/wiki/

**Setup iniziale, una tantum** (l'unico passo che richiede sudo):

```bash
sudo mkdir -p /srv/www/wiki && sudo chown "$USER:$USER" /srv/www/wiki
sudo sh -c 'cat deploy/wiki.nginx.conf >> /etc/nginx/sites-available/funnel'  # vedi nota
sudo nginx -t && sudo systemctl reload nginx
```

> ⚠️ Lo snippet va inserito **dentro** il `server { … }` e **prima** della
> `location /` finale che ritorna 404, non appeso in fondo al file.

**Aggiornamenti**, senza sudo:

```bash
./deploy/deploy.sh    # sync + build + rsync su /srv/www/wiki
```

## Deploy — Cloudflare Pages (alternativa)

Build automatica a ogni push su `main`.

| | |
|---|---|
| Build command | `npx quartz plugin install --from-config && npx quartz build` |
| Output directory | `public` |
| Node | pinnato in `.nvmrc` (Pages **non** legge `engines` da package.json) |

## Aggiornare Quartz

Il remote `upstream` punta al repo Quartz originale:

```bash
git fetch upstream && git merge upstream/v5
```

## Contributi

Il sito è in sola lettura; le proposte si fanno via pull request.

⚠️ **Nodo ancora aperto:** `content/` è rigenerato da `sync.py` a partire
dal vault, quindi una PR che modifica `content/` verrebbe sovrascritta al
sync successivo. Prima di aprire i contributi va deciso il percorso di
ritorno verso il vault.
