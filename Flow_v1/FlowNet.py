import numpy as np
import networkx as nx
import matplotlib as mat
import matplotlib.pyplot as plt

class FlowNet:
    
    def __init__(self,file):
        
        data = open(file, "r")
        Graphtype = nx.DiGraph()
        self.G = nx.parse_edgelist(data, delimiter=';', create_using=Graphtype,nodetype=str, data=(('capacity', int),))
        arc_capacity = dict([((u,v,),d['capacity']) for u,v,d, in self.G.edges(data=True)])
        doublon = []
        for i in arc_capacity:
            if arc_capacity[i] < 0:
                raise Exception('Error at edge :'+str(i)+" --> "+str(arc_capacity[i])+' Arc cannot be negativ')
            
            if ((i[1],i[0])) in arc_capacity and not doublon:
                doublon.append((i[1],i[0]))
                self.G.remove_edge(i[1],i[0])
                print('doublon ("' + str(i[1])+'","'+str(i[0])+'", capacity : '+str(arc_capacity[(i[1],i[0])]) +') removed from graph because edge ("'+str(i[0])+'","'+str(i[1])+'" capacity :'+str(arc_capacity[(i[0],i[1])])+') already exist')
        self.max = None
        
    
    def compute_max_flow(self):

    
    def get_flow(self):
    
        return self.max
 
    
    
    def export(self,output):
        plt.clf()
        flow_value, flow_dict = nx.maximum_flow(self.G, "s", "t")
        Gres = nx.DiGraph()
        capaG = dict([((u,v,),d['capacity']) for u,v,d, in self.G.edges(data=True)])
        for i in flow_dict :
            for n in flow_dict[i] :
                Gres.add_edge(i, n, flow=flow_dict[i][n] , capacity=capaG[i,n])

        pos=nx.spring_layout(Gres)
        labels={ e : '{}|{}'.format(Gres[e[0]][e[1]]['flow'],Gres[e[0]][e[1]]['capacity']) for e in Gres.edges}
        nx.draw_networkx_edge_labels(Gres, pos=pos, edge_labels=labels)
        nx.draw(Gres,pos, node_size=500,with_labels=True,node_color='#D5D5D5')
        plt.savefig(output)
