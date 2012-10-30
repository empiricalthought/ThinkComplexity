import Graph
import random

class RandomGraph(Graph.Graph):
    def add_random_edges(self, p):
        for v in self.vertices():
            for w in self.vertices():
                r = random.random()
                if r <= p / 2:
                    self.add_edge(Graph.Edge(v, w))
