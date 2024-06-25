import xml.etree.ElementTree as ET
import networkx as nx 
import matplotlib.pyplot as plt 

tree = ET.parse('algorithms/BPMN_metodology.drawio.xml')
root = tree.getroot()

#print(len(root.findall('.//mxCell')))
#for e in root.iter():
#    print(e)

class GraphVisualization: 
   
    def __init__(self): 
          
        # visual is a list which stores all  
        # the set of edges that constitutes a 
        # graph 
        self.visual = [] 
          
    # addEdge function inputs the vertices of an 
    # edge and appends it to the visual list 
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 
          
    # In visualize function G is an object of 
    # class Graph given by networkx G.add_edges_from(visual) 
    # creates a graph with a given list 
    # nx.draw_networkx(G) - plots the graph 
    # plt.show() - displays the graph 
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 


class Node:
    def __init__(self, id, name, cid = -1):
        self.id = id
        self.name = name.split('#')[0]
        self.chainId = cid
    
    def __str__(self):
        return f"{self.id}: {self.name}"


class Chain:
    def __init__(self, id):
        self.id = id
        self.parts = []

        self.ins = []
        self.outs = []
        # eliminare links
        self.links = []
    
    def addElem(self, node):
        self.parts.append(node)
    
    def sort(self):
        self.parts = [t for x in vsnfs for t in self.parts if t.name == x]

    def __str__(self):
        ret = str(self.id) + ': '
        for p in self.parts:
            ret += str(p) + ', '
        ret += ' ' + str(self.links)
        return ret


vsnfs = ['Intrusion Detection System', 'Malware Scanner', 'Deep Packet Inspection', 'Firewall', 'Intrusion Prevention System', 'Anti-Spoofing', 'Honeypot', 'Reverse Proxy', 'Service Mesh', 'Authentication Function', 'Key Management Function', 'Policy Management Function', 'Sniffer', 'DNS Security', 'Proxy']
cons_vsnf = ['Authentication Function', 'Key Management Function', 'Policy Management Function']

elems = root.findall('.//mxCell')

nodes = {}
chains = {}
network = {}
network_dl = {}

max = -1
for e in elems:
    a = e.attrib
    if 'value' in a and int(a['id']) > max:
        max = int(a['id'])

for e in elems:
    a = e.attrib
    if 'value' in a:
        if not a['value'].split('#')[0] in vsnfs:
            nodes[int(a['id'])] = Node(int(a['id']), a['value'])
            network[int(a['id'])] = []

            network_dl[int(a['id'])] = []
        else:
            id = int(a['value'].split('#')[1]) + max
            if not id in chains:
                chains[id] = Chain(id)
            nodes[int(a['id'])] = Node(int(a['id']), a['value'], id)
            chains[id].addElem(nodes[int(a['id'])])
            network[id] = []

            network_dl[id] = []

# TO REMOVE per provare merge...
nodes[1] = Node(1, 'Proxy', 65)
chains[65].addElem(nodes[1])

for e in elems:
    a = e.attrib
    if 'source' in a and 'target' in a:
        sid = nodes[int(a['source'])].chainId
        did = nodes[int(a['target'])].chainId
        
        # finire registrazione e movimento di link interni alle chain...
        # collegamenti da chain a vsnf e da chain a chain riconoscendo lato in e lato out
        if (did != -1) or (sid != -1):
            if did != -1:
                chains[nodes[int(a['target'])].chainId].links.append([int(a['source']), int(a['target'])])
            else:
                chains[nodes[int(a['source'])].chainId].links.append([int(a['source']), int(a['target'])])

        if sid == -1:
            sid = int(a['source'])
        if did == -1:
            did = int(a['target'])

        if sid != did:
            network[sid].append(did)

            network_dl[sid].append(did)
            network_dl[did].append(sid)

for k, c in chains.items():
    chains[k].sort()

print(network)
#print(network_dl)
# for k, n in nodes.items():
#     print(n)
for k, n in chains.items():
    print(n)


def findChainNeighs():
    res = {}
    for k, n in chains.items():
        temp_neighs = network[k]
        neighs = []
        for neigh in temp_neighs:
            if neigh in chains:
                neighs.append(neigh)
        res[k] = neighs
    return res

def contains(a, b):
    res = True
    for el in b.parts:
        found = False
        for f in a.parts:
            if el.name == f.name:
                found = True
        if not found:
            res = False
    return res

def containsElem(a, b):
    found = False
    for f in a.parts:
        if b.name == f.name:
            found = True
    return found

def findLinks(c):
    res = network[c.id]
    for k, n in network.items():
        if c.id in n:
            res.append(k)
    return res

def moveLinks(a, b):
    if b.id in network[a.id]:
        network[a.id].remove(b.id)
    else:
        network[b.id].remove(a.id)

    # l1 = findLinks(a)
    # l2 = findLinks(b)
    # for el in l2:
    #     if not el in l1:
    #         l1.append(el)

    network[a.id] = network[a.id] + network[b.id]

    chains.pop(b.id, None)
    network.pop(b.id, None)

    for k, n in network.items():
        if (k != a.id) and (b.id in n) and (not k in network[a.id]):
            network[k][network[k].index(b.id)] = a.id
        elif (k != a.id) and (b.id in n) and (k in network[a.id]):
            network[k].remove(b.id)

def merge(a, b):
    for el in b.parts:
        if not containsElem(a, el):
            a.addElem(el)


# Semplificazione funzioni in catena...
nodes_new = {}
chains_new = {}
network_new = {}
network_dl_new = {}

pos = 0
while pos != -1:
    chains_neighs = findChainNeighs()
    pos = -1
    for k, n in chains_neighs.items():
        if len(n) > 0:
            pos = k
            break
    if pos != -1:
        el = chains_neighs[pos][0]
        if contains(chains[pos], chains[el]):
            print(str(pos) + '<-' + str(el) + ': b in a')
            moveLinks(chains[pos], chains[el])
        elif contains(chains[el], chains[pos]):
            print(str(pos) + '->' + str(el) + ': a in b')
            moveLinks(chains[el], chains[pos])
        else:
            print('merge in a')
            merge(chains[pos], chains[el])
            chains[pos].sort()
            moveLinks(chains[pos], chains[el])

print(network)


# Semplificare funzioni da consultare...



G = GraphVisualization()
for k, n in network.items():
    for l in n:
        G.addEdge(k, l)
#G.visualize()
