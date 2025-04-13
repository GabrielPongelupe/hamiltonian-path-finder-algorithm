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







