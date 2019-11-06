import matplotlib.pyplot as plt
import pylab
from pylab import rcParams
import networkx as nx
import numpy as np

rcParams['figure.figsize'] = 10, 10
G = nx.DiGraph()
G.add_edges_from([('K', 'I'), ('R', 'T'), ('V', 'T')], weight=3)
G.add_edges_from([('T', 'K'), ('T', 'H'), ('I', 'T'), ('T', 'H')], weight=4)
G.add_edges_from([('I', 'R'), ('H', 'N')], weight=5)
G.add_edges_from([('R', 'N')], weight=6)
val_map = {'K': 1.5, 'I': 0.9, 'R': 0.6, 'T': 0.2}
values = [val_map.get(node, 1.0) for node in G.nodes()]

edge_labels = dict([((u,v,),d['weight']) for u, v, d in G.edges(data=True)])
red_edges = [('R', 'T'), ('T', 'K')]
edge_colors = ['green' if not edge in red_edges else 'red' for edge in G.edges()]

pos = nx.spring_layout(G)
nx.draw_networkx_edges(G, pos, width=2.0, alpha=0.65)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

nx.draw(G, pos, node_color=values, node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
pylab.show()