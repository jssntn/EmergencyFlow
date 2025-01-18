class Aresta_Info:
    def __init__(self, cap, cost, prob):
        self.cap = cap
        self.cost = cost
        self.prob = prob

class Grafo:
    
    _rotulos = []
    _lista_adj : dict[str, list[str]] = {}
    _arestas : dict[tuple[str, str], tuple[int, int, float]] = {}
    
    def __init__(self):
        pass
    
    def adicionar_vertice(self, rotulo):
        if rotulo in self._rotulos:
            return False
        
        self._rotulos.append(rotulo)
        
        self._lista_adj[rotulo] = []
        
        return True
    
    def adicionar_aresta(self, v1, v2, cap, cost, prob):
        if v1 not in self._rotulos or v2 not in self._rotulos:
            return False
        
        if v2 in self._lista_adj[v1]:
            self._arestas[(v1, v2)] = (cap, cost, prob)
            return False
        
        self._lista_adj[v1].append(v2)
        self._arestas[(v1, v2)] = Aresta_Info(cap, cost, prob)
        return True
    
    def __str__(self):
        texto = ""
        
        for rotulo in self._rotulos:
            texto += f"{rotulo}: {self._lista_adj[rotulo]}\n"
        
        return texto
        
        
                
