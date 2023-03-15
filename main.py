from colorama import init
from termcolor import colored

from algorithm.girvan_newman import my_girvan_newman
from algorithm.just_newman import newman, my_newman
from graphics.graphs import printResultGraphics
from utils.gmlReader import converter, reader

def printResults():
    init()
    print("Rezultatele pentru testele date : ")
    print("\nKARATE")
    print("Numar aproximat : 2")
    r1 = newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\\karate\\karate.gml"))
    print([list(x) for x in r1])

    print("Numar comunitati : " + str(len(r1)))
    print(colored("-- CU ALGORITMUL MEU --", "red"))
    r1m = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\karate\\karate.gml"), 1)
    print(r1m)
    print("Numar comunitati : " + str(len(set(r1m))))

    print("\nFOOTBALL")
    print("Numar aproximat : 12")
    r2 = newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\\football\\football.gml"))
    print([list(x) for x in r2])

    print("Numar comunitati : " + str(len(r2)))
    print(colored("-- CU ALGORITMUL MEU --", "red"))
    r2m = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\football\\football.gml"), 0)
    print(r2m)
    print("Numar comunitati : " + str(len(set(r2m))))

    print("\nDOLPHINS")
    print("Numar aproximat : 2")
    r3 = newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\\dolphins\\dolphins.gml"))
    print([list(x) for x in r3])

    print("Numar comunitati : " + str(len(r3)))
    print(colored("-- CU ALGORITMUL MEU --", "red"))
    r3m = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\dolphins\\dolphins.gml"))
    print(r3m)
    print("Numar comunitati : " + str(len(set(r3m))))

    print("\nKREBS")
    print("Numar aproximat : 3")
    r4 = newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\\krebs\\krebs.gml"))
    print([list(x) for x in r4])

    print("Numar comunitati : " + str(len(r4)))
    print(colored("-- CU ALGORITMUL MEU --", "red"))
    r4m = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\krebs\\krebs.gml"))
    print(r4m)
    print("Numar comunitati : " + str(len(set(r4m))))

    print("\nRezultate pentru testele mele : ")
    i = 1
    aproximari = [3, 0, 0, 0, 0, 0]
    while i <= 6:
        print("\nTEST " + str(i))
        print("Numar aproximat : " + str(aproximari[i - 1]))
        r = 0
        r = newman(converter("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test" + str(i) + ".gml"))
        print([list(x) for x in r])
        print("Numar comunitati : " + str(len(r)))
        print("--")

        print(colored("-- CU ALGORITMUL MEU --", "red"))
        rm = my_newman(reader("C:\Proiecte SSD\Python\lab2AI\\networks\\myNetworks\\test" + str(i) + ".gml"), 0)
        print(rm)
        print("Numar comunitati : " + str(len(set(rm))))


        i += 1

def printResultGraphs():
    printResultGraphics()

if __name__ == '__main__':
    #printResults()
    printResultGraphs()

