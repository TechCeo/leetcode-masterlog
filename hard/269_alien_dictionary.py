"""
Problem 269: Alien Dictionary
https://leetcode.com/problems/alien-dictionary/

Given a sorted list of words from an alien language, return a possible order
of the letters in that language. If no valid order exists, return an empty
string.

Examples:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Input: words = ["z","x","z"]
Output: ""
"""

from collections import defaultdict, deque
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Topological sort using Kahn's algorithm.

        Strategy:
        - Every unique character is a graph node.
        - Compare each pair of neighboring words.
        - The first different character gives one ordering rule.
        - Topologically sort those rules.

        Time Complexity: O(c) - c is the total number of characters.
        Space Complexity: O(u + e) - Unique characters plus ordering edges.
        """
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for char in word:
                indegree.setdefault(char, 0)

        for first, second in zip(words, words[1:]):
            min_length = min(len(first), len(second))

            if len(first) > len(second) and first[:min_length] == second:
                return ""

            for i in range(min_length):
                before = first[i]
                after = second[i]

                if before != after:
                    if after not in graph[before]:
                        graph[before].add(after)
                        indegree[after] += 1
                    break

        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(indegree):
            return ""

        return "".join(order)


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.alienOrder,
        ["wrt", "wrf", "er", "ett", "rftt"],
        "wertf",
        "Test 1 - Standard ordering",
    )
    test(sol.alienOrder, ["z", "x"], "zx", "Test 2 - Two letters")
    test(sol.alienOrder, ["z", "x", "z"], "", "Test 3 - Cycle")
    test(sol.alienOrder, ["abc", "ab"], "", "Test 4 - Invalid prefix")
    test(sol.alienOrder, ["a"], "a", "Test 5 - Single word")


"""
Reflection:
Alien Dictionary is Course Schedule wearing a trench coat. The hard part is
not the topological sort itself; it is building the graph correctly.

Only the first differing character between two adjacent words tells us
anything. After that first difference, the rest of the letters do not create
ordering rules. The prefix case is the sneaky invalid input: ["abc", "ab"]
can never be sorted lexicographically in a valid dictionary because the longer
word appears before its exact prefix.
"""
