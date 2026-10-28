# graph.py
import json
import os

class CityGraph:
    def __init__(self):
        # Структура: { 'A': { 'B': {'weight': 4, 'time': 10}, ... }, ... }
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, u, v, weight, time_val=0, directed=False):
        if weight < 0 or time_val < 0:
            raise ValueError("Қабырға салмағы немесе уақыты теріс болмауы тиіс!")
        
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.adj_list[u][v] = {'weight': weight, 'time': time_val}
        if not directed:
            self.adj_list[v][u] = {'weight': weight, 'time': time_val}

    def remove_edge(self, u, v, directed=False):
        if u in self.adj_list and v in self.adj_list[u]:
            del self.adj_list[u][v]
        if not directed:
            if v in self.adj_list and u in self.adj_list[v]:
                del self.adj_list[v][u]

    def save_to_json(self, filepath="data/city_graph.json"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.adj_list, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filepath="data/city_graph.json"):
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r', encoding='utf-8') as f:
            self.adj_list = json.load(f)