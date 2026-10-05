---
title: "Hugging Face"
id: hugging-face
pageType: entity
entityType: organization
sourceIds:
  - sources/libre-webui-github.md
  - sources/brix-ia-newsletter-news-aprile-2026.md
updatedAt: 2026-09-01T00:00:00Z
publish: true
---

# Hugging Face

**Type:** organization — hub di distribuzione modelli, ecosistema di librerie
**Sito:** https://huggingface.co
**Rilevanza per questo vault:** è l'indirizzo da cui arriva ogni peso open-weight
che questo vault raccomanda di eseguire. Compare in nove pagine sempre nella stessa
posizione — dentro un percorso di download — e mai come soggetto

## Prodotti

### Hub

Catalogo di modelli. La cifra che circola nel vault è "**1M+ models** for chat, TTS,
images, embeddings, STT", dichiarata da [Libre WebUI](../sources/libre-webui-github.md)
e mai verificata alla fonte.

I repository effettivamente citati come coordinate operative nelle pagine di questo
vault:

| Repo | Cosa contiene | Citato in |
|---|---|---|
| `zai-org/GLM-5.1` | pesi GLM-5.1, licenza MIT | [Z.AI](z-ai.md) |
| `unsloth/*-GGUF` | i quant dinamici | [Unsloth](unsloth.md) |
| `nvidia/parakeet-tdt-0.6b-v2` | modello STT | [NVIDIA](nvidia.md) |

### Ecosistema di librerie

`bitsandbytes` (quantizzazione 4/8 bit) è citato fra i formati in
[Quantization](../concepts/quantization.md); le convenzioni
di nomenclatura dei quant (`TQ2_0`, `TQ1_0`) sono registrate come "nomi HF" anche
quando il formato è di [ggml](ggml.md).

### Autenticazione come infrastruttura

Libre WebUI usa HuggingFace OAuth/OIDC per l'accesso a ruoli, accanto a GitHub. È
l'unico punto del vault in cui HF compare come *fornitore di identità* e non come
scaffale di pesi.

## Perché ci interessa

Per una ragione di rischio, più che di capacità. Ogni raccomandazione di inferenza
locale in questo vault — che è il tema su cui BRIX-IA fa consulenza — presuppone
implicitamente che i pesi si scarichino da qui. È una dipendenza singola, mai
esaminata: nessuna pagina discute cosa succede a una PMI se un repo cambia licenza,
sparisce, o diventa irraggiungibile, né quali dei modelli raccomandati siano
mirrorati altrove.

**Limite di questa pagina.** Non esiste in questo vault alcun dato aziendale su
Hugging Face — non funding, non modello di business, non termini di servizio. È una
scheda di come l'organizzazione appare *dall'interno delle nostre pipeline*, che è
l'unico materiale disponibile, e va usata solo per quello.

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Anthropic](anthropic.md)
- [BRIX-IA](brix-ia.md)
- [OpenRouter](openrouter.md)
- [scrya-com](scrya-com.md)
- [Z.AI (Zhipu AI)](z-ai.md)
<!-- openclaw:wiki:related:end -->
