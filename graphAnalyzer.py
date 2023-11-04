import networkx as nx
import pickle
import matplotlib.pyplot as plt
the_graph = open("ExpGraph.pickle","rb")

G = pickle.load(the_graph)

def sumUp(G,nodename):
    summ = 0
    for k in G[nodename].values():
        summ += k['weight']
    return summ
G.remove_nodes_from(list(nx.isolates(G)))
for k in G.nodes():
    G.nodes[k]['influence'] = sumUp(G,k)*30
print(G.nodes["Terannia"])
pos=nx.spring_layout(G)

print(G.edges(data = True))
#print(G.nodes(data = True))


nx.draw_networkx_nodes(G,pos,node_size=[n[1]['influence'] for n in G.nodes(data=True)],node_color=[n[1]['node_type'] for n in G.nodes(data=True)],alpha = 0.5)
nx.draw_networkx_edges(G,pos,width=[n[2]['weight']*1.5 for n in G.edges(data=True)] )
nx.draw_networkx_labels(G, pos, font_size=5.8, font_family='sans-serif')

plt.show()