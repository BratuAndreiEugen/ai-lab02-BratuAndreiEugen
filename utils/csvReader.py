import csv
import os

import networkx as nx
import numpy as np
import pandas as pd

from algorithm.just_newman import my_newman
from graphics.graphs import plotNetwork
from utils.gmlReader import reader


def readFromCsv(file_name):
    import csv

    node_number = 0
    edges_number = 0
    dict_nodes ={}

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            edges_number += 1
            if row[0] not in dict_nodes:
                dict_nodes[row[0]] = node_number
                node_number += 1
            if row[1] not in dict_nodes:
                dict_nodes[row[1]] = node_number
                node_number += 1

    matrix = [[0] * node_number for _ in range(node_number)]
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            node_i = dict_nodes[row[0]]
            node_j = dict_nodes[row[1]]
            matrix[node_j][node_i] = 1
            matrix[node_i][node_j] = 1

    net = {
        'noNodes': len(dict_nodes),
        'mat': matrix,
        'noEdges': edges_number,
    }

    a = np.array(net['mat'])
    g = nx.from_numpy_array(a)

    return g
n = readFromCsv("C:\Proiecte SSD\Python\lab2AI\\networks\\others\\book1.csv")
print(my_newman(n))
print(len(set(my_newman(n))))
plotNetwork(n, my_newman(n), "GAME OF THRONES : " + str(len(set(my_newman(n)))))

n = reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\astro.gml")
rez = my_newman(n)
plotNetwork(n, rez, "ASTRO " + str(len(set(rez))))