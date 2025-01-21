from grafo import Grafo
from EmergencyNetwork import example_usage

example_usage()
# grafo = Grafo()
#
# f = open("network.txt", "r")
#
# for line in f.readlines():
#     parts = line.split()
#     if len(parts) == 2:
#         grafo.adicionar_no(*parts)
#     elif len(parts) == 4:
#         grafo.adicionar_aresta(*parts)
#
#
# print(grafo.calcular_fluxo("vs", "vt"))
#
# print(grafo.calcular_tempo())