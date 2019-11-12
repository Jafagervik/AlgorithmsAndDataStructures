import queue
from graph import *
from priority_queue import PriorityQueue


def Dijkstras(G, w, s):
    """

    :param G: Graph G = (V,E)
    :param w: Int, weight
    :param s: Node, source node
    :TODO: Implement Return
    :TODO: Use Binary Heap instead of min priority queue?
    :return: List<Int>, Shortest path from one node to all the other nodes
    """
    Initialize_Single_Source(G, s)
    S = {}
    Q = PriorityQueue(queue=G.V)
    while not (Q.isEmpty()):
        u = Q.Extract_Min()
        S = S | u
        for v in u.adj:
            Relax(u, v, w)
