def calculate_cost(G, relax):
    cost = 0
    for i in range(len(relax)-1):
        cost += G[relax[i]][relax[i+1]]['weight']
    return cost