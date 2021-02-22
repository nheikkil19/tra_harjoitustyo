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
WHITE = 0
GREY = 1
BLACK = 2


class Edge:
    def __init__(self, node, weight):
        self.node = node        # mihin solmuun viivaa pitkin päästään
        self.weight = weight    # viivan paino eli tien korkeus
        self.next = None 


class Graph:
    def __init__(self, nV):
        self.nVert = nV
        self.edgeList = {}
        self.vertices = []
        self.height = {}        # Kertoo matalimman reitin korkeuden kyseiseen kaupunkiin. 
        self.pred = {}          # Kertoo solmujen edeltäjän.
        self.colors = {}

        for i in range(1, self.nVert + 1):
            self.edgeList[i] = None
            self.vertices.append(i)
            # Alustetaan äärettömäksi, koska etsitään matalinta.
            self.height[i] = INF        
            self.pred[i] = None
            self.colors[i] = WHITE

def add_edge(graph, x, y, weight):
    """ Lisää viivan x:n ja y:n välille painolla weight
    """
    # Lisätään reitti
    ed = graph.edgeList[x]
    if ed == None:
        graph.edgeList[x] = Edge(y, weight)
    else:
        while ed.next != None:
            ed = ed.next
        ed.next = Edge(y, weight)

    # Lisätään myös toiseen suuntaan, koska suuntaamaton graafi.
    ed = graph.edgeList[y]
    if ed == None:
        graph.edgeList[y] = Edge(x, weight)
    else:
        while ed.next != None:
            ed = ed.next
        ed.next = Edge(x, weight)

def print_edges(graph, x):
    """Tulostaa reunat tietystä pisteestä
    """
    y = graph.edgeList[x]
    while y != None:
        print("EDGE:  ", x, "--", y.weight, "--", y.node)
        y = y.next

def find_route(graph, start, end):
    """ Etsii leveyshaun avulla reitin start-nodesta end-nodeen
    """

    # Alustetaan värit valkoiseksi
    for v in graph.vertices:
        graph.colors[v] = WHITE

    # Prioriteettijono perustuu listaan
    priority_Q = []

    lowest = start
    
    while lowest != end:

        edge = graph.edgeList[lowest]

        while edge != None:
            # Käydään läpi kaikki välit, joita ei olla löydetty
            if graph.colors[edge.node] != BLACK:
                if graph.colors[edge.node] == WHITE:
                    # Lisätään kohdekaupunki prioriteettijonoon
                    heap_insert(priority_Q, edge)
                    # priority_Q.append(edge.node)
                    graph.colors[edge.node] = GREY  # Merkataan kaupunki löydetyksi
                
                # Päivitetään korkeus pienemmäksi, jos löytyy mahdollinen reitti
                if graph.height[lowest] < graph.height[edge.node] and edge.weight < graph.height[edge.node]:
                    graph.height[edge.node] = edge.weight
                    graph.pred[edge.node] = lowest
            edge = edge.next
        
        graph.colors[lowest] = BLACK            # Merkataan kaupunki tutkituksi
        lowest = priority_Q.pop(0).node         # Otetaan matalin reitti jonosta
        



def min_heap(li):
    """Rakentaa minimikeon annetusta listasta.
    """
    halfway = get_parent(len(li) - 1)
    for i in range(halfway, -1, -1):
        min_heapify(li, i)

def min_heapify(li, i):
    """ Järjestelee kekoa annetusta juuresta
    """
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if right < len(li):             # Tarkastetaan, onko oikeanpuoleista lasta
        if li[left].weight < li[right].weight:
            if li[left].weight < li[i].weight:
                smallest = left

        else:
            if li[right].weight < li[i].weight:
                smallest = right    
    
    elif left < len(li):
        if li[left].weight < li[i].weight:
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

def heap_insert(li, x):
    """Lisää kekoon alkion
    """
    li.append(x)
    
    # Järjestele juuret alhaalta
    parent = get_parent(len(li) - 1)
    while parent != -1:
        min_heapify(li, parent)
        parent = get_parent(parent)

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

def extract_min_heap(li):
    """ Poistaa ja palauttaa minimin keosta
    """
    switch(li, 0, len(li) - 1)
    min = li.pop()
    min_heapify(li, 0)

    return min.node

def get_parent(x):
    """ Antaa annetun indeksin vanhemman.
    """
    assert x >= 0
    return floor(((x + 1) / 2) - 1)