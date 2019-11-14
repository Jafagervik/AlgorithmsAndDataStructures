"""
Well this one will be fun to implement
"""
from queue import Queue
from bfs import *
from math import inf


def Edmonds_Karp(G, s, t):
    """
    Algorithm for finding maximum flow through a flow network
    :param G: Graph G = (V,E) a flow network
    :param s: Node, source vertex
    :param t: Node, sink vertex
    :return: Int, maximum flow allowed
    """
    flow = 0
    # Pred tells us how we got ot the end such that we can easily know which nodes to traverse
    pred = G.V
    # This next segment should be repeated
    while pred[t] is not None:
        shortest_path = BFS(G, s) # algorithm should return shortest path from source to sink
        Q = Queue()
        Q.enqueue(s)

        while not Q.is_empty():
            cur = Q.dequeue()
            for edge in G.V[cur]:
                if pred[edge.t] is None and edge.t != s and edge.cap > edge.flow:
                    pred[edge.t] = edge
                    Q.enqueue(edge.t)

        if pred[t] is not None:
            # Aka we found an augmenting path, see how much flow we can send
            df = inf
            edge = pred[t]
            while edge is not None:
                df = min(df, edge.cap - edge.flow)
                edge = pred[edge.s]

            edge = pred[t]
            while edge is not None:
                edge.flow += df
                edge.rev_flow -= df

            flow += df

    return flow

#def BreadthFirstSearch(capacity, neighbours, flows, start, end):


