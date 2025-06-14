"""
Problem 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group the anagrams together.

An anagram is a string formed by rearranging the letters of another string.

Examples:
Input: ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: ["x"]
Output: [["x"]]

Input: [""]
Output: [[""]]

Constraints:
- 1 <= strs.length <= 1000
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test_unordered_groups
from typing import List


class FrequencySignature:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams using character frequency signature as dictionary key.

        Time: O(m * n) – m = number of words, n = max word length
        Space: O(m * n) – storing frequency tuples and result groups
        """
        groups = {}
        for word in strs:
            rep = [0] * 26
            for char in word:
                rep[ord(char) - ord("a")] += 1
            key = tuple(rep)
            groups.setdefault(key, []).append(word)
        return list(groups.values())


if __name__ == "__main__":
    print("\nFrequency Signature Solution:")
    solver = FrequencySignature()
    test_unordered_groups(solver.groupAnagrams, 
                          ["act", "pots", "tops", "cat", "stop", "hat"],
                          [["hat"], ["act", "cat"], ["stop", "pots", "tops"]],
                          "Test 1")
    test_unordered_groups(solver.groupAnagrams, [""], [[""]], "Test 2")
    test_unordered_groups(solver.groupAnagrams, ["x"], [["x"]], "Test 3")
