import matplotlib.pyplot as plt
import networkx as nx

# Função para desenhar o grafo com personalizações
def draw_graph(adj_matrix, path=None):
    G = nx.Graph()

    # Adicionar os vértices e as arestas
    for i in range(len(adj_matrix)):
        for j in range(i + 1, len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)

    # Definir posições dos vértices (usando layout forçado)
    pos = nx.spring_layout(G)

    # Desenhar os vértices
    node_color = ['red' if node in path else 'lightblue' for node in G.nodes()]
    node_shape = ['s' if node in path else 'o' for node in G.nodes()]  # Quadrado para parte do caminho, círculo para os outros
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=700)

    # Desenhar as arestas
    edge_color = ['red' if (u in path and v in path) else 'gray' for u, v in G.edges()]
    edge_width = [3 if (u in path and v in path) else 1 for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=edge_width)

    # Desenhar os rótulos dos vértices
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    # Exibir o gráfico
    plt.title("Hamiltonian Path Visualization")
    plt.axis('off')
    plt.show()

# Exemplo de matriz de adjacência (para um grafo simples)
adj_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Exemplo de caminho Hamiltoniano (ordem dos vértices visitados)
path = [0, 1, 2, 3]

# Chamar a função de visualização
draw_graph(adj_matrix, path)
