# hamiltonian-path-finder-algorithm

I chose to write this project in English so it could reach a wider audience. Since people from different parts of the world might visit my profile, I thought it would be a great way to make the content more accessible and maybe even connect with others who are also interested in algorithm design.

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

## 📊 Asymptotic Complexity Analysis
### Time Complexity
* Worst-case (O(N!)): In the worst case, the algorithm explores all possible permutations of the vertices. For a graph with N vertices, there are N! possible ways to arrange these vertices in a path. Thus, in the worst-case scenario, the algorithm must check every permutation, leading to a time complexity of O(N!).
* __Best-case (O(N)):__ In the best case, the algorithm may find the Hamiltonian path early, such as on the first few branches of the search tree. If a valid path is found quickly, the algorithm performs in a nearly linear fashion, giving a time complexity of O(N).
* __Average-case (Exponential Growth):__ The average-case complexity depends on the structure and density of the graph. In a dense graph, where many vertices are connected, the search tree grows rapidly, and the algorithm may explore many possible paths before finding a solution. This results in exponential time complexity, often approximated as O(2^N), where N is the number of vertices.



### Conclusion
The overall complexity is dominated by the factorial growth in the worst case, which makes the algorithm inefficient for large graphs. The actual performance can vary depending on the graph's structure, but in general, the Hamiltonian Path problem is NP-complete and has high computational demands as the number of vertices increases.

---

## ⚙️ Analysis Using the Master Theorem
The Master Theorem is typically applied to problems that exhibit a recursive structure, where the problem is divided into smaller subproblems of the same kind. This kind of recursive breakdown fits the recurrence relation:
```
T(n) = aT(n/b) + f(n)
```
Here:
* a is the number of subproblems,
* n/b represents the size of each subproblem,
* f(n) is the time complexity of dividing the problem and combining the results.

However, this approach doesn't align with the structure of the Hamiltonian Path algorithm. Instead of dividing the problem into smaller, manageable pieces, the algorithm explores multiple potential solutions through a backtracking process. This means the problem doesn't follow a clean recursive division of the input, which makes it incompatible with the type of recurrence required for applying the Master Theorem.

### ❓ Why the Master Theorem Doesn't Fit Here
The Master Theorem doesn't apply to the Hamiltonian Path algorithm because it doesn't divide the problem into smaller subproblems in a systematic way. Instead, the algorithm explores different path combinations and backtracks when necessary. The search space grows exponentially, and it doesn't fit the required format for using the Master Theorem, which relies on dividing the problem recursively. Therefore, the Master Theorem isn't useful for analyzing this algorithm.

---
## 🧠 Complexity Classification: P, NP, NP-Complete, and NP-Hard
### What is Complexity Classification?
Complexity classification refers to categorizing computational problems based on how their difficulty scales as the size of the input increases. These categories help us understand how efficiently a problem can be solved and what resources (time and space) are required to find a solution. The main classifications are:

* __P Class:__ Problems that can be solved in polynomial time. These are the easiest problems to solve, where the time taken grows at a manageable rate as the input size increases.

* __NP Class:__ Problems for which solutions can be verified in polynomial time. While it may be hard to find a solution, if you're given a solution, you can check if it’s correct quickly.

* __NP-Complete:__ These are the hardest problems within NP. If any NP-Complete problem can be solved in polynomial time, then all NP problems can be solved in polynomial time. However, no polynomial-time algorithm is currently known for any NP-Complete problem.

* __NP-Hard:__ Problems that are at least as hard as NP problems but may not be in NP. They might not even have a solution that can be verified in polynomial time.

### 🔍 Analysis
The Hamiltonian Path problem is categorized as NP-Complete:

- NP Class: For problems in this category, checking whether a given solution is correct can be done in polynomial time.

- NP-Complete: These problems are some of the most challenging in NP. A well-known problem like the Traveling Salesman Problem (TSP) can be transformed into a Hamiltonian Path problem, highlighting its complexity.

Despite being classified in NP, no polynomial-time algorithm has been found that can solve all instances of NP-Complete problems efficiently.

---

## 🖼️ Visualization
Visualization of the Hamiltonian Path solution provides a graphical representation to enhance understanding of the algorithm’s process and results. This feature is optional but serves as a great visual aid for anyone looking to see how the algorithm works in action.

### ✨ Features:
* All vertices and edges of the graph are displayed.

* The Hamiltonian Path, if found, is highlighted in red to distinguish it from the rest of the graph.

### 🏁 How to Run the Visualization:
If you'd like to visualize the graph and the Hamiltonian Path, follow these steps:
__1. Ensure Dependencies Are Installed__
Before running the visualization, make sure the required libraries are installed. If you haven’t already, you can install them using:
```bash
pip install networkx matplotlib
```
__2. Run the Visualization Script After setting up the project, navigate to the project directory and run the visualization script:__
```bash
python hamiltonianPathView.py
```
This will launch a graphical window showing the graph with vertices, edges, and the Hamiltonian Path in red, if one is found.

### 💡 Example:
When you run the visualization, you’ll see something like this:

![GRAPH_COMPLEMENT](/images/image.png)

- A graph with connected nodes (vertices) and edges linking them.

- If the Hamiltonian Path is discovered, it will be drawn in red, allowing you to visually follow the path through the graph.

This visual feedback helps to understand how the algorithm explores different paths and highlights the solution when found.

---


