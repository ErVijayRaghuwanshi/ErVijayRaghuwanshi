# Recursion

here are 10 easy-level recursion problems, starting from the very basics. These problems are designed to help you grasp the core concepts of base cases, recursive steps, and how recursion breaks down larger problems.

1.  **Factorial of a Number:**
    * **Problem:** Write a recursive function to calculate the factorial of a non-negative integer `n`. (n! = n \* (n-1) \* ... \* 1, and 0! = 1)
    * **Example:** `factorial(5)` should return `120`.
    * **Why it's easy:** Classic recursive example, clear base case (0! or 1!), and simple recursive step.

2.  **Sum of Natural Numbers:**
    * **Problem:** Write a recursive function to find the sum of the first `n` natural numbers. (1 + 2 + ... + n)
    * **Example:** `sum_natural(4)` should return `10` (1+2+3+4).
    * **Why it's easy:** Similar to factorial, a straightforward additive recursive step.

3.  **Print Numbers from N to 1:**
    * **Problem:** Write a recursive function to print numbers from `n` down to 1.
    * **Example:** `print_n_to_1(5)` should print `5 4 3 2 1`.
    * **Why it's easy:** Introduces the concept of performing an action *before* the recursive call (or after, depending on the order you want).

4.  **Print Numbers from 1 to N:**
    * **Problem:** Write a recursive function to print numbers from 1 up to `n`.
    * **Example:** `print_1_to_n(5)` should print `1 2 3 4 5`.
    * **Why it's easy:** A slight twist on the previous problem, requiring the print statement after the recursive call.

5.  **Fibonacci Sequence (Nth term):**
    * **Problem:** Write a recursive function to find the `n`-th term of the Fibonacci sequence. (F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2) for n > 1)
    * **Example:** `fibonacci(6)` should return `8`.
    * **Why it's easy:** Introduces multiple recursive calls in one step, but the base cases are simple. (Note: A naive recursive Fibonacci is inefficient, but good for learning the concept).

6.  **Power of a Number:**
    * **Problem:** Write a recursive function to calculate `base` raised to the power of `exponent`. Assume `exponent` is a non-negative integer.
    * **Example:** `power(2, 3)` should return `8`.
    * **Why it's easy:** Can be solved with a simple multiplicative recursive step and a clear base case (`exponent == 0`).

7.  **Sum of Digits of a Number:**
    * **Problem:** Write a recursive function to calculate the sum of the digits of a given non-negative integer.
    * **Example:** `sum_digits(123)` should return `6`.
    * **Why it's easy:** Requires using the modulo operator (`%`) and integer division (`//`) to break down the number.

8.  **Reverse a String:**
    * **Problem:** Write a recursive function to reverse a given string.
    * **Example:** `reverse_string("hello")` should return `"olleh"`.
    * **Why it's easy:** Involves slicing the string and concatenating parts in reverse order, a good exercise in string manipulation with recursion.

9.  **Check Palindrome (String):**
    * **Problem:** Write a recursive function to check if a given string is a palindrome (reads the same forwards and backward).
    * **Example:** `is_palindrome("madam")` should return `True`. `is_palindrome("apple")` should return `False`.
    * **Why it's easy:** Combines checking first and last characters with a recursive call on the inner substring.

10. **Product of Array Elements:**
    * **Problem:** Given an array (or list) of numbers, write a recursive function to find the product of all elements in the array.
    * **Example:** `product_array([1, 2, 3, 4])` should return `24`.
    * **Why it's easy:** A good introductory problem to applying recursion to data structures like arrays/lists, with a simple base case (empty or single-element array).

These problems should provide a solid foundation for understanding and writing recursive functions. Remember to always identify your base case(s) and your recursive step!