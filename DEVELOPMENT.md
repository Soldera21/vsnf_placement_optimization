## Idee
Data business app trovare VSNF basandosi su minacce o vulnerabilità

Come raccogliere le info su minacce o vulnerabilità a cui è soggetta una app di business o un servizio
Dataset Alibaba su workload delle parti di una app

Percorso che permetta di arrivare alla fine semplice e poi aggiungere dettagli

Percorso di studio:
* Sviluppo della parte relativa al risk assessment data una business application e le minacce a cui può essere soggetta
* Elaborazione del grafo della business app con le VSNF
* Integrare un algoritmo di piazzamento già esistente in letteratura del grafo sviluppato (VNE - Virtual Network Embedding)
* Sviluppare l'acquisizione di dati delle business applications da suggerimenti dello sviluppatore o dati i servizi usati trovare VSNF necessarie basandosi su CVSS ecc.
* Esecuzione della generazione del grafo e del piazzamento in contemporanea per migliorare l'efficienza

---
## Risk Assessment

Ricerca su risk assessment (caratteristiche di sicurezza e impatto sull'app variando il piazzamento delle VSNFs)

https://www.assured.se/posts/cvss40
- CVSS -> https://www.cvedetails.com/
- OWASP Risk Rating

CVSS with python https://github.com/toolswatch/pycvss3

Come trovare attacco da CVE?
https://github.com/cve-search/PyCVESearch
Su CVEdetails ci sono ma non so come ricavarli

Creare associazione tra attacco e funzioni/pattern che lo mitigano.

In CVE serve vendor, prodotto e versione

CVE to MITRE ATT&CK ???


## Algoritmo
Elaborare algoritmo a mano con gli step per partire da minacce/attacchi forniti e ottenere le funzioni da inserire!!! Identificare la funzione migliore per ogni attacco in base alla situazione.

#### Idea:
Creare una lista di priorità per ogni VSNF così da risolvere le ambiguità (es in base al loro impatto sulle prestazioni nel caso specifico del rilevare quell'attacco). Poi si analizzano gli attacchi e dei loro sottogruppi per capire quali funzioni di sicurezza ottimizzano al meglio le richieste. Inoltre bisogna dare una priorità alle funzioni per far si che l'ordine sia efficace.

function riskAssessment(List vsnfs, List attacchi, Matrix vsnfAttack, Grafo businessApp, List attacchiPerServizio):
    Grafo app <- businessApp

    foreach(funct in businessApp):
        requisiti <- attacchiperServizio[funct]
        secFuncts <- ottimizzaFunzioni(vsnfs, attacchi, vsnfAttack, requisiti)
        app <- inserisciInGrafo(app, funct, secFuncts)
    end

    ritorna app
end

function ottimizzaFunzioni(List vsnfs, List attacchi, Matrix vsnfAttack, List requisiti):
    req <- mapToMatrixIndex(requisiti)

    // trovare tutti i possibili sottogruppi di qualsiasi dimensione degli attacchi partendo da gruppi più grandi e che creino n attacchi univoci

    List migliorComb
    foreach(c in combinazioneDiGruppi):
        funzioni <- estraiFunzioni(c, vsnfAttack)
        se funzioni not empty and len(funzioni) < len(migliorComb):
            migliorComb <- funzioni
        end
    end

    ritorna migliorComb
end

function estraiFunzioni(List combGruppi, Matrix vsnfAttack):
    List functs

    Int i = 0
    foreach(gruppo in combGruppi):
        foreach(vsnf in vsnfAttacchi):
            se vsnf contiene gruppo:
                functs.append(vsnf)
            end
        end
        se functs[i] = undefined:
            functs.append(-1)
        end
        i++
    end

    se -1 in functs:
        ritorna []
    altrimenti:
        ritorna functs
    end
end

Semplificazioni:
- singola applicazione e/o duplicazione di servizi di sicurezza
- performance ridotta a numero di VSNF
- risk assessment parzialmente fatto perché abbiamo l'input che sono le tattiche di attacco

#### Altra Idea:

Considerazione nuovo approccio:
- lo sviluppatore fornisce grafo app e lista di asset (operazione sensibili a livello di sicurezza) da proteggere
- asset -> che security property si può compromettere con questo asset tramite tecniche di attacco -> proporre mitigation con VSNF
- l'input è l'asset da proteggere e dove si trova

Dare un ordine alle funzioni per far si che quando ne piazzo più di una nella stessa posizione queste non interferiscano tra di loro.


type Asset: [ tipo, proprietà[ 3 ] ]
type Posizione: [ posizione, List\<Asset\> assetsRichiesti ]

function riskAssessment(Matrix vsnfAttack, Matrix assetsAttacks, Grafo businessApp, List\<Posizione\> posizioniDaProteggere):
    Grafo app <- businessApp

    for position in posizioniDaProteggere:
        possibleAttacks <- trovaAttacchi(position[ assetsRichiesti ], assetsAttacks)
        secFuncts <- ottimizzaFunzioni(vsnfAttack, possibleAttacks)
        app <- inserisciInGrafo(app, secFuncts, position[ posizione ])
    end

    ritorna app
end

function trovaAttacchi(List\<Assets\> assets, Matrix assetsAttacks)
    List attacks

    for asset in assets:
        for row in assetsAttacks[ asset[ tipo ] ]:
            if asset[ proprietà ] in row and row[ attack ] not in attacks:
                attacks.add(row[ attack ])
            end
        end
    end

    ritorna attacks
end

function ottimizzaFunzioni(Matrix vsnfAttack, List attacks)

    // trovare tutti i possibili sottogruppi di qualsiasi dimensione degli attacchi partendo da gruppi più grandi e che creino n attacchi univoci

    List migliorComb
    foreach c in combinazioneDiGruppi:
        funzioni <- estraiFunzioni(c, vsnfAttack)
        se funzioni not empty and len(funzioni) < len(migliorComb):
            migliorComb <- funzioni
        end
    end

    ritorna migliorComb
end

function estraiFunzioni(List combGruppi, Matrix vsnfAttack):
    List functs

    Int i = 0
    foreach(gruppo in combGruppi):
        foreach(vsnf in vsnfAttacchi):
            se vsnf contiene gruppo:
                functs.append(vsnf)
            end
        end
        se functs[i] = undefined:
            functs.append(-1)
        end
        i++
    end

    se -1 in functs:
        ritorna []
    altrimenti:
        ritorna functs
    end
end

Semplificazioni:
- performance ridotta a numero di VSNF -> idea di valutare performance sommando uso di cpu, mem e moltiplicare per inverso di latenza e tempo di risposta ???? oppure reare una lista di priorità per ogni VSNF così da risolvere le ambiguità

prossimi step:
- costo con cpu si trova online ???

#### Esempio:
L'applicazione presa come esempio si occupa di prendere dei dati da delle API pubbliche con il servizio "Data Aggregator". Questo poi richiede l'elaborazione di alcuni di questi dati al "ML Service". Entrambi salvano nel database "MongoDB". "API Service" recupera i dati da "MongoDB" e li espone con delle API pubbliche e private oppure li invia al "Front-End". Da questi due ultimi servizi si va verso internet.

Asset individuati:
- ML Service:
    - Computation: C I
- Data Aggregator:
    - Computation: C I
- Gateway:
    - Gateway: A
    - API: C A
    - AuthN/AuthZ: C A
- Front-End:
    - /
- API Service:
    - Communication: C I
- MongoDB:
    - Storage: C I A

Questo è l'input raffinato per la procedura di risk assessment. Il prossimo passo è acquisire le tabelle di associazione tra VSNFs-attacchi e assets-attacchi. A questo punto l'algoritmo prevede l'acquisizione degli asset precedentemente individuati.

Ora si itera su ogni posizione in cui questi sono stati individuati per ottimizzare le funzioni che proteggono tutti gli assets trovati lì.

- ML Service: dalla tabella assets-attacchi trovo che qui posso essere soggetto a [ DDoS, Malwares, Injections, XSS, Zero-Day, Cryptojacking, Eavesdropping ]; quindi devo utilizzare la seguente miglior configurazione di VSNFs dalla tabella VSNFs-attacchi per proteggere [ Intrusion Detection System, Deep Packet Inspection, Authentication Function ]  -> altre opzioni potrebbero essere ad esempio: [ IPS, DPI, Authentication Function ] (omesse nei prossimi servizi per semplicità)
- Data Aggregator: dalla tabella assets-attacchi trovo che qui posso essere soggetto a [ DDoS, Malwares, Injections, XSS, Zero-Day, Cryptojacking, Eavesdropping ]; quindi devo utilizzare la seguente miglior configurazione di VSNFs dalla tabella VSNFs-attacchi per proteggere [ Intrusion Detection System, Deep Packet Inspection, Authentication Function ]
- Gateway: dalla tabella assets-attacchi trovo che qui posso essere soggetto a [ DDoS, Malwares, Injections, Port Scanning, XSS, DNS Spoofing, Zero-Day, ARP Spoofing, MitM, Path Traversal, Phishing, Brute Force, Cryptanalysis, Replay Attack, Key Attacks, DNS Attack, Eavesdropping ]; quindi devo utilizzare la seguente miglior configurazione di VSNFs dalla tabella VSNFs-attacchi per proteggere [ Authentication Function, Key Management Function, Intrusion Detection System, Deep Packet Inspection, Anti-Spoofing, DNS Security ]
- Front-End: /
- API Service: dalla tabella assets-attacchi trovo che qui posso essere soggetto a [ DDoS, Malwares, XSS, DNS Spoofing, IP Spoofing, Zero-Day, ARP Spoofing, MitM, MAC Spoofing, Key Attacks, DNS Attack, Eavesdropping, Criptojacking ]; quindi devo utilizzare la seguente miglior configurazione di VSNFs dalla tabella VSNFs-attacchi per proteggere [ Authentication Function, Key Management Function, Intrusion Detection System, Deep Packet Inspection, Anti-Spoofing ]
- MongoDB: dalla tabella assets-attacchi trovo che qui posso essere soggetto a [ DDoS, Malwares, Injections, Port Scanning, XSS, DNS Spoofing, Zero-Day, ARP Spoofing, Path Traversal, Phishing, Brute Force, Cryptanalysis, Key Attacks, DNS Attack ]; quindi devo utilizzare la seguente miglior configurazione di VSNFs dalla tabella VSNFs-attacchi per proteggere [ Intrusion Detection System, Deep Packet Inspection, Anti-Spoofing, Authentication Function, Key Management Functions, DNS Security ]

Infine si inseriscono le VSNFs nel grafo dell'app.

A questo punto abbiamo ottenuto il grafo completo di funzioni di sicurezza i cui servizi possono essere piazzati tramite un algoritmo di Virtual Network Embedding.


Problema: anche cercando di mettere delle capabilities prima possibile si ha duplicazione di funzioni.
Possibile soluzione: indicare i tragitti dei dati per ridurre le funzioni e aggregarle.


#### Idea Semplificazione:
Verificare per ogni funzione nel grafo finale se è vicina a un'altra funzione identica ed eliminarne una delle due. Bisogna stabilire dei tipi di funzione (che viene attraversata e che viene consultata). Quelle consultate possono essere unificate e consulatate in un punto unico della rete.

#### Algoritmo:

vsnfConsultate = [ Authentication Function, Key Management Functions, Policy Management Functions ]

function reduceVSNFs(Grafo reteCompleta):
    // semplificazione funzioni attraversate dal traffico...
    foreach(vert in reteCompleta):
        foreach(neighbour in vert):
            if(neighbour.type == vert.type):
                moveLinks(neighbour, vert)      // sposta tutti i link dal vicino dello stesso tipo al nodo su cui ci troviamo
                removeVert(neighbour)
            end
        end
    end

    // semplificazione funzioni da consultare...
    contPerTipo = [ null ]*len(vsnfConsultate)
    foreach(vert in estraiFunzioni(reteCompleta, vsnfConsultate)):      // estraiFunzioni() estrae dal grafo le funzioni del tipo indicato
        if(contPerTipo[ vert.type ] == null):
            contPerTipo[ vert.type ] = vert
        else:
            moveLinks(vert, contPerTipo[ vert.type ])
            removeVert(vert)
        end
    end

    // semplificazione lati ridondanti del grafo...
    foreach(lato in reteCompleta):
        if(lato.side1 == lato.side2):
            removeLato(lato)
        else:
            foreach(lato2 in reteCompleta):
                if(lato.side1 == lato2.side1 && lato.side2 == lato2.side2):
                    removeLato(lato2)
                end
            end
        end
    end
end

*dubbio: così le funzioni di sicurezza fungono anche da router in alcuni casi con regole di inoltro*


**Algoritmo con catene:**

*Posizione: può essere individuata da un nodo, un lato, un nodo e un lato*

vsnfConsultate = [ Authentication Function, Key Management Functions, Policy Management Functions ]

function reduceVSNFs(Grafo reteCompleta):
    // stabilisco che le catene sono nell'ordine di priorità precedentemente deciso (lista ordinata)
    // semplifico le catene vicine unendole...
    foreach(catena in reteCompleta):
        foreach(catenaVicina in catena):
            if(catenaVicina in catena):
                spostaLinks(catenaVicina, catena)   // sposta il punto di entrata e uscita dalla catena contenuta in quella che contiene
                                                    // in corrispondenza delle funzioni richieste
            elseif(catena in catenaVicina):
                spostaLinks(catena, catenVicina)
            else:
                mergeCatene(catena, catenaVicina)   // unisce le catene nella prima, le ordina e trasferisce i link sulla prima
            end
        end
    end

    // semplificazione funzioni da consultare...
    contPerTipo = [ null ]*len(vsnfConsultate)
    foreach(vert in estraiFunzioni(reteCompleta, vsnfConsultate)):      // estraiFunzioni() estrae dal grafo le funzioni del tipo indicato
        if(contPerTipo[ vert.type ] == null):
            contPerTipo[ vert.type ] = vert
        else:
            moveLinks(vert, contPerTipo[ vert.type ])
            removeVert(vert)
        end
    end

    // semplificazione lati ridondanti del grafo...
    foreach(lato in reteCompleta):
        if(lato.side1 == lato.side2):
            removeLato(lato)
        else:
            foreach(lato2 in reteCompleta):
                if(lato.side1 == lato2.side1 && lato.side2 == lato2.side2):
                    removeLato(lato2)
                end
            end
        end
    end
end


**Pattern nell'esempio:**

- Composition: Authentication Function, Key Management Function
- Loop: Authentication Function, Key Management Function
- Pass-Through: IDS, DPI, DNS Security, Anti-Spoofing
- Branch-and-Merge: IDS, DPI, DNS Security, Anti-Spoofing -> su Semplificato 1
- Ordered: IDS, DPI, DNS Security, Anti-Spoofing -> su Semplificato 1 con catene


#### Con Analisi Flussi:
L'approccio sembra più complicato di quello appena proposto semplificando i vicini. Analizzando e semplificando i flussi si rischia di togliere funzioni ridondanti per un flusso ma necessarie per un altro. Inoltre questo comporta percorsi obbligati per i dati, difficilmente dinamici.
Altro approccio potrebbe essere di partire dalle intersezioni tra i flussi per preservare le funzioni in comune. Qui però si rischia di avere un filtraggio del flusso troppo tardi rispetto al punto di entrata nella rete con danneggiamento degli asset che è richiesto di proteggere.

