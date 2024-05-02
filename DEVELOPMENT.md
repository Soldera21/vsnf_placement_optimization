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
- costo con cpu si trova online
- fare prova a mano con la metodologia del BPMN
