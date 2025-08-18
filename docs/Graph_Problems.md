# Graph Problems

You're right! Starting with the absolute basics is crucial for building a strong foundation in graph algorithms. Let's break it down to the most fundamental concepts and problems.

Here are 10 even more basic graph problems to get you started, focusing on core concepts and simple traversals:

---

### More Basic Graph Problems

1.  **Graph Representation: Adjacency List & Adjacency Matrix**
    * **Problem:** Given the number of vertices `V` and a list of `E` edges (e.g., `(u, v)` for an edge between `u` and `v`), represent this graph using:
        1.  An Adjacency List (a list of lists/dictionaries).
        2.  An Adjacency Matrix (a 2D array).
    * **Goal:** Write functions or code snippets to build both representations from input edges.
    * **Why Basic:** This is the absolute first step for any graph problem. You need to know how to store and access graph data.

2.  **Basic Breadth-First Search (BFS) Traversal**
    * **Problem:** Given a graph (e.g., as an adjacency list) and a starting node, perform a BFS traversal and print the nodes in the order they are visited.
    * **Goal:** Implement BFS using a queue, ensuring you don't revisit nodes already processed in the current traversal path.
    * **Why Basic:** Directly applies the concept of level-by-level exploration.

3.  **Basic Depth-First Search (DFS) Traversal**
    * **Problem:** Given a graph (e.g., as an adjacency list) and a starting node, perform a DFS traversal and print the nodes in the order they are visited.
    * **Goal:** Implement DFS using recursion (or an explicit stack), again managing visited nodes.
    * **Why Basic:** Directly applies the concept of going deep before backtracking.

4.  **Find Direct Neighbors of a Node**
    * **Problem:** Given a graph and a specific node `X`, return a list of all nodes that are directly connected to `X` (its immediate neighbors).
    * **Goal:** Perform a direct lookup in your chosen graph representation (e.g., iterate through `adj_list[X]`).
    * **Why Basic:** Tests your understanding of how to access adjacency information from your chosen representation.

5.  **Check if an Edge Exists**
    * **Problem:** Given a graph and two nodes `u` and `v`, determine if there is a direct edge connecting `u` and `v`.
    * **Goal:** Check if `v` is in `u`'s adjacency list (or `adj_matrix[u][v]` is `1`).
    * **Why Basic:** Simple validation using your graph representation.

6.  **Count Nodes and Edges**
    * **Problem:** Given a graph (e.g., as an adjacency list), calculate and return the total number of vertices and the total number of edges in the graph. (For an undirected graph, each edge `(u,v)` is counted once).
    * **Goal:** Iterate through your representation and sum up appropriately.
    * **Why Basic:** Reinforces understanding of how graph elements are stored and counted.

7.  **Count Degree of Each Vertex**
    * **Problem:** Given an undirected graph, for each vertex, calculate and print its degree (the number of edges connected to it).
    * **Goal:** For an adjacency list, it's the length of the list for each vertex. For an adjacency matrix, it's the sum of the row/column.
    * **Why Basic:** Another simple property based on graph representation.

8.  **Grid Traversal: Check if a Cell is Reachable (Simple Maze)**
    * **Problem:** Given a 2D grid representing a simple maze (e.g., `.` for path, `#` for wall), a starting cell `(sr, sc)`, and a target cell `(tr, tc)`, determine if the target cell is reachable from the start. You can only move horizontally or vertically.
    * **Concept:** This is a direct application of BFS or DFS on a grid, where cells are nodes and valid moves are edges.
    * **Why Basic:** Introduces grid problems which are common graph variants, but without complex counting or shortest path logic.

9.  **Binary Tree Traversal: Inorder, Preorder, Postorder**
    * **Problem:** Given the root of a binary tree (a specific type of graph), implement its three standard traversal orders: Inorder (Left-Root-Right), Preorder (Root-Left-Right), and Postorder (Left-Right-Root).
    * **Concept:** These are fundamental applications of DFS, often implemented recursively.
    * **Why Basic:** Trees are fundamental graph structures, and these traversals are essential building blocks for many tree-related problems.

10. **Check if Graph is Empty**
    * **Problem:** Given a graph representation, determine if the graph is empty (contains no vertices or no edges).
    * **Goal:** Simple check on `V` and `E` counts or the representation itself.
    * **Why Basic:** A trivial check that confirms understanding of graph state.

---

This revised list provides a gentler introduction, starting with how to represent graphs, then moving to their most fundamental traversals and basic properties, before touching on very simple applications. Good luck!




Graph problems are a cornerstone of algorithmic thinking, covering a wide range of applications from social networks to routing. Here's a list of 10 graph problems, starting with easier ones and progressively increasing in complexity, to help you build a strong foundation.

---

### 10 Graph Problems to Practice

1.  **Basic Graph Traversal (BFS / DFS Implementation)**
    * **Concept:** This isn't usually a direct LeetCode problem, but it's the fundamental building block. Practice implementing Breadth-First Search (BFS) and Depth-First Search (DFS) on a given graph (represented as an adjacency list or matrix).
    * **Goal:** For a given starting node, print all reachable nodes in BFS order and then in DFS order. Understand how to keep track of visited nodes to prevent cycles.
    * **Why Easy:** Focuses on the core mechanics of graph exploration.

2.  **Find if Path Exists in Graph (LeetCode 1971)**
    * **Problem:** Given the number of nodes `n`, a list of `edges`, a `source` node, and a `destination` node, determine if there is a valid path from `source` to `destination`.
    * **Concept:** Direct application of either BFS or DFS. You simply need to explore from the source and see if the destination is reachable.
    * **Why Easy:** It's a straightforward reachability check.

3.  **Number of Connected Components in an Undirected Graph (LeetCode 323 - Premium, but a common problem)**
    * **Problem:** Given `n` nodes and a list of `edges` representing an undirected graph, return the number of connected components in the graph.
    * **Concept:** Iterate through all nodes. If a node hasn't been visited, start a BFS/DFS from it, increment your component count, and mark all reachable nodes as visited.
    * **Why Easy:** Builds on basic traversal by counting disjoint sets. Can also be solved efficiently with Disjoint Set Union (Union-Find).

4.  **Number of Islands (LeetCode 200)**
    * **Problem:** Given an `m x n` 2D binary grid representing a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    * **Concept:** This is a classic grid traversal problem. Treat the grid cells as nodes in a graph. For each '1' that hasn't been visited, start a BFS/DFS to explore its connected land cells, marking them visited, and increment your island count.
    * **Why Easy/Medium:** It's a graph problem disguised as a grid problem. Good for practicing multi-directional BFS/DFS.

5.  **Clone Graph (LeetCode 133)**
    * **Problem:** Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value and a list of its neighbors.
    * **Concept:** You need to traverse the graph (using BFS or DFS) and create new nodes corresponding to the original ones. Crucially, you must maintain a mapping between original nodes and their newly cloned counterparts to correctly set up the `neighbors` pointers and avoid infinite loops or re-cloning nodes.
    * **Why Medium:** Requires careful state management (visited map/dictionary) during traversal to ensure correct copying.

6.  **Is Graph Bipartite? (LeetCode 785)**
    * **Problem:** Given an undirected graph, return `true` if and only if it is bipartite. A graph is bipartite if the nodes can be divided into two disjoint sets, A and B, such that every edge connects a node in A to one in B.
    * **Concept:** Use BFS or DFS to try to 2-color the graph. Start from an uncolored node, assign it one color. Then assign its neighbors the opposite color. If you ever try to assign a node a color that conflicts with its existing color (i.e., an adjacent node has the same color), the graph is not bipartite.
    * **Why Medium:** Introduces graph coloring and cycle detection (specifically, odd-length cycles).

7.  **Course Schedule (LeetCode 207)**
    * **Problem:** There are `n` courses you have to take, labeled from `0` to `n - 1`. Some courses may have prerequisites. Given the total number of courses and a list of prerequisite pairs, return `true` if you can finish all courses.
    * **Concept:** This is a classic application of **Topological Sort**. The courses and their prerequisites form a Directed Acyclic Graph (DAG). If there's a cycle in the graph, you cannot complete all courses. You can solve this using BFS (Kahn's algorithm, tracking in-degrees) or DFS (detecting back-edges).
    * **Why Medium:** Requires understanding directed graphs and the concept of dependencies.

8.  **Shortest Path in Binary Matrix (LeetCode 1091)**
    * **Problem:** Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. A clear path is a path from the top-left cell to the bottom-right cell such that all visited cells are `0` and adjacent cells are connected in 8 directions (horizontally, vertically, or diagonally).
    * **Concept:** This is a shortest path problem on an unweighted graph, which is perfectly suited for **BFS**. The "distance" is the number of cells in the path. You'll need to explore all 8 neighbors.
    * **Why Medium:** Extends grid BFS to 8 directions and involves tracking distance.

9.  **Network Delay Time (LeetCode 743)**
    * **Problem:** You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as `[u, v, w]`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from `u` to `v`. A signal is sent from a given node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If not all nodes can receive the signal, return `-1`.
    * **Concept:** This is a **Shortest Path problem on a Weighted Graph**. Since edge weights (times) are non-negative, **Dijkstra's Algorithm** is the ideal solution. You'll use a min-priority queue to efficiently select the next node to visit.
    * **Why Medium:** Introduces weighted graphs and the need for Dijkstra's algorithm.

10. **Minimum Spanning Tree (Conceptual / Problem like LeetCode 1135: Connecting Cities With Minimum Cost)**
    * **Problem:** (General MST concept) Given a connected, undirected graph with weighted edges, find a subset of the edges that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
    * **Concept:** This is solved using either **Kruskal's Algorithm** (greedily picking the smallest edges if they don't form a cycle, typically using DSU) or **Prim's Algorithm** (greedily growing a tree from a starting node, typically using a min-priority queue).
    * **Why Medium/Hard:** These are more advanced graph algorithms that require understanding specific data structures (DSU for Kruskal's, Priority Queue for Prim's) and proofs of correctness.

---

These problems will help you understand different graph representations, traversal techniques, and key algorithms that are essential for solving more complex graph challenges. Good luck!