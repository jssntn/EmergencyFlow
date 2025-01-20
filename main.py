from grafo import Grafo

grafo = Grafo()

# Função para carregar o grafo a partir do arquivo network.txt
def carregar_grafo(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        if len(parts) == 3:  # Vértice
            grafo.adicionar_vertice(*parts)
        elif len(parts) == 4:  # Aresta
            grafo.adicionar_aresta(*parts)


# Carregando os dados do arquivo
carregar_grafo('network.txt')

print("ANTES\n", grafo)

grafo.simular_bloqueio()

print("\nDEPOIS\n", grafo)
