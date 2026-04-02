"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Division between two integers should truncate toward zero.
"""

from typing import List
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Stack-based evaluation.
        
        Time Complexity: O(n) - Single pass through tokens.
        Space Complexity: O(n) - Stack can grow up to the number of operands.
        """
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # Use float division then int cast for "truncate toward zero"
                # This handles negative truncation correctly in Python 
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
                
        return stack[0]

if __name__ == "__main__":
    sol = Solution()

    test(sol.evalRPN, ["2", "1", "+", "3", "*"], 9, "Basic calculation")
    test(sol.evalRPN, ["4", "13", "5", "/", "+"], 6, "Division truncation")
    test(sol.evalRPN, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22, "Complex expression")
    
"""
Initial Intuition:
The logic follows the standard way humans process RPN: "If I see a number, I remember it. If I see an operator, I apply it to the last two numbers I remembered." 
This "Last-In, First-Out" behavior is the definition of a Stack.

Key Insight: Python's Division Quirk
The most common trap in this problem is integer division with negative numbers.

In Python, -1 // 10 evaluates to -1 (floor division).

LeetCode requires "truncation toward zero," where -1 / 10 should become 0.

Solution: Using int(float(b) / a) or int(b / a) forces Python to truncate the decimal toward zero rather than flooring it."""
