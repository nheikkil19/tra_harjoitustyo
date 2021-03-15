# Kirjasto harjoitustyön funktioille


from math import floor

INF = float("inf")

class Edge:
    def __init__(self, node, weight):
        self.node = node        # Mihin solmuun viiva menee
        self.weight = weight

class Graph:
    def __init__(self, nV):
        self.nVert = nV
        self.edgeList = {}
        self.height = {}        # Kertoo matalimman reitin korkeuden kyseiseen kaupunkiin. 
        self.pred = {}
        self.vertices = []

        for i in range(1, self.nVert + 1):
            self.edgeList[i] = []
            # Alustetaan korkeus äärettömäksi, koska etsitään matalinta.
            self.height[i] = INF
            self.pred[i] = None
            self.vertices.append(i)

    def add_edge(self, x, y, weight):
        """ Lisää viivan x:n ja y:n välille painolla weight
        """
        # Lisätään reitti
        self.edgeList[x].append(Edge(y, weight))
        # Lisätään myös toiseen suuntaan, koska suuntaamaton graafi.
        self.edgeList[y].append(Edge(x, weight))

class minHeap:
    def __init__(self, names, priors):
        assert len(names) == len(priors)
        self.names = names
        self.priors = priors

    def min_heap(self):
        """ Järjestelee minimikeon
        """
        halfway = get_parent(len(self.names) - 1)
        for i in range(halfway, -1, -1):
            self.min_heapify(i)
       
    def min_heapify(self, i):
        """ Järjestelee kekoa annetusta juuresta
        """
        # Solmujen indeksit
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if right < len(self.names):      # Tarkastetaan, onko oikeanpuoleista lasta
            smallest = min(smallest, left, right, key=self.get_prior)
        
        elif left < len(self.names):     # Tarkastetaan, onko vasemmanpuoleista lasta
            smallest = min(smallest, left, key=self.get_prior)
        
        if smallest != i:
            self.switch(i, smallest)
            self.min_heapify(smallest)
    
    def get_prior(self, i):
        """ Palauttaa annetun indeksin alkion prioriteetin
        """
        return self.priors[self.names[i]]

    def switch(self, x, y):
        """ Vaihtaa alkioiden paikkaa
        """
        temp = self.names[x]
        self.names[x] = self.names[y]
        self.names[y] = temp

    def extract_min(self):
        """ Poistaa ja palauttaa pienimmän alkion nimen
        """
        assert len(self.names) > 0
        
        self.switch(0, len(self.names) - 1)
        min = self.names.pop()
        self.min_heapify(0)

        return min

    def raise_priority(self, x, prior):
        """ Nostaa alkion prioriteettiä / laskee reitin maksimikorkeutta.
            Muuttaa samalla graph.height-sanakirjan arvoja
        """
        assert prior <= self.priors[x]
        for i, key in enumerate(self.names):
            if key == x:
                self.priors[key] = prior
                # Järjestää keon uudestaan
                parent = get_parent(i)
                while parent != -1:
                    self.min_heapify(parent)
                    parent = get_parent(parent)

                break

def get_parent(i):
    """ Antaa annetun indeksin vanhemman.
    """
    assert i >= 0
    return floor(((i + 1) / 2) - 1)


def find_route(graph, start, end):
    """ Etsii reitin start-solmusta end-solmuun.
    """
    assert len(graph.vertices) > 1
    assert start != end
    # Aloitetaan annetusta kaupungista
    graph.height[start] = 0
    # Prioriteettijono toteutettu minimikeolla
    priority_Q = minHeap(graph.vertices, graph.height) 
    priority_Q.min_heap()
    lowest = priority_Q.extract_min()

    while lowest != end or not priority_Q:
        for edge in graph.edgeList[lowest]:
            # Katsotaan nouseeko reitin maksimikorkeus, kun väli kuljetaan.
            new_height = max(graph.height[lowest], edge.weight)
            # Tutkitaan, onko uusi reitti matalampi
            if new_height < graph.height[edge.node]:
                # Tallennetaan reitti kaupunkiin
                graph.pred[edge.node] = lowest
                # Nostetaan reitin prioriteettiä prioriteettijonossa
                priority_Q.raise_priority(edge.node, new_height)

        # Otetaan matalin reitti jonosta
        lowest = priority_Q.extract_min()

def print_route(graph, start, end):
    """ Tulostaa reitin start-solmusta end-solmuun. 
    """
    if graph.pred[end] == None:
        print("Ei ole reittiä kaupungista {} kaupunkiin {}.".format(start, end))
    
    else:
        # Tekee reitistä listan alkaen lopusta
        route = []
        node = end
        maxHeight = -INF
        while node != None:
            route.append(node)
            maxHeight = max(graph.height[node], maxHeight)
            node = graph.pred[node]
        
        print("Reitti kaupungista {} kaupunkiin {}:".format(start, end))
        for i in range(len(route) - 1, 0, -1):
            print("{:>5} ----> {:<5}".format(route[i], route[i - 1]))
        
        print("Reitin suurin korkeus: {}".format(maxHeight))
