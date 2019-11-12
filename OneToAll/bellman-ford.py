import math
from graph import *





def Bellman_Ford(G, w, s):
    """
    Much dank algorithm to compute epic graphs and their acycleness
    :param G: Graph G = (V,E) containing list of vertices and edges
    :param w: Int, weight of edge bewteen nodes
    :param s: Node, source node
    :return: Bool, negative wieght-cycle reachable from source
    """
    Initialize_Single_Source(G, s)
    for i in range(1, len(G.V)-1):
        for edge in G.E: # Edge is a tuple!!
            Relax(edge.u, edge.v, w) # u = edge[0] and v = edge[1]
    for edge in G.E:
        if edge.v.d > edge.u.d + edge.w: # w(u, v)
            return False
    return True
