import heapq
import numpy as np

from modules.utils import calculate_cost

def bound(G, path):
    cost = 0

    cost = calculate_cost(G, path)

    for start in G.nodes:
        edges = []
        if start not in path:
            for end in G.nodes:
                if end != start:
                    edges.append(G[start][end]['weight'])
            m = min(edges)
            cost += m
            edges.remove(m)
            cost += min(edges)

    return np.ceil(cost/2)

def queue_bnb(G):
    best = calculate_cost(G, [x for x in G])
    print(best)

    b = bound(G, [1]) 
    queue = [(b, [1])]

    while queue:
        b, path = heapq.heappop(queue)
        
        if b > best:
            break

        if len(path) == len(G):
            cost = calculate_cost(G, path + [1])
            if cost < best:
                best = cost
                print(best)
                print(path)

        elif b < best:
            if len(path) < len(G):
                for i in G:
                    b = bound(G, path + [i])
                    if i not in path and b < best:
                        heapq.heappush(queue, (b, path + [i]))

    return best


best = 0

def rec_bnb(G):
    global best
    best = calculate_cost(G, [x for x in G])
    print("First solution:", best)

    search = recursive_bnb(G, [1])
    if search == -1:
        return best
    return search
    
def recursive_bnb(G, path):
    global best, heigth
    b = bound(G, path)

    if b > best:
        return -1

    if (len(path) == len(G.nodes)):
        cost = calculate_cost(G, path + [1])
        if cost < best:
            best = cost
            print("New best:", best)
            return cost
        return -1

    answers = []
    for i in G:
        if i not in path:
            answers.append(recursive_bnb(G, path + [i]))
    
    positives = [x for x in answers if x > 0]

    local_best = -1

    if len(positives) > 0:
        local_best = min(positives)

    return local_best


# Opção alternativa, executar o arquivo
# Cria uma instância menor do problema para ser executado
# ~ python BnB.py <qtd_vertices> <método: 'queue', 'recursive'>
if __name__ == "__main__":
    import tsplib95
    import networkx as nx
    import sys

    import tracemalloc

    qtd = int(sys.argv[1])
    method = sys.argv[2]

    problem = tsplib95.load('../data/small/berlin52.tsp')
    G = problem.get_graph()

    for i in range(qtd+1, 53):
        G.remove_node(i)
    
    if method == "queue":
        print(queue_bnb(G))
    else:
        print(rec_bnb(G))

    