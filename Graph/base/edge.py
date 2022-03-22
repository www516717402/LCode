class Edge:
    def __init__(self, start_vertex, end_vertex, weight=1, directed=True):
        self._strat_vertex = start_vertex
        self._end_vertex = end_vertex
        self._weight = weight
        self._directed = directed

    def __str__(self) -> str:
        _str_ = ""
        _str_ += f"start:{str(self._strat_vertex)},"
        _str_ += f"end:{str(self._end_vertex)},"
        _str_ += f"weight:{str(self._weight)},"
        _str_ += f"directed:{str(self._directed)},"
        return _str_

    @property
    def get_start_vertex(self):
        return self._strat_vertex

    @property
    def get_end_vertex(self):
        return self._end_vertex

    @property
    def get_weight(self):
        return self._weight

    def __lt__(self, obj):
        return self.get_weight() < obj.get_weight()

    def __eq__(self, obj):
        weight_eq = self.get_weight() == obj.get_weight()
        start_eq = self.get_start_vertex() == obj.get_start_vertex()
        end_eq = self.get_end_vertex() == obj.get_end_vertex()
        return weight_eq and start_eq and end_eq

    # Set的存储是通过hash实现的
    def __hash__(self) -> int:
        return hash(
            self.get_start_vertex.get_label
            + self.get_end_vertex.get_label
            + str(self.get_weight)
        )
