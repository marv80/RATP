#use module collections with the datatype defaultdict and deque
from collections import defaultdict, deque

# this class contains our main variables to build the graph
class Graph():
# initialization of variables
    def __init__(self):
        self.nodes = set()
# use of a dictionary of list
        self.edges = defaultdict(list)
        self.distances = {}

# function to add a node with its value
    def add_node(self, value):
        self.nodes.add(value)
# function add an edge from a node to another, and keep its distance
    def add_edge(self, origin_node, destination_node, distance):
        self.edges[origin_node].append(destination_node)  # add an edge between two nodes origin and destination
        self.edges[destination_node].append(origin_node)   # add an edge between two nodes: destination and the origin
        self.distances[(origin_node, destination_node)] = distance # add the distance between two nodes: the origin and the destination

# function to find the shortest path
def dijkstra(graph, initial):
    visited = {initial: 0} # dictionary which contains all the visited nodes with their weight/ distance, initial is the start point
    path = {} # correspond to the shortest path, it is a dictionnary

    nodes = set(graph.nodes)

    while nodes: # while nodes exist
        min_node = None  # min_node correspond to the node with the minimum weight
        for node in nodes:  # for each node
            if node in visited:  #if the node is visited
                if min_node is None:  # if the node with minimum weight is null
                    min_node = node # the minimum node takes the value of the node
                elif visited[node] < visited[min_node]:  # else if the weight visited node is inferior than the weight of the minimum node
                    min_node = node # the minimum node takes the value of the node
        if min_node is None:  # if the node with minimum weight is null -> stop the execution in the loop
            break
