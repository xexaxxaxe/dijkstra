# dijkstra.py
import heapq
import time

def dijkstra(graph, start, end, weight_key='weight'):
    if start not in graph.adj_list or end not in graph.adj_list:
        raise ValueError("Бастапқы немесе соңғы төбе графта жоқ!")

    start_time = time.time()
    
    distances = {vertex: float('inf') for vertex in graph.adj_list}
    previous = {vertex: None for vertex in graph.adj_list}
    
    distances[start] = 0
    pq = [(0, start)] # (current_distance, current_vertex)
    
    visited_nodes_count = 0

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > distances[u]:
            continue

        visited_nodes_count += 1

        if u == end:
            break

        for v, data in graph.adj_list[u].items():
            weight = data[weight_key]
            distance = current_dist + weight

            if distance < distances[v]:
                distances[v] = distance
                previous[v] = u
                heapq.heappush(pq, (distance, v))

    execution_time = (time.time() - start_time) * 1000 # миллисекундпен

    # Маршрутты қалпына келтіру (reconstruct path)
    path = []
    curr = end
    while curr is not None:
        path.insert(0, curr)
        curr = previous[curr]

    if distances[end] == float('inf'):
        return [], float('inf'), visited_nodes_count, execution_time

    return path, distances[end], visited_nodes_count, execution_time