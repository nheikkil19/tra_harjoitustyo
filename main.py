# TIETORAKENTEET JA ALGORITMIT -KURSSIN HARJOITUSTYÖ 2020
# Niko Heikkilä     ***REMOVED*** 

from mylib import *
from time import perf_counter
import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Give filename: ")
    
    try:
        G, dest = read_graph(filename)
    except FileNotFoundError:
        print("File not found!")
        quit()

    find_route(G, 1, dest)
    print_route(G, 1, dest)


def read_graph(filename):
    """ Lukee tiedoston ja tekee siitä graafin. Palauttaa graafin ja kohdekaupungin
    """
    with open(filename) as f:
        for i, row in enumerate(f):
            row_list = row.rstrip("\n").split(" ")
            row_list = [int(i) for i in row_list]

            if i == 0:
                cities, roads = row_list[0], row_list[1]
                G = Graph(cities)

            elif i == roads + 1:
                dest = row_list[0]
                break
            else:
                G.add_edge(row_list[0], row_list[1], row_list[2])
    
    return G, dest


if __name__ == "__main__":

    # start = perf_counter()
    main()
    # end = perf_counter()
    # print("Execution time: {:6f} seconds".format(end - start))
