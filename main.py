# Tehtävä:
# - sovellus joka etsii parhaan (matalimman) reitin verkosta
# - Dijkstran algoritmilla muokattu versio
# Ongelma osissa:
# - tiedoston luku
# - verkko-tietorakenne
# - reitinetsintäalgoritmi (Dijkstra?)
# - UI
from mylib import *
from time import perf_counter

def main():
    # start_time = perf_counter()
    data = read_file("graph_large_testdata/graph_ADS2018_2000.txt")
    # data = read_file("graafi.txt")
    # data_time = perf_counter()
    G, dest = make_graph(data)
    # graph_time = perf_counter()
    find_route(G, 1, dest)
    # route_time = perf_counter()
    print_route(G, 1, dest)

    # print("Data time: {:6f} seconds".format(data_time - start_time))
    # print("Grph time: {:6f} seconds".format(graph_time - data_time))
    # print("Rout time: {:6f} seconds".format(route_time - graph_time))
    # print("Tota time: {:6f} seconds".format(route_time - start_time))



def read_file(filename):
    """ Lukee tiedoston ja palautaa sen listana riveistä
    """
    data = []
    with open(filename) as f:
        for row in f:
            data.append(row)
    
    return data

def make_graph(li):
    """ Tekee listasta graafin
    """
    
    ctr = 0
    while ctr != -1:
        for row in li:
            row_list = row.rstrip("\n").split(" ")
            row_list = [int(i) for i in row_list]
            
            if ctr == 0:
                cities, roads = row_list[0], row_list[1]
                G = Graph(cities)
                ctr += 1

            elif ctr == roads + 1:
                dest = row_list[0]
                ctr = -1

            else:
                G.add_edge(row_list[0], row_list[1], row_list[2])
                ctr += 1
    
    return G, dest


if __name__ == "__main__":

    start = perf_counter()
    main()
    end = perf_counter()
    print("Execution time: {:6f} seconds".format(end - start))