"""
155. Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

class MinStack:
    def __init__(self):
        # Each element is a tuple: (val, min_at_this_depth)
        self.stack = []

    def push(self, val: int) -> None:
        """
        Time: O(1)
        Space: O(n) - One tuple per element.
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        """Time: O(1)"""
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """Time: O(1)"""
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Time: O(1)"""
        return self.stack[-1][1]

def test_min_stack():
    try:
        obj = MinStack()
        results = []
        
        # Simulation of Example 1
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        results.append(obj.getMin()) # -3
        obj.pop()
        results.append(obj.top())    # 0
        results.append(obj.getMin()) # -2
        
        expected = [-3, 0, -2]
        if results == expected:
            print("MinStack Implementation ✅ Passed")
        else:
            print(f"MinStack Implementation ❌ Failed. Got {results}, Expected {expected}")
    except Exception as e:
        print(f"MinStack Implementation Error: {e}")

if __name__ == "__main__":
    test_min_stack()