## Explanation of the Bubble Sort Implementation

### Code Overview
Below is a detailed explanation of the Python implementation of Bubble Sort:

```python
arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

if __name__ == '__main__':
    bubble_sort(arr)
    print(arr)
```

### Step-by-Step Breakdown

1. **Input Array**:
   The array `arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]` is the input to be sorted.

2. **Function Definition**:
   The `bubble_sort(arr)` function performs the sorting. It uses a while-loop combined with nested iterations to repeatedly "bubble" the largest unsorted elements to their correct positions.

3. **Initialization**:
   - `n = len(arr)` determines the number of elements in the array.
   - `flag = True` is used as a control variable to track whether a swap occurred in the previous pass. If no swaps occur, the array is sorted.

4. **Outer Loop (`while flag`)**:
   - The `while` loop ensures the algorithm continues making passes through the array as long as swaps are happening (indicated by `flag = True`).
   - At the beginning of each pass, `flag` is reset to `False`.

5. **Inner Loop (`for i in range(1, n)`)**:
   - The `for` loop compares adjacent elements in the array, from `arr[0]` to `arr[n-1]`.
   - If `arr[i-1] > arr[i]`, the two elements are swapped using Python's tuple unpacking syntax: `arr[i-1], arr[i] = arr[i], arr[i-1]`.
   - When a swap occurs, `flag` is set to `True`, signaling that another pass through the array is needed.

6. **Swapping**:
   Swapping ensures the largest element of the unsorted portion of the array moves to the end of the array in each pass.

7. **Sorting Completion**:
   - When no swaps are made during a full pass, `flag` remains `False`, and the `while` loop terminates.
   - At this point, the array is sorted.

8. **Main Functionality**:
   The `if __name__ == '__main__':` block calls the `bubble_sort` function and prints the sorted array.

### Example Execution
#### Input:
```python
[-5, 3, 2, 1, -3, -3, 7, 2, 2]
```

#### Pass 1:
Swaps are made to push the largest value `7` to the end. Intermediate state:
```python
[-5, 3, 2, 1, -3, -3, 2, 2, 7]
```

#### Pass 2:
Pushes the next largest value to its position. Intermediate state:
```python
[-5, 2, 1, -3, -3, 2, 3, 2, 7]
```

#### Subsequent Passes:
Repeats until the array is fully sorted:
```python
[-5, -3, -3, 1, 2, 2, 2, 3, 7]
```

#### Final Output:
```python
[-5, -3, -3, 1, 2, 2, 2, 3, 7]
```

### Complexity
- **Time Complexity**:
  - Worst-case: \(O(n^2)\) for \(n\) elements in the array.
  - Best-case (already sorted): \(O(n)\) due to the `flag` optimization.
- **Space Complexity**: \(O(1)\) as sorting is done in place.

### Key Features of the Code
- **In-place Sorting**: The algorithm does not use extra space, modifying the input array directly.
- **Optimization with `flag`**: Prevents unnecessary passes when the array becomes sorted early.

This code provides a simple and clear implementation of Bubble Sort, suitable for learning and understanding the concept of iterative sorting algorithms.
