# 49. Group Anagrams

🔗 https://leetcode.com/problems/group-anagrams/

---

## Problem Summary

Group all anagrams from a list of strings. An anagram contains the same characters but possibly in a different order.

---

## Reflection

Having previously solved the "Valid Anagram" problem, I came into this one with a well-formed instinct: character frequency is often the cleanest way to model anagrams. In "Valid Anagram", I used a fixed-size array of 26 elements to represent lowercase letter counts. That approach immediately translated well here — instead of checking for equality, I simply used the frequency array (as a tuple) as a dictionary key to group matching words.

Initially, I considered sorting each string and grouping by the sorted version, which works but has a higher time cost (O(n log n) per word). By switching to the frequency signature method, I achieved both better performance and greater control.

This problem also introduced a subtle edge case in testing: since the order of groups and the order of words within each group doesn’t matter, I couldn’t directly compare the function’s output with the expected result using a standard equality check. To address this, I wrote a dedicated test function that performs order-insensitive comparison for nested lists. It sorts both the outer and inner lists before comparing them. This new function is now part of my shared utils module and will help me accurately validate solutions to any future problems with unordered group output (e.g., combinations, permutations, grouping problems).

---

## Key Takeaways

- Reuse successful strategies across problems with similar constraints
- Choose frequency-based models over sorting when order isn’t required
- Use tuples to represent immutable, hashable keys
- Let problem constraints guide your choice of data structures (e.g., fixed-length arrays for 26 lowercase letters)
- Build reusable test utilities to support less straightforward output comparisons

---

## Complexity

- Time: O(m × n), where m = number of words, n = average word length
- Space: O(m × n), for storing frequency maps and grouped results
