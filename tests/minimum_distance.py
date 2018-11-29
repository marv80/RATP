
def minimum_distance(graph,self, distance, shortest_path_tree):
    visited = {0}
    path = {}
    min =0
    vertex = set(graph.vertex)
    for v in range(self.V):
        if distance[v] < min and shortest_path_tree[v] == False:
            min = distance[v]
            min_index = v

    return min_index
