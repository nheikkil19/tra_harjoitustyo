# Kirjasto harjoitustyön funktioille

INF = float("inf")

class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
        self.next = None

        
        

class Graph:
    def __init__(self, nV):
        self.nVert = nV
        self.adjList = {}
        self.vertices = []
        for i in range(1, self.nVert + 1):
            self.adjList[i] = None
            self.vertices.append(i)
        
        self.dist = {}
        for i in range(1, self.nVert + 1):
            self.dist[i] = INF
        
        self.pred = {}
        for i in range(1, self.nVert + 1):
            self.pred[i] = None


def add_edge(graph, x, y, weight):
    nd = graph.adjList[x]
    if nd == None:
        graph.adjList[x] = Edge(y, weight)
    else:
        while nd.next != None:
            nd = nd.next
        nd.next = Edge(y, weight)

    nd = graph.adjList[y]
    if nd == None:
        graph.adjList[y] = Edge(x, weight)
    else:
        while nd.next != None:
            nd = nd.next
        nd.next = Edge(x, weight)

def print_edges(graph, x):
    y = graph.adjList[x]
    while y != None:
        print("EDGE:  ", x, "--", y.weight, "--", y.node)
        y = y.next