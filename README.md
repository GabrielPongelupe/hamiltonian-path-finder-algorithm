# hamiltonian-path-finder-algorithm

This project explores the use of backtracking to solve the Hamiltonian Path problem, implemented in Python. The algorithm systematically searches for a path that visits each vertex in a graph exactly once, without forming a cycle. By recursively exploring all possible routes and backtracking when a dead-end is reached, the solution demonstrates how computationally intensive this problem can be, especially for larger graphs. This implementation was created as part of a coursework assignment in the Foundations of Algorithm Design and Analysis discipline at PUC Minas, focusing on understanding NP-complete problems and applying classic algorithmic strategies.

---

## 🚀 How to Run the Project

### ✅ Prerequisites

- Python 3.x installed  
- (Optional) `networkx` and `matplotlib` libraries for graph visualization  

You can install the required libraries using:

```bash
pip install -r requirements.txt
```
If a requirements.txt file is not provided, install the optional packages manually:

```bash
pip install networkx matplotlib
```
---

### 📂 Setup and Execution
1. Clone the repository

```bash
git clone git@github.com:GabrielPongelupe/hamiltonian-path-finder-algorithm.git
```

2. Navigate to the project folder
```
cd code
```

3. Run the main script to execute the Hamiltonian Path algorithm

```bash
python main.py
```
This script runs the backtracking algorithm and displays the result in the terminal.
If you want to see a graphical representation of the graph and the Hamiltonian path (if found):
```
python hamiltonianPathView.py
```
---

## 🧩 Understanding the Logic Behind the Hamiltonian Path Algorithm
The Hamiltonian Path algorithm using backtracking works by trying to construct a path that visits each vertex in a graph exactly once. Starting from an initial vertex, the algorithm recursively explores all unvisited neighbors, marking each visited vertex along the way. If it reaches a point where no unvisited adjacent vertices are available and the path is incomplete, it backtracks to the previous step and tries a different route. This process continues until a valid path covering all vertices is found or all possibilities are exhausted.

---

## 🔍 Step-by-Step Explanation of the Hamiltonian Path Solver
This section breaks down how the Hamiltonian Path algorithm using backtracking works in this Python implementation.
[See detailed explanation of the Hamiltonian Path in the code/README.md](code/README.md)

---

## Asymptotic Complexity Analysis
### Time Complexity
* Worst-case (O(N!)): In the worst case, the algorithm explores all possible permutations of the vertices. For a graph with N vertices, there are N! possible ways to arrange these vertices in a path. Thus, in the worst-case scenario, the algorithm must check every permutation, leading to a time complexity of O(N!).
* __Best-case (O(N)):__ In the best case, the algorithm may find the Hamiltonian path early, such as on the first few branches of the search tree. If a valid path is found quickly, the algorithm performs in a nearly linear fashion, giving a time complexity of O(N).
* __Average-case (Exponential Growth):__ The average-case complexity depends on the structure and density of the graph. In a dense graph, where many vertices are connected, the search tree grows rapidly, and the algorithm may explore many possible paths before finding a solution. This results in exponential time complexity, often approximated as O(2^N), where N is the number of vertices.



### Conclusion
The overall complexity is dominated by the factorial growth in the worst case, which makes the algorithm inefficient for large graphs. The actual performance can vary depending on the graph's structure, but in general, the Hamiltonian Path problem is NP-complete and has high computational demands as the number of vertices increases.

---

## Analysis Using the Master Theorem
The Master Theorem is typically applied to problems that exhibit a recursive structure, where the problem is divided into smaller subproblems of the same kind. This kind of recursive breakdown fits the recurrence relation:
```
T(n) = aT(n/b) + f(n)
```
Here:
* a is the number of subproblems,
* n/b represents the size of each subproblem,
* f(n) is the time complexity of dividing the problem and combining the results.

However, this approach doesn't align with the structure of the Hamiltonian Path algorithm. Instead of dividing the problem into smaller, manageable pieces, the algorithm explores multiple potential solutions through a backtracking process. This means the problem doesn't follow a clean recursive division of the input, which makes it incompatible with the type of recurrence required for applying the Master Theorem.

### Why the Master Theorem Doesn't Fit Here
The Hamiltonian Path algorithm works by exploring potential paths through a backtracking process, which is not based on a systematic problem subdivision. Unlike algorithms that divide the problem into smaller subproblems (as required for the Master Theorem), this algorithm attempts different path combinations and backtracks whenever a path doesn't work. The search space grows exponentially because the algorithm checks many possible configurations. Therefore, the problem cannot be expressed in the standard recurrence form of T(n) = aT(n/b) + f(n), which is a requirement for applying the Master Theorem.

As a result, the Master Theorem is not applicable here, as the algorithm does not divide the problem into smaller subproblems in a structured manner. The algorithm’s complexity arises from the exploration of possible paths, not from recursively solving smaller parts of the problem. Thus, the Master Theorem would not provide meaningful insights into the analysis of this algorithm.

























