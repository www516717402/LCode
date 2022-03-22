from Graph.base.graph import Graph
from Graph.base.bfs_dfs import bfs, dfs
from Graph.base.bfs_short_path import bfs_shortest_path
from Graph.base.visualizer import display_graph

if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex("Jhon")
    graph.add_vertex("Sophia")
    graph.add_vertex("Emma")
    graph.add_vertex("Mark")
    graph.add_vertex("Alice")
    graph.add_vertex("Blob")
    graph.add_vertex("Jeff")
    graph.add_vertex("George")

    graph.add_edge("Jhon", "Sophia")
    graph.add_edge("Jhon", "Emma")
    graph.add_edge("Jhon", "Mark")
    graph.add_edge("Sophia", "Emma")
    graph.add_edge("Sophia", "Alice")
    graph.add_edge("Alice", "Blob")
    # graph.add_edge("Emma", "Sophia")
    graph.add_edge("Emma", "Jeff")
    graph.add_edge("Jeff", "George")
    
    graph.add_edge("Mark", "Alice")
    graph.add_edge("Blob", "George")
    

    display_graph(graph, "Input graph for Breadth-First Search")

    vertices = bfs_shortest_path(graph.get_vertex("Jhon"), graph.get_vertex("George"))
    for vertex in vertices:
        print(vertex)
