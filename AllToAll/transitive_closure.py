from graph import *


def Transitive_Closure(G):
    """
    This version depends on several tables
    TODO: Fix this hardcoded shit
    :param G:
    :return:
    """
    n = len(G.V)
    T = [[0 for i in range(n)] for j in range(n)]
    for i in range(1,n):
        for j in range(1, n):
            if i == j or (i, j) in G.E:
                T[i][j] = 1
            else:
                T[i][j] = 0

    # Grunntilfellet er nå på plass og er tilstrekkelig

    for k in range(1, n):
        T_k = [[0 for i in range(n)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, n):
                T_k[i][j] = 42

    return T

def Transitive_Closure_Simple(G):
    """

    :param G: Graph G = (V,E)
    :return: Table T for shortest paths
    """
    n = len(G.V)
    T = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i == j or (i, j) in G.E:
                T[i][j] = 1
            else:
                T[i][j] = 0

    #Grunntilfellet er nå på plass
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])
    return T

