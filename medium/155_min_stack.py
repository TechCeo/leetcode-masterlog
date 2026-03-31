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
        """
        Using two stacks:
        1. self.stack: Stores all the elements.
        2. self.min_stack: Stores the minimum element present in the stack 
           at the time that specific element was pushed.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # The new minimum is the lesser of the current value 
        # and the previous minimum (if it exists)
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

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