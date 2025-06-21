"""
Problem 76: Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the shortest substring of s such that every character in t (including duplicates) is present in the substring. 
If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Input: s = "OUZODYXAZV", t = "XYZ" → Output: "YXAZ"
Input: s = "xyz", t = "xyz"        → Output: "xyz"
Input: s = "x", t = "xy"           → Output: ""

Constraints:
- 1 <= s.length <= 1000
- 1 <= t.length <= 1000
- s and t consist of uppercase and lowercase English letters.
--------------------------------------------------

## My Thought Process

1. My first intuition was to expand a window over `s` and check if it contains all characters from `t`.
2. However, repeated full checks are inefficient. So I optimized by maintaining a running frequency count for characters in the window and using a two-pointer sliding window.
3. The key was knowing when the current window is valid and then minimizing it while keeping it valid.

"""

from collections import Counter
from typing import Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Returns the minimum window in s which will contain all the characters in t.

        Time: O(n)
        Space: O(k) — k is the size of t's unique character set.
        """

        if not t or not s:
            return ""

        t_count = Counter(t)
        window = {}
        have, need = 0, len(t_count)
        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink window from the left
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""



# Test cases
if __name__ == "__main__":
    def test(fn, args: Tuple[str, str], expected: str, test_name: str):
        result = fn(*args)
        if result == expected:
            print(f"{test_name} ✅ Passed")
        else:
            print(f"{test_name} ❌ Failed")
            print(f"   Input: {args}")
            print(f"   Output: {result}")
            print(f"   Expected: {expected}")

    sol = Solution()
    test(sol.minWindow, ("OUZODYXAZV", "XYZ"), "YXAZ", "Test 1")
    test(sol.minWindow, ("xyz", "xyz"), "xyz", "Test 2")
    test(sol.minWindow, ("x", "xy"), "", "Test 3")
    test(sol.minWindow, ("ADOBECODEBANC", "ABC"), "BANC", "Test 4")  # Classic example
