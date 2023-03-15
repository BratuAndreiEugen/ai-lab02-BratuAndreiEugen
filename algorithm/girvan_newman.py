import networkx as nx

import numpy as np

from algorithm.just_newman import newman
from utils.gmlReader import converter, reader


def my_girvan_newman(network): # network - matrice de adiacenta
    a = np.array(network)
    g = nx.from_numpy_array(a)

    from networkx.algorithms import community
    comp = community.girvan_newman(g)
    top_level = next(comp)

    communities = tuple(sorted(c) for c in top_level)
    return communities

def gn_for_nx(network): # network - networkx graph
    from networkx.algorithms import community
    comp = community.girvan_newman(network)
    top_level = next(comp)
    communities = tuple(sorted(c) for c in top_level)
    return communities

#
# print(my_girvan_newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\krebs\krebs.gml")))
# #print(gn_for_nx(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\krebs\krebs.gml")))