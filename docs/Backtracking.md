# Backtracking

Here are 10 easy-level problems that are perfect for practicing Recursive Backtracking. They gradually introduce core concepts like making choices, exploring paths, maintaining state, and backtracking.

---

### Easy Backtracking Problems

1.  **Generate Binary Strings**
    * **Problem:** Given an integer `n`, print all binary strings of length `n`.
    * **Example:**
        * If `n = 2`, output: `00`, `01`, `10`, `11`
    * **Why it's easy:** This is the simplest form of backtracking. At each position, you have two choices (0 or 1). No complex constraints.

2.  **Generate All Permutations of a String (Unique Characters)**
    * **Problem:** Given a string `s` consisting of unique characters, print all its possible permutations.
    * **Example:**
        * If `s = "abc"`, output: `abc`, `acb`, `bac`, `bca`, `cab`, `cba`
    * **Why it's easy:** A classic permutation problem. You pick one character at a time from the available ones and recursively build the permutation. You'll need a way to track which characters have been used.

3.  **Generate All Subsets of a Set (Power Set)**
    * **Problem:** Given a set of distinct integers `nums`, return all possible subsets (the power set).
    * **Example:**
        * If `nums = [1, 2, 3]`, output: `[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]`
    * **Why it's easy:** For each element, you have two choices: either include it in the current subset or exclude it. This leads to a simple binary choice tree.

4.  **Find if a Subset Sums to Target**
    * **Problem:** Given an array of integers `nums` and an integer `target`, determine if there exists a subset of `nums` that sums up exactly to `target`. (Return `True` or `False`).
    * **Example:**
        * `nums = [3, 34, 4, 12, 5, 2]`, `target = 9` -> `True` (because `4 + 5 = 9` or `3 + 4 + 2 = 9`)
    * **Why it's easy:** Similar to generating subsets, but with a condition. At each step, decide whether to include the current number or not, and update the remaining `target`.

5.  **Combinations Sum I (Each number used at most once)**
    * **Problem:** Given an array of *distinct* integers `candidates` and a target integer `target`, find all unique combinations where the `candidates` numbers sum to `target`. Each number in `candidates` can be used **at most once**.
    * **Example:**
        * `candidates = [2, 3, 6, 7]`, `target = 7` -> `[[7]]`
        * `candidates = [10, 1, 2, 7, 6, 1, 5]`, `target = 8` -> `[[1,7], [1,2,5], [2,6], [1,1,6]]` (note: handle duplicates in candidates if they occur, and unique combinations in output)
    * **Why it's easy:** A step up from simple subset sum, as you need to build and store the combinations. The "at most once" constraint helps simplify the choices at each step.

6.  **Rat in a Maze (Path Exists)**
    * **Problem:** Given a 2D grid (maze) where `1` represents an open path and `0` represents a blocked wall, determine if there is a path from the top-left cell (0,0) to the bottom-right cell (N-1, N-1). You can only move up, down, left, or right.
    * **Example:**
        ```
        maze = [[1, 1, 0],
                [0, 1, 1],
                [0, 0, 1]]
        ```
        Output: `True`
    * **Why it's easy:** A fundamental pathfinding problem. At each cell, you try all 4 directions. Remember to mark visited cells to avoid cycles and backtrack if a path doesn't lead to the destination.

7.  **Generate Valid Parentheses (Simple Cases)**
    * **Problem:** Given an integer `n`, generate all combinations of well-formed parentheses of length `2n`.
    * **Example:**
        * If `n = 1`, output: `"()"`
        * If `n = 2`, output: `"()()"`, `"(())"`
    * **Why it's easy:** It involves balancing open and closed parentheses. The backtracking choices are "add an open parenthesis" or "add a closed parenthesis," with simple constraints (cannot add more than `n` open, cannot add more closed than open).

8.  **Letter Case Permutations**
    * **Problem:** Given a string `s`, we can transform every letter individually to be lowercase or uppercase to create a new string. Return a list of all possible strings we could create.
    * **Example:**
        * If `s = "a1b2"`, output: `["a1b2", "a1B2", "A1b2", "A1B2"]`
    * **Why it's easy:** For each character, if it's a digit, you have one choice. If it's a letter, you have two choices (lowercase or uppercase). A clear recursive structure.

9.  **Count Paths in a Grid (Right/Down Only)**
    * **Problem:** Given an `m x n` grid, starting from the top-left cell (0,0), find the number of unique paths to reach the bottom-right cell (m-1, n-1). You can only move right or down.
    * **Example:**
        * If `m = 3`, `n = 2`, output: `3` (Paths: R-D-D, D-R-D, D-D-R)
    * **Why it's easy:** A simpler grid traversal problem because there are only two allowed moves (no need to track visited cells, as you always move towards the destination). It's a good way to see how backtracking can count possibilities.

10. **Combination of Phone Number Letters**
    * **Problem:** Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. (Standard phone keypad mapping, e.g., '2' maps to 'abc', '3' to 'def').
    * **Example:**
        * If `digits = "23"`, output: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`
    * **Why it's easy:** For each digit in the input string, you iterate through the corresponding letters and recursively combine them. This is a good example of how to iterate through choices for each "slot" in the output.

---

When practicing these, focus on identifying:
* **Base Case(s):** When do you stop the recursion?
* **Choices:** What are the options at each step?
* **Constraints:** What rules limit your choices?
* **State:** What information do you need to pass to the next recursive call (e.g., current path, remaining target, visited cells)?
* **Backtracking Step:** How do you "undo" a choice to explore other possibilities? (This is crucial for "exploring all paths").