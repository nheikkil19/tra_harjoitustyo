# Kirjasto harjoitustyön funktioille

# TODO:
# ASSERTIT
# PARANTAA DOKUMENTAATIOTA
# PRIORITEETTIJONO KUNTOON
#   - KUMPI TAPA ON PAREMPI
# FORMATOIDA KOODIA
# KIRJOTTAA ANALYYSI
# JÄRJESTELLÄ FUNKTIOT OIKEIN
# GRAAFIN LUKU MAIN TIEDOSTOSSA
# MIKÄ ALGORITMI, DIJIKSJTRA VAI LEVEYSHAKU
# TULOSTAA PARHAAN REITIN TAI ETTEI REITTIÄ OLE

from math import floor

INF = float("inf")

class Edge:
    def __init__(self, node, weight):
        self.node = node        # mihin solmuun viivaa pitkin päästään
        self.weight = weight    # viivan paino eli tien korkeus


class Graph:
    def __init__(self, nV):
        self.nVert = nV
        self.edgeList = {}
        self.height = {}        # Kertoo matalimman reitin korkeuden kyseiseen kaupunkiin. 
        self.pred = {}          # Kertoo solmujen edeltäjän.
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
    def __init__(self, li=[], priors={}):
        assert len(li) == len(priors)
        self.list = li
        self.priors = priors
    
    def insert(self, x, pr):
        """Lisää kekoon alkion x prioriteetillä pr
        """
        self.list.append(x)
        self.priors.append(pr)
        
        # Järjestele juuret alhaalta
        parent = get_parent(len(self.list) - 1)
        while parent != -1:
            self.min_heapify(parent)
            parent = get_parent(parent)

    def min_heap(self):
        """ Järjestelee minimikeon
        """
        halfway = get_parent(len(self.list) - 1)
        for i in range(halfway, -1, -1):
            self.min_heapify(i)
       
    def min_heapify(self, i):
        """ Järjestelee kekoa annetusta juuresta
        """
        # Solmujen indeksit
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if right < len(self.list):      # Tarkastetaan, onko oikeanpuoleista lasta
            smallest = min(smallest, left, right, key=self.get_prior)
        
        elif left < len(self.list):     # Tarkastetaan, onko vasemmanpuoleista lasta
            smallest = min(smallest, left, key=self.get_prior)
        
        if smallest != i:
            self.switch(i, smallest)
            self.min_heapify(smallest)
    
    def get_prior(self, i):
        """ Palauttaa annetun indeksin alkion prioriteetin
        """
        return self.priors[self.list[i]]

    def switch(self, x, y):
        """ Vaihtaa alkioiden paikkaa
        """
        temp = self.list[x]
        self.list[x] = self.list[y]
        self.list[y] = temp

    def extract_min(self):
        """ Poistaa ja palauttaa minimin avaimen
        """
        assert len(self.list) > 0
        
        self.switch(0, len(self.list) - 1)
        min = self.list.pop()
        # self.priors.popitem()
        self.min_heapify(0)

        return min

    def lower_priority(self, x, prior):
        """ Laskee alkion prioriteettiä
        """

        for i, key in enumerate(self.list):
            if key == x:
                assert prior <= self.priors[key]
                self.priors[key] = prior

                # Järjestää keon uudestaan
                parent = get_parent(i)
                while parent != -1:
                    self.min_heapify(parent)
                    parent = get_parent(parent)

                break


def get_parent(x):
    """ Antaa annetun indeksin vanhemman.
    """
    assert x >= 0
    return floor(((x + 1) / 2) - 1)


def find_route(graph, start, end):
    """ Etsii leveyshaun avulla reitin start-nodesta end-nodeen
    """

    # Aloitetaan annetusta kaupungista
    graph.height[start] = 0
    # Alustetaan prioriteettijono
    priority_Q = minHeap(graph.vertices, graph.height) 
    priority_Q.min_heap()
    lowest = priority_Q.extract_min()

    while lowest != end:
        for edge in graph.edgeList[lowest]:

            # Katsotaan nouseeko reitin maksimikorkeus, kun väli kuljetaan.
            new_height = max(graph.height[lowest], edge.weight)
                
            # Tutkitaan, onko uusi reitti matalampi
            if new_height < graph.height[edge.node]:
                # graph.height[edge.node] = new_height

                # Tallennetaan reitti kaupunkiin
                graph.pred[edge.node] = lowest

                # Lasketaan reitin korkeutta prioriteettijonossa
                priority_Q.lower_priority(edge.node, new_height)

        # Otetaan matalin reitti jonosta         
        lowest = priority_Q.extract_min()
        

def extract_min(li):
    """Hakee listasta kaupungin, johon reitin korkeus on matalin. Palauttaa kaupungin numeron.
    """
    minweight = INF
    for e in li:
        if e.weight < minweight:
            minweight = e.weight
            min = e

    li.remove(min)
    return min

def print_route(graph, start, end):
    """ Tulostaa reitin start-nodesta end-nodeen. 
    """
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
        print("{}--{}".format(route[i], route[i - 1]))
    
    print("Reitin suurin korkeus: {}".format(maxHeight))

def print_edges(graph, x):
    """Tulostaa reunat tietystä pisteestä
    """
    y = graph.edgeList[x]
    while y != None:
        print("EDGE:  ", x, "--", y.weight, "--", y.node)
        y = y.next