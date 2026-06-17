"""
Problem 207: Course Schedule
https://leetcode.com/problems/course-schedule/

There are numCourses courses labeled from 0 to numCourses - 1.
Prerequisites are given as pairs [a, b], meaning you must take course b before
course a.

Return True if you can finish all courses, otherwise return False.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: True

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False
"""

from collections import deque
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Kahn's algorithm for topological sorting.

        If we can repeatedly take courses with zero prerequisites until all
        courses are taken, there is no cycle.

        Time Complexity: O(v + e) - Courses plus prerequisite edges.
        Space Complexity: O(v + e) - Adjacency list and indegree array.
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses


if __name__ == "__main__":
    sol = Solution()

    test(sol.canFinish, 2, [[1, 0]], True, "Test 1 - Simple dependency")
    test(sol.canFinish, 2, [[1, 0], [0, 1]], False, "Test 2 - Cycle")
    test(
        sol.canFinish,
        5,
        [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]],
        True,
        "Test 3 - Multiple prerequisite paths",
    )
    test(sol.canFinish, 3, [], True, "Test 4 - No prerequisites")
