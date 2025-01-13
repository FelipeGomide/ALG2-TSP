import networkx as nx

from modules.utils import calculate_cost, remove_duplicates

def christofides(G):
    MST = nx.minimum_spanning_tree(G)

    # Lista de nós com lista de adjacência de tamanho ímpar
    odd_nodes = [x for x in MST.nodes if len(MST[x]) % 2 == 1]

    # Matching do Subgrafo Induzido
    odd = nx.induced_subgraph(G, odd_nodes)
    matching = nx.min_weight_matching(odd)

    # União da Árvore geradora com o matching
    MG = nx.MultiGraph()
    MG.add_edges_from(MST.edges)
    MG.add_edges_from(matching)

    # Circuito euleriano de Christofides
    circuit = list(nx.eulerian_circuit(MG))

    # Faço relaxação do circuito, removendo repetições de vértices
    tsp = remove_duplicates(circuit)

    cost = calculate_cost(G, tsp)
    return cost