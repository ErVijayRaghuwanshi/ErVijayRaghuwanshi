# Recursion

Here are 10 easy-level linked list problems, starting from the very basic:

1.  **Implement a Singly Linked List:**
    * **Problem:** Create a basic `Node` class (with `data` and `next` attributes) and a `LinkedList` class. Implement methods for `append(data)` (add to the end) and `display()` (print all elements).
    * **Why it's easy:** Focuses on fundamental node creation and traversal.

2.  **Count Nodes in a Linked List:**
    * **Problem:** Given the head of a linked list, return the total number of nodes in the list.
    * **Why it's easy:** Simple iteration through the list, incrementing a counter.

3.  **Search for an Element:**
    * **Problem:** Given the head of a linked list and a value, determine if the value exists in the list. Return `True` if found, `False` otherwise.
    * **Why it's easy:** Basic traversal and comparison.

4.  **Insert at Beginning:**
    * **Problem:** Given the head of a linked list and a new value, insert a new node with this value at the beginning of the list. Return the new head.
    * **Why it's easy:** Involves changing the head pointer, but no complex searching.

5.  **Delete Node by Value (First Occurrence):**
    * **Problem:** Given the head of a linked list and a value, delete the first node that contains that value. Handle the case where the head needs to be deleted.
    * **Why it's easy:** Introduces the concept of maintaining `previous` and `current` pointers.

6.  **Print Linked List in Reverse:**
    * **Problem:** Given the head of a linked list, print its elements in reverse order. *Hint: Recursion can be a very elegant solution here.*
    * **Why it's easy:** While recursion is involved, the base case and recursive step are straightforward for this specific problem.

7.  **Check if Linked List is Empty:**
    * **Problem:** Given the head of a linked list, return `True` if the list is empty, `False` otherwise.
    * **Why it's easy:** A simple null check on the head pointer.

8.  **Get Nth Node Data:**
    * **Problem:** Given the head of a linked list and an integer `n`, return the data of the `n`-th node (1-indexed). Assume `n` is always valid.
    * **Why it's easy:** Simple iteration, stopping after `n-1` steps.

9.  **Concatenate Two Linked Lists:**
    * **Problem:** Given the heads of two linked lists, `list1` and `list2`, append `list2` to the end of `list1`. Return the head of the concatenated list.
    * **Why it's easy:** Requires finding the tail of the first list and linking it to the head of the second.

10. **Find Middle Node:**
    * **Problem:** Given the head of a singly linked list, return the middle node of the list. If the list has an even number of nodes, return the second middle node (e.g., for 1->2->3->4, return 3).
    * **Why it's easy:** Can be solved with two pointers (slow and fast), a classic and simple linked list pattern.

These problems progressively introduce more concepts while remaining within the "easy" difficulty, making them ideal for someone just starting with linked lists. Good luck!