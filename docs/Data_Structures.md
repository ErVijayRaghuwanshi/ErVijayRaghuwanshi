# Data Structures

For Google SDE III preparation, a strong grasp of Data Structures and Algorithms (DSA) is paramount, along with System Design and Behavioral skills. Here's a concise list of key DSA topics with descriptions:

1.  **Arrays & Strings:**
    * **Description:** Fundamental linear data structures. Arrays store elements in contiguous memory locations, allowing for O(1) random access. Strings are sequences of characters, often implemented as character arrays.
    * **Key Concepts:** Fixed vs. dynamic arrays, multi-dimensional arrays, string immutability, common string operations (substring, concatenation, regex), two-pointer techniques.
    * **Google Focus:** Efficient searching, sorting, manipulating, and identifying patterns within arrays and strings.

2.  **Linked Lists:**
    * **Description:** Linear data structures where elements are stored in nodes, with each node containing data and a reference (or link) to the next node. Can be singly, doubly, or circular.
    * **Key Concepts:** Traversal, insertion, deletion, reversing, cycle detection (Floyd's Tortoise and Hare), merging, finding middle elements.
    * **Google Focus:** Manipulating pointers efficiently, optimizing space, and solving problems involving dynamic data sequences.

3.  **Stacks & Queues:**
    * **Description:**
        * **Stack:** LIFO (Last-In, First-Out) data structure. Operations: `push` (add), `pop` (remove), `peek` (view top).
        * **Queue:** FIFO (First-In, First-Out) data structure. Operations: `enqueue` (add), `dequeue` (remove), `front/rear` (view ends).
    * **Key Concepts:** Implementations using arrays or linked lists, common applications (expression evaluation, function call stack, BFS, task scheduling).
    * **Google Focus:** Correct usage for specific problem types, handling edge cases, and understanding their role in algorithms like BFS and DFS.

4.  **Hash Tables (Hash Maps/Dictionaries):**
    * **Description:** Data structures that store key-value pairs, providing average O(1) time complexity for insertion, deletion, and retrieval. Uses a hash function to map keys to array indices.
    * **Key Concepts:** Hashing functions, collision resolution (chaining, open addressing), load factor, resizing.
    * **Google Focus:** Efficient lookups, frequency counting, deduplication, and solving problems that require quick access to data.

5.  **Trees:**
    * **Description:** Non-linear, hierarchical data structures where elements are organized in nodes connected by edges.
    * **Key Concepts:**
        * **Binary Trees:** Each node has at most two children.
        * **Binary Search Trees (BSTs):** Left subtree nodes are less than the root, right subtree nodes are greater.
        * **Balanced BSTs (AVL, Red-Black Trees):** Self-balancing trees that maintain logarithmic height, ensuring O(log N) operations.
        * **Heaps (Min-Heap, Max-Heap):** Complete binary trees satisfying the heap property (parent is always smaller/larger than children). Used for priority queues.
        * **Tries (Prefix Trees):** Tree-like data structures used for efficient retrieval of keys in a dataset of strings, especially for prefix matching.
    * **Google Focus:** Traversals (inorder, preorder, postorder, level-order), properties of different tree types, searching, insertion, deletion, finding LCA, and tree-specific optimizations.

6.  **Graphs:**
    * **Description:** Non-linear data structures consisting of nodes (vertices) and edges (connections between vertices). Can be directed/undirected, weighted/unweighted.
    * **Key Concepts:**
        * **Representations:** Adjacency matrix, adjacency list.
        * **Traversal:** Breadth-First Search (BFS), Depth-First Search (DFS).
        * **Shortest Path Algorithms:** Dijkstra's, Bellman-Ford (for negative weights), Floyd-Warshall (all-pairs).
        * **Minimum Spanning Tree:** Prim's, Kruskal's.
        * **Topological Sort:** For Directed Acyclic Graphs (DAGs).
        * **Cycle Detection, Connected Components, Strongly Connected Components.**
    * **Google Focus:** Graph traversal, pathfinding, network problems, understanding connectivity, and modeling real-world relationships.

### Algorithms

7.  **Recursion & Backtracking:**
    * **Description:**
        * **Recursion:** A function calling itself to solve smaller instances of the same problem. Essential for many tree and graph algorithms.
        * **Backtracking:** A general algorithmic technique for finding all (or some) solutions to computational problems, especially constraint satisfaction problems, by incrementally building candidates to the solutions and abandoning a candidate ("backtracking") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
    * **Key Concepts:** Base cases, recursive steps, recursion tree, memoization (for optimization).
    * **Google Focus:** Solving problems with natural recursive structure, exploring all possibilities, generating permutations/combinations, and understanding the trade-offs with iterative solutions.

8.  **Sorting & Searching:**
    * **Description:**
        * **Sorting:** Arranging elements in a specific order (e.g., Merge Sort, Quick Sort, Heap Sort, Insertion Sort, Bubble Sort).
        * **Searching:** Finding a specific element within a data structure (e.g., Linear Search, Binary Search).
    * **Key Concepts:** Time and space complexity analysis of various algorithms, choosing the appropriate algorithm for different scenarios.
    * **Google Focus:** Binary search variations (on rotated arrays, for specific ranges), efficient sorting for large datasets, and understanding stability and in-place properties.

9.  **Dynamic Programming (DP):**
    * **Description:** An algorithmic technique for solving complex problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid recomputing them.
    * **Key Concepts:** Optimal substructure, overlapping subproblems, memoization (top-down), tabulation (bottom-up), recognizing common DP patterns (knapsack, longest common subsequence, edit distance).
    * **Google Focus:** A critical topic. Identifying DP problems, formulating recurrence relations, and optimizing solutions for various complex optimization problems.

10. **Greedy Algorithms:**
    * **Description:** An algorithmic paradigm that makes the locally optimal choice at each step with the hope that this choice will lead to a globally optimal solution.
    * **Key Concepts:** Proving correctness (usually by exchange argument), understanding when greedy approach applies vs. when DP or other methods are needed.
    * **Google Focus:** Activity selection, Huffman coding, scheduling problems, minimum spanning trees (Prim's/Kruskal's).

11. **Bit Manipulation:**
    * **Description:** Performing operations directly on the bits of a number.
    * **Key Concepts:** Bitwise operators (`AND`, `OR`, `XOR`, `NOT`, shifts), checking/setting/clearing bits, counting set bits.
    * **Google Focus:** Optimizing space and time for certain problems, solving puzzles that leverage bitwise properties.

### Beyond Core DSA (Important for SDE III)

* **System Design:** This is *crucial* for SDE III. It involves designing scalable, reliable, and maintainable software systems. Not a DSA topic, but heavily reliant on your understanding of DSA trade-offs.
* **Object-Oriented Design (OOD):** Understanding SOLID principles, design patterns (Singleton, Factory, Observer, etc.), and how to structure code for maintainability and extensibility.
* **Concurrency & Multithreading:** Concepts like deadlocks, race conditions, mutexes, semaphores, and concurrent data structures.
* **Operating Systems & Computer Networks Basics:** Understanding processes, threads, memory management, TCP/IP, HTTP, DNS, etc. While not directly "DSA problems," they form the foundation for discussing system design and understanding performance.

For SDE III at Google, expect problems that might combine multiple DSA concepts, require nuanced understanding of time/space complexity, and demand a clear, concise, and well-tested coding solution, along with strong communication skills. Good luck!