# Tehtävä:
# - sovellus joka etsii parhaan (matalimman) reitin verkosta
# - Dijkstran algoritmilla muokattu versio
# Ongelma osissa:
# - tiedoston luku
# - verkko-tietorakenne
# - reitinetsintäalgoritmi (Dijkstra?)
# - UI
from mylib import *



if __name__ == "__main__":
    
    # Tiedoston luku
    filename = "graafi.txt"
    with open(filename) as f:
        ctr = 0
        while ctr != -1:
            for row in f:
                row_list = row.rstrip("\n").split(" ")
                row_list = [int(i) for i in row_list]
                if ctr == 0:
                    cities, roads = row_list[0], row_list[1]
                    g = Graph(cities)
                    ctr += 1
                elif ctr == roads + 1:
                    dest = row_list[0]
                    ctr = -1
                else:
                    add_edge(g, row_list[0], row_list[1], row_list[2])
                    ctr += 1


    dijkstra(g, 1, dest)

    
    print(g.pred)