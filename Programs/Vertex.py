class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
        self.buildings = {"Left": None,"Right": None,"Top": None,"Bottom": None}

    def add_edge(self, vertex, weight = 0):
        self.edges[vertex] = weight 
    
    def add_building(self, building, loc):
       self.buildings[loc] = building
       
    def get_edges(self):
        return list(self.edges.keys())

