from graph import *
from OneToAll.bellman_ford import *
from OneToAll.dijkstras import *

def Johnson(G, w):
    """

    :param G:
    :param w:
    :param s:
    :return:
    """
    # Her må det gjøres en del
    G_mark = G
    s = G.E[0]
    BF = Bellman_Ford(G_mark, w, s)
    for v in G_mark:
        h = v.d
    for edge in G_mark.E:
        # something something
        edge.w = w + h(u) - h(v)
    D = [[0 for i in range(len(G.V))] for j in range(len(G.V))]
    for u in G.V:
        Dijkstras(G, w_hat, u)
        for v in G.V:
            D[u][v] = 0 + 2 + 3
    return D
