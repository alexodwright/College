class Vertex:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element

class Edge:
    def __init__(self, element, v1, v2):
        self.label = element
        self.vertices = (v1, v2)

    def __str__(self):
        return str((self.element, self.vertices))

    def vertices(self):
        return self.vertices

    def opposite(self, x):
        return self.vertices[0] if x != self.vertices[0] else self.vertices[1]

    def element(self):
        return self.label

    def first_vertex(self):
        return self.vertices[0]

    def second_vertex(self):
        return self.vertices[1]

# Using an Adjacency List

class Graph:
    def __init__(self):
        self.adj_list = {}

    def get_edge(self, x ,y):
        for v in self.adj_list[x]:
            if v.second_vertex == y:
                return v

    def degree(self, x):
        return len(self.adj_list[x])

    def get_edges(self, x):
        return self.adj_list[x]

    def add_vertex(self, element):
        v = Vertex(element)
        self.adj_list[v] = []
        return v

    def add_edge(self, x, y, element):
        edge = Edge(element, x, y)
        self.adj_list[x].append(edge)
        self.adj_list[y].append(edge)

    def remove_edge(self, e):
        self.adj_list[e.vertices[0]].remove(e)
        self.adj_list[e.vertices[1]].remove(e)

    def remove_vertex(self, x):
        adjacent_vertices = [e.opposite(x) for e in self.adj_list[x]]

        for v in adjacent_vertices:
            for e in self.adj_list[v]:
                if e.opposite(v) == x:
                    self.adj_list[v].remove(e)
        del self.adj_list[x]

    def get_vertex_by_label(self, label):
        for v in self.adj_list:
            if v.element() == label:
                return v
