import networkx as nx
import numpy as np

from utils.gmlReader import converter, reader


def newman(network): # network - adjacency matrix
    a = np.array(network)
    g = nx.from_numpy_array(a)

    from networkx.algorithms import community
    comp = community.greedy_modularity_communities(g)
    return comp

def input_modifier(network):
    nodes1 = nx.nodes(network)
    edges1 = nx.edges(network)
    map_nodes = {}
    start = 0
    edges = []
    nodes = []
    for nod in nodes1:
        map_nodes[nod] = start
        nodes.append([start])
        start+=1

    for edge in edges1:
        edges.append([map_nodes[edge[0]], map_nodes[edge[1]]])

    return [nodes, edges]

def my_newman(network, karate = 0): # networkx network

    noNodes = len(nx.nodes(network))
    noEdges = len(nx.edges(network))
    communities = input_modifier(network)[0]
    edges = input_modifier(network)[1]
    m = nx.adjacency_matrix(network)
    matrix = m.todense()  # matricea de adiacenta

    # formez matricea e( e[i][j] - number of edges that connect group i to group j )
    e = []
    for i in range(0, noNodes):
        e.append([])
        for j in range(0, noNodes):
            e[i].append(matrix[i][j]/noEdges)
    # formez vectorul a ( a[i] - number of edges that connect to elements in group i )
    a = []
    for i in range(0, noNodes):
        a.append(sum(e[i]))

    # calculez Q initial
    # Q = 0
    # for comun in communities:
    #     if karate == 1:
    #         comun[0] -=1
    #     Q = Q - (sum(matrix[comun[0]])/(2*noEdges))**2
    # print(Q)
    Q = 0
    for i in range(0, noNodes):
        Q = Q - a[i] ** 2


    # mapez pe un vector diecare nod in ce comunitate va fi
    start = 0
    communities_map = []
    for comun in communities:
        communities_map.append(start)
        start += 1


    # calculez deltaQ pentru fiecare muchie care uneste doua comunitati distincte si aplic
    # join pe comunitatile cu deltaQ maxim rezultat
    cuts = []
    cuts.append([communities_map,Q])
    joins = 0
    while joins < noNodes-1:
        maxDetlaQ = -10
        assimilator = -1
        assimilated = -1
        assimilated_community = - 1
        assimilator_community = -1
        for k in range(0, noEdges):
                edge = edges[k]
                i = edges[k][0]
                j = edges[k][1]
                if communities_map[i] != communities_map[j]: # dc nu e si e[i][j] != 0
                    deltaQ = e[i][j]+ e[j][i] - 2*(a[i])*(a[j])
                    if deltaQ > maxDetlaQ:
                        maxDetlaQ = deltaQ
                        assimilator = i
                        assimilated = j
                        assimilator_community = communities_map[i]
                        assimilated_community = communities_map[j]

        a[assimilator] += a[assimilated]
        a[assimilator] -= e[assimilated][assimilator]
        #print(assimilated, assimilator)
        for k in range(0, noNodes):
            if communities_map[k] == assimilated_community:
                communities_map[k] = assimilator_community
            e[assimilator][k] += e[assimilated][k]
            e[assimilated][k] = 0
            e[k][assimilator] += e[k][assimilated]
            e[k][assimilated] = 0
        for k in range(0, noEdges):
            if edges[k][0] == assimilated:
                edges[k][0] = assimilator
            if edges[k][1] == assimilated:
                edges[k][1] = assimilator


        deltaQ = maxDetlaQ
        Q += deltaQ
        joins+=1
        cuts.append([communities_map.copy(), Q])
        #print(cuts[joins])
        #print(len(set(cuts[joins][0])))

    maxQ = -10
    final_map = []
    for cut in cuts:
        if cut[1] > maxQ:
            maxQ = cut[1]
            final_map = cut[0]
    #print(maxQ)
    #print(final_map)
    return final_map




#print(my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\karate\karate.gml"), 1))
#print(my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\krebs\krebs.gml")))
# print(newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\karate\karate.gml")))
# print(newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\dolphins\dolphins.gml")))
# print(newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\\football\\football.gml")))
# r = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\karate\\karate.gml"))
# print(r)
# print(len(set(r)))
#
# r2 = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\football\\football.gml"))
# print(r2)
# print(len(set(r2)))
#
# r2 = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\dolphins\\dolphins.gml"))
# print(r2)
# print(len(set(r2)))
#
# r2 = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\krebs\\krebs.gml"))
# print(r2)
# print(len(set(r2)))