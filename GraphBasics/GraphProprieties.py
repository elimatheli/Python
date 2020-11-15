import numpy as np
import networkx as nx
import matplotlib as mat
import matplotlib.pyplot as plt

## PARTIE 1 ##

g = np.array([[0,1,1,0],[1,0,1,0],[1,1,0,0],[0,0,0,0]])

# g
# array([[0, 1, 1, 0],
#        [1, 0, 1, 0],
#        [1, 1, 0, 0],
#        [0, 0, 0, 0]])

def testarrete(g,som1,som2):
    
    return g[som1][som2] == 1

#>>> testarrete(g,0,2)
#True

#testarrete(g,1,2)
#True

def voisins (graphe, sommet):
    res = []
    index = 0
    for i in graphe[sommet]:
        if i == 1:
            res.append(index)
        index += 1
    return res


# >>> voisins(g,0)
# [1, 2]


# >>> voisins(g,1)
# [0, 2]


def taille (graphe):
    res = 0
    for i in graphe[0]:
        res += 1
    return res


def creer (graphe, nombre_de_sommets):

    res = [[0]*nombre_de_sommets for _ in range(nombre_de_sommets)]
    for sub in graphe:
        res[sub[0]][sub[1]] = 1
        res[sub[1]][sub[0]] = 1
    return np.array(res)

# creer([(0,3), (1, 2), (1, 3)],4)
# array([[0, 0, 0, 1],
#        [0, 0, 1, 1],
#        [0, 1, 0, 0],
#        [1, 1, 0, 0]])


def ajouter_arete (graphe, sommet1, sommet2):

    graphe[sommet1][sommet2] = 1
    graphe[sommet2][sommet1] = 1

## PARTIE 2 ##
    
    
def test_defined_arrete(graphe,sommet1,sommet2):
    
    if sommet2 in graphe[sommet1]:
        return True
    else:
        return False
    
def taille_list(list):
    
    return len(list)


def creer_list (graphe, nombre_de_sommets):
    reslist = [[] for _ in range(nombre_de_sommets+1)]
    for sublist in graphe:
        reslist[sublist[0]].append(sublist[1])
        reslist[sublist[1]].append(sublist[0])
    return reslist


def ajouter_arete_list (graphe, sommet1, sommet2):

    graphe[sommet1].append(sommet2)
    graphe[sommet2].append(sommet1)

    
## PARTIE 3 ##
    
#Q1

def constructgraph():
    g = nx.Graph()
    g.add_nodes_from([1,2,3,4])
    g.add_edges_from([(1,2),(2,3),(2,4),(1,4),(1,3)])
    nx.draw(g,node_color="#d5d5d5",with_labels=True,node_size=800,font_size=13,font_weight=800)
    plt.show()
    return g


#Q2
    
def get_number_of_nodes(g):
    
    return g.number_of_nodes()

# gr = constructgraph()
# get_number_of_nodes(gr)
# 4

def get_number_of_edges(g):
    
    return g.number_of_edges()

# gr = constructgraph()
# get_number_of_edges(gr)
# 5

def get_degree_of_node(g,node):
    
    return g.degree[node]

# get_degree_of_node(gr,1)
# 3
# get_degree_of_node(gr,2)
# 3


def get_neighbors_of_node(g,node):
    
    return list(g.neighbors(node))

# gr = constructgraph()
# get_neighbors_of_node(gr,2)
# [1, 3, 4]


def degre_max(g):
    
    assert isinstance(g,nx.classes.graph.Graph)
    maxdegree = 0
    list_of_nodes = list(g.nodes)
    for i in list_of_nodes:
        if maxdegree < len(list(g.neighbors(i))):
            maxdegree = len(list(g.neighbors(i)))
            whatdegree = i
    print("The node "+str(i)+" has a degree of "+str(maxdegree)) 
    return maxdegree

# h = nx.Graph([('Paul','Jacques'),('Paul','Maryse')])
# degre_max(h)
# The node Maryse has a degree of 2
# 2


def est_complet(g):
    assert isinstance(g,nx.classes.graph.Graph)
    return nx.is_connected(g)


# h = nx.Graph([('Paul','Jacques'),('Paul','Maryse')])
# est_complet(h)
# True


# h = nx.Graph([('Paul','Jacques')])
# h.add_node("test")
# est_complet(h)
# False


def est_isomorphe(g1,g2):
    
    assert isinstance(g1,nx.classes.graph.Graph)
    assert isinstance(g2,nx.classes.graph.Graph)
    
    return nx.is_isomorphic(g1,g2)

# h = nx.Graph([('Paul','Jacques'),('Paul','Maryse'),('Maryse','Pierre'),('Pierre','Jacques'),('Pierre','Paul')])
# G = nx.Graph([(1,2),(2,3),(2,4),(1,4),(1,3)])
# notiso = nx.Graph([(1,2),(2,3),(1,3)])
# est_isomorphe(h,G)
# True
# est_isomorphe(h,notiso)
# False
# est_isomorphe(G,notiso)
# False