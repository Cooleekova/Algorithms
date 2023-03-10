# Breadth-first search (BFS) is an algorithm 
# for searching a tree data structure for a node that satisfies a given property. 
# It starts at the tree root and explores all nodes at the present depth 
# prior to moving on to the nodes at the next depth level. 
# Extra memory, usually a queue, 
# is needed to keep track of the child nodes that were encountered but not yet explored.


# MAIN FUNCTIONALITY OF BFS: 
# 1) FIND IF OBJECT IS INSIDE THE DATA STRUCTURE 
# 2) iF SO, FIND THE NEAREST TO THE START OF SEARCH OBJECT WITH DESIRED CHARACTERISTICS

from collections import defaultdict, deque


class Graph:
    """The class represents directed graph"""

    def __init__(self):
        # dictionary to store graph
        self.graph = defaultdict(list)


    # method to add an edge to the graph
    def add_edge(self, parent_node, new_vertice):
        self.graph[parent_node].append(new_vertice)


    # the function just prints the order of iteration
    # but it is possible to add any searching logic in it
    # see example below 
    def breadth_first_search(self, search_start):
        """
        Sequentially go around all the vertices of the graph, 
        respecting the order,
        starting from the vertex passed to function
        """
        # assume all the vertices in the graph as not visited,
        # create empty "visited" list
        visited = []
        # create an emty queue to store the elements to be visited
        queue = deque()
        # insert starting element to the queue
        queue.append(search_start)
        # check each element in the queue while it is not empty
        while queue:
            # each time take the first element from the queue
            element = queue.popleft()
            # check that the chosen element was not yet visited
            if not element in visited:
                # add all the element's adjacent vertices to the queue
                queue.extend(self.graph[element])
                # mark the element as visited by adding it to the "visited" list
                visited.append(element)

        return(f"the BFS order of iterating through graph: {visited}")


# create a graph object "g"
g = Graph()
# add some vertices to the graph
g.add_edge(4,9)
g.add_edge(4,2)
g.add_edge(9,2)
g.add_edge(2,5)
g.add_edge(2,4)
g.add_edge(5,6)
# print newly created graph
print("Graph: ", g.graph)
# call the BFS function that iterates over all the values in the graph
print(g.breadth_first_search(4))



# in educational purposes I have created a function
# which will search first number divisible by three in a graph
# using Breadth-first search algorithm
def bfs(vertice):
    """Breadth-first search function.
    It searches in the graph the nearest to the vertice number divisible by three"""
    # create an emty queue to store the vertices to be visited
    queue = deque()
    # insert starting vertice to the queue
    queue.append(vertice)
    # at the start all the vertices in the graph as not checked,
    # create empty "checked" list
    checked = []
    # check each element in the queue while it is not empty
    while queue:
        # each time take the first element from the queue
        element = queue.popleft()
        # check that the chosen element was not yet checked
        if not element in checked:
            # if the element is divisible by three, return it
            if element % 3 == 0:
                return f"Found the nearest to vertice '{vertice}' number divisible by three! it is {element}"
            # if the element is NOT divisible by three,
            # mark the element as checked by adding it to the "checked" list
            checked.append(element)
            # add all the element's adjacent vertices to the queue
            queue += g.graph[element]
    # if nothing was found, return 404 answer
    return '"404" No numbers divisible by three without a remainder in the graph'


# call the bfs function 
# and searche the nearest number divisible by three
print(bfs(2))
