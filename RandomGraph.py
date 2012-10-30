import Graph
import random

class RandomGraph(Graph.Graph):
    def add_random_edges(self, p):
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j <= i: continue
                if random.random() > p: continue
                self.add_edge(Graph.Edge(v, w))
