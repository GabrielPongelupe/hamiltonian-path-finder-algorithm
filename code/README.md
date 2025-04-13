# 🧩 Understanding the Logic Behind the Hamiltonian Path Algorithm

### 1. This helper function checks whether a candidate vertex can be added to the current path.

```python
def is_safe(vertex, current_pos, route, adj_matrix):
```

__What it does:__
* ✅ Edge Check: Verifies if the previous vertex in the route is connected to the candidate vertex.
```python
if adj_matrix[route[current_pos - 1]][vertex] == 0:
    return False
```
* 🚫 Repetition Check: Ensures the vertex hasn’t already been visited.
```python
if vertex in route:
    return False
```
* ✅ If both conditions pass, the vertex is safe to add.

### 2. solve_path_util(adj_matrix, route, current_pos)
This is the recursive function that performs backtracking to explore all possible paths.
```python
def solve_path_util(adj_matrix, route, current_pos):
```
__What it does:__
* 🏁 Base Case: If all vertices have been included (current_pos == len(adj_matrix)), check if there’s an edge back to the starting vertex to form a cycle (if needed).
```python
if current_pos == len(adj_matrix):
    return adj_matrix[route[current_pos - 1]][route[0]] == 1
```
* 🔁 Recursive Exploration: Loop through each vertex (starting from 1, since 0 is the starting point).
```python
for candidate in range(1, len(adj_matrix)):
```
* ✅ Try Adding Vertex: If the candidate vertex is safe, add it to the route and continue recursively.
```python
if is_safe(candidate, current_pos, route, adj_matrix):
    route[current_pos] = candidate
```
* 🔙 Backtracking: If the recursive call fails, remove the vertex and try another.
```python
route[current_pos] = -1
```

### 3. solve_hamiltonian_path(adj_matrix)
This is the main function that initializes the path and starts the recursive process.
```python
def solve_hamiltonian_path(adj_matrix):
```

__What it does:__
* 🛣️ Initialize Route: Create a route list initialized with -1, and set the starting vertex (index 0) to 0.
```python
route = [-1] * len(adj_matrix)
route[0] = 0
```
* 🚀 Start Recursion: Begin solving from position 1 using solve_path_util.
```python
if not solve_path_util(adj_matrix, route, 1):
    return None
```
* ✅ Return Result: If a valid path is found, return it. Otherwise, return None.
