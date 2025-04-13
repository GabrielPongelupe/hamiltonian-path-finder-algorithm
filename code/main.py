from hamiltonian import solve_hamiltonian_path

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    result = solve_hamiltonian_path(graph)
    if result:
        print("Hamiltonian Path found:", result)
    else:
        print("No Hamiltonian Path exists.")
