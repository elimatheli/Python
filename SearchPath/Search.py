import numpy as np
import networkx as nx
import matplotlib as mat
import matplotlib.pyplot as plt

## Partie 1 - parcours en largeur et en profondeur


g = nx.Graph([(0,1),(0,2),(1,3),(2,4),(2,1),(3,5),(5,1)])

#Q1
def parcours_en_largeur(graphe, sommet):

    visited = []
    nextNodes = []
    nextNodes.append(sommet)
    while nextNodes:
        searchNeighborsNode = nextNodes.pop(0)
        visited.append(searchNeighborsNode)
        for i in graphe[searchNeighborsNode]:
            if i not in visited and i not in nextNodes:
                nextNodes.append(i)
        print(nextNodes)
    return visited

# >>> parcours_en_largeur(g, 0)
# [0, 1, 2, 3, 5, 4]


#Q2
def parcours_en_profondeur(graphe, sommet):
    
    visited = []
    nextNodes = []
    nextNodes.append(sommet)

    while nextNodes:
        sommet = nextNodes.pop()
        if sommet not in visited:
            visited.append(sommet)
            unvisited = [n for n in graphe[sommet] if n not in visited]
            nextNodes += unvisited
    return visited

#>>> parcours_en_profondeur(g,0)
# [0, 2, 1, 5, 3, 4]
    

## Partie 2 - amélioration du parcours

#Q1

#>>> parcours_en_profondeur(g,0)
# [1, 2]
# [1, 4, 1]    -- le sommet 1 est empilé deux fois
# [1, 4, 3, 5]
# [1, 4, 3, 3]
# [1, 4, 3]
# [1]
# [0, 2, 1, 5, 3, 4]

#Q2
def parcours_en_profondeur_ameliore(graphe,sommet):
    
    visited = []
    nextNodes = []
    nextNodes.append(sommet)

    while nextNodes:
        sommet = nextNodes.pop()
        if sommet not in visited:
            visited.append(sommet)
            unvisited = [n for n in graphe[sommet] if n not in visited and n not in nextNodes]
            nextNodes += unvisited
            print(nextNodes)
    return visited

# >>> parcours_en_profondeur_ameliore(g, 0)
# [1, 2]
# [1, 4]    le sommet 1 n'est compilé qu'une fois
# [1]
# [3, 5]
# [3]
# []
# [0, 2, 4, 1, 5, 3]


##Partie 3 - arbre de parcours

#Q1
def arbre_couvrant (graphe, sommet):
    
    visited = []
    nextNodes = []
    tree = []
    nextNodes.append(sommet)


