
import networkx as nx

G = nx.read_edgelist('sample.txt')

def n(G):
    return nx.number_of_nodes (G)

def m(G):
    return nx.number_of_edges (G)


