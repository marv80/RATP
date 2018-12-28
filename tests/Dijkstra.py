# use of module collections with the datatype defaultdict and deque
from collections import defaultdict, deque


# this class contains our main variables to build the graph
class Graph():
    # initialization of variables
    def __init__(self):
        # initialization of a set for the nodes
        self.nodes = set()
        # initialization of a dictionary of lists to link nodes through edges
        self.edges = defaultdict(list)
        # initialization of a dictionary to store the distance between 2 nodes
        self.distances = {}

    # function to add a node with its value (the name of the node)
    def add_node(self, value):
        self.nodes.add(value)

    # function to add an edge from a node to another, and store the  distance in between the nodes
    def add_edge(self, origin_node, destination_node, distance):
        self.edges[origin_node].append(destination_node)  # add an edge between two nodes: origin and destination
        self.edges[destination_node].append(origin_node)  # add an edge between two nodes: destination and the origin
        self.distances[(origin_node, destination_node)] = distance  # add the distance between the origin and the dest

    # nodes accessor
    def get_nodes(self):
        return self.get_nodes()


# function to find the shortest path in a graph
def dijkstra(graph, initial):
    visited = {initial: 0}  # dictionary which contains all the visited nodes with their weight/ distance, initial is the start point
    path = {}  # correspond to the shortest path, it is a dictionary

    node_bag = set(graph.nodes) # get a set holding each nodes of the graph

    while node_bag:  # while the node set is not empty
        min_node = None  # min_node is the node with the minimum weight
        for node in node_bag:  # for each node in the set
            if node in visited:  # if the node is visited
                if min_node is None:  # if the node with minimum weight is null
                    min_node = node  # the minimum node takes the value of the node
                elif visited[node] < visited[min_node]:  # else if the weight visited node is inferior than the weight of the minimum node
                    min_node = node  # the minimum node takes the value of the node
        if min_node is None:  # if the node with minimum weight is null -> stop the execution in the loop
            break

        node_bag.remove(min_node) # remove the node with the smallest weigth from the node set
        current_weight = visited[min_node] # store the weigth of that node

        for edge in graph.edges[min_node]: # for each edge between the minimum node and the other nodes it is linked to
            try:
                weight = current_weight + graph.distances[(min_node, edge)] # store the weight of the node (nodeB) that is connected to the minimal node (nodeA)
            except:
                continue
            if edge not in visited or weight < visited[edge]: # if the nodeB wasn't visited yet or if its weight is smaller than the last time it got visited
                visited[edge] = weight # set the nodeB in the visited list and store its weight
                path[edge] = min_node # add the path from nodeA to nodeB to the list of the shortest paths

    return visited, path  # return of all the nodes which were visited and the path with the nodes in the shortest path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin) # get the set of the visited nodes and the shortest paths between 2 connected nodes
    full_path = deque() # initialize a deque set, a double ended queue
    _destination = paths[destination] # store the shortest path from the destination node to its adjunct nodes

    while _destination != origin: # while we didn't reached the wanted origin of the path
        full_path.appendleft(_destination) # push the shortest path in the beginning of the double ended queue
        _destination = paths[_destination] # set the new destination node to the closest adjunct node of the former destination node

    full_path.appendleft(origin) # push the origin node in the beginning
    full_path.append(destination) # push the destination sent in the parameters at the end of the final path

    return visited[destination], list(full_path)



if __name__ == '__main__':
    graph = Graph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'D', 105)
    graph.add_edge('C', 'D', 30)
    graph.add_edge('B', 'E', 50)
    graph.add_edge('D', 'E', 30)
    graph.add_edge('E', 'F', 5)
    graph.add_edge('F', 'G', 2)

    print(shortest_path(graph, 'A', 'D'))

