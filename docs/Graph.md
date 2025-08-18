# Graph

Certainly! Let's break down what a **Graph** is in the context of Data Structures and Algorithms (DSA).

---

### What is a Graph in DSA?

In Data Structures and Algorithms, a **Graph** is a non-linear data structure that represents a set of objects (called **vertices** or **nodes**) where some pairs of these objects are connected by **links** (called **edges** or **arcs**).

Think of it like a network. For example:
* **Social Networks:** People are vertices, and friendships are edges.
* **Road Maps:** Cities are vertices, and roads connecting them are edges.
* **Computer Networks:** Computers are vertices, and network cables are edges.
* **Web Pages:** Web pages are vertices, and hyperlinks between them are edges.

Graphs are incredibly versatile and are used to model relationships between entities in various real-world scenarios.

---

### Key Components of a Graph

1.  **Vertices (Nodes):**
    * These are the fundamental entities or objects in the graph.
    * They are typically represented as circles or dots in a diagram.
    * For example, in a road map, cities like "Indore" or "Bhopal" would be vertices.

2.  **Edges (Arcs / Links):**
    * These represent the connections or relationships between pairs of vertices.
    * They are typically represented as lines connecting the circles/dots.
    * For example, a road connecting "Indore" and "Bhopal" would be an edge.

---

### Types of Graphs

Graphs can be classified based on various properties:

1.  **Directed Graph (Digraph):**
    * Edges have a direction, meaning the connection goes only one way.
    * Represented by arrows.
    * If there's an edge from A to B, it doesn't necessarily mean there's an edge from B to A.
    * **Example:** One-way streets, Twitter followers (A follows B doesn't mean B follows A).

2.  **Undirected Graph:**
    * Edges have no direction; the connection is bidirectional.
    * Represented by simple lines.
    * If there's an edge between A and B, it means A is connected to B, and B is connected to A.
    * **Example:** Friendships on Facebook (if A is friends with B, B is friends with A), two-way roads.

3.  **Weighted Graph:**
    * Each edge has an associated numerical value (weight or cost).
    * This weight can represent distance, time, cost, capacity, etc.
    * **Example:** Road map where edges have distances (km), network where edges have latency (ms).

4.  **Unweighted Graph:**
    * Edges have no associated weight; all connections are considered equal.
    * **Example:** A simple social network where you just care about who is connected to whom.

5.  **Cyclic Graph:**
    * Contains at least one cycle (a path that starts and ends at the same vertex, visiting other vertices in between).
    * **Example:** A circular road connecting cities.

6.  **Acyclic Graph:**
    * Contains no cycles.
    * A Directed Acyclic Graph (DAG) is particularly important in many algorithms (e.g., representing task dependencies).
    * **Example:** Prerequisites for courses (you can't take a course that depends on itself).

7.  **Connected Graph (for Undirected):**
    * There is a path between every pair of vertices.
    * **Example:** A single network where every computer can eventually send a message to any other computer.

8.  **Disconnected Graph (for Undirected):**
    * Consists of two or more connected components (separate "islands" of connected vertices).
    * **Example:** Two separate social networks that have no common users.

9.  **Sparse vs. Dense Graphs:**
    * **Sparse Graph:** A graph with relatively few edges compared to the maximum possible number of edges ($E \ll V^2$). Adjacency List is usually preferred.
    * **Dense Graph:** A graph with many edges, close to the maximum possible ($E \approx V^2$). Adjacency Matrix might be preferred.

---

### More Graph Terminology & Concepts

1.  **Degree of a Vertex:**
    * In an **undirected graph**, the degree of a vertex is the number of edges incident to it.
    * In a **directed graph**:
        * **In-degree:** The number of edges pointing *into* the vertex.
        * **Out-degree:** The number of edges pointing *out from* the vertex.
    * **Sum of Degrees Theorem:** In any undirected graph, the sum of the degrees of all vertices is equal to twice the number of edges ($ \sum_{v \in V} \text{deg}(v) = 2E $).

2.  **Path:**
    * A sequence of distinct vertices where each consecutive pair is connected by an edge.
    * **Length of a path:** The number of edges in the path.

3.  **Cycle:**
    * A path that starts and ends at the same vertex, visiting at least one other vertex in between.

4.  **Subgraph:**
    * A graph formed by a subset of the vertices and edges of another graph.

---

### Common Graph Representations

How do we store a graph in memory for algorithmic processing?

1.  **Adjacency List:**
    * **Concept:** For each vertex, store a list of its adjacent vertices.
    * **Implementation:** Typically an array of lists/sets, or a hash map where keys are vertices and values are lists/sets of neighbors.
    * **Pros:**
        * Space efficient for sparse graphs ($O(V+E)$ space).
        * Efficient to find all neighbors of a vertex ($O(\text{degree})$).
    * **Cons:**
        * Checking if an edge exists between two specific vertices can be $O(\text{degree})$ (or $O(V)$ in the worst case if the list is not sorted).
    * **Example (Undirected):**
        ```
        Graph with 4 vertices (0,1,2,3) and edges (0,1), (0,2), (1,3), (2,3)
        
        adj_list = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }
        ```

2.  **Adjacency Matrix:**
    * **Concept:** A $V \times V$ 2D array where `matrix[i][j]` is 1 (or `true`) if there's an edge from vertex `i` to vertex `j`, and 0 (or `false`) otherwise. For weighted graphs, it stores the weight.
    * **Implementation:** A 2D list or array.
    * **Pros:**
        * Fast $O(1)$ lookup to check if an edge exists between any two vertices.
        * Simple to implement.
    * **Cons:**
        * Space inefficient for sparse graphs (always uses $O(V^2)$ space).
        * Iterating all neighbors of a vertex takes $O(V)$ time.
    * **Example (Undirected):**
        ```
          0 1 2 3
        0[0 1 1 0]
        1[1 0 0 1]
        2[1 0 0 1]
        3[0 1 1 0]
        ```

3.  **Edge List:**
    * **Concept:** A simple list of all edges in the graph. Each edge is represented as a tuple or an array, usually `(u, v)` for unweighted, or `(u, v, weight)` for weighted graphs.
    * **Implementation:** A list of tuples.
    * **Pros:**
        * Very simple to understand and implement.
        * Space efficient ($O(E)$ space, which is good for sparse graphs).
        * Easy to sort edges (e.g., for Kruskal's algorithm).
    * **Cons:**
        * Inefficient to find all neighbors of a given vertex (requires iterating through the entire list of edges, $O(E)$ time).
        * Inefficient to check if an edge between two specific vertices exists ($O(E)$ time).
    * **Example (Undirected, Unweighted):**
        ```
        edge_list = [
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3)
        ]
        ```
    * **Example (Directed, Weighted):**
        ```
        edge_list = [
            (0, 1, 5),  # edge from 0 to 1 with weight 5
            (0, 2, 3),
            (1, 3, 2)
        ]
        ```

---

---

### Common Graph Algorithms

Graphs are the basis for many fundamental algorithms:

* **Traversal Algorithms:**
    * **Breadth-First Search (BFS):** Explores all neighbor nodes at the current level before moving to the next level. Useful for finding shortest paths in unweighted graphs, finding connected components.
    * **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking. Useful for cycle detection, topological sorting, finding connected components.

* **Shortest Path Algorithms:**
    * **Dijkstra's Algorithm:** Finds the shortest paths from a single source vertex to all other vertices in a graph with non-negative edge weights.
    * **Bellman-Ford Algorithm:** Finds the shortest paths from a single source vertex to all other vertices in a graph that can have negative edge weights (and detects negative cycles).
    * **Floyd-Warshall Algorithm:** Finds all-pairs shortest paths in a weighted graph.

* **Minimum Spanning Tree (MST) Algorithms:**
    * **Prim's Algorithm:** Builds an MST by iteratively adding the cheapest edge from a growing tree to a new vertex.
    * **Kruskal's Algorithm:** Builds an MST by greedily adding the cheapest edges that do not form a cycle.

* **Other Important Algorithms:**
    * **Topological Sort:** Orders the vertices of a Directed Acyclic Graph (DAG) such that for every directed edge $u \to v$, $u$ comes before $v$ in the ordering.
    * **Detecting Cycles:** Crucial for many graph properties (e.g., in DAGs, bipartite graphs).
    * **Strongly Connected Components (SCCs):** In directed graphs, a set of vertices where every vertex is reachable from every other vertex within the set.

In DSA, understanding graphs is fundamental because they provide a powerful framework for modeling and solving complex problems involving relationships and networks.