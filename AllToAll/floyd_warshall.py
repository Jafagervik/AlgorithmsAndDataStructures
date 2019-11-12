from graph import *


def Floyd_Warshall(W):
    """
    :param W:
    :return:
    """
    n = len(W) # n = W.rows
    D = [W]
    for k in range(1, n):
        D[k] = [[0 for i in range(n)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, n):
                d = D[k]
                d_k = D[k - 1]
                d[i][j] = min(d_k[i][j], d[i][k] + d[k][j])
    return D[n]
