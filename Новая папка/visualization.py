# visualization.py
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph_obj, path=None, title="Ақылды қала графы"):
    G = nx.Graph()

    # Төбелер мен қабырғаларды қосу
    for u, neighbors in graph_obj.adj_list.items():
        for v, data in neighbors.items():
            G.add_edge(u, v, weight=data['weight'], time=data['time'])

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42) # Төбелердің тұрақты орналасуы үшін seed

    # Барлық қабырғаларды салу
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    edge_labels = {(u, v): f"{d['weight']}км" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')

    # Егер маршрут таңдалса, оны ерекшелеу (қызыл түспен)
    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color='pink')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='violet', node_size=700)

    plt.title(title)
    plt.axis('off')
    plt.show()