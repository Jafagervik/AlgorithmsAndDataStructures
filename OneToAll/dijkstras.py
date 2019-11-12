import queue
from graph import *
from priority_queue import PriorityQueue


def Dijkstras(G, w, s):
    """

    :param G: Graph G = (V,E)
    :param w: Int, weight
    :param s: Node, source node
    :return: List<Int>, Shortest path from one node to all the other nodes
    """
    Initialize_Single_Source(G, s)
    S = ([])
    Q = PriorityQueue(queue=G.V)
    while Q is not None:
        u = Q.V +