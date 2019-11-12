import math
import random


class Node:
    def __init__(self, d=None, prev=None, debug=True, name=None):
        if debug:
            self.name = name
        self.d = d
        self.prev = prev


class Edge:
    def __init__(self, u, v, w=None):
        """

        :param u: Node, start node
        :param v: Node, end node
        :param w: Int, weight of edge between these two nodes
        """
        self.u = u
        self.v = v
        self.w = w


class Graph:

    def __init__(self, V=None, E=None):
        """

        :param V: List<Int>, Vertices
        :param E: List<Tuple<Node,Node>>, Edges
        """
        self.V = V
        self.E = E

    def Traverse(self):
        pass

    def add_Node(self):
        pass

    def remove_Node(self, name):
        pass


def Initialize_Single_Source(G, s):
    for v in G.V:
        v.d = math.inf
        v.prev = None
    s.d = 0


def Relax(u, v, w):
    """
    Triangle equality by Lemma 24.1
    :param u:
    :param v:
    :param w:
    :return:
    """
    if v.d > u.v + w:
        v.d = u.v + w
        v.prev = u

