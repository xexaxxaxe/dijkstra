# main.py
from graph import CityGraph
from dijkstra import dijkstra
from visualization import draw_graph

def initialize_default_graph():
    g = CityGraph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for v in vertices:
        g.add_vertex(v)

    # Кестедегі деректерді қосу 
    edges_data = [
        ('A', 'B', 4, 10), ('A', 'C', 2, 5),
        ('B', 'C', 1, 3), ('B', 'D', 5, 12), ('B', 'F', 9, 20),
        ('C', 'E', 7, 15), ('C', 'F', 4, 8), ('C', 'H', 10, 25),
        ('D', 'E', 2, 6), ('D', 'G', 6, 14),
        ('E', 'F', 1, 2), ('E', 'H', 3, 7), ('E', 'K', 8, 18),
        ('F', 'H', 5, 11), ('F', 'I', 8, 19),
        ('G', 'H', 2, 4), ('G', 'J', 7, 16), ('G', 'N', 6, 13),
        ('H', 'I', 2, 5), ('H', 'K', 6, 15),
        ('I', 'L', 4, 10), ('I', 'M', 9, 22),
        ('J', 'K', 1, 3), ('J', 'N', 8, 18),
        ('K', 'L', 3, 7), ('K', 'N', 5, 12),
        ('L', 'M', 2, 5), ('L', 'O', 7, 16),
        ('M', 'O', 3, 8),
        ('N', 'O', 4, 9)
    ]

    for u, v, w, t in edges_data:
        g.add_edge(u, v, weight=w, time_val=t, directed=False)
        
    return g

if __name__ == "__main__":
    city_graph = initialize_default_graph()
    city_graph.save_to_json()

    print("--- 1. A -> O маршрутын есептеу (Қашықтық бойынша) ---")
    path, total_weight, visited_count, exec_time = dijkstra(city_graph, 'A', 'O', weight_key='weight')
    print(go := f"Маршрут: {' -> '.join(path)}")
    print(f"Жалпы қашықтық: {total_weight} км")
    print(f"Қаралған төбелер саны: {visited_count}, Орындалу уақыты: {exec_time:.4f} мс")

    # Визуализация нәтижесі
    draw_graph(city_graph, path=path, title="Ең қысқа жол: A -> O")

    print("\n--- 2. Жолды уақытша жабу тесті (Мысалы, E-H қабырғасын өшіру) ---")
    city_graph.remove_edge('E', 'H')
    path_alt, weight_alt, _, _ = dijkstra(city_graph, 'A', 'O', weight_key='weight')
    print(f"Жабылғаннан кейінгі жаңа маршрут: {' -> '.join(path_alt)}")
    print(f"Жаңа жалпы қашықтық: {weight_alt} км")
    
    draw_graph(city_graph, path=path_alt, title="Балама маршрут (E-H жабылғаннан кейін)")