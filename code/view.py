import networkx as nx
import matplotlib.pyplot as plt
from hamiltonian import find_hamiltonian_path 

def plot_graph_with_path(adjacency_matrix, hamiltonian_route=None):
    graph = nx.Graph()

    vertex_count = len(adjacency_matrix)
    
    for i in range(vertex_count):
        graph.add_node(i)

    for i in range(vertex_count):
        for j in range(i + 1, vertex_count):
            if adjacency_matrix[i][j] == 1:
                graph.add_edge(i, j)

    positions = nx.spring_layout(graph, seed=42)

    nx.draw(graph, positions, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
    
    if hamiltonian_route:
        hamiltonian_edges = [(hamiltonian_route[i], hamiltonian_route[i + 1]) for i in range(len(hamiltonian_route) - 1)]
        hamiltonian_edges.append((hamiltonian_route[-1], hamiltonian_route[0]))  # Para formar o ciclo
        nx.draw_networkx_edges(graph, positions, edgelist=hamiltonian_edges, edge_color='red', width=2)

    plt.title("Graph with Hamiltonian Path" if hamiltonian_route else "Graph without Hamiltonian Path")
    plt.show()

if __name__ == "__main__":
    example_graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    route = find_hamiltonian_path(example_graph)
    
    plot_graph_with_path(example_graph, route)
