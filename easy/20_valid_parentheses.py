"""
20. Valid Parentheses

Given a string s containing just the characters:
'(', ')', '{', '}', '[' and ']',

Determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type
- Open brackets are closed in the correct order
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack Approach

        Push opening brackets onto stack.
        For closing brackets:
            - Check if stack is non-empty
            - Check if top matches

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:
                # Closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)

        return len(stack) == 0


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.isValid,
         "[]",
         True,
         "Simple Valid")

    test(sol.isValid,
         "([{}])",
         True,
         "Nested Valid")

    test(sol.isValid,
         "[(])",
         False,
         "Incorrect Order")

    test(sol.isValid,
         "(",
         False,
         "Single Open")

    test(sol.isValid,
         ")",
         False,
         "Single Close")

    test(sol.isValid,
         "",
         True,
         "Empty String")


"""
Reflection:
This is a classic stack problem where order matters.

The key idea:
- Opening brackets go onto the stack
- Closing brackets must match the most recent opening bracket

This enforces both:
- Correct pairing
- Correct ordering

A great example of using a stack to simulate real-world nesting behavior.
"""