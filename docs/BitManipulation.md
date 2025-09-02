
---

# ⚡ Bit Manipulation (Python Guide)

Bit manipulation is about solving problems using binary operations directly.
This guide starts with **core basics**, then explains **7 key problems** in increasing difficulty.

---

## Step 1: Core Basics

Before diving into problems, let’s quickly review the essential operators:

* **Bitwise AND (`&`)**

  * Keeps only `1`s that appear in both numbers.

  ```python
  5 & 3  # 0101 & 0011 = 0001 → 1
  ```

* **Bitwise OR (`|`)**

  * Keeps `1` if at least one number has `1`.

  ```python
  5 | 3  # 0101 | 0011 = 0111 → 7
  ```

* **Bitwise XOR (`^`)**

  * Keeps `1` if bits differ.

  ```python
  5 ^ 3  # 0101 ^ 0011 = 0110 → 6
  ```

* **Bitwise NOT (`~`)**

  * Flips all bits (in Python, uses 2’s complement for negatives).

  ```python
  ~5  # = -6
  ```

* **Left shift (`<<`)**

  * Moves bits left (multiply by `2^n`).

  ```python
  5 << 2  # 00000101 << 2 = 00010100 → 20
  ```

* **Right shift (`>>`)**

  * Moves bits right (integer division by `2^n`).

  ```python
  20 >> 2  # 00010100 >> 2 = 00000101 → 5
  ```

---

## ✅ Easy Problems (Warm-up)

### 1. Single Number

**Problem:** Every number appears twice except one. Find it.

**Key Idea:**

* XOR cancels duplicates (`a ^ a = 0`).
* XORing all numbers leaves the unique element.

**Python Code:**

```python
def singleNumber(nums):
    result = 0
    for n in nums:
        result ^= n  # cancel duplicates
    return result

print(singleNumber([2, 2, 1]))  # Output: 1
```

---

### 2. Number of 1 Bits

**Problem:** Count how many `1`s are in the binary form of a number.

**Key Idea:**

* Use trick `n & (n - 1)` → removes the lowest set bit each time.

**Python Code:**

```python
def hammingWeight(n):
    count = 0
    while n:
        n &= (n - 1)  # drop lowest set bit
        count += 1
    return count

print(hammingWeight(11))  # 11 = 1011 → 3
```

---

### 3. Counting Bits

**Problem:** For every number `0..n`, count set bits.

**Key Idea:**

* DP relation:

  ```
  bits[i] = bits[i >> 1] + (i & 1)
  ```

  * `i >> 1` removes last bit
  * `(i & 1)` adds 1 if last bit is set

**Python Code:**

```python
def countBits(n):
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits

print(countBits(5))  # [0,1,1,2,1,2]
```

---

### 4. Reverse Bits

**Problem:** Reverse bits of a 32-bit unsigned integer.

**Key Idea:**

* Extract last bit (`n & 1`)
* Append it to result (shift left)
* Shift `n` right

**Python Code:**

```python
def reverseBits(n):
    result = 0
    for _ in range(32):  # 32-bit
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(reverseBits(43261596))  
# Input: 00000010100101000001111010011100
# Output: 964176192 (00111001011110000010100101000000)
```

---

## ⚡ Medium Problems (Deeper Logic)

### 5. Bitwise AND of Numbers Range

**Problem:** Find bitwise AND of all numbers in `[left, right]`.

**Key Idea:**

* The result only keeps the **common prefix bits** of `left` and `right`.
* Keep shifting right until they match, then shift back left.

**Python Code:**

```python
def rangeBitwiseAnd(left, right):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift

print(rangeBitwiseAnd(5, 7))  # Output: 4
```

---

### 6. Single Number III

**Problem:** Every number appears twice except two. Find both.

**Key Idea:**

* XOR all numbers → `a ^ b` (where `a` and `b` are unique).
* Find a distinguishing bit (`mask = xor & -xor`).
* Split numbers into two groups and XOR separately.

**Python Code:**

```python
def singleNumberIII(nums):
    xor = 0
    for n in nums:
        xor ^= n

    mask = xor & -xor  # lowest set bit
    a = b = 0
    for n in nums:
        if n & mask:
            a ^= n
        else:
            b ^= n
    return [a, b]

print(singleNumberIII([1,2,1,3,2,5]))  # [3,5]
```

---

### 7. Sum of Two Integers

**Problem:** Add two integers without `+` or `-`.

**Key Idea:**

* Use binary addition rules:

  * `sum = a ^ b` (XOR → add without carry)
  * `carry = (a & b) << 1`
  * Repeat until `carry = 0`

**Python Code:**

```python
def getSum(a, b):
    mask = 0xFFFFFFFF
    while b:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    # handle negative numbers in Python
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

print(getSum(1, 2))  # Output: 3
```

---

## 🚀 Extra Tricks & Notes

* **Check if number is power of 2:**

  ```python
  def isPowerOfTwo(n):
      return n > 0 and (n & (n - 1)) == 0
  ```

* **Get lowest set bit:**

  ```python
  lowest = n & -n
  ```

* **Clear lowest set bit:**

  ```python
  n = n & (n - 1)
  ```

* **Toggle k-th bit:**

  ```python
  n ^= (1 << k)
  ```

---

## 🔑 Recommended Learning Order

1. Single Number
2. Number of 1 Bits
3. Counting Bits
4. Reverse Bits
5. Bitwise AND of Numbers Range
6. Single Number III
7. Sum of Two Integers

---

