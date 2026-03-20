"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string,
and decode it back to the original list.

Example:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encode each string as: <length>#<string>

        Example:
        ["abc", "de"] -> "3#abc2#de"

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []

        for word in strs:
            res.append(f"{len(word)}#{word}")

        return "".join(res)


    def decode(self, s: str) -> List[str]:
        """
        Parse the encoded string by reading length until '#',
        then extract that many characters.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        l = 0
        result = []

        while l < len(s):
            j = l

            # Find delimiter '#'
            while s[j] != "#":
                j += 1

            size = int(s[l:j])
            start = j + 1
            end = start + size

            result.append(s[start:end])
            l = end

        return result


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(lambda strs: sol.decode(sol.encode(strs)),
         ["lint", "code", "love", "you"],
         ["lint", "code", "love", "you"],
         "Basic Case")

    test(lambda strs: sol.decode(sol.encode(strs)),
         ["", "abc", "", "def"],
         ["", "abc", "", "def"],
         "Empty Strings")

    test(lambda strs: sol.decode(sol.encode(strs)),
         ["#", "##", "###"],
         ["#", "##", "###"],
         "Delimiter Edge Case")

    test(lambda strs: sol.decode(sol.encode(strs)),
         [],
         [],
         "Empty List")


"""
💭 Reflection:
This problem highlights the importance of designing a robust encoding scheme.

The key challenge is ensuring that the delimiter does not conflict with actual string content.
Using a length-prefix approach avoids ambiguity entirely.

A good reminder that sometimes the safest way to encode data is not by relying on separators,
but by explicitly storing structure (lengths) alongside the data.
"""