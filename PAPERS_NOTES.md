# Notes

### Stefano Berlato, Roberto Carbone, Adam J. Lee, and Silvio Ranise. 2021. "Formal Modelling and Automated Trade-off Analysis of Enforcement Architectures for Cryptographic Access Control in the Cloud." ACM Trans. Priv. Secur. 25, 1, Article 2 (February 2022), 37 pages. https://doi.org/10.1145/3474056
Cryptographic Access Control (CAC) is an obvious solution for sharing data among an organization. In this paper a new scheme to select the best architecture for CAC is proposed to system administrators. The main focus is on understanding which data can reside in a private cloud or in a CPS's data center based on a risk assessment and the score of a set of trust assumptions.

For every element of the risk assessment we assign a score that will be the weight of that attribute in the final decision about the archutecture to be used. To achieve this "Best" and "Ad Hoc" algorithm have been developed through a "what-if" analysis. This software can be used through a web dashboard. "Best" selects only the Pareto Optimal solutions and then it lets the administrator to choose the best solution for the organization (Multi-Dimensional Maximum Vector Problem). "Ad Hoc" the problem is taken to a single final solution which should be the best based on performance and risk exposure (Single-Objective Optimisation Problem). The complexity of "Ad Hoc" is significantly lower than "Best".

Finally these concepts are summarized in a Java application named CryptoAC (which acts as a proxy) that needs to be installed on the user equipment to store user's key and get keys of the files that the user wants to access based on the policies.

##### Main Questions:


### A. Shameli-Sendi, Y. Jarraya, M. Pourzandi and M. Cheriet, "Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns," in IEEE Transactions on Services Computing, vol. 12, no. 4, pp. 534-549, 1 July-Aug. 2019, doi: 10.1109/TSC.2016.2616867.
In the context of microservice placement the security aspect is an important factor used to evalute the location, but many times it is under-estimated. The security requirements are based on a set of standard patterns. These patterns are chained together to compose the entire netwrok with all the security constraints. Every time a constraint is established it has to be satisfied with one or more patterns.

The approach to find a new placement algortihm used in this paper is Security Defense Pattern Aware Placement (SDPAP). We base the computation on two initial steps before finding the optimal placement: partitioning and segmentation. In partitioning we compute independent blocks with different paths to go from the same source to the same destination. The final solution resides in one block and is not affected by this process. In segmentation we divide each block in generally three segments (source, destination and core) to exclude an incorrect placement hypothesis based on constraints. This is made to avoid unuseful attemps to place security functions.

The final algorithm has been implemented in OpenStack and the performance is improved significantly making it almost real-time for a maximum network size of 69,696 nodes. After this limit the computation becomes difficult also for SDPAP.

##### Main Questions:


### R. Doriguzzi-Corin, S. Scott-Hayward, D. Siracusa, M. Savi and E. Salvadori, "Dynamic and Application-Aware Provisioning of Chained Virtual Security Network Functions," in IEEE Transactions on Network and Service Management, vol. 17, no. 1, pp. 294-307, March 2020, doi: 10.1109/TNSM.2019.2941128.
In this paper a new algorithm is proposed to deploy chains of network functions based on security policies, computing capabilities of the network and the security service itself. The main differences with "Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns" and this work are that before the algorithm is limited to fat-tree topology, needs to compute the complete flow and does not take into account the latency of the links.

The Progressive Embedding of Security Services (PESS) algorithm computes the shortest path between source and destination to find all the possible nodes where a VSNF chain can be placed. The more enhanced version also considers high-capacity nodes and the path in both directions computing subpaths that are assembled. The choosen solution is based mainly on the metrics. Then latency and bandwidth are subtracted from the links used by the solution. The results are compared with PESS and standard Kubernetes on a random network, the Stanford University network and the GARR network and a significant boost of performance is evident.

##### Main Questions:


### N. Moradi, A. Shameli-Sendi and A. Khajouei, "A Scalable Stateful Approach for Virtual Security Functions Orchestration," in IEEE Transactions on Parallel and Distributed Systems, vol. 32, no. 6, pp. 1383-1394, 1 June 2021, doi: 10.1109/TPDS.2021.3049804.
The main focus of this paper is a stateful approach in service placement inside a data center with fat-tree topology. Before creating a new microservice the system evaluates the nodes where an existing service is running to try to assemble more than one together. This method can save resources and time that translates into money because in the end less functions are created and many time an accomodation is found for the service that we are deploying.

Another step that is done in this paper is to divide into zones the netwrok that we are analyzing. This results in a faster computation of the placement of the service. The negative note of zoning is that it does pre-processing and function for the same flow are created on different nodes. So this important aspect is excluded by the zoning algorithm.

##### Main Questions:
Can we reuse an already existing VSNF if it can respect all my constraints?
Can this improve performance and reduce the cost?

### W. Qiao et al., "A Novel Method for Resource Efficient Security Service Chain Embedding Oriented to Cloud Datacenter Networks," in IEEE Access, vol. 9, pp. 77307-77324, 2021, doi: 10.1109/ACCESS.2021.3082644.
This paper wants to propose a new method to find the optimal placement of a Security Service Chain in data center networks. The proposed algorithm is called Particle Swarm Optimization (PSO) and uses a new approach to instantiate chains of functions.

The approach is to first compute the best paths to go from source to destination with a k-Dijkstra algorithm, then find the set of VSNFs needed based on the security level of the application we are deploying and finally the best position for the VSNFs is found iteratively. The main focus of the paper is on having developed an algithm that focuses on security requirements and can deploy the chain without wasting resources that in other cases are used because the maximum level of security is adpoted also if not needed.

The results show that the PSO algorithm finds a new solution that can optimize the deployment of SSCs with less resource comsuption, a better latency between nodes due to deploying not only in most powerful nodes but also taking into account the links and it has a lower complexity than the other algorithms analyzed.

##### Main Questions:
How can we optimize SSC deployment and delay between functions using the precise requirements of every application and VSNF?

### A. Bagheri and A. Shameli-Sendi, "Automating the Translation of Cloud Users’ High-Level Security Needs to an Optimal Placement Model in the Cloud Infrastructure," in IEEE Transactions on Services Computing, vol. 16, no. 6, pp. 4580-4590, Nov.-Dec. 2023, doi: 10.1109/TSC.2023.3327632.


##### Main Questions:


### H. Wu, Y. Zhang, H. Yang, G. Yu and J. Cao, "Virtualized Security Function Placement for Security Service Chaining in Cloud," 2018 IEEE 24th International Conference on Parallel and Distributed Systems (ICPADS), Singapore, 2018, pp. 628-637, doi: 10.1109/PADSW.2018.8644566.


##### Main Questions:


---
## Other Possibly Related Papers

1. P.-C. Lin, C.-F. Wu and P.-H. Shih, "Optimal Placement of Network Security Monitoring Functions in NFV-Enabled Data Centers," 2017 IEEE 7th International Symposium on Cloud and Service Computing (SC2), Kanazawa, Japan, 2017, pp. 9-16, doi: 10.1109/SC2.2017.10.

2. S. Demirci, M. Demirci and S. Sagiroglu, "Optimal Placement of Virtual Security Functions to Minimize Energy Consumption," 2018 International Symposium on Networks, Computers and Communications (ISNCC), Rome, Italy, 2018, pp. 1-6, doi: 10.1109/ISNCC.2018.8530989.

---
## Excluded Papers

1. B. Xia, C. Li, Z. Zhou and J. Liu, "Research on Deployment Method of Service function Chain based on Network function Virtualization in Distribution communication Network," 2023 IEEE 6th Information Technology,Networking,Electronic and Automation Control Conference (ITNEC), Chongqing, China, 2023, pp. 1410-1414, doi: 10.1109/ITNEC56291.2023.10082364.

2. A. Mohammadkhan, S. Ghapani, G. Liu, W. Zhang, K. Ramakrishnan, and T. Wood, “Virtual function placement and traffic steering in flexible and dynamic software defined networks,” in Proc. IEEE Int. Workshop Local Metropolitan Area Netw., 2015, pp. 1–6.

3. B. Addis, D. Belabed, M. Bouet, and S. Secci, “Virtual network functions placement and routing optimization,” in Proc. IEEE 4th Int. Conf. Cloud Netw., 2015, pp. 171–177.

4. R. Doriguzzi-Corin, S. Scott-Hayward, D. Siracusa and E. Salvadori, "Application-Centric provisioning of virtual security network functions," 2017 IEEE Conference on Network Function Virtualization and Software Defined Networks (NFV-SDN), Berlin, Germany, 2017, pp. 276-279, doi: 10.1109/NFV-SDN.2017.8169861.

---
## Domande

#### Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns

1. Con SDPAP andiamo a piazzare i moduli di sicurezza nella stessa partizione di sorgente e destinazione con un algoritmo più efficiente di quelli usati attualmente per un problema NP-Hard. Non mi è ancora chiaro quale sia il ruolo dei requisiti di un determinato servizio nell'algoritmo di piazzamento.

2. Il piazzamento ottimale di un servizio viene standardizzato per tutti e quindi può non essere ottimale per alcuni oppure se ci si rende conto che non è sufficiente per un servizio questo viene ri-piazzato?
