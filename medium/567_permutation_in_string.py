"""
Problem 567: Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given strings s1 and s2, return True if s2 contains a permutation of s1 as a substring.

A permutation means that s2 must contain a substring with the exact same characters (in any order) as s1.

Examples:
Input: s1 = "abc", s2 = "lecabee"     → Output: True ("cab" is in s2)
Input: s1 = "abc", s2 = "lecaabee"    → Output: False

Constraints:
- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of lowercase English letters only
"""

from typing import List
from collections import Counter
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


# Initial approach using Counter (dictionary-based frequency count)
class SlidingWindowCounter:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(n)
        Space: O(1) – Fixed alphabet size (26 lowercase letters)

        Strategy:
        - Use a sliding window of length len(s1)
        - Compare character frequency (Counter) of s1 and current window in s2
        - Update the window in O(1) per step
        """
        k = len(s1)
        if k > len(s2):
            return False

        set_s1 = Counter(s1)
        window = Counter(s2[:k])

        if window == set_s1:
            return True

        for right in range(k, len(s2)):
            left = right - k
            window[s2[right]] += 1
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            if window == set_s1:
                return True

        return False


# Optimized approach using fixed-size array for frequency count
class SlidingWindowArray:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(n)
        Space: O(1) – Only 26-character arrays used

        Optimized version of sliding window:
        - Replace Counter with a fixed 26-length array
        - Compare s1's frequency signature with each substring window
        """
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False


if __name__ == "__main__":
    print("\nSliding Window (Counter) Solution:")
    sol1 = SlidingWindowCounter()
    test(sol1.checkInclusion, "abc", "lecabee", True, "Test 1")
    test(sol1.checkInclusion, "abc", "lecaabee", False, "Test 2")

    print("\nSliding Window (Array) Optimized Solution:")
    sol2 = SlidingWindowArray()
    test(sol2.checkInclusion, "abc", "lecabee", True, "Test 3")
    test(sol2.checkInclusion, "abc", "lecaabee", False, "Test 4")
    test(sol2.checkInclusion, "ab", "eidbaooo", True, "Test 5")
    test(sol2.checkInclusion, "ab", "eidboaoo", False, "Test 6")




"""
Reflection:

I initially solved this problem using Python’s Counter, leveraging its simplicity and clarity to quickly build a correct sliding window solution. 
This approach made it easy to reason about character frequencies and match substrings, but I recognized that using hash maps (Counter) introduces extra overhead in both time and space.

To optimize further, I transitioned to using fixed-size arrays of length 26 to represent the character counts. This avoids hashing altogether, 
improves comparison speed (constant-time list comparison), and guarantees O(1) space usage since the alphabet is fixed.
The two-pass journey not only solidified my grasp of sliding window techniques but also reinforced a key lesson: clarity first, then optimize for constraints. 
It mirrors real-world problem-solving — start with correctness, refine for efficiency.
"""