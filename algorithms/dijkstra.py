from data_structures.min_heap import MinHeap

def dijkstra(graph, start_id, end_id, weight_fn):
    distances = {node_id:float("inf") for node_id in graph.get_all_nodes()}
    previous = {node_id:None for node_id in graph.get_all_nodes()}
    distances[start_id] = 0
    heap = MinHeap()
    heap.push(0,start_id)
    visited = set()

    while not heap.is_empty():
        current_cost, current_node = heap.pop()

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end_id:
            break

        for edge in graph.get_neighbors(current_node):
            neighbor = edge["to"]
            if neighbor in visited:
                continue

            weight = weight_fn(edge)
            new_cost = current_cost + weight

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current_node
                heap.push(new_cost, neighbor)

    if distances[end_id] == float("inf"):
        return None

    path = []
    node = end_id
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()

    return {"path":path, "total_cost":distances[end_id]}