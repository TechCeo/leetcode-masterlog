"""
853. Car Fleet

There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers `position` and `speed`, both of length n.
- `position[i]` is the starting position of the i-th car.
- `speed[i]` is the speed of the i-th car.

Return the number of car fleets that will arrive at the destination.

A car fleet is a non-empty set of cars driving at the same speed in the same position.
A car that catches up to a fleet becomes part of it.

Constraints:
- 1 <= n <= 1000
- 0 < target <= 1000
- 0 < speed[i] <= 100
- 0 <= position[i] < target
- All position values are unique
"""

from typing import List
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

            # If current car catches up to previous fleet, merge
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.carFleet, 10, [1, 4], [3, 2], 1, "Test 1")
    test(sol.carFleet, 10, [4, 1, 0, 7], [2, 2, 1, 1], 3, "Test 2")
    test(sol.carFleet, 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3, "Test 3")
    test(sol.carFleet, 100, [0, 2, 4], [4, 2, 1], 1, "Test 4")


"""
Time Complexity: O(n log n)
  - Sorting the cars by starting position takes O(n log n)
  - Looping through the sorted cars is O(n)
  - Total: O(n log n)

Space Complexity: O(n)
  - We use a stack to keep track of fleets (up to n)

Reflection:
This problem is about understanding how cars merge into fleets based on their arrival time to the target.
Once I understood that faster cars can't pass but can catch up and merge, using time-to-target with a stack made the implementation clear and efficient.
"""