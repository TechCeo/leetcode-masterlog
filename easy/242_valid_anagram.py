"""
Problem 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return True if t is an anagram of s, else False.

Examples:
Input: s = "racecar", t = "carrace" → Output: True
Input: s = "jar", t = "jam"         → Output: False

Constraints:
- s and t consist of lowercase English letters
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


# Brute-force approach: sort and compare
class BruteForce:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n log n) – due to sorting
        Space: O(1) – ignoring sort temp memory
        """
        return sorted(s) == sorted(t)


# Optimized frequency count using a dictionary
class CharCount:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n) – count frequencies
        Space: O(1) – bounded to 26 lowercase letters
        """
        if len(s) != len(t):
            return False

        count = [0] * 26  # for a-z

        for cs, ct in zip(s, t):
            count[ord(cs) - ord('a')] += 1
            count[ord(ct) - ord('a')] -= 1

        return all(c == 0 for c in count)


if __name__ == "__main__":
    print("\nBrute Force Solution:")
    bf = BruteForce()
    test(bf.isAnagram, "racecar", "carrace", True, "Test 1")
    test(bf.isAnagram, "jar", "jam", False, "Test 2")
    test(bf.isAnagram, "a", "a", True, "Test 3")

    print("\n--------------------------------------------------")
    print("Character Count Optimized Solution:")
    opt = CharCount()
    test(opt.isAnagram, "racecar", "carrace", True, "Test 1")
    test(opt.isAnagram, "jar", "jam", False, "Test 2")
    test(opt.isAnagram, "a", "a", True, "Test 3")
