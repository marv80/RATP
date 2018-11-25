from collections import defaultdict

#declaration of the graph class
class Graph():

    def __init__(self):   #constructor
        self.vertex = None
        self.edge = None
        self.distance = {}

    def add_vertex(self, data):
        self.vertex.add(data)

    def addEdge(self, start_vertex, end_vertex, distance):
        self.edges[start_vertex].append(end_vertex)  #add an element from start_vertex to end_vertex
        self.edges[start_vertex].append(end_vertex)
        self.distances[(start_vertex, end_vertex)] = distance

    def print_data(self, start_vertex, end_vertex, distance):
        print("Here is the shortest path:", start_vertex, end_vertex, "with distance: ", distance)