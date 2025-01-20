import random

class Aresta_Info:
    def __init__(self, cap, prob):
        self.cap = float(cap)
        self.fluxo = 0
        self.prob = float(prob)
    
    def setFluxo(self, fluxo):
        if fluxo > self.cap:
            return
        
        self.fluxo = fluxo

class Vertice_Info:
    def __init__(self, suprimentos, demanda):
        self.suprimentos = float(suprimentos)
        self.demanda = float(demanda)
        
class Grafo:
    
    _rotulos = []
    _lista_adj : dict[str, list[str]] = {}
    _vertices: dict[str, Vertice_Info] = {}
    _arestas : dict[tuple[str, str], Aresta_Info] = {}
    
    def __init__(self):
        pass
    
    def adicionar_vertice(self, rotulo, suprimentos, demanda):
        if rotulo in self._rotulos:
            return False
        
        self._rotulos.append(rotulo)
        self._lista_adj[rotulo] = []
        self._vertices[rotulo] = Vertice_Info(suprimentos, demanda)
        
        return True
    
    def adicionar_aresta(self, v1, v2, cap, prob):
        if v1 not in self._rotulos or v2 not in self._rotulos:
            return False
        
        if v2 in self._lista_adj[v1]:
            self._arestas[(v1, v2)] = Aresta_Info(cap, prob)
            return False
        
        self._lista_adj[v1].append(v2)
        self._arestas[(v1, v2)] = Aresta_Info(cap, prob)
        return True
    
    def simular_bloqueio(self):
        bloqueios = []
        
        for (v1, v2), aresta_info in self._arestas.items():
            random_value = random.uniform(0, 1)  # Gera um número aleatório entre 0 e 1
            if random_value < aresta_info.prob:  # Compara com a probabilidade de bloqueio
                bloqueios.append((v1, v2))
        
        for pair in bloqueios:
            self._arestas.pop(pair)
            self._lista_adj[pair[0]].remove(pair[1])
    
    def __str__(self):
        texto = ""
        
        for rotulo in self._rotulos:
            texto += f"{rotulo}: {self._lista_adj[rotulo]}\n"
        
        return texto
        
        
                
