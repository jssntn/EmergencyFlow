import heapq
from collections import defaultdict


class EmergencyNetwork:
    def __init__(self, vertices, edges, priorities):
        self.V = vertices
        self.E = edges
        self.priorities = priorities
        self.TE = {} # Information on edge times
        self.Ts = {} # Information on vertices times
        self.capacities = {}
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, capacity, travel_time):
        self.E.add((u, v))
        self.capacities[(u, v)] = capacity
        self.TE[(u, v)] = travel_time
        self.adj_list[u].append(v)

    def set_vertex_residence_time(self, vertex, time):
        self.Ts[vertex] = time

    def get_adjacent(self, vertex):
        return self.adj_list[vertex]

    def _reconstruct_path(self, labels, source, sink):
        if labels[sink][0] == float('inf'):
            return None

        path = []
        current = sink

        while current != source:
            previous = labels[current][1]
            path.append((previous, current))
            current = previous

        return path[::-1]

    def _calculate_path_time(self, path):
        total_time = 0

        for u, v in path:
            total_time += self.TE[(u, v)]

        vertices = [v for _, v in path]
        vertices.insert(0, path[0][0])

        for v in vertices[:-1]:
            total_time += self.Ts.get(v, 0)

        return total_time

    def _update_residual_capacities(self, path, flow):
        for u, v in path:
            self.capacities[(u, v)] -= flow

    def find_augmenting_path(self, source, sink):
        labels = {v: (float('inf'), None, 0) for v in self.V}
        labels[source] = (0, None, float('inf'))
        priority_queue = [(0, source)]
        visited = set()

        while priority_queue:
            current_time, u = heapq.heappop(priority_queue)
            if u in visited:
                continue

            visited.add(u)

            if u == sink:
                return self._reconstruct_path(labels, source, sink)

            for v in self.get_adjacent(u):
                if v in visited or self.capacities.get((u, v), 0) <= 0:
                    continue

                new_time = current_time + self.TE[(u, v)] + self.Ts.get(v, 0)

                priority_factor = self._calculate_priority_factor(v)
                adjusted_time = new_time * priority_factor

                if adjusted_time < labels[v][0]:
                    labels[v] = (adjusted_time, u, min(
                        labels[u][2],
                        self.capacities[(u, v)]
                    ))
                    heapq.heappush(priority_queue, (adjusted_time, v))

        return None

    def _calculate_priority_factor(self, vertex):
        max_priority = max(self.priorities.values())
        vertex_priority = self.priorities.get(vertex, 1)
        return (max_priority - vertex_priority + 1) / max_priority

    def distribute_supplies(self, source, sink, total_supply):
        current_flow = 0
        paths = []
        times = []

        while current_flow < total_supply:
            path = self.find_augmenting_path(source, sink)
            if not path:
                break

            possible_flow = min(
                total_supply - current_flow,
                min(self.capacities[edge] for edge in path)
            )

            current_flow += possible_flow
            paths.append((path, possible_flow))
            times.append(self._calculate_path_time(path))

            self._update_residual_capacities(path, possible_flow)

        return paths, times, current_flow

def example_usage():
    vertices = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
    edges = {('s', 'v1'), ('s', 'v2'), ('v1', 'v3'), ('v2', 'v3'), ('v3', 't')}
    priorities = {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 1, 't': 3}

    network = EmergencyNetwork(vertices, edges, priorities)

    network.add_edge('s', 'v1', capacity=10, travel_time=2)
    network.add_edge('s', 'v2', capacity=8, travel_time=3)
    network.add_edge('v1', 'v3', capacity=5, travel_time=2)
    network.add_edge('v2', 'v3', capacity=6, travel_time=3)
    network.add_edge('v3', 't', capacity=12, travel_time=1)

    network.set_vertex_residence_time('v1', 1)
    network.set_vertex_residence_time('v2', 1)
    network.set_vertex_residence_time('v3', 2)

    paths, times, total_flow = network.distribute_supplies('s', 't', 15)

    print(f"Total flow: {total_flow}")
    for i, (path, flow) in enumerate(paths):
        print(f"Path {i + 1}: {path}, Flow: {flow}, Time: {times[i]}")

def example_medium_usage():
    vertices = {f'v{i}' for i in range(40)}  # v0, v1, ..., v39
    edges = {
        ('v0', 'v1'), ('v0', 'v2'), ('v1', 'v3'), ('v1', 'v4'), ('v2', 'v5'), 
        ('v3', 'v6'), ('v4', 'v7'), ('v5', 'v8'), ('v6', 'v9'), ('v7', 'v10'), 
        ('v8', 'v11'), ('v9', 'v12'), ('v10', 'v13'), ('v11', 'v14'), ('v12', 'v15'),
        ('v13', 'v16'), ('v14', 'v17'), ('v15', 'v18'), ('v16', 'v19'), ('v17', 'v20'),
        ('v18', 'v21'), ('v19', 'v22'), ('v20', 'v23'), ('v21', 'v24'), ('v22', 'v25'),
        ('v23', 'v26'), ('v24', 'v27'), ('v25', 'v28'), ('v26', 'v29'), ('v27', 'v30'),
        ('v28', 'v31'), ('v29', 'v32'), ('v30', 'v33'), ('v31', 'v34'), ('v32', 'v35'),
        ('v33', 'v36'), ('v34', 'v37'), ('v35', 'v38'), ('v36', 'v39'), ('v2', 'v9'),
        ('v3', 'v15'), ('v5', 'v20'), ('v8', 'v30'), ('v10', 'v25'), ('v12', 'v35'),
        ('v13', 'v32'), ('v18', 'v34'), ('v19', 'v38'), ('v6', 'v17'), ('v7', 'v22'),
        ('v11', 'v26'), ('v14', 'v28'), ('v16', 'v29'), ('v31', 'v36'), ('v4', 'v12'),
        ('v9', 'v21'), ('v20', 'v27'), ('v22', 'v31'), ('v26', 'v39')
    }
    priorities = {f'v{i}': (i % 5) + 1 for i in range(40)}

    network = EmergencyNetwork(vertices, edges, priorities)

    for u, v in edges:
        capacity = (hash(u) + hash(v)) % 10 + 1
        travel_time = (hash(u) * hash(v)) % 5 + 1 
        network.add_edge(u, v, capacity=capacity, travel_time=travel_time)

    for vertex in vertices:
        residence_time = hash(vertex) % 4
        network.set_vertex_residence_time(vertex, time=residence_time)


    paths, times, total_flow = network.distribute_supplies('v0', 'v39', 100)

    # Exibe os resultados
    print(f"Total flow: {total_flow}")
    for i, (path, flow) in enumerate(paths):
        print(f"Path {i + 1}: {path}, Flow: {flow}, Time: {times[i]}")

def example_large_usage():
    vertices = {f'v{i}' for i in range(200)}

    edges = set()
    edges.update((f'v0', f'v{i}') for i in range(1, 8)) 

    for i in range(1, 200):
        if len(edges) >= 500:
            break
        for j in range(1, 4):
            v1 = f'v{i}'
            v2 = f'v{(i + j) % 200}'
            edges.add((v1, v2))
            if len(edges) >= 500:
                break

    priorities = {f'v{i}': (i % 5) + 1 for i in range(200)}

    network = EmergencyNetwork(vertices, edges, priorities)

    for u, v in edges:
        capacity = (int(u[1:]) + int(v[1:])) % 20 + 1
        travel_time = (int(u[1:]) * int(v[1:])) % 10 + 1  
        network.add_edge(u, v, capacity=capacity, travel_time=travel_time)

    for vertex in vertices:
        residence_time = int(vertex[1:]) % 4
        network.set_vertex_residence_time(vertex, time=residence_time)

    paths, times, total_flow = network.distribute_supplies('v0', 'v35', 300)

    print(f"Total flow: {total_flow}")
    for i, (path, flow) in enumerate(paths):
        print(f"Path {i + 1}: {path}, Flow: {flow}, Time: {times[i]}")