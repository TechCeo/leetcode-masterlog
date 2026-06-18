"""
Problem 399: Evaluate Division
https://leetcode.com/problems/evaluate-division/

You are given equations like a / b = value. Answer queries asking for the
division result between two variables.

If the answer cannot be determined, return -1.0.

Examples:
Input:
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0,0.5,-1.0,1.0,-1.0]
"""

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        """
        Weighted graph DFS.

        Treat each equation a / b = value as:
        - edge a -> b with weight value
        - edge b -> a with weight 1 / value

        Then each query is a path-product search.

        Time Complexity: O(q * (v + e)) in the worst case.
        Space Complexity: O(v + e)
        """
        graph = defaultdict(list)

        for (numerator, denominator), value in zip(equations, values):
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1 / value))

        def dfs(current: str, target: str, visited: set[str]) -> float:
            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)
                if result != -1.0:
                    return weight * result

            return -1.0

        answers = []
        for numerator, denominator in queries:
            if numerator not in graph or denominator not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(numerator, denominator, set()))

        return answers


def test_close(result, expected):
    if len(result) != len(expected):
        return False

    return all(abs(a - b) < 1e-5 for a, b in zip(result, expected))


def test_calc_equation(equations, values, queries, expected, name):
    result = Solution().calcEquation(equations, values, queries)

    if test_close(result, expected):
        print(f"{name} Passed")
    else:
        print(f"{name} Failed")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}")


if __name__ == "__main__":
    test_calc_equation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        [6.0, 0.5, -1.0, 1.0, -1.0],
        "Test 1 - Basic equation chain",
    )
    test_calc_equation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]],
        [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        [3.75, 0.4, 5.0, 0.2],
        "Test 2 - Multiple components",
    )
