import networkx as nx

from modules.utils import calculate_cost

def twice_around_tree(graph):
    MST = nx.minimum_spanning_tree(graph)

    traversal = list(nx.dfs_edges(MST, source=1))

    # Seleciono somente o vértice descoberto a cada passo da DFS
    relax = list(map(lambda x: x[1], traversal))
    # Coloco 
    relax.insert(0, 1)
    relax.append(1)

    return calculate_cost(graph, relax)