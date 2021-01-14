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
    # filename = "graafi.txt"
    # with open(filename) as f:
    #     for row in f:
    #         print(row.rstrip("\n").split(" "))

    g = Graph(4)

    add_edge(g, 1, 2, 7)
    add_edge(g, 1, 3, 5)
    add_edge(g, 1, 4, 3513)
    add_edge(g, 2, 4, 313)
    add_edge(g, 3, 4, 123)

    print_edges(g, 4)