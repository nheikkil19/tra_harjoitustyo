from mylib import *
from time import perf_counter
from random import randrange


if __name__ == "__main__":
    n = int(input("Give n: "))
    while n != -1:
        

        edges = []
        L = []
        H = []

        for _ in range(n):
            random = Edge(0, randrange(2 * n))
            edges.append(random)
        
        start = perf_counter()
        print("ADDING TO LIST...")
        for i in edges:
            L.append(i)
        add_list_time = perf_counter() - start

        start = perf_counter()
        print("ADDING TO HEAP...")
        for i in edges:
            heap_insert(H, i)
        add_heap_time = perf_counter() - start

        start = perf_counter()
        print("EXRACTING MIN FROM LIST...")
        for _ in range(n):
            extract_min(L)
        ext_list_time = perf_counter() - start

        start = perf_counter()
        print("EXTRACTING MIN FROM HEAP...")
        for _ in range(n):
            extract_min_heap(H)
        ext_heap_time = perf_counter() - start

        print("\nEXECUTION TIMES:")
        print("\nLIST ADD: {:.6} seconds".format(add_list_time))
        print("LIST EXT: {:.6} seconds".format(ext_list_time))
        print("LIST SUM: {:.6} seconds".format(add_list_time + ext_list_time))
        print("\nHEAP ADD: {:.6} seconds".format(add_heap_time))
        print("HEAP EXT: {:.6} seconds".format(ext_heap_time))
        print("HEAP SUM: {:.6} seconds".format(add_heap_time + ext_heap_time))


        n = int(input("\nGive n: "))


