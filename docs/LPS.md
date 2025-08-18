# LPS (Longest Palindromic Substring)

Okay, the "Longest Palindromic Substring" (LPS) is a classic medium-level DP problem. To really grasp it, you need a solid foundation in string manipulation, basic algorithms, and the core concept of palindromes.

Here are 5 easy-level problems that build up the intuition and skills necessary to approach LPS, starting from the very basics:

---

### Easy-Level Problems to Understand Longest Palindromic Substring

1.  **Check if a String is a Palindrome:**
    * **Problem:** Given a string, determine if it reads the same forwards and backward (i.e., if it's a palindrome).
    * **Example:**
        * `"madam"` -> `True`
        * `"racecar"` -> `True`
        * `"hello"` -> `False`
    * **Why it helps:** This is the absolute fundamental building block. You'll need to know how to efficiently check if *any* given substring is a palindrome when solving LPS. It introduces concepts like two-pointers (one from start, one from end) or reversing and comparing.

2.  **Find All Substrings of a String:**
    * **Problem:** Given a string, generate and print all possible substrings.
    * **Example:**
        * `"abc"` -> `"a", "b", "c", "ab", "bc", "abc"`
    * **Why it helps:** LPS involves looking at *all possible substrings*. This problem helps you understand how to systematically generate every single substring, which is often done with nested loops (one for start index, one for end index). This brute-force approach (generate all substrings, then check if palindrome) is the naive way to solve LPS, so understanding this step is crucial.

3.  **Count Palindromic Substrings:**
    * **Problem:** Given a string, count how many palindromic substrings it contains. (Note: "a" and "b" in "aba" count as separate palindromes, as does "aba").
    * **Example:**
        * `"aba"` -> `3` (`"a"`, `"b"`, `"aba"`)
        * `"aaa"` -> `6` (`"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, `"aaa"`)
    * **Why it helps:** This moves beyond just checking *one* string. It forces you to iterate through substrings (like problem 2) and apply the palindrome check (problem 1). It also indirectly introduces the "expand around center" idea (though you might not implement it that way initially), as each character/pair can be a potential center.

4.  **Longest Palindrome from a Character Set:**
    * **Problem:** Given a string consisting of lowercase or uppercase English letters, find the length of the longest palindrome that can be built with those letters. Case sensitivity matters (e.g., "Aa" is not a palindrome).
    * **Example:**
        * `"abccccdd"` -> `7` ("dccaccd")
        * `"aabb"` -> `4` ("abba")
    * **Why it helps:** This problem shifts focus slightly from contiguous substrings to character frequencies. It helps you think about what properties a string needs to have to be a palindrome (most characters must appear an even number of times, at most one character can appear an odd number of times, which forms the center). While not directly about *substrings*, it deepens your understanding of palindrome structure.

5.  **Expand Around Center (Concept for LPS):**
    * **Problem:** This isn't a standalone coding problem as much as an algorithmic technique you can practice.
        * **Implement:** A function `expandAroundCenter(s, left, right)` that takes a string `s` and two pointers `left` and `right`. It should expand outwards from `left` and `right` as long as the characters match and are within bounds, returning the length of the palindrome found.
    * **Example:**
        * `expandAroundCenter("babad", 1, 1)` (center 'a') -> `3` (for "bab")
        * `expandAroundCenter("cbbd", 1, 2)` (center 'bb') -> `2` (for "bb")
    * **Why it helps:** This is *the core insight* for an efficient LPS solution. Instead of checking every possible substring (O(N^2) substrings) and then checking if each is a palindrome (O(N) for each, total O(N^3)), you can pick every possible center (single character or two adjacent characters) and expand outwards. This reduces the check for each potential palindrome to O(N), making the overall solution O(N^2) time.

By solving these progressively, you'll build the necessary skills to understand the efficient O(N^2) "Expand Around Center" solution for the Longest Palindromic Substring problem. Good luck!