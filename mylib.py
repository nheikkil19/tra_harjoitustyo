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
GRAY = 1
BLACK = 2


class Edge:
    def __init__(self, node, weight):
        self.node = node        # mihin solmuun viivaa pitkin päästään
        self.weight = weight    # viivan paino eli tien korkeus
        self.color = WHITE
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

    def add_edge(self, x, y, weight):
        """ Lisää viivan x:n ja y:n välille painolla weight
        """
        # Lisätään reitti
        ed = self.edgeList[x]
        if ed == None:
            self.edgeList[x] = Edge(y, weight)
        else:
            while ed.next != None:
                ed = ed.next
            ed.next = Edge(y, weight)

        # Lisätään myös toiseen suuntaan, koska suuntaamaton graafi.
        ed = self.edgeList[y]
        if ed == None:
            self.edgeList[y] = Edge(x, weight)
        else:
            while ed.next != None:
                ed = ed.next
            ed.next = Edge(x, weight)

class minHeap:
    def __init__(self):
        self.list = []

    
    def insert(self, x, pr):
        """Lisää kekoon alkion x prioriteetillä pr.

        """
        self.list.append({"key": x, "prior": pr})
        
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
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if right < len(self.list):             # Tarkastetaan, onko oikeanpuoleista lasta
            if self.list[left]["prior"] < self.list[right]["prior"]:
                if self.list[left]["prior"] < self.list[i]["prior"]:
                    smallest = left

            else:
                if self.list[right]["prior"] < self.list[i]["prior"]:
                    smallest = right    
        
        elif left < len(self.list):
            if self.list[left]["prior"] < self.list[i]["prior"]:
                    smallest = left
        
        if smallest != i:
            self.switch(i, smallest)
            self.min_heapify(smallest)
    

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
        self.min_heapify(0)

        return min["key"]


def get_parent(x):
    """ Antaa annetun indeksin vanhemman.
    """
    assert x >= 0
    return floor(((x + 1) / 2) - 1)


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
    priority_Q = minHeap() 
    # Aloitetaan annetusta kaupungista
    lowest = start
    graph.height[lowest] = -INF

    while lowest != end:

        edge = graph.edgeList[lowest]

        while edge != None:
            # Käydään läpi kaikki välit, joita ei olla löydetty
            if graph.colors[edge.node] != BLACK:
                
                if graph.colors[edge.node] == WHITE:
                    # Katsotaan nouseeko reitin maksimikorkeus, kun väli kuljetaan.
                    if graph.height[lowest] > edge.weight:
                        higher = graph.height[lowest]
                    else:
                        higher = edge.weight
                    
                    # Tutkitaan, onko uusi reitti matalampi
                    if higher < graph.height[edge.node]:
                        graph.height[edge.node] = higher

                        # Tallennetaan reitti kaupunkiin
                        graph.pred[edge.node] = lowest

                    # Lisätään kohdekaupunki tutkittavien listaan
                    priority_Q.insert(edge.node, graph.height[edge.node])
                    # priority_Q.append(edge.node)
                    # Merkataan kohde löydetyksi
                    graph.colors[edge.node] = GRAY
                
                else: 
                    # FIND FROM HEAP WITH KEY
                    # CHECK THE PRIORITY
                    # IF NEW IS LOWER, CHANGE AND ARRANGE
            
            # Valitaan seuraava väli
            edge = edge.next

        # Merkataan kaupunki tutkituksi
        graph.colors[lowest] = BLACK   
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

    route = [end]
    pred = graph.pred[end]
    while pred != None:
        route.append(pred)
        pred = graph.pred[pred]
    
    maxHeight = -INF
    print("Reitti kaupungista {} kaupunkiin {}:".format(start, end))
    for i in range(len(route) - 1, 0, -1):
        print("{}--{}".format(i, i - 1))
        if maxHeight < graph.edgeList:
            print("Reitin suurin korkeus: {}".format(maxHeight))