"""
Problem 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Examples:
Input: "zxyzxyz"   → Output: 3  (e.g., "xyz")
Input: "xxxx"      → Output: 1  (e.g., "x")
Input: "abcabcbb"  → Output: 3  (e.g., "abc")

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


# Brute-force solution
class BruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n^3) – Generate all substrings and check for uniqueness.
        Space: O(n) – For storing substrings.
        """
        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if len(set(substring)) == len(substring):
                    max_len = max(max_len, j - i + 1)

        return max_len


# Optimized solution using sliding window
class SlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n) – Each character is visited at most twice.
        Space: O(n) – For the character set.
        """
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    print("\nBrute Force Solution:")
    bf = BruteForce()
    test(bf.lengthOfLongestSubstring, "zxyzxyz", 3, "Test 1")
    test(bf.lengthOfLongestSubstring, "xxxx", 1, "Test 2")
    test(bf.lengthOfLongestSubstring, "", 0, "Edge Case: Empty string")
    test(bf.lengthOfLongestSubstring, "abcabcbb", 3, "Test 3")

    print("\n--------------------------------------------------")
    print("Optimized Sliding Window Solution:")
    sw = SlidingWindow()
    test(sw.lengthOfLongestSubstring, "zxyzxyz", 3, "Test 1")
    test(sw.lengthOfLongestSubstring, "xxxx", 1, "Test 2")
    test(sw.lengthOfLongestSubstring, "", 0, "Edge Case: Empty string")
    test(sw.lengthOfLongestSubstring, "abcabcbb", 3, "Test 3")
