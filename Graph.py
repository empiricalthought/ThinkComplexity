class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """create a new graph.  (vs) is a list of vertices;
        (es) is a list of edges."""
        for v in vs:
            self.add_vertex(v)
        
        for e in es:
            self.add_edge(e)
    
    def add_vertex(self, v):
        """add (v) to the graph"""
        self[v] = {}
        
    def add_edge(self, e):
        """add (e) to the graph by adding an entry in both directions.

        If there is already an edge connecting these vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """get the Edge object connecting two vertices."

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> e = Edge(u, v)
        >>> g = Graph([u, v], [e])
        >>> g.get_edge(u, v)
        Edge(Vertex('u'), Vertex('v'))
        """
        try:
            return self[v][w]
        except KeyError:
            return None

    def remove_edge(self, e):
        """Remove an edge from the graph.

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> e = Edge(u, v)
        >>> g = Graph([u, v], [e])
        >>> g.remove_edge(e)
        >>> g.edges()
        []
        """
        v, w = e
        del self[v][w]
        del self[w][v]

    def vertices(self):
        """Return all of the vertices in the graph as a list.

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> e = Edge(u, v)
        >>> g = Graph([u, v], [e])
        >>> set(g.vertices()) == set([u, v])
        True
        """
        return list(self.keys())

    def edges(self):
        """Return all of the edges in the graph as a list.

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> e = Edge(u, v)
        >>> g = Graph([u, v], [e])
        >>> g.edges()
        [Edge(Vertex('u'), Vertex('v'))]
        """
        result = set()
        for v in self.keys():
            for w in self[v]:
                result.add(self[v][w])
        return list(result)

    def out_vertices(self, v):
        """Return all of the vertices connected to a given 
        vertex.

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> w = Vertex('w')
        >>> e = Edge(u, v)
        >>> f = Edge(u, w)
        >>> g = Graph([u, v, w], [e, f])
        >>> set(g.out_vertices(u)) == set([v, w])
        True
        """
        return list(self[v].keys())

    def out_edges(self, v):
        """Return all of the edges connected to a given vertex.

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> w = Vertex('w')
        >>> e = Edge(u, v)
        >>> f = Edge(u, w)
        >>> g = Graph([u, v, w], [e, f])
        >>> set(g.out_edges(u)) == set([e, f])
        True
        """
        return list(self[v].values())

    def add_all_edges(self):
        """Connect every vertex in the graph.  

        >>> u = Vertex('u')
        >>> v = Vertex('v')
        >>> w = Vertex('w')
        >>> g = Graph([u, v, w])
        >>> g.add_all_edges()
        >>> set(g.out_vertices(u)) == set([v, w])
        True
        >>> set(g.out_vertices(v)) == set([u, w])
        True
        >>> set(g.out_vertices(w)) == set([u, v])
        True
        """
        for v in self.keys():
            for w in self.keys():
                if v != w:
                    self.add_edge(Edge(v, w))

    def add_regular_edges(self, degree):
        """Connect vertices in such a way that the graph is regular.
        >>> u,v,w,x = [Vertex(c) for c in "uvwx"]
        >>> g1 = Graph([u,v,w,x])
        >>> g1.add_regular_edges(1)
        >>> list(len(g1.out_vertices(n)) for n in g1.vertices())
        [1, 1, 1, 1]
        >>> g2 = Graph([u,v,w,x])
        >>> g2.add_regular_edges(2)
        >>> list(len(g2.out_vertices(n)) for n in g2.vertices())
        [2, 2, 2, 2]
        """
        for i in range(0, degree):
            vertices = self.keys()
            while len(vertices) > 0:
                v = vertices.pop()
                for w in vertices:
                    if w not in self.out_vertices(v):
                        vertices.remove(w)
                        self.add_edge(Edge(v, w))
                        break


class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

if __name__ == "__main__":
    import doctest
    doctest.testmod()
