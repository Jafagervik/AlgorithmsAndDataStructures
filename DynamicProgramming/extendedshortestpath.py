from math import inf


def extend_shortest_paths(L, W):
    """
    O(n^3) time implementation of all pairs shortest path
    Terrible algorithm
    :param L: Matrix
    :param W: Weight matrix
    :return:
    """
    n = len(L.R)
    L_mark = [[inf for i in range(n)] for k in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                L_mark[i][j] = min(L_mark[i][j], L_mark[i][k] + W[k][j])
    return L_mark


def slow_all_pairs_shortest_path(W):
    """
    Whack ass O(n^4) algorithm
    :param W:
    :return:
    """
    n = len(W)
    L = []
    L[0] = W
    for m in range(2, n-1):
        L[m] = extend_shortest_paths(L[m-1], W)
    return L[n-1]


def faster_all_pairs_shortest_path(W):
    n = len(W)
    L = [[] for i in range n]
    L[0] = W
    m = 1
    while m < n - 1:
        L[2*m] =