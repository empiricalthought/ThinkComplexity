from Graph import *
from GraphWorld import *

vs = [Vertex(c) for c in "abcdefgh"]
g = Graph(vs)
g.add_regular_edges(6)
layout = CircleLayout(g)

# draw the graph
gw = GraphWorld()
gw.show_graph(g, layout)
gw.mainloop()
