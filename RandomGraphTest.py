from RandomGraph import *
from Graph import *

tries = 30
iterations = 10

def run_test(size):
    vertices = [Vertex(n) for n in range(0, size)]
    p = 0.5
    for i in range(1, iterations):
        connected_count = 0.0
        for j in range(0, tries):
            g = RandomGraph(vertices)
            g.add_random_edges(p)
            if g.is_connected():
                connected_count = connected_count + 1.0
        percent = connected_count / tries
        print "p: %f, average connected = %f" % (p, percent)
        offset = 1.0 / 2**(i+1)
        if percent > 0.5:
            p = p - offset
        else:
            p = p + offset

for n in (8, 32, 256):
    print "n = %d" % n
    run_test(n)
