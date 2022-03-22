from Graph.graph import Graph
from Graph.visualizer import display_graph


class TestDirectedGraph():
    def __init__(self):
        # initialize graph will be called once per each test (test fixture)
        self._graph = Graph()

        self._graph.add_vertex("1")
        self._graph.add_vertex("2")
        self._graph.add_vertex("3")
        self._graph.add_vertex("4")
        self._graph.add_vertex("5")
        self._graph.add_vertex("6")

        self._graph.add_edge("1", "2", 1)
        self._graph.add_edge("1", "3", 2)
        self._graph.add_edge("2", "3", 3)
        self._graph.add_edge("2", "6", 4)
        self._graph.add_edge("4", "3", 5)
        self._graph.add_edge("5", "2", 6)
        self._graph.add_edge("5", "3", 7)
        self._graph.add_edge("6", "4", 8)
        self._graph.add_edge("6", "5", 9)

    def tearDown(self):
        pass  # deinitialize will be called once per each test (test fixture)

    def test_add_vertex(self):
        assert len(self._graph.get_vertices) == 6
        assert self._graph.get_vertex("7") is None

        self._graph.add_vertex("7")

        assert len(self._graph.get_vertices) == 7
        assert self._graph.get_vertex("7") is not None

    def test_add_the_same_vertex_multiple_times(self):
        assert (len(self._graph.get_vertices()), 6)
        self.assertIsNone(self._graph.get_vertex("7"))

        self._graph.add_vertex("7")
        self._graph.add_vertex("7")
        self._graph.add_vertex("7")

        assert (len(self._graph.get_vertices()), 7)
        self.assertIsNotNone(self._graph.get_vertex("7"))

    def test_add_edge(self):
        assert len(self._graph.get_edges) == 9
        assert self._graph.get_indegree("1") == 0
        assert self._graph.get_outdegree("5") == 2

        self._graph.add_edge("5", "1")

        assert len(self._graph.get_edges) == 10
        assert self._graph.get_indegree("1") == 1
        assert self._graph.get_outdegree("5") == 3

    def test_add_edge_with_the_same_direction_and_other_weight(self):
        assert (len(self._graph.get_edges()), 9)
        assert (self._graph.get_indegree("3"), 4)
        assert (self._graph.get_outdegree("1"), 2)

        self._graph.add_edge("1", "3", 3)

        assert (len(self._graph.get_edges()), 10)
        assert (self._graph.get_indegree("3"), 5)
        assert (self._graph.get_outdegree("1"), 3)

    def test_add_the_same_edge_multiple_times(self):
        assert (len(self._graph.get_edges()), 9)
        assert (self._graph.get_indegree("1"), 0)
        assert (self._graph.get_outdegree("5"), 2)

        self._graph.add_edge("5", "1", 6)
        self._graph.add_edge("5", "1", 6)
        self._graph.add_edge("5", "1", 6)

        assert (len(self._graph.get_edges()), 10)
        assert (self._graph.get_indegree("1"), 1)
        assert (self._graph.get_outdegree("5"), 3)

    def test_remove_vertex(self):
        assert self._graph.get_vertex("2") is not None
        assert len(self._graph.get_vertices) == 7

        self._graph.remove_vertex("2")

        assert self._graph.get_vertex("2") is None
        assert len(self._graph.get_vertices) == 6

    def test_remove_not_existing_vertex(self):
        with self.assertRaises(ValueError):
            self._graph.remove_vertex("NonExistingVertex")

    def test_remove_edge(self):
        assert (self._graph.get_indegree("3"), 4)
        assert (self._graph.get_outdegree("5"), 2)
        assert (len(self._graph.get_edges()), 9)

        self._graph.remove_edge("5", "3", 7)

        assert (self._graph.get_indegree("3"), 3)
        assert (self._graph.get_outdegree("5"), 1)
        assert (len(self._graph.get_edges()), 8)

    def test_remove_not_existing_edge(self):
        with self.assertRaises(ValueError):
            self._graph.remove_edge(
                "NonExistingVertex1", "NonExistingVertex2", 4)

    def test_vertices_count(self):
        assert len(self._graph.get_vertices) == 6

    def test_edges_count(self):
        assert len(self._graph.get_edges) == 9

    def test_get_vertex(self):
        assert self._graph.get_vertex("1") is not None

    def test_get_not_existing_vertex(self):
        self.assertIsNone(self._graph.get_vertex("NonExistingVertex"))

    def test_vertex_indegree(self):
        assert (self._graph.get_indegree("3"), 4)

    def test_vertex_outdegree(self):
        assert (self._graph.get_outdegree("6"), 2)

    def test_degree(self):
        assert (self._graph.get_degree("6"), 3)

    def test_graph_is_directed(self):
        self.assertTrue(self._graph.is_directed())


if __name__ == "__main__":
    ttt = TestDirectedGraph()
    display_graph(getattr(ttt, '_graph'))
    ttt.test_add_vertex()
    # ttt.test_add_the_same_vertex_multiple_times()
    ttt.test_add_edge()
    # ttt.test_add_edge_with_the_same_direction_and_other_weight()
    ttt.test_remove_vertex()
    ttt.test_vertices_count()
    ttt.test_edges_count()
