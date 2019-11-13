from graph import *
from queue import *
from math import inf

def BFS(G, s):
    """

    :param G: Graph G = (V, E)
    :param s: Node, source node
    :return: List<Node>,
    """
    # Initialiation of set J
    J = set(G.V) - set(s)
    for vertex in J:
        vertex.color = "White"
        vertex.prev = None
    s.color = "Grey"
    s.d = 0

    Q = Queue()
    Q.enqueue(s)
    while not Q.is_empty():
        u = Q.dequeue()
        for v in u.adj:
            if v.color == "White":
                v.color = "Grey"
                v.d += 1
                v.prev = u
                Q.enqueue(v)
        u.color = "Black"

