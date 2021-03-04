import networkx as nx
import matplotlib.pyplot as plt

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
    G = nx.Graph()
    ctr = 0
    while ctr != -1:
        for row in li:
            row_list = row.rstrip("\n").split(" ")
            row_list = [int(i) for i in row_list]
            
            if ctr == 0:
                cities, roads = row_list[0], row_list[1]
                ctr += 1
            
            elif ctr == roads + 1:
                dest = row_list[0]
                ctr = -1

            else:
                G.add_edge(row_list[0], row_list[1], weight=row_list[2])
                ctr += 1
    
    return G

def draw_graph(G):
    options = {
    'node_color': 'green',
    'node_size': 400,
    'width': 2,
    'with_labels': True,
    'weight': True,
    }

    plt.subplot(111)
    nx.draw_kamada_kawai(G, **options)
    plt.show()

def main():
    data = read_file("graafi.txt")
    G = make_graph(data)
    
    draw_graph(G)


if __name__ == "__main__":
    main()