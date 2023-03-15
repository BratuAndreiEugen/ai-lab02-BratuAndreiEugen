import networkx as nx
import scipy as sp
import numpy as np

def converter(path): # returns adjecency matrix
    graph = nx.read_gml(path)
    m = nx.adjacency_matrix(graph)
    matrix = m.todense() # matricea de adiacenta
    return matrix

def reader(path): # returns networkx graph
    graph = nx.read_gml(path)
    return graph

# print(converter("C:\Proiecte SSD\Python\lab2AI\\networks\dolphins\dolphins.gml"))