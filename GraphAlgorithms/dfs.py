from graph import *
from queue import *
from math import inf

time = 0
def DFS(G):
    """

    :param G: Graph G = (V, E)
    :return: List<Node>,
    """
    for vertex in G.V:
        vertex.color = "White"
        vertex.prev = None
    for vertex in G.V:
        if vertex.color == "White":
            DFS_Visit(G, vertex)


def DFS_Visit(G, u):
    global time
    time += 1
    u.d = time
    u.color = "Grey"
    for v in u.adj:
        if v.color == "White":
            v.prev = u
            DFS_Visit(G, v)
    u.color = "Black"
    time += 1
    u.f = time
