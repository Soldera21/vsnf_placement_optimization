# Notes

### Stefano Berlato, Roberto Carbone, Adam J. Lee, and Silvio Ranise. 2021. "Formal Modelling and Automated Trade-off Analysis of Enforcement Architectures for Cryptographic Access Control in the Cloud." ACM Trans. Priv. Secur. 25, 1, Article 2 (February 2022), 37 pages. https://doi.org/10.1145/3474056
Cryptographic Access Control (CAC) is an obvious solution for sharing data among an organization. In this paper a new scheme to select the best architecture for CAC is proposed to system administrators. The main focus is on understanding which data can reside in a private cloud or in a CPS's data center based on a risk assessment and the score of a set of trust assumptions.

For every element of the risk assessment we assign a score that will be the weight of that attribute in the final decision about the architecture to be used. To achieve this "Best" and "Ad Hoc" algorithm have been developed through a "what-if" analysis. This software can be used through a web dashboard. "Best" selects only the Pareto Optimal solutions and then it lets the administrator to choose the best solution for the organization (Multi-Dimensional Maximum Vector Problem). "Ad Hoc" the problem is taken to a single final solution which should be the best based on performance and risk exposure (Single-Objective Optimisation Problem). The complexity of "Ad Hoc" is significantly lower than "Best".

Finally these concepts are summarized in a Java application named CryptoAC (which acts as a proxy) that needs to be installed on the user equipment to store user's key and get keys of the files that the user wants to access based on the policies.

##### Main Questions:
How can the best architecture for storing and computing business data be choosen to balance costs and security requirements?

##### Main Topics:
- requirements: intended as requirements of the deployed application

### A. Shameli-Sendi, Y. Jarraya, M. Pourzandi and M. Cheriet, "Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns," in IEEE Transactions on Services Computing, vol. 12, no. 4, pp. 534-549, 1 July-Aug. 2019, doi: 10.1109/TSC.2016.2616867.
In the context of microservice placement the security aspect is an important factor used to evalute the location, but many times it is under-estimated. The security requirements are based on a set of standard patterns. These patterns are chained together to compose the entire netwrok with all the security constraints. Every time a constraint is established it has to be satisfied with one or more patterns.

The approach to find a new placement algortihm used in this paper is Security Defense Pattern Aware Placement (SDPAP). We base the computation on two initial steps before finding the optimal placement: partitioning and segmentation. In partitioning we compute independent blocks with different paths to go from the same source to the same destination. The final solution resides in one block and is not affected by this process. In segmentation we divide each block in generally three segments (source, destination and core) to exclude an incorrect placement hypothesis based on constraints. This is made to avoid unuseful attemps to place security functions.

The final algorithm has been implemented in OpenStack and the performance is improved significantly making it almost real-time for a maximum network size of 69,696 nodes. After this limit, the computation becomes difficult also for SDPAP.

##### Main Questions:
Can the security requirements aspect be considered when placing microservices?
Can this also improve performances during service placement or at least maintain the same performance?

##### Main Topics:
- performance: intended as performance of the algorithm
- requirements: intended as requirements of the logic of the chain of NFs

- based on needs of the single VNF

### R. Doriguzzi-Corin, S. Scott-Hayward, D. Siracusa, M. Savi and E. Salvadori, "Dynamic and Application-Aware Provisioning of Chained Virtual Security Network Functions," in IEEE Transactions on Network and Service Management, vol. 17, no. 1, pp. 294-307, March 2020, doi: 10.1109/TNSM.2019.2941128.
In this paper a new algorithm is proposed to deploy chains of network functions based on security policies, computing capabilities of the network and the security services themselves. The main differences with "Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns" and this work are that before the algorithm is limited to fat-tree topology, needs to compute the complete flow and does not take into account the latency of the links.

The Progressive Embedding of Security Services (PESS) algorithm computes the shortest path between source and destination to find all the possible nodes where a VSNF chain can be placed. The more enhanced version also considers high-capacity nodes and the path in both directions computing subpaths that are assembled. The choosen solution is based mainly on the metrics. Then latency and bandwidth are subtracted from the links used by the solution. The results are compared with PESS and standard Kubernetes on a random network, the Stanford University network and the GARR network and a significant boost of performance is evident.

##### Main Questions:
Can the approach of computing the best placement based on security requirements be expanded to every type of network topology?
Is it possible to think about a new algorithm to deploy VSNFs considering also the overhead of nodes and links?

##### Main Topics:
- performance: intended as performance of the links because delay and bandwidth are subtracted when a new service is added
- requirements or policies: based on security best practices

- path based

### N. Moradi, A. Shameli-Sendi and A. Khajouei, "A Scalable Stateful Approach for Virtual Security Functions Orchestration," in IEEE Transactions on Parallel and Distributed Systems, vol. 32, no. 6, pp. 1383-1394, 1 June 2021, doi: 10.1109/TPDS.2021.3049804.
The main focus of this paper is a stateful approach in service placement inside a data center with fat-tree topology. Before creating a new microservice the system evaluates the nodes where an existing service is running to try to assemble more than one together. This method can save resources and time that translates into money because in the end, less functions are created and many times an accomodation is found for the service that we are deploying. The new function can be deployed in an already existing node, moving and merging an old function or creating a new function with the assembled services.

Another step that is done in this paper is to divide into zones the network that we are analyzing to overcome the problem that the algorithm is non-scalable. This results in a faster computation of the placement of the service. The negative note of zoning is that it does pre-processing more times and sometimes functions for the same flow are created on different nodes. So this important aspect is excluded by the zoning algorithm.

##### Main Questions:
Can we reuse an already existing VSNF if it can respect all required constraints?
Can this improve performance and reduce the cost?

##### Main Topics:
- performance: the stateful placement increments performace when deploying functions
- requirements: security constraints of new and old applications

- based on needs of the single VNF and on already present VNFs

### W. Qiao et al., "A Novel Method for Resource Efficient Security Service Chain Embedding Oriented to Cloud Datacenter Networks," in IEEE Access, vol. 9, pp. 77307-77324, 2021, doi: 10.1109/ACCESS.2021.3082644.
This paper wants to propose a new method to find the optimal placement of a Security Service Chain in data center networks. The proposed algorithm is called Particle Swarm Optimization (PSO) and uses a new approach to instantiate chains of functions.

The approach is to first compute the best paths to go from source to destination with a k-Dijkstra algorithm, then find the set of VSNFs needed based on the security level of the application we are deploying and finally the best position for the VSNFs is found iteratively. The main focus of the paper is on having developed an algithm that focuses on security requirements and can deploy the chain without wasting resources that in other cases are used because the maximum level of security is adpoted also if not needed.

The results show that the PSO algorithm finds a new solution that can optimize the deployment of SSCs with less resource comsuption, a better latency between nodes due to deploying not only in most powerful nodes but also taking into account the links and it has a lower complexity than the other algorithms analyzed.

##### Main Questions:
How can we optimize SSC deployment and delay between functions using the precise requirements of every application and VSNF inside data centers?

##### Main Topics:
- performance: the algorithm wants to optimize the performance of the deployed NFs in terms of delay and bandwidth
- requirements: security requirements of the deployed application
- optimization: of the deployment algorithm

- path based
- NFs deployment based on policies

### A. Bagheri and A. Shameli-Sendi, "Automating the Translation of Cloud Users’ High-Level Security Needs to an Optimal Placement Model in the Cloud Infrastructure," in IEEE Transactions on Services Computing, vol. 16, no. 6, pp. 4580-4590, Nov.-Dec. 2023, doi: 10.1109/TSC.2023.3327632.
In this paper for the first time the problem of placing VNFs based on users' needs and cloud providers' placement objectives has been analyzed. The TUSNPM (Translating User’s Security Needs into the Placement Model) algorithm has been developed for fat-tree topology in data centers to understand which is the maximum number of nodes to have a function placement in almost real time.

Results are based on five objectives (Max-N, Max-C, Max-CN, Max-C-Fixed-N, Max-N-Fixed-C) from the cloud provide side and QoS and cost from the user side. To test the performance of the algorithm three scenarios have been tested and when k goes over 32 the runtime becomes higher esponentially causing the computation hard to do in almost real time. Requirements are foundamentals to determine the final cost of the placement.

##### Main Questions:
Can users' needs be satisfied when placing VNFs in fat-tree data centers?

##### Main Topics:
- performace: intended as performance of the placement
- requirements: needs of the users and of the CSP

- users have security needs and CSP has performance needs

### H. Wu, Y. Zhang, H. Yang, G. Yu and J. Cao, "Virtualized Security Function Placement for Security Service Chaining in Cloud," 2018 IEEE 24th International Conference on Parallel and Distributed Systems (ICPADS), Singapore, 2018, pp. 628-637, doi: 10.1109/PADSW.2018.8644566.
This paper takes a new framework named MCE to compute VNF placement. First of all it does a check on the reachability of the nodes, then it simplifies the confilicting policies with the BSIS-RC algorithm based on bit sequence intersection computation.

In the end six solutions are compared with three different algorithms with and without MCE in a fat-tree topology with 8 pods. MCE takes a great performance improvement in the success rate of the mapping algorithm when used. MCE takes also TBC reduction, but the mapping algorithm choosen is the main responsible for this value. Finally the best value of tau is 5 because over it the improvement becomes insignificant.

##### Main Questions:
Can the performance of the placement of VNF be improved simplifying the requirement evaluation of each NF?

##### Main Topics:
- performance: intended as performance of the placement (but also for the TBC reduction)
- requirements: based on security policies

- reachability
- policy conflicts

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
## Papers Chronological Resume

One of the first papers developed in the argument of multi-objective microservice orchestration is "Virtualized Security Function Placement for Security Service Chaining in Cloud" in 2018 where the authors tried to optimize the computation of VSNFs placement, simplifying the conflicting policies of the application and the requirements of each VSNF with a new framework called MCE in fat-tree topology networks. The only performace factor of the application that they evaluated is the Total Bandwidth Consumption.

Then we can find another study that is "Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns" in 2019 which wants to optimize the placement of VSNFs based on a bunch of paths that data can do to go from source to destination with the process of partitioning. Then with segmentation the pool of available nodes is reduced based on if the VSNF needs to stay near the source, the destination or in the core. The difference with the previous one is that here the authors have defined some patterns to describe the requirements to place the VSNFs. In both the needs of the single VSNF are considered and the path of the data is not uniquely defined.

Following this paper, one of the authors A. Shameli-Sendi produced other two studies that I think they could be considered an extension of what he has already produced. First of all "A Scalable Stateful Approach for Virtual Security Functions Orchestration" from 2021 that talks about trying to assemble a new deployed VSNF with other existing ones. To make the algorithm scalable a zoning algorithm is applied. This causes a faster computation but sometimes more nodes are used. From this paper a possible "gap" in the state of art can be found because the authors don't consider moving old VSNFs to leave space on a node for a new one and find another balance in the network that can be optimal for balancing every application. The second study is "Automating the Translation of Cloud Users’ High-Level Security Needs to an Optimal Placement Model in the Cloud Infrastructure" from 2023 and the authors' main question is about how to combine the security requirements of the user (intended as developer of the application) like costs and QoS and the performance needs of the CSP based on five classes of objectives. Reading all these arcticles from A. Shameli-Sendi the impression is that he wants to start from the general problem to go then in more specific fields like the stateful placement and the consideration of users' needs.

In 2020 the paper "Dynamic and Application-Aware Provisioning of Chained Virtual Security Network Functions" has been developed and I think that this one could be considered as a follow-up of the one from 2019. What the authors wanted to achieve was to expand the placement algorithm from the other study to every type of network topology and to consider the overhead on the links. This also computes the entire path from source to destination to find the best placement for all the VSNFs.

Then in 2021 the study "A Novel Method for Resource Efficient Security Service Chain Embedding Oriented to Cloud Datacenter Networks" has been written. The main focus of the authors here is on optimizing delays between VNFs inside data centers while trying to respect every security requirement of the applications and without applying the maximum level of security by default. The computation of the placement is based on the paths that data can follow.

I think that the underlying theme of all the papers found during this research is trying to find an optimal balance between performance of the placement algorithm, the respect of the security requirement of the application, the needs of the CSP and the performance of the deployed VSNFs.

---
## Objectives of the Papers

| | Year | Performance of placement algorithm | Performance of deployment | Performance of application | Based on req. of single VNF | Path based | Based on existing VNFs | Fat-tree topology | Every topology | General DC network |
| - | - | - | - | - | - | - | - | - | - | - |
| Efficient Provisioning of Security Service Function Chaining Using Network Security Defense Patterns | 2019 | x | | | x | | | x | | |
| Dynamic and Application-Aware Provisioning of Chained Virtual Security Network Functions | 2020 | | | x | | x | | | x | |
| A Scalable Stateful Approach for Virtual Security Functions Orchestration | 2021 | | x | x | x | | x | x | | |
| A Novel Method for Resource Efficient Security Service Chain Embedding Oriented to Cloud Datacenter Networks | 2021 | | | x | | x | | | | x |
| Automating the Translation of Cloud Users’ High-Level Security Needs to an Optimal Placement Model in the Cloud Infrastructure | 2023 | | x | | x | | | x | | |
| Virtualized Security Function Placement for Security Service Chaining in Cloud | 2018 | x | | x\* | x | | | x | | |

\* only for Total Bandwidth Consumption (TBC) reduction

All these objectives are achieved always taking into account with a good priority the security requirements of the deployment. The main goal is to achieve a compromise between performance and security needs.

---
## Possible Thesis Arguments
- An old function can be migrated to leave optimal place for a new one (re-organizing the network)
- From Stateful Approach: Note that the only criterion for selecting the edge is not the current bandwidth, but the number of flows passed and their traffic rate are also important criteria. In terms of nodes, the number of processors and more memory are the criteria, but the created functions in the node and the traffic rate that is entered into them must also be considered. In this paper, a formula for combining these criteria for the cost of edge and node is not provided.
- Generalize an already studied approach to every topology

#### Observations:
- Computing multiple paths and then place VSNFs not only considering the shortest seems preferred
- In the last studies the main focus is on the performance of the application or of the deployment

---
- scrivere related work su latex

- file minute???
