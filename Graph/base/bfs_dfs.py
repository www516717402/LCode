from collections import deque
from queue import Queue


def dfs(start_vertex):
    queue = deque()
    queue.append(start_vertex)
    visited_vertices = set()
    result = []
    while len(queue):
        current_vertex = queue.pop()

        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)
        result.append(current_vertex.get_label)

        adjacent_vertices = []
        for edge in current_vertex.get_outbound_edges:
            adjacent_vertex = edge.get_end_vertex
            if adjacent_vertex not in visited_vertices:
                adjacent_vertices.append(adjacent_vertex)

        queue.extend(adjacent_vertices)
    return result


def bfs(start_vertex):
    queue = Queue()
    queue.put(start_vertex)
    visited_vertices = set()
    result = []
    while not queue.empty():
        current_vertex = queue.get()

        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)
        result.append(current_vertex.get_label)

        for edge in current_vertex.get_outbound_edges:
            adjacent_vertex = edge.get_end_vertex
            if adjacent_vertex not in visited_vertices:
                queue.put(adjacent_vertex)

    return result
