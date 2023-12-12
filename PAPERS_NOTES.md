# Notes

### Formal Modelling and Automated Trade-Off Analysis of Enforcement Architectures for Cryptographic Access Control in the Cloud
Cryptographic Access Control (CAC) is an obvious solution for sharing data among an organization. In this paper a new scheme to select the best architecture for CAC is proposed to system administrators. The main focus is on understanding which data can reside in a private cloud or in a CPS's data center based on a risk assessment and the score of a set of trust assumptions.

For every element of the risk assessment we assign a score that will be the weight of that attribute in the final decision about the archutecture to be used. To achieve this "Best" and "Ad Hoc" algorithm have been developed through a "what-if" analysis. This software can be used through a web dashboard. "Best" selects only the Pareto Optimal solutions and then it lets the administrator to choose the best solution for the organization (Multi-Dimensional Maximum Vector Problem). "Ad Hoc" the problem is taken to a single final solution which should be the best based on performance and risk exposure (Single-Objective Optimisation Problem). The complexity of "Ad Hoc" is significantly lower than "Best".

Finally these concepts are summarized in a Java application named CryptoAC (which acts as a proxy) that needs to be installed on the user equipment to store user's key and get keys of the files that the user wants to access based on the policies.

### Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns
In the context of microservice placement the security aspect is an important factor used to evalute the location, but many times it is under-estimated. The security requirements are based on a set of standard patterns. These patterns are chained together to compose the entire netwrok with all the security constraints. Every time a constraint is established it has to be satisfied with one or more patterns.

The approach to find a new placement algortihm used in this paper is Security Defense Pattern Aware Placement (SDPAP). We base the computation on two initial steps before finding the optimal placement: partitioning and segmentation. In partitioning we compute independent blocks with different paths to go from the same source to the same destination. The final solution resides in one block and is not affected by this process. In segmentation we divide each block in generally three segments (source, destination and core) to exclude an incorrect placement hypothesis based on constraints. This is made to avoid unuseful attemps to place security functions.

The final algorithm has been implemented in OpenStack and the performance is improved significantly making it almost real-time for a maximum network size of 69,696 nodes. After this limit the computation becomes difficult also for SDPAP.

### Dynamic and Application-Aware Provisioning of Chained Virtual Security Network Functions
In this paper a new algorithm is proposed to deploy chains of network functions based on security policies, computing capabilities of the network and the security service itself. The main differences with "Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns" and this work are that before the algorithm is limited to fat-tree topology, needs to compute the complete flow and does not take into account the latency of the links.

The Progressive Embedding of Security Services (PESS) algorithm computes the shortest path between source and destination to find all the possible nodes where a VSNF chain can be placed. The more enhanced version also considers high-capacity nodes and the path in both directions computing subpaths that are assembled. The choosen solution is based mainly on the metrics. Then latency and bandwidth are subtracted from the links used by the solution. The results are compared with PESS and standard Kubernetes on a random network, the Stanford University network and the GARR network and a significant boost of performance is evident.

---
## Domande

#### Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns
1. Con SDPAP andiamo a piazzare i moduli di sicurezza nella stessa partizione di sorgente e destinazione con un algoritmo più efficiente di quelli usati attualmente per un problema NP-Hard. Non mi è ancora chiaro quale sia il ruolo dei requisiti di un determinato servizio nell'algoritmo di piazzamento.
