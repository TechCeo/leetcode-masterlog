"""
Problem 424: Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s consisting of only uppercase English characters and an integer k. 
You can choose up to k characters in the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring that contains only one distinct character.

Examples:
Input: s = "AABABBA", k = 1  → Output: 4  (change the second 'B' to 'A' to get "AAABBA" → "AAAA")
Input: s = "ABAB", k = 2     → Output: 4  (change both 'B' to 'A')

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test
from collections import Counter


# Brute-force solution
class BruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(n^2 * 26) – Check all substrings and count character frequencies.
        Space: O(n)
        """
        n = len(s)
        max_len = 0

        for i in range(n):
            count = Counter()
            for j in range(i, n):
                count[s[j]] += 1
                most_freq = count.most_common(1)[0][1]
                if (j - i + 1) - most_freq <= k:
                    max_len = max(max_len, j - i + 1)
        return max_len


# Optimized solution using sliding window
class SlidingWindow:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(n) – Right pointer moves through the string once, left only shifts forward.
        Space: O(26) – Constant space for character counts.
        """
        count = {}
        max_freq = 0
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # If window is invalid (too many replacements), move left pointer
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


if __name__ == "__main__":
    print("\nBrute Force Solution:")
    bf = BruteForce()
    test(bf.characterReplacement, "AABABBA", 1, 4, "Test 1")
    test(bf.characterReplacement, "ABAB", 2, 4, "Test 2")
    test(bf.characterReplacement, "AAAA", 0, 4, "Test 3")

    print("\n--------------------------------------------------")
    print("Optimized Sliding Window Solution:")
    sw = SlidingWindow()
    test(sw.characterReplacement, "AABABBA", 1, 4, "Test 1")
    test(sw.characterReplacement, "ABAB", 2, 4, "Test 2")
    test(sw.characterReplacement, "AAAA", 0, 4, "Test 3")
