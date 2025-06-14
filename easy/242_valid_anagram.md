# 242. Valid Anagram

🔗 https://leetcode.com/problems/valid-anagram/

---

##  Problem Summary

Given two strings `s` and `t`, determine if `t` is an anagram of `s`.

An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

---

##  Reflection

This problem looked deceptively simple at first — just check if two strings are made up of the same characters. My initial instinct was to compare the sets of both strings:

However, I quickly realized this was flawed: sets ignore character frequency, so "aabb" and "ab" would incorrectly appear equal.

I moved on to using collections.Counter to track character frequencies. While this was a step forward and worked well, I still had to manage the dictionary manually — checking for key presence and count underflow introduced complexity and some subtle edge cases.

Eventually, I reached a cleaner and more optimal solution: using a fixed-size array of 26 integers to represent each lowercase English letter. This allowed me to:

Traverse both strings in a single loop

Increment for one string and decrement for the other

Confirm an anagram by ensuring the array ends up with all zeroes

This array-based approach gave me a time complexity of O(n) and constant space (O(1), bounded by the 26 letters), making it ideal for this problem.

---
## Key Takeaways

Be cautious when using set() for frequency-based problems

collections.Counter is powerful, but not always optimal

Fixed-size arrays are excellent for problems with bounded input domains

Optimal solutions often come from modeling the problem with the right data structure