def calculate_cost(G, relax):
    cost = 0
    for i in range(len(relax)-1):
        cost += G[relax[i]][relax[i+1]]['weight']

    return cost

def remove_duplicates(circuit):
    nodes = []
    nodes.append(circuit[0][0])

    for edge in circuit:
        if edge[1] not in nodes:
            nodes.append(edge[1])

    nodes.append(nodes[0])
    
    return nodes