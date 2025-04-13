def is_safe(vertex, current_pos, route, adj_matrix):
    if adj_matrix[route[current_pos - 1]][vertex] == 0:
        return False
    if vertex in route:
        return False
    return True

def solve_path_util(adj_matrix, route, current_pos):
    if current_pos == len(adj_matrix):
        return adj_matrix[route[current_pos - 1]][route[0]] == 1

    for candidate in range(1, len(adj_matrix)):
        if is_safe(candidate, current_pos, route, adj_matrix):
            route[current_pos] = candidate
            if solve_path_util(adj_matrix, route, current_pos + 1):
                return True
            route[current_pos] = -1  # backtrack
    return False

def find_hamiltonian_path(adj_matrix):
    route = [-1] * len(adj_matrix)
    route[0] = 0  # starting from vertex 0

    if not solve_path_util(adj_matrix, route, 1):
        return None
    return route
