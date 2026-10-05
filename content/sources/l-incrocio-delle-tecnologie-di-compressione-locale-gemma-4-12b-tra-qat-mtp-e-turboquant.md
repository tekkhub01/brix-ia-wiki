---
pageType: source
id: source.l-incrocio-delle-tecnologie-di-compressione-locale-gemma-4-12b-tra-qat-mtp-e-turboquant
title: L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT,
  MTP e TurboQuant
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/media/inbound/Esperimenti_Quantizzazione_Gemma_4_1---96861467-650a-41d7-bc76-eedb62006fd3.pdf
ingestedAt: 2026-08-28T09:14:57.014Z
updatedAt: 2026-08-28T09:14:57.014Z
status: active
publish: true
date: 2026-06-11
tags: [quantization, qat, mtp, turboquant, kv-cache, gemma, local-inference, llama-cpp, vllm]
---

# L'Incrocio delle Tecnologie di Compressione Locale — Gemma 4 12B tra QAT, MTP e TurboQuant

## Source
- Type: `local-file`
- Origine: PDF allegato da PK su Telegram (2026-06-11), 17 pagine, reso da Google Docs
- Estrazione: PyMuPDF 1.27.2 con ricostruzione di titoli e tabelle (MinerU irraggiungibile il 2026-08-28)
- Bytes: 38672
- Updated: 2026-08-28T09:14:57.014Z

## Content
## L'Incrocio delle Tecnologie di Compressione Locale: Analisi Tecnica e Sperimentale di Gemma 4 12B tra QAT, MTP e TurboQuant

La corsa verso l'ottimizzazione dell'inferenza locale su hardware di livello consumer ha registrato una forte accelerazione con il rilascio, avvenuto il 3 giugno 2026, del modello Gemma 4 12B Unified. [1] Sviluppato da Google DeepMind, questo modello si colloca strategicamente tra i compatti modelli per dispositivi mobili (come Gemma 4 E2B ed E4B) e le varianti più pesanti destinate ai server (quali la 26B Mixture of Experts e la 31B Dense). [3] L'elemento di maggiore interesse per i ricercatori e gli ingegneri dei sistemi risiede nella possibilità di eseguire flussi di lavoro multimodali e agentici complessi su laptop standard dotati di soli 16 GB di memoria unificata o VRAM, offrendo prestazioni teoriche ed empiriche che sfiorano quelle del modello 26B, ma con un'impronta di memoria dimezzata. [3]

L'interesse scientifico e applicativo per Gemma 4 12B non è limitato alla sua sola scala di parametri. [5] La community di sviluppatori e ricercatori sta conducendo esperimenti avanzati integrando tre tecnologie di frontiera: l'addestramento consapevole della quantizzazione (Quantization-Aware Training, o QAT) [6], la decodifica speculativa tramite Multi-Token Prediction (MTP) [8] e la compressione geometrica del cache Key-Value (KV) mediante la tecnologia TurboQuant. [10] L'analisi di queste metodologie svela dinamiche di sistema complesse, sinergie inaspettate e barriere architetturali non banali che si manifestano quando si tenta di combinare la compressione dei pesi con quella del runtime di calcolo. [12]

### L'Architettura Encoder-Free di Gemma 4 12B Unified

Gemma 4 12B Unified implementa un modello denso, decoder-only, composto da 11,95 miliardi di parametri attivi, strutturato su 48 strati di transformer, con una finestra di attenzione locale (sliding window) impostata a 1024 token e un contesto globale massimo che si estende fino a 256K token. [14] A differenza dei modelli multimodali tradizionali, che innestano encoder esterni e congelati per elaborare immagini e audio (richiedendo solitamente un modello di visione da 550M parametri e un modulo conformer da 300M parametri), il modello 12B adotta un'architettura unificata e completamente priva di encoder. [5]

[ Input Multimodali ]​

│​ ┌──────────────────────────┼──────────────────────────┐​ ▼ ▼ ▼​ [ Immagini ] [ Audio ]​ │ │ │​ │ (Vision Embedder 35M) (Linear Projection)​ │ 48x48 patches via matmul 16 kHz / 40ms slices​ │ │ │​ └──────────────────────────┼──────────────────────────┘​ │​ ▼​ ​ (Condivisione totale pesi)​ Il trattamento dei flussi multimodali avviene proiettando direttamente i dati grezzi nello spazio degli embedding del decoder [5]:

●​ Vision Embedder (35M parametri): Questo componente leggero sostituisce integralmente i 27 strati di vision transformer tipicamente impiegati nelle altre varianti

medie della famiglia Gemma 4. [5] Le patch d'immagine grezze da pixel vengono proiettate nella dimensione nascosta dell'LLM tramite un'unica moltiplicazione di matrice (matmul). [5] Un sistema di coordinate fattorizzato (Lookup su matrici X e Y) associa le informazioni spaziali direttamente all'input. [5]

●​ Audio Wave Projection: Elimina la necessità di ricorrere a un encoder audio dedicato, bypassando i 12 strati conformer delle varianti minori. [5] Il segnale audio analogico, campionato a 16 kHz, viene segmentato in frame da 40 ms (ciascuno composto da 640 float) e proiettato linearmente nello spazio dei token del decoder. [5]

●​ Ottimizzazione del Fine-Tuning: Poiché gli input di testo, immagine e audio condividono gli stessi pesi del decoder, decade la necessità di sintonizzare separatamente i diversi moduli. [5] Eventuali adattatori downstream (come LoRA) o sessioni di fine-tuning completo aggiornano l'intero ciclo di token multimodali in un unico passaggio su librerie come Unsloth o Hugging Face. [5]

Sotto il profilo del software di runtime locale, l'ecosistema si appoggia alla suite Google AI Edge. [4] Su macOS, applicazioni desktop native come Google AI Edge Gallery sfruttano le GPU Apple Silicon per abilitare l'esecuzione offline di script Python complessi e rendering 3D (tramite librerie come Trimesh) con capacità di auto-correzione del codice in un singolo turno. [15] Inoltre, l'applicazione Eloquent introduce Voice Edit, un sistema che elabora nativamente i comandi vocali sfruttando l'architettura encoder-free per la dettatura e la ristrutturazione del testo in tempo reale. [15] La distribuzione a riga di comando si avvale del CLI di LiteRT-LM, il quale introduce il comando serve per creare endpoint locali compatibili con gli standard industriali di

integrazione (come Continue, Aider e OpenClaw), sfruttando la cache dei prefissi stateless in memoria per annullare la latenza di pre-riempimento (prefill). [5]

| Parametro Architetturale | Valore / Specifica | Impatto di Sistema |
|---|---|---|
| Parametri Totali | 11,95 Miliardi [14] | Bilanciamento tra hardware locale e capacità di ragionamento [3] |
| Strati Transformer | 48 [14] | Profondità strutturale equivalente alla variante 31B Dense [5] |
| Dimensione Vocabolario | 262K token [14] | Tokenizzazione ottimizzata per ridurre la lunghezza delle sequenze [16] |
| Finestra Scorrevole | 1024 token [14] | Limitazione della memoria locale negli strati ad attenzione locale [17] |
| Contesto Massimo | 256K token [14] | Supporto per l'analisi di lunghi flussi multimodali (es. video) [1] |
| Footprint BF16 (Peso) | 26,7 GB [2] | Richiede hardware di classe workstation per l'esecuzione non quantizzata [2] |
| Footprint Q4_0 (Peso) | 6,7 GB [2] | Consente l'esecuzione su laptop consumer con 16 GB di RAM [3] |

### Quantization-Aware Training (QAT) e l'Approccio Unsloth Dynamic

La contrazione del modello per l'esecuzione locale richiede solitamente tecniche di quantizzazione post-addestramento (Post-Training Quantization, o PTQ). [6] Tuttavia, l'arrotondamento dei pesi matematici applicato a posteriori introduce errori sistematici che compromettono le capacità logiche complesse e l'aderenza alle istruzioni. [12] Per aggirare questa degradazione, Google ha introdotto checkpoint ottimizzati tramite Quantization-Aware Training (QAT). [6]

Durante la fase di QAT, l'effetto della riduzione di precisione (es. a 4 bit) viene simulato direttamente all'interno del ciclo di ottimizzazione del modello. [6] I pesi del transformer imparano così a compensare matematicamente l'errore di discretizzazione, preservando quasi interamente la qualità originale del modello a piena precisione (BF16). [12]

Un problema tecnico rilevante sorge quando si convertono i checkpoint QAT BF16 nativi nel diffuso formato GGUF di llama.cpp. [18] Poiché llama.cpp calcola le scale in precisione F16, mentre il formato originale QAT utilizza scale BF16, una conversione ingenua determina inesattezze sistematiche che riducono l'accuratezza Top-1 del modello 26B-A4B ad appena il 70,20%. [18] Inoltre, l'esattezza dei byte rispetto al checkpoint originale si attesta su un modesto 24,77%. [18]

Per colmare questo divario, gli ingegneri di Unsloth hanno sviluppato il metodo Unsloth Dynamic (UD-Q4_K_XL). [18] Questo approccio forza un allineamento matematico preciso tra il formato di scala di llama.cpp e quello di QAT, elevando l'esattezza dei byte al 99,96%. [18] Il metodo ottimizza le dimensioni del file omettendo le quantizzazioni elevate Q6_K sugli embedding (giudicate ridondanti) e riducendo l'ingombro su disco di circa 200 MB rispetto a un quantizzatore Q4_0 ingenuo, incrementando contemporaneamente le prestazioni logiche del modello. [18]

#### Analisi Comparativa delle Prestazioni: Naive Q4_0 vs Unsloth Dynamic QAT

La tabella seguente illustra il divario di accuratezza e di divergenza di Kullback-Leibler (KLD) indotto dai due diversi metodi di quantizzazione su tutta la famiglia Gemma 4. [18] Una divergenza KL inferiore indica una fedeltà superiore al modello BF16 non quantizzato. [18]

| Modello e Configurazione | Accuratezza Top-1 | Divergenza KL Media | KLD al Percentile 99.9% | Dimensione File (GB) |
|---|---|---|---|---|
| Gemma 4 E2B (Naive Q4_0) | 89,29% [18] | 0,05109 [18] | 1,0513 [18] | 3,35 GB [18] |
| Gemma 4 E2B (Unsloth Dynamic) | 98,16% [18] | 0,00173 [18] | 0,0557 [18] | 2,62 GB [18] |
| Gemma 4 E4B (Naive Q4_0) | 90,94% [18] | 0,03778 [18] | 0,6722 [18] | 5,15 GB [18] |
| Gemma 4 E4B | 98,54% [18] | 0,00121 [18] | 0,0536 [18] | 4,22 GB [18] |

| (Unsloth Dynamic) |  |  |  |  |
|---|---|---|---|---|
| Gemma 4 12B (Naive Q4_0) | 74,08% [18] | 0,50702 [18] | 14,7323 [18] | 6,98 GB [18] |
| Gemma 4 12B (Unsloth Dynamic) | 88,76% [18] | 0,13288 [18] | 9,2740 [18] | 6,72 GB [18] |
| Gemma 4 26B-A4B (Naive Q4_0) | 70,20% [18] | 0,36094 [18] | 4,5420 [18] | 14,44 GB [18] |
| Gemma 4 26B-A4B (Unsloth Dynamic) | 85,63% [18] | 0,09788 [18] | 2,7087 [18] | 14,25 GB [18] |
| Gemma 4 31B (Naive Q4_0) | 87,91% [18] | 0,09349 [18] | 3,0030 [18] | 17,65 GB [18] |
| Gemma 4 31B (Unsloth Dynamic) | 96,67% [18] | 0,01403 [18] | 1,3659 [18] | 17,29 GB [18] |

La compressione basata su QAT garantisce un risparmio di memoria complessivo che si attesta sistematicamente attorno al 72% rispetto al formato a piena precisione, rendendo i modelli di grandi dimensioni adatti all'uso su macchine con risorse limitate. [18] Per scenari ultra-leggeri (es. smartphone), Google ha rilasciato i formati Mobile Mixture QAT per E2B ed E4B, che quantizzano selettivamente a 2 bit (usando il formato TQ2_0) gli strati responsabili della generazione dei token (MLP profondi), preservando a una precisione più elevata i blocchi dedicati alle funzioni di ragionamento. [7] In questo modo, il modello E2B Mobile Mixture occupa solo 2,19 GB a fronte di un'accuratezza Top-1 del 97,82%. [18]

### Multi-Token Prediction (MTP) e Decodifica Speculativa

L'inferenza locale è fortemente vincolata dalla larghezza di banda della memoria della GPU (memory-bandwidth bound). [9] Per ovviare all'inefficienza di muovere l'intera matrice dei parametri della rete neurale per generare un singolo token alla volta, la famiglia Gemma 4 introduce modelli di bozza (drafter) dedicati per abilitare la decodifica speculativa tramite Multi-Token Prediction (MTP). [8]

Nel flusso MTP, il modello di bozza predice in anticipo più token logici consecutivi, sfruttando un'infrastruttura condivisa con il modello principale. [8] Il modello target verifica poi l'intera

sequenza ipotizzata in parallelo all'interno di un unico passaggio di verifica. [8]

──► [ Embedding Condiviso ] ──►​ │​ ▼​ [ Proiezione Lineare ]​ │​ ▼​ ​ Il drafter MTP non opera in totale autonomia, ma sfrutta relazioni strutturali strette con l'LLM di riferimento [8]:

1.​ Condivisione degli Embedding: Il modello di bozza riutilizza la medesima tabella di

lookup degli embedding del modello target. [5]

2.​ Concatenazione delle Attivazioni: Le attivazioni estratte dall'ultimo strato del modello

target vengono concatenate con gli embedding dei token e proiettate verso il basso per adattarsi alla dimensione interna del drafter. [5]

3.​ Riuso del KV Cache: Il modello drafter scrive e consulta lo stesso KV cache del modello

principale, minimizzando i tempi di accesso alle strutture di memoria. [9]

4.​ Clustering del Vocabolario: Nei modelli più compatti (E2B ed E4B), il drafter evita di

calcolare la probabilità sull'intero vocabolario di 262K token. [8] I token simili vengono raggruppati in cluster; il drafter individua prima il cluster di destinazione e successivamente restringe la computazione lineare ai soli elementi interni ad esso. [5]

#### Benchmarks e Latenze: Impatto Sperimentale di MTP

I test eseguiti su GPU NVIDIA H100 mettono a confronto le metriche prestazionali della decodifica classica rispetto all'adozione di MTP e DFlash (un'alternativa di decodifica speculativa). [19]

●​ Gemma 4 31B Dense (MTP vs Baseline vs DFlash): Ad una concorrenza pari a 1, la decodifica baseline produce 40,3 token/secondo (t/s). [19] L'abilitazione di MTP innalza le prestazioni a 125,3 t/s (pari a un incremento di 3,11x), superando DFlash che si attesta su 122,1 t/s. [19] All'aumentare della concorrenza (16 richieste simultanee), la baseline tocca 375 t/s complessivi, DFlash raggiunge 725 t/s, mentre MTP domina la classifica con 953 t/s. [19]

●​ Comportamento per Categoria (Gemma 4 31B): L'efficacia della speculazione varia a seconda del compito testato. La scrittura di codice (coding) registra i miglioramenti più significativi con un incremento di velocità pari a 3,82x con MTP. [19] Il ragionamento

matematico e logico ottiene un'accelerazione di 3,37x (MTP) e 3,09x (DFlash). [19] Al contrario, compiti legati alla scrittura creativa o al gioco di ruolo (roleplay) registrano guadagni modesti (1,56x), poiché la natura aperta e meno prevedibile del testo riduce drasticamente il tasso di accettazione dei token ipotizzati dal modello drafter. [19]

●​ Il Trade-off sulla Latenza del Primo Token (TTFT): Il tempo di generazione del primo token (Time to First Token, o TTFT) risente negativamente della decodifica speculativa, poiché il sistema deve caricare preventivamente il modello di bozza ed eseguire i controlli iniziali. [19] A bassa concorrenza, il ritardo è trascurabile: 67,7 ms (baseline) contro 78,2 ms (MTP). [19] Con 16 richieste concorrenti, l'accumulo di calcolo speculativo dilata il TTFT a 1551 ms per MTP e a ben 3381 ms per DFlash, a fronte dei soli 192 ms della baseline. [19] Il tempo di generazione dei token intermedi (Time Per Output Token, o TPOT) scende invece da 24,4 ms (baseline) a 8,0 ms (MTP) ad una concorrenza pari a 1. [19]

●​ Modelli Mixture of Experts (Gemma 4 26B-A4B): Sui modelli MoE, il vantaggio di MTP si riduce a causa dei vincoli di routing. [8] Poiché token diversi attivano esperti fisicamente allocati in indirizzi di memoria differenti, la verifica parallela dei token speculativi costringe la GPU a richiamare dinamicamente pesi aggiuntivi, azzerando parte dei benefici temporali. [8] A concorrenza 1, DFlash (1,73x di incremento) supera MTP (1,49x), mantenendo il primato su quasi tutti i benchmark quantitativi. [19]

Sotto il profilo dell'hardware consumer locale, i test condotti su hardware Apple Mac M3 Max (64 GB di RAM unificata) mostrano che Gemma 4 12B ottiene 42 t/s senza speculazione. [20] L'abilitazione di MTP con l'impostazione di 2 token speculativi innalza la velocità a 47 t/s. [20] Tuttavia, configurando il sistema per predire 4 token speculativi, la velocità crolla in un intervallo compreso tra 29 e 36 t/s. [20] Questo calo prestazionale evidenzia che un numero eccessivo di token di bozza, se rifiutati dal modello principale, satura la computazione e rallenta l'intero processo di generazione locale. [21] Per scopi comparativi, la tabella sottostante riassume queste

metriche, affiancandole a quelle di Qwen 3.5-9B. [20]

#### Generazione Locale: Gemma 4 12B vs Qwen 3.5-9B su Mac M3 Max

| Modello | Configurazione Decodifica | Token al Secondo (TPS) | Osservazione Prestazionale |
|---|---|---|---|
| Gemma 4 12B | Senza MTP [20] | 42 t/s [20] | Baseline stabile su hardware a memoria unificata [20] |
| Gemma 4 12B | MTP (2 token | 47 t/s [20] | Guadagno netto di |

|  | ipotizzati) [20] |  | efficienza (+11,9%) [20] |
|---|---|---|---|
| Gemma 4 12B | MTP (4 token ipotizzati) [20] | 29 - 36 t/s [20] | Rallentamento causato dall'elevato tasso di scarto dei token [20] |
| Qwen 3.5-9B-Base | Senza MTP [20] | 48 t/s [20] | Margine di velocità superiore dovuto al minor numero di parametri [20] |
| Qwen 3.5-9B-Base | MTP (1 token ipotizzato) [20] | 52 t/s [20] | Massima efficienza registrata per l'architettura concorrente [20] |
| Qwen 3.5-9B-Base | MTP (2 token ipotizzati) [20] | 48 t/s [20] | Ritorno al livello prestazionale di partenza senza speculazione [20] |
| Qwen 3.5-9B-Base | MTP (4 token ipotizzati) [20] | 33 t/s [20] | Degradazione prestazionale analoga a quella riscontrata su Gemma [20] |

Nonostante le criticità di configurazione fine, l'adozione coordinata di checkpoint QAT accoppiati a sintonizzatori MTP consente di raggiungere velocità straordinarie su hardware consumer. [21] Alcuni utenti della community di LocalLLaMA hanno riportato il raggiungimento di circa 120 t/s reali su GPU dedicate dotate di soli 12 GB di VRAM (es. RTX 4070 o RTX 3080) impiegando Gemma 4 12B QAT integrato con il modulo MTP. [21]

### TurboQuant e PolarQuant: Rivoluzione Geometrica del KV Cache

Durante l'elaborazione di contesti estesi (oltre i 32K token), l'impronta di memoria dei soli parametri del modello diventa secondaria rispetto alla crescita lineare del cache Key-Value (KV), che satura rapidamente la memoria ad alta larghezza di banda (HBM) delle schede grafiche professionali o la VRAM dei PC domestici. [10] Introdotto da Google Research e presentato formalmente a ICLR 2026, TurboQuant è un framework di quantizzazione online

progettato per comprimere il cache KV fino a 3 o 4 bit a runtime con perdita di accuratezza nulla, eliminando l'overhead di memorizzazione tipico dei metodi tradizionali. [10]

La compressione tradizionale raggruppa i dati in blocchi e salva costanti di scala e zero-point in formato a piena precisione, occupando da 1 a 2 bit aggiuntivi per ogni singolo parametro compresso. [10] TurboQuant aggira questo limite modificando la geometria dei vettori multidimensionali in ingresso tramite due tecnologie: PolarQuant (presentata ad AISTATS 2026) e la trasformata Quantized Johnson-Lindenstrauss (QJL). [11]

[ Vettori KV in Coordinate Cartesiane ]​ │​ ▼​ ​ (Rotazione casuale via S)​ │​ ▼​ ​ Estrazione raggio + angoli fitti​ │​ ▼​ ​ Zero overhead di scale o zero-point​ La trasformazione polare di PolarQuant si articola nelle seguenti fasi logiche [11]:

●​ Precondizionamento Spaziale: Ciascun vettore KV viene moltiplicato per una matrice di

proiezione casuale composta da valori indipendenti e identicamente distribuiti (i.i.d.) tratti da una distribuzione normale standard. [11] In base al lemma di Johnson-Lindenstrauss, questa rotazione ne preserva le distanze interne e le norme geometriche. [11]

●​ Concentrazione di Misura: A seguito della rotazione, le coordinate del vettore convergono verso una distribuzione gaussiana controllata in alta dimensione. [11] Questo rende gli assi del vettore mutuamente indipendenti e non correlati, consentendo di trattare ciascuna coordinata singolarmente in fase di quantizzazione. [11]

●​ Conversione Polare Ricorsiva: Il vettore in (con dimensione d pari a una potenza di 2) viene elaborato accoppiando le coordinate e convertendole ricorsivamente in raggio e

angolo. [11] Il processo viene ripetuto volte, distillando l'intera informazione in un

unico raggio finale e in una serie concentrata di angoli. [11]

●​ Griglia Circolare Condivisa: Poiché gli angoli generati dal precondizionamento casuale si concentrano stabilmente secondo distribuzioni matematicamente precalcolabili, il sistema può mappare i vettori su una griglia sferica fissa e predeterminata. [11] In questo modo, non è più necessario calcolare e memorizzare i fattori di scala per ogni blocco, azzerando completamente il "memory overhead" sistematico della quantizzazione. [10]

Qualora residui un margine d'errore geometrico dovuto alla quantizzazione degli angoli, TurboQuant applica un "trucco a 1 bit" basato sulla trasformata Quantized Johnson-Lindenstrauss (QJL) sul vettore residuo. [10] Lo stato residuo viene ridotto a un vettore di soli segni (+1 o -1), fungendo da correttore matematico veloce che elimina le distorsioni e le asimmetrie nel calcolo del prodotto interno. [10] Il calcolo finale dell'attenzione rimane unbiased, garantendo prestazioni inalterate in contesti estesi (ago nel pagliaio) pur riducendo l'ingombro del cache KV di un fattore pari ad almeno 6x (fino a 3 bit totali). [10] Inoltre, grazie all'ottimizzazione del codice per acceleratori GPU H100, la riduzione delle transizioni di memoria permette a TurboQuant a 4 bit di registrare calcoli dei logit di attenzione fino a 8 volte più rapidi rispetto alla baseline non compressa a 32 bit. [10]

### Analisi Sperimentale di TurboQuant in vLLM e llama.cpp

L'implementazione industriale di TurboQuant ha evidenziato divari qualitativi e prestazionali marcati tra le diverse varianti algoritmicamente possibili, in particolare all'interno del framework di serving vLLM. [26]

#### 1. Le Varianti Algoritmiche in vLLM

●​ TurboQuant k8v4: Quantizza le Key a 8 bit (senza rotazione o calcolo MSE) e i Value a 4 bit. [26] Le evidenze empiriche indicano che questa variante non apporta benefici significativi rispetto all'adozione dello standard nativo FP8 del framework (--kv-cache-dtype fp8). [26] Il guadagno in capacità di memoria è modesto (2,4x contro 2,0x) ed è compensato negativamente da perdite stabili in termini di throughput e latenza complessiva. [26]

●​ TurboQuant 4bit-nc: Rappresenta la scelta ottimale tra le varianti TurboQuant. [26] Pur registrando lievi regressioni in termini di latenza e throughput, garantisce un'estensione considerevole del cache KV a fronte di una perdita qualitativa marginale, risultando idoneo per distribuzioni locali sensibili allo spazio di memoria. [26]

●​ TurboQuant k3v4-nc e 3bit-nc: Queste varianti aggressive comprimono il cache KV a 3 bit o meno. [26] I benchmark evidenziano un grave decadimento qualitativo, quantificabile in una perdita di circa 8 punti percentuali nei test matematici e logici complessi come AIME25 e LiveCodeBench-v6. [26] Nei test di recupero a lungo contesto (Context Arena), l'AUC (Area Under Curve) crolla dal valore di riferimento BF16 al 33,5% per la variante k3v4-nc e al 31,2% per la 3bit-nc (pari a un decadimento del 30% relativo). [26] L'accumularsi degli errori di quantizzazione sui contesti lunghi (128K-256K) rende queste versioni inadatte all'uso in produzione. [26]

#### 2. L'Asimmetria nel Trattamento delle Key (K) e dei Value (V)

L'analisi dei vettori d'attenzione evidenzia che la precisione geometrica del cache delle Key (

) esercita un impatto qualitativo molto più critico rispetto a quella dei Value ( ). [28] Poiché i vettori Key partecipano direttamente alla funzione esponenziale del softmax, qualsiasi

micro-errore di arrotondamento in viene amplificato in modo esponenziale durante

l'inferenza. [28] Al contrario, le inesattezze introdotte nei vettori Value ( ) vengono diluite attraverso una media lineare sull'intera lunghezza del contesto, attenuando l'impatto dell'errore di compressione. [28]

Questa dinamica giustifica la configurazione asimmetrica adottata nel modulo vllm-metal per Apple Silicon. [28] Il runtime impone l'abilitazione dell'attenzione paginata (VLLM_METAL_USE_PAGED_ATTENTION=1) e supporta configurazioni bilanciate [28]:

●​ Configurazione q8_0 (K) / q3_0 (V): Rappresenta lo standard di riferimento per mantenere l'accuratezza inalterata rispetto al formato BF16, garantendo al contempo una compressione complessiva del cache KV pari a 2,56x. [28]

●​ Configurazione q4_0 (K) / q3_0 (V): Riduce il cache KV di 3,76x, registrando una regressione qualitativa lieve e tollerabile, pienamente in linea con i dati esposti nel paper teorico di TurboQuant. [28]

●​ Configurazione int2 (K) / q2_0 (V): Risulta strutturalmente instabile e inutilizzabile a causa dell'insorgenza di cicli di ripetizione degenerati ("concept concept concept...") dovuti alla saturazione dell'errore esponenziale sulle Key. [28]

Nel contesto di llama.cpp, sono nati fork specializzati come quello sviluppato da atomicmilkshake. [23] Questo progetto integra le ottimizzazioni dei kernel CUDA di TurboQuant (turbo2, turbo3, turbo4) con la tecnologia TriAttention per la potatura (pruning) accelerata in GPU del cache KV. [23] Sfruttando la struttura geometrica dei vettori Key invertiti tramite RoPE, TriAttention calcola l'importanza relativa dei token in cache ed elimina quelli a basso valore informativo direttamente in VRAM. [23] Questo approccio garantisce l'esecuzione di contesti estremamente estesi su schede consumer (es. 75 t/s stabili su Qwen 3 8B utilizzando una RTX 3080) escludendo costosi rallentamenti dovuti al passaggio dati sul bus PCIe. [23]

#### 3. Evidenze Sperimentali su Hardware Consumer (llama.cpp)

I test empirici condotti tramite il fork TheTom/llama-cpp-turboquant (ramo feature/turboquant-kv-cache) mostrano la fattibilità tecnica della compressione dinamica del cache KV su singole schede grafiche consumer, mantenendo intatta la precisione dei pesi del modello. [24]

| GPU e VRAM | Modello e Quantizz azione Peso | Tipo Cache KV | Limite Contesto | Latenza Media (TPS) | Memoria VRAM Totale | Implicazi one di Sistema |
|---|---|---|---|---|---|---|
| RTX 3090 (24 GB) | Mistral Small 3.2 24B (Q4_K_M) ) | Classico (F16) | 8.192 token [24] | 51,0 t/s [24] | 15,3 GB [24] | Limite fisico imposto dalla saturazio ne del cache non compress o [24] |
| RTX 3090 (24 GB) | Mistral Small 3.2 24B (Q4_K_M) ) | TurboQu ant (turbo3) | 100.000 token [24] | 47,2 t/s [24] | 17,1 GB [24] | Estension e di 12,2x del contesto a fronte di una perdita di velocità di appena il 7,4% [24] |
| RTX 4070 Laptop (8 GB) | Llama 3.1 8B (Q4_K_M) ) | Classico (F16) | 8.192 token [24] | 49,8 t/s [24] | 5,7 GB [24] | Configura zione standard per notebook di fascia media [24] |
| RTX 4070 Laptop (8 GB) | Llama 3.1 8B (Q4_K_M) ) | TurboQu ant (turbo3) | 64.000 token [24] | 47,5 t/s [24] | 6,2 GB [24] | Estension e di 7,8x del contesto con un |

La compressione del cache KV si rivela particolarmente vantaggiosa per contesti estesi (oltre gli 8K token). [29] Su contesti brevi, l'overhead computazionale dovuto alla compressione e decompressione dinamica dei vettori attenua i benefici complessivi di velocità, limitandoli alla sola contrazione dello spazio di memoria occupato. [29]

### L'Incompatibilità Strutturale tra MTP e TurboQuant

Nonostante l'attrattiva teorica di combinare la compressione dei pesi QAT, la decodifica speculativa MTP e la compressione del cache KV tramite TurboQuant per raggiungere prestazioni locali elevatissime, i tentativi di implementazione simultanea condotti dalla community hanno evidenziato incompatibilità architetturali profonde e colli di bottiglia nei sistemi di compilazione. [13]

Diversi ingegneri software hanno riportato fallimenti sistematici nel tentativo di compilare e distribuire modelli Gemma 4 integrando contemporaneamente sia l'assistente MTP che il modulo TurboQuant (usando, ad esempio, l'approccio basato sul fork docker "mitkox"). [13] I tempi di compilazione delle immagini Docker si sono estesi fino a 120 minuti per iterazione, risolvendosi spesso in errori fatali di runtime o blocchi completi dell'inferenza. [13] Le motivazioni tecniche di questo fallimento sono riconducibili a due problematiche strutturali: 1. Il Conflitto tra Hybrid Attention e la Fast Walsh-Hadamard Transform

L'architettura globale di Gemma 4 non adotta uno schema di attenzione interamente uniforme. [14] Al fine di ottimizzare l'uso della memoria locale, alterna strati ad attenzione locale con finestra scorrevole (Sliding Window Attention impostata a 1024 token) a strati ad attenzione globale dotati di Grouped-Query Attention (GQA) e Proportional RoPE (p-RoPE). [14]

Le implementazioni correnti di TurboQuant (inclusi i backend vLLM e vllm-metal) si basano sul presupposto che la trasformata veloce di Walsh-Hadamard (FWHT) venga eseguita su matrici di attenzione globali stabili. [26] TurboQuant non supporta modelli dotati di attenzione a finestra scorrevole o architetture ibride con blocchi di memoria ricorrente (come le reti dotate di blocchi GDN). [26] L'attivazione di TurboQuant su Gemma 4 genera conflitti di runtime insolvibili o costringe il compilatore a bypassare la quantizzazione per i blocchi ad attenzione locale, annullando gran parte dei benefici prestazionali cercati. [26]

#### 2. Disallineamento Geometrico tra Speculative Decoding e KV Cache Compresso

Come evidenziato in precedenza, l'architettura MTP di Gemma 4 è progettata per riutilizzare

direttamente il KV cache calcolato dal modello principale durante il passaggio di verifica speculativa. [9] Tuttavia, TurboQuant agisce a runtime ruotando geometricamente lo spazio dei vettori Key e Value tramite matrici di proiezione casuale e applicando una quantizzazione non uniforme basata su centroidi sferici PolarQuant. [11]

Questo genera una disconnessione strutturale [11]:

●​ Il modello drafter MTP genera le sue ipotesi operando in uno spazio di embedding standard cartesiano non ruotato. [8]

●​ Quando l'LLM principale tenta di verificare i token proposti dal drafter, non può confrontarli direttamente con il cache KV quantizzato e ruotato da TurboQuant, a meno di non eseguire una decodifica inversa completa (un-rotation). [13]

●​ Questa operazione di decompressione e de-rotazione geometrica è estremamente onerosa e rallenta l'intero processo, azzerando i benefici temporali introdotti dalla speculazione o degradando drasticamente il tasso di accettazione dei token ipotizzati. [13]

La combinazione simultanea di queste tre tecnologie si traduce in un calo drastico delle prestazioni complessive, rendendo il sistema inefficiente rispetto alle singole configurazioni ottimizzate. [13]

#### La Soluzione Alternativa: Quantizzazione NVFP4 e MTP

Per superare l'impasse ingegneristico di TurboQuant sui sistemi di calcolo parallelo (come DGX Spark), alcuni sviluppatori hanno suggerito di rinunciare alla quantizzazione dinamica del cache KV, focalizzandosi invece su formati di compressione dei pesi più avanzati. [13]

La raccomandazione operativa consiste nell'utilizzare il modello Gemma 4 31B compresso tramite quantizzazione a 4 bit nativa per Tensor Core NVIDIA (formato ebircak/gemma-4-31B-it-4bit-NVFP4A16-GPTQ), mantenendo il cache KV non quantizzato in formato FP16. [13] L'adozione coordinata di questa quantizzazione unita al modulo speculativo MTP consente di raggiungere velocità stabili comprese tra 30 e 40 t/s su carichi di lavoro reali complessi, mantenendo in memoria un cache KV esteso fino a 1,2 milioni di token senza incorrere in conflitti architetturali o rallentamenti di sistema. [13]

### Conclusioni e Linee Guida Operative

L'analisi sistematica dell'ecosistema Gemma 4 12B Unified e delle relative tecnologie di compressione consente di tracciare linee guida chiare per ricercatori e sviluppatori interessati all'inferenza locale:

1.​ La Configurazione Consigliata per Macchine Consumer (16 GB): Per un utilizzo

stabile su laptop consumer, il punto di equilibrio ideale è costituito dall'adozione di Gemma 4 12B QAT distribuito in formato Unsloth Dynamic (UD-Q4_K_XL). [12] Questa configurazione riduce l'impronta di memoria dei pesi a soli 6,72 GB sul disco, garantendo al contempo un'aderenza qualitativa del 99,96% al modello non quantizzato e lasciando ampio spazio di memoria per l'esecuzione del sistema operativo e la gestione di contesti di lavoro estesi. [18]

2.​ Abilitazione Strategica dell'MTP: L'integrazione del modello di bozza MTP è

caldamente raccomandata per flussi di lavoro strutturati e prevedibili, quali l'analisi e la

generazione di codice sorgente (coding) o la risoluzione di problemi matematici. [19] In questi contesti, la decodifica speculativa consente di abbattere significativamente il tempo di generazione dei token (TPOT), a patto di limitare il numero di token ipotizzati dal drafter (impostando un valore pari a 1 o 2) per evitare sovraccarichi computazionali dovuti a un tasso di scarto elevato. [20]

3.​ Gestione del Cache KV: A causa delle incompatibilità architetturali insite nell'attenzione

ibrida di Gemma 4 e dei conflitti con la decodifica speculativa MTP, l'applicazione di TurboQuant su questo specifico modello è sconsigliata per ambienti di produzione. [13] Per estendere la lunghezza del contesto senza saturare la memoria, gli sviluppatori dovrebbero prediligere quantizzazioni asymetriche del cache KV native all'interno di engine stabili (come l'allocazione q8_0 per le Key e q3_0 per i Value in vllm-metal), rimandando l'adozione di TurboQuant al momento della sua integrazione ufficiale e nativa all'interno dei rami principali di sviluppo di llama.cpp e vLLM. [28]

#### Bibliografia

1.​ Gemma 4 12B: Specs, Benchmarks & How to Run It Locally - Build Fast with AI,

accesso eseguito il giorno giugno 10, 2026, https://www.buildfastwithai.com/blogs/gemma-4-12b-guide 2.​ Gemma 4 12B Developer Guide: Benchmarks & Specs | Lushbinary, accesso

eseguito il giorno giugno 10, 2026, https://lushbinary.com/blog/gemma-4-12b-developer-guide-benchmarks-multimod al/ 3.​ Google Gemma 4 12B nearly matches 26B benchmarks — and runs on your

laptop, accesso eseguito il giorno giugno 10, 2026, https://thenewstack.io/google-gemma-local-ai/ 4.​ Introducing Gemma 4 12B: a unified, encoder-free multimodal model - Google

Blog, accesso eseguito il giorno giugno 10, 2026, https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gem ma-4-12b/ 5.​ Gemma 4 12B: The Developer Guide - Google Developers Blog, accesso

eseguito il giorno giugno 10, 2026, https://developers.googleblog.com/gemma-4-12b-the-developer-guide/ 6.​ Google Gemma4 QAT models : Faster AI for Mobiles and Laptops, accesso

eseguito il giorno giugno 10, 2026, https://medium.com/data-science-in-your-pocket/google-gemma4-qat-models-fast er-ai-for-mobiles-and-laptops-3beb2a6d8d8f 7.​ Gemma 4 with quantization-aware training - Google Blog, accesso eseguito il

giorno giugno 10, 2026, https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aw are-training-gemma-4/ 8.​ Speed-up Gemma 4 with Multi-Token Prediction | Google AI for Developers,

accesso eseguito il giorno giugno 10, 2026, https://ai.google.dev/gemma/docs/mtp/overview

9.​ Accelerating Gemma 4: faster inference with multi-token prediction drafters -

Google Blog, accesso eseguito il giorno giugno 10, 2026, https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-pred iction-gemma-4/ 10.​TurboQuant vs Traditional Quantization Eliminating Memory Overhead in LLMs -

Medium, accesso eseguito il giorno giugno 10, 2026, https://medium.com/@tahirbalarabe2/turboquant-vs-traditional-quantization-elimin ating-memory-overhead-in-llms-24524af4adb8 11.​TurboQuant: Redefining AI efficiency with extreme compression, accesso eseguito

il giorno giugno 10, 2026, https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-com pression/ 12.​Gemma 4 QAT Self-Hosting Guide: Ollama, vLLM | Lushbinary, accesso eseguito

il giorno giugno 10, 2026, https://lushbinary.com/blog/gemma-4-qat-self-hosting-guide-ollama-llama-cpp-vllm / 13.​Has anyone actually succeeded in deploying gemma4 dense using both the new

MTP AND turboquant? - DGX Spark / GB10 - NVIDIA Developer Forums, accesso eseguito il giorno giugno 10, 2026, https://forums.developer.nvidia.com/t/has-anyone-actually-succeeded-in-deploying -gemma4-dense-using-both-the-new-mtp-and-turboquant/369248 14.​google/gemma-4-12B-it-assistant - Hugging Face, accesso eseguito il giorno

giugno 10, 2026, https://huggingface.co/google/gemma-4-12B-it-assistant 15.​Bringing Gemma 4 12B to your Laptop: Unlocking Local, Agentic Workflows with

Google AI Edge, accesso eseguito il giorno giugno 10, 2026, https://developers.googleblog.com/bringing-gemma-4-12b-to-your-laptop-unlockin g-local-agentic-workflows-with-google-ai-edge/ 16.​Gemma 4 MTP released : r/LocalLLaMA - Reddit, accesso eseguito il giorno

giugno 10, 2026, https://www.reddit.com/r/LocalLLaMA/comments/1t4jq6h/gemma_4_mtp_released / 17.​TurboQuant for Efficient LLMs and How Gemma 4 Utilizes It - Pinggy, accesso

eseguito il giorno giugno 10, 2026, https://pinggy.io/blog/turboquant_for_efficient_llms_and_how_gemma_4_utilizes_it / 18.​Gemma 4 QAT | Unsloth Documentation, accesso eseguito il giorno giugno 10,

2026, https://unsloth.ai/docs/models/gemma-4/qat 19.​Benchmarking Gemma 4 MTP vs DFlash on a Single H100 | Jarvis Labs Blog,

accesso eseguito il giorno giugno 10, 2026, https://jarvislabs.ai/blog/gemma-4-mtp-vs-dflash-benchmark 20.​[Opinion/Benchmark] Gemma4-12B's architecture change is too big of a tradeoff;

A quick reasoning comparison between Gemma4-12B and Qwen 3.5-9B : r/LocalLLaMA - Reddit, accesso eseguito il giorno giugno 10, 2026, https://www.reddit.com/r/LocalLLaMA/comments/1u13do9/opinionbenchmark_ge mma412bs_architecture_change/

21.​Gemma 4 QAT + MTP: max 33% speed increase in token generation, any ideas? -

Reddit, accesso eseguito il giorno giugno 10, 2026, https://www.reddit.com/r/LocalLLaMA/comments/1u0aj1b/gemma_4_qat_mtp_ma x_33_speed_increase_in_token/ 22.​120 tok/s on 12GB VRAM with Gemma 4 12B QAT MTP, accesso eseguito il

giorno giugno 10, 2026, https://www.reddit.com/r/LocalLLaMA/comments/1typjmc/120_toks_on_12gb_vra m_with_gemma_4_12b_qat_mtp/ 23.​llama.cpp — TurboQuant + TriAttention - GitHub, accesso eseguito il giorno

giugno 10, 2026, https://github.com/atomicmilkshake/llama-cpp-turboquant 24.​TurboQuant on Consumer GPUs — 100K Context ... - Hugging Face, accesso

eseguito il giorno giugno 10, 2026, https://huggingface.co/spaces/ai-engineering-at/llama-cpp-turboquant-guide 25.​TurboQuant - Wikipedia, accesso eseguito il giorno giugno 10, 2026,

https://en.wikipedia.org/wiki/TurboQuant 26.​A First Comprehensive Study of TurboQuant: Accuracy and Performance | vLLM

Blog, accesso eseguito il giorno giugno 10, 2026, https://vllm.ai/blog/2026-05-11-turboquant 27.​turboquant - vLLM, accesso eseguito il giorno giugno 10, 2026,

https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/turboqua nt/ 28.​Turboquant - vllm-metal, accesso eseguito il giorno giugno 10, 2026,

https://docs.vllm.ai/projects/vllm-metal/en/latest/turboquant/ 29.​Running a 35B Model Locally with TurboQuant — What's Actually Possible Right

Now, accesso eseguito il giorno giugno 10, 2026, https://pub.towardsai.net/running-a-35b-model-locally-with-turboquant-whats-actu ally-possible-right-now-1ac5327430b0

## Notes
<!-- openclaw:human:start -->
### Nel vault
- Sintesi: [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
- [Google](../entities/google.md) — Gemma 4 12B Unified è di Google DeepMind · [scrya-com](../entities/scrya-com.md) — TurboQuant/RotorQuant
- [Unsloth](../entities/unsloth.md) — la variante Dynamic QAT confrontata qui con la Naive Q4_0
- Confronto metodologico: [Qwen3.8-Flash-Next — MoE 125B locale a 75GB](../syntheses/qwen3-8-flash-next-moe-125b-locale-a-75gb-unified-ram.md) e [Hardware per inferenza locale domestica](../syntheses/hardware-per-inferenza-locale-domestica-presente-e-futuro.md)

**Attenzione:** l'estrazione conserva le note di citazione del documento come `[N]`; la bibliografia è in fondo. Le percentuali (17) e i formati di quantizzazione (Q4_0, Q4_K_M, Q4_K_XL, Q6_K, TQ2_0, NVFP4) sono stati verificati uno a uno contro il testo grezzo del PDF.
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Esperimenti Quantizzazione Gemma 4 12B — QAT, MTP, TurboQuant](../syntheses/esperimenti-quantizzazione-gemma-4-12b-qat-mtp-turboquant.md)
<!-- openclaw:wiki:related:end -->
