# Dijkstra's (/ˈdaɪkstrəz/) algorithm 
# is an algorithm for finding the shortest paths between nodes in a weighted graph.


# create a dictionary which will serve as a weighted graph
graph = {}
graph['start'] = {'a': 6, 'b': 2}
graph['a'] = {'finish': 1}
graph['b'] = {'a': 3, 'finish': 5}
graph['finish'] = {}
print(f'Graph: {graph}')

# create a dictionary which will handle sum of weights for each node of the graph
# (sum of weights from the start node)
infinity = float('inf')
weights = {}
weights['a'] = 6
weights['b'] = 2
weights['finish'] = infinity
print(f'Weights: {weights}')

# create a dictionary for storing information about parent node
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['finish'] = None
print(f'Parent nodes: {parents}')

# create a list for storing already processed nodes to avoid double check
processed = []


# create function which will search for a neighbor node with a lowest weight
def find_lowest_weight_node(list_of_weights, processed):
    """First step of Dijkstra's algorithm:
     finding a neighbor node with a lowest weight."""
    # at the beginning the lowest weight is unknown,
    # so it is an infinite number
    lowest_weight = float('inf')
    # at the beginning the node with a lowest weight is unknown
    # so it is None
    lowest_weight_node = None
    # check the weight of each node
    for node in list_of_weights:
        weight = list_of_weights[node]
        # if the weight is less than lowest weight
        # update the lowest weight and lowest_weight_node variables
        if weight < lowest_weight and node not in processed:
            lowest_weight = weight
            lowest_weight_node = node
    return lowest_weight_node


# create function which will return the shortest path
# from the start to the end of the graph
def find_shortest_path(graph, weights, parents, processed):
    """Second step of Dijkstra's algorithm:
     for found node with a lowest weight 
     check weight of its neighbors and find the lowest one."""
    # check all yet unprocessed nodes
    while len(processed) < len(weights.keys()):
        # find the neighbor node with the lowest weight
        node = find_lowest_weight_node(weights, processed)
        # find the weight of the node
        weight = weights[node]
        # find the neighbors of the node
        neighbors = graph[node]
        # count the total weight of edges 
        # from the start to each neighbor of the current node
        for n in neighbors.keys():
            new_weight = weight + neighbors[n]
            # if there is a shorter path,
            # update lowest weight info in 'weights'
            if weights[n] > new_weight:
                weights[n] = new_weight
                parents[n] = node
        # mark the node as processed
        processed.append(node)
    return f"Lowest weights: {weights},\nShortest path weight: {weights['finish']}\n--------------------"     


# have fun and find the shortest path
print(find_shortest_path(graph, weights, parents, processed))

# SECOND GRAPH
# create a dictionary which will serve as a weighted graph
graph_a = {}
graph_a['start'] = {'a': 5, 'b': 2}
graph_a['a'] = {'c': 4, 'd': 2}
graph_a['b'] = {'a': 8, 'd': 7}
graph_a['c'] = {'finish': 3, 'd': 6}
graph_a['d'] = {'finish': 1}
graph_a['finish'] = {}
print(f'Graph_A: {graph_a}')

# create a dictionary which will handle sum of weights for each node of the graph
# (sum of weights from the start node)
weights_a = {}
weights_a['a'] = 5
weights_a['b'] = 2
weights_a['c'] = 9
weights_a['d'] = 9
weights_a['finish'] = infinity
print(f'Weights_A: {weights_a}')

# create a dictionary for storing information about parent node
parents_a = {}
parents_a['a'] = 'start'
parents_a['b'] = 'start'
parents_a['finish'] = None
print(f'Parent A nodes: {parents_a}')

# create a list for storing already processed nodes to avoid double check
processed_a = []

# have fun and find the shortest path
print(find_shortest_path(graph_a, weights_a, parents_a, processed_a))
