class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex
    
    def add_edge(self, from_vertex, to_vertex, weight = 1):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    
