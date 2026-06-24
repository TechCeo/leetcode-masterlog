"""
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Design a data structure that supports adding integers from a stream and
finding the median of all values added so far.

Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2.0
"""

import heapq
import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class MedianFinder:
    def __init__(self):
        # lower_half is a max-heap represented with negated values.
        self.lower_half = []
        self.upper_half = []

    def addNum(self, num: int) -> None:
        """
        Add a number and rebalance the two halves.

        Time Complexity: O(log n)
        Space Complexity: O(n) across all added values
        """
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def findMedian(self) -> float:
        """
        Return the middle value, or the mean of the two middle values.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])

        return (-self.lower_half[0] + self.upper_half[0]) / 2


def medians_after_each_addition(values: List[int]) -> List[float]:
    """Build a stream and collect each running median for local tests."""
    median_finder = MedianFinder()
    medians = []

    for value in values:
        median_finder.addNum(value)
        medians.append(median_finder.findMedian())

    return medians


if __name__ == "__main__":
    test(
        medians_after_each_addition,
        [1, 2, 3],
        [1.0, 1.5, 2.0],
        "Test 1 - Increasing stream",
    )
    test(
        medians_after_each_addition,
        [5, 3, 8, 9, 2],
        [5.0, 4.0, 5.0, 6.5, 5.0],
        "Test 2 - Unsorted stream",
    )
    test(
        medians_after_each_addition,
        [-1, -2, -3, -4],
        [-1.0, -1.5, -2.0, -2.5],
        "Test 3 - Negative values",
    )
    test(
        medians_after_each_addition,
        [2, 2, 2, 2],
        [2.0, 2.0, 2.0, 2.0],
        "Test 4 - Duplicate values",
    )


"""
Reflection:
The median divides the data into a lower half and an upper half. We represent
the lower half with a max-heap so its largest value is immediately available,
and the upper half with a min-heap so its smallest value is immediately
available. Python only provides a min-heap, so values in the lower heap are
stored as negatives.

After every insertion, the lower heap is kept either the same size as the
upper heap or one element larger. With an odd number of values, the lower root
is the median. With an even number, the two roots are the middle pair and their
average is the median.

Storing every streamed value requires O(n) space. Each insertion performs a
constant number of heap operations for O(log n) time, while reading the median
is O(1). Unlike sorting after every insertion, this preserves the work already
done as the stream grows.
"""
