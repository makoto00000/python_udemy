# pip install networkx
# pip install matplotlib

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_node(1)   # nodeを一つ追加

G.add_nodes_from([2, 3])  # nodeを２つ追加

G.add_edge(1, 2)  # node1と2を繋ぐ
G.add_edge(2, 3)  # node2と3を繋ぐ

nx.draw(G)
plt.show()

