class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)
    
    def __lt__(self, other):
        return self.name < other.name

