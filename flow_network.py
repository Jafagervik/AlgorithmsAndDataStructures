

class FlowNetwork:

    class Node:
        def __init__(self, distance, prev_node, adj_edges=None):
            """

            :param distance: Node, distance from start node
            :param prev_node: Node, pointer to previous node
            :param adj_edges: List<Edges>, list of edges going from this node
            """
            self.d = distance
            self.prev = prev_node
            if adj_edges is None:
                self.adj_edges = []

    class Edge:
        def __init__(self, source, sink, flow, cap, rev_flow=0):
            """
            Edges in a flow network will store flow and capacity instead of weight
            :param source: Node, start node
            :param sink: Node, end node
            :param flow: Int, flow currently used
            :param cap: Int, max flow allowed through edge
            """
            self.flow = flow
            self.rev_flow = rev_flow
            self.cap = cap

            self.source = source
            self.sink = sink

            self.flow_cap = [self.flow, self.cap]
            self.edge = [self.flow, self.rev_flow]
            self.edge_nodes = (source, sink)

    def __init__(self):
        """
        graph[v] should be the list of edges coming out of vertex v in the
                 original graph and their corresponding constructed reverse edges
                 which are used for push-back flow.
        """
        self.graph = []

    def add_edges(self, edge):
        self.graph.append(edge)
