import tsplib95 as tsp

from modules.TaT import twice_around_tree
from modules.Christofides import christofides

import sys
import time
import tracemalloc

def main():
    method = sys.argv[1]
    file = sys.argv[2]
    #print("File name:", file)

    start_time = time.time()

    # Importo o problema e crio o grafo como instância Networkx
    problem = tsp.load(file)
    G = problem.get_graph() 

    graph_time = time.time()
    #print(f"Criação do grafo:\t {graph_time - start_time:.4f}s")

    tracemalloc.start()

    match(method):
        case "-t": #Twice-around-the-tree
            result = twice_around_tree(G)
        case "-b": # Branch-and-Bound
            raise NotImplementedError
        case "-c": # Christofides
            result = christofides(G)

    end_time = time.time()

    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(peak)

    # print(end_time - graph_time)
    # print(result)

main()
