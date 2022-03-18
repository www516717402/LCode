class Vertex:
    def __init__(self, label, directed=True) -> None:
        self._label = label
        self._directed = directed
        self._edges = set()
    
    def __str__(self) -> str:
        return None
    
    def get_outbound_edges(self):
        if self._directed == False:
            return self._edges
        outbound_edges = []
        