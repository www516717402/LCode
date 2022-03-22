
def bfs_shortest_path(start_vertex, goal_vertex):
    """
    When we use BFS to find a shortest path we have to track path from source to goal.
    1. We may store parent vertex for each child, so this let us to get a path from goal to start
    when we hit a goal.
    2. We may store in queue list with path to vertex instead of single vertex, so the last item in list will
    represent a current vertex (we use this approach in the algorithm below)
    """
    if start_vertex == goal_vertex:
        return start_vertex

    # initially, queue contains only the list with start vertex
    # and all vertices are not visited
    queue = [[start_vertex]]
    visited_vertices = set()

    while len(queue) > 0:
        # pop a vertex from the queue
        path_to_vertex = queue.pop(0)
        current_vertex = path_to_vertex[-1]

        # ignoring this vertex if it has been visited
        if current_vertex in visited_vertices:
            continue

        # return path to vertex if we find goal vertex
        if current_vertex == goal_vertex:
            return path_to_vertex

        # mark as visited, so we will not visit it anymore
        visited_vertices.add(current_vertex)

        # get all adjacent vertices which HAVE NOT been visited
        adjacent_vertices = []
        for edge in current_vertex.get_outbound_edges:
            if edge.get_end_vertex not in visited_vertices:
                adjacent_vertices.append(edge.get_end_vertex)

        # push a list with path to each adjacent vertex in our queue
        for adjacent_vertex in adjacent_vertices:
            new_path = path_to_vertex.copy()
            new_path.append(adjacent_vertex)
            queue.append(new_path)

    # return None if there no a path between start and goal vertices
    return None
