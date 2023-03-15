# plot a network
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from algorithm.just_newman import my_newman
from utils.gmlReader import reader


def plotNetwork(network, communities = [1, 1, 1, 1, 1, 1], name = "ANY"):
    np.random.seed(123) #to freeze the graph's view (networks uses a random view)
    A=nx.to_numpy_array(network)
    G=network
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=50, cmap=plt.cm.RdYlBu, node_color = communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.title(name)
    plt.show()

def printResultGraphics():
    r = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\karate\\karate.gml"))
    print("KARATE " + str(len(set(r))))
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\karate\\karate.gml"),r, "KARATE "+ str(len(set(r))))
    r = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\dolphins\\dolphins.gml"))
    print("DOLPHINS " + str(len(set(r))))
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\dolphins\\dolphins.gml"), r, "DOLPHINS " + str(len(set(r))))
    r = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\football\\football.gml"))
    print("FOOTBALL " + str(len(set(r))))
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\football\\football.gml"), r,  "FOOTBALL " + str(len(set(r))))
    r = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\krebs\\krebs.gml"))
    print("KREBS " + str(len(set(r))))
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\krebs\\krebs.gml"), r, "KREBS " + str(len(set(r))))

    # TESTELE MELE
    print("TEST 1 ( ChatGPT generated )")
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test1.gml"), my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test1.gml")), "CHATGPT GENERATED")
    print("TEST 2 ( Les Miserables )")
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test2.gml"), my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test2.gml")), "LES MISERABLES")
    print("TEST 3 ( Co-authorships in network science )")
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test3.gml"), my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test3.gml")), "CO-AUTORSHIPS IN NETWORK SCIENCE")
    print("TEST 4 ( Neural network )")
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test4.gml"), my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test4.gml")), "NEURAL NETWORK")
    print("TEST 5 ( Political blogs )")
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test5.gml"), my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test5.gml")), "POLITICAL BLOGS")
    print("TEST 6 ( World adjacencies )")
    plotNetwork(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test6.gml"), my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test6.gml")), "WORLD ADJACENCIES")

