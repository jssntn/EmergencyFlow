from grafo import Grafo

grafo = Grafo()

# Função para carregar o grafo a partir do arquivo network.txt
def carregar_grafo(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        if len(parts) == 1:  # Vértice
            grafo.adicionar_vertice(parts[0])
        elif len(parts) == 5:  # Aresta
            grafo.adicionar_aresta(parts[0], parts[1], parts[2], parts[3], parts[4])


# Carregando os dados do arquivo
carregar_grafo('network.txt')

print(grafo)
