# Kirjasto harjoitustyön funktioille

from math import log2

INF = float("inf")
WHITE = 0
BLACK = 1


class Edge:
    def __init__(self, node, weight):
        self.node = node        # mihin solmuun viivaa pitkin päästään
        self.weight = weight    # viivan paino eli tien korkeus
        self.next = None 


class Graph:
    def __init__(self, nV):
        self.nVert = nV
        self.adjList = {}
        self.vertices = []
        for i in range(1, self.nVert + 1):
            self.adjList[i] = None
            self.vertices.append(i)
        
        # Kertoo matalimman reitin korkeuden kyseiseen solmuun eli kaupunkiin. 
        # Alustetaan äärettömäksi, koska etsitään matalinta.
        self.height = {}
        for i in range(1, self.nVert + 1):
            self.height[i] = INF
        
        # Kertoo solmujen edeltäjän.
        self.pred = {}
        for i in range(1, self.nVert + 1):
            self.pred[i] = None


def add_edge(graph, x, y, weight):
    """ Lisää viivan x: ja y:n välille painolla weight
    """
    # Lisätään reitti
    ed = graph.adjList[x]
    if ed == None:
        graph.adjList[x] = Edge(y, weight)
    else:
        while ed.next != None:
            ed = ed.next
        ed.next = Edge(y, weight)

    # Lisätään myös toiseen suuntaan, koska suuntaamaton graafi.
    ed = graph.adjList[y]
    if ed == None:
        graph.adjList[y] = Edge(x, weight)
    else:
        while ed.next != None:
            ed = ed.next
        ed.next = Edge(x, weight)

def print_edges(graph, x):
    """Tulostaa reunat tietystä pisteestä
    """
    y = graph.adjList[x]
    while y != None:
        print("EDGE:  ", x, "--", y.weight, "--", y.node)
        y = y.next

def dijkstra(graph, start, end):
    
    # Alustetaan värit valkoiseksi
    colors = {}
    for v in graph.vertices:
        colors[v] = WHITE

    Q = []

    lowest = start
    edge = graph.adjList[lowest]
    while lowest != end:

        while edge != None:
            # Käydään läpi kaikki välit, joita ei olla käyty = merkattu mustaksi
            if colors[edge.node] == WHITE:
                # Lisätään kohdekaupunki listaan, jos se ei ole siellä vielä.
                if not edge.node in Q:
                    Q.append(edge.node)
                # Päivitetään korkeus pienemmäksi, jos löytyy mahdollinen reitti
                if edge.weight < graph.height[edge.node]:
                    graph.height[edge.node] = edge.weight 
                graph.pred[edge.node] = lowest
            edge = edge.next
        colors[lowest] = BLACK          # Merkataan kaupunki käydyksi
        lowest = extract_min(graph, Q)  # Otetaan matalin reitti jonosta
        edge = graph.adjList[lowest]


def extract_min(graph, li):
    """Hakee listasta kaupungin, johon reitin korkeus on matalin. Palauttaa kaupungin numeron.
    """
    minheight = INF
    for e in li:
        if graph.height[e] < minheight:
            minheight = graph.height[e]
            min = e

    list.remove(min)
    return min

def min_heap(li):
    """Rakentaa minimikeon annetusta listasta.
    """
    halfway = int(len(li) / 2) - 1
    for i in range(halfway, -1, -1):
        min_heapify(li, i)

def min_heapify(li, i):
    """ Tähän jotain
    """
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if right < len(li):             # Tarkastetaan, onko oikeanpuoleista lasta
        if li[left] < li[right]:
            if li[left] < li[i]:
                smallest = left

        else:
            if li[right] < li[i]:
                smallest = right    
    
    elif left < len(li):
        if li[left] < li[i]:
                smallest = left
    
    if smallest != i:
        switch(li, i, smallest)
        min_heapify(li, smallest)


def switch(li, x, y):
    """ Vaihtaa alkioiden paikkaa listassa
    """
    temp = li[x]
    li[x] = li[y]
    li[y] = temp