from collections import deque

class Grafo:
    def __init__(self):
        self.nos = set()
        self.arestas = {}
        self.capacidades = {}
        self.tempo_arestas = {}
        self.tempo_nos = {}

    def adicionar_no(self, no, tempo_no=0):
        self.nos.add(no)
        self.tempo_nos[no] = int(tempo_no)

    def adicionar_aresta(self, origem, destino, capacidade, tempo):
        self.arestas[(origem, destino)] = 0  # Fluxo inicial
        self.capacidades[(origem, destino)] = int(capacidade)
        self.tempo_arestas[(origem, destino)] = int(tempo)

    def calcular_fluxo(self, origem, destino):
        fluxo_total = 0
        caminho = self.encontrar_caminho(origem, destino)

        while caminho:
            capacidade_minima = min(
                self.capacidades[(u, v)] - self.arestas[(u, v)] for u, v in caminho
            )

            for u, v in caminho:
                self.arestas[(u, v)] += capacidade_minima
                if (v, u) in self.arestas:  # Fluxo reverso
                    self.arestas[(v, u)] -= capacidade_minima
                else:
                    self.arestas[(v, u)] = -capacidade_minima
                self.capacidades[(v, u)] = 0

            fluxo_total += capacidade_minima
            caminho = self.encontrar_caminho(origem, destino)

        return fluxo_total

    def encontrar_caminho(self, origem, destino):
        visitados = {origem}
        fila = deque()
        fila.append((origem, []))

        while fila:
            no_atual, caminho = fila.popleft()

            for vizinho in self.nos:
                if (no_atual, vizinho) in self.arestas.keys():
                    cap = self.capacidades[(no_atual, vizinho)]
                    fluxo = self.arestas[(no_atual, vizinho)]
                    capacidade_residual = cap - fluxo
                    if capacidade_residual > 0 and vizinho not in visitados:
                        novo_caminho = caminho + [(no_atual, vizinho)]
                        if vizinho == destino:
                            return novo_caminho
                        fila.append((vizinho, novo_caminho))
                        visitados.add(vizinho)

        return None

    def calcular_tempo(self):
        
        tempo = 0

        for aresta, fluxo in self.arestas.items():
            if fluxo > 0:
                tempo += fluxo * self.tempo_arestas[aresta]

        for _, tempo in self.tempo_nos.items():
            tempo += tempo

        return tempo
