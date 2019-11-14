

class FlowNetwork:

    class Node:
        def __init__(self):
            pass


    class Edge:
        def __init__(self, u, v, flow, cap, rev_flow=0):
            """
            Edges in a flow network will store flow and capacity instead of weight
            :param u: Node, start node
            :param v: Node, end node
            :param flow: Int, flow currently used
            :param cap: Int, max flow allowed through edge
            """
            self.flow = flow
            self.rev_flow = rev_flow
            self.cap = cap
            self.edge = (u, v)
            self.u = u
            self.v = v

    def __init__(self):
        self.graph = 0