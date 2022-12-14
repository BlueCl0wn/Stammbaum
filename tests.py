import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node(1)
G.add_nodes_from([2, 3])

G.add_nodes_from({0: ((1, {"color": "red"}), (2, {"color": "red"}))})
G.add_edges_from([(0, 1, {"color":"red"})])
print(G.nodes())
print(G.edges())