import warnings
from copy import copy, deepcopy

from .edge import Edge
from .vertex import Vertex


# code from https://github.com/YuriiBarninets/graph/blob/master/graph/vertex.py
class Graph:
    def __init__(self, directed=True) -> None:
        self._vertices = dict()
        self._edges = set()
        self._directed = directed

    def __str__(self) -> str:
        graph_str = ""
        for key in self._verticess:
            graph_str += str(self._verticess) + "\n"
        return graph_str

    def add_vertex(self, label):
        if label in self._vertices:
            warnings.warn(
                f"label ==> {label} already exist.\
                and it will overload."
            )
        self._vertices[label] = Vertex(label, self._directed)

    def add_edge(self, start_label, end_label, weight=1):
        start_vertex = self.get_vertex(start_label)
        end_vertex = self.get_vertex(end_label)

        assert start_vertex and end_vertex, "Cant find start or end vertex"
        assert start_vertex != end_vertex, "Cant support start equal end"

        tmp_edge = Edge(start_vertex, end_vertex, weight, self._directed)
        start_vertex.add_edge(tmp_edge)
        end_vertex.add_edge(tmp_edge)
        self._edges.add(tmp_edge)

    def remove_edge(self, start_label, end_label, weight=1):
        start_vertex = self.get_vertex(start_label)
        end_vertex = self.get_vertex(end_label)
        assert start_vertex and end_vertex, "Cant find start or end vertex"
        tmp_edge = Edge(start_vertex, end_vertex, weight, self._directed)
        if tmp_edge not in self._edges:
            warnings.warn("Cant find this edge")
            return
        start_vertex.remove(tmp_edge)
        end_vertex.remove(tmp_edge)
        self._edges.remove(tmp_edge)

    def remove_vertex(self, label):
        if label not in self.get_vertices:
            raise TypeError("Cant find label in vertices")
        del_vertex = self.get_vertex(label)
        for del_edge in copy(del_vertex.get_edges):
            if del_edge.get_start_vertex != del_vertex:
                del_edge.get_end_vertex.get_edges.remove(del_edge)
            else:
                del_edge.get_start_vertex.get_edges.remove(del_edge)
            self._edges.remove(del_edge)

        del self._vertices[label]

    def get_vertex(self, label):
        return self._vertices.get(label)

    @property
    def get_vertices(self):
        return self._vertices

    @property
    def get_edges(self):
        return self._edges

    def get_indegree(self, label):
        return len(self.get_vertex(label).get_inbound_edges)

    def get_outdegree(self, label):
        return len(self.get_vertex(label).get_outbound_edges)

    @property
    def get_degree(self, label):
        degree = len(self.get_vertex(label).get_inbound_edges) + len(
            self.get_vertex(label).get_outbound_edges
        )
        return degree if self.is_directed else degree // 2

    @property
    def is_directed(self):
        return self._directed
