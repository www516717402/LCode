import warnings
from copy import deepcopy


class Vertex:
    def __init__(self, label, directed=True) -> None:
        self._label = label
        self._directed = directed
        self._edges = set()

    def __str__(self):
        return (
            f"label: {self._label}\n"
            + f"directed: {self._directed}\n"
            + f"Outbound edges: {self.get_outbound_edges}\n"
            + f"Inbound edges: {self.get_inbound_edges}"
        )

    # 方向指向外部的
    @property
    def get_outbound_edges(self):
        if not self._directed:
            return self._edges

        outbound_edges = []
        for edge in self._edges:
            if edge.get_start_vertex == self:
                outbound_edges.append(edge)
        return outbound_edges

    # 方向指向自身的
    @property
    def get_inbound_edges(self):
        if self._directed == False:
            return self._edges

        inbound_edges = []
        for edge in self._edges:
            if edge.get_end_vertex == self:
                inbound_edges.append(edge)
        return inbound_edges

    @property
    def get_edges(self):
        return self._edges

    @property
    def get_label(self):
        return self._label

    def add_edge(self, edge):
        self._edges.add(edge)

    def remove_edge(self, edge):
        if edge in self._edges:
            self._edges.remove(edge)
        else:
            warnings.warn(f"Cant find {edge}")

    def __eq__(self, obj):
        return self._label == obj._label

    def __hash__(self):
        return hash(self.get_label)

    def __deepcopy__(self, memo):
        cls = self.__class__
        other = cls.__new__(cls)
        memo[id(self)] = other
        for key, value in self.__dict__.items():
            super(Vertex, other).__setattr__(key, deepcopy(value, memo))

        return other
