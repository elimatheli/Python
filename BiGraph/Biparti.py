# TP3 - détection de graphes biparti (en autonomie)

import numpy as np
import networkx as nx
import matplotlib as mat
import matplotlib.pyplot as plt

# Approche du problème :

# Q1
g8 = nx.Graph([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8)])

def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller
        

def est_biparti_naif(graphe):
    
    list_nodes = list(graphe.nodes)
    res_part = partition(list_nodes)
    for n in res_part:
        if(len(n) == 2):
            test_value = True
            while(test_value == True):
                for i in n:
                    if(test_value == False):
                        break
                    for j in i:
                        if(test_value == False):
                            break
                        list_nei = list(graphe[j])
                        for h in list_nei:
                            if(test_value == False):
                                break
                            if(h in i):
                                test_value = False
                                break
                if(test_value == True):
                        print("Les deux Ensembles sont :")
                        print(n)
                        return True

                                
    print("Il n'y a pas d'ensembles")     
    return False
                  