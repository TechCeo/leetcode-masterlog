from collections import deque
from typing import List, Tuple


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(len(nums)):

            # remove indices outside window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # record result
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


if __name__ == "__main__":

    def test(fn, args: Tuple[List[int], int], expected: List[int], test_name: str):
        result = fn(*args)
        if result == expected:
            print(f"{test_name} ✅ Passed")
        else:
            print(f"{test_name} ❌ Failed")
            print(f"   Input: {args}")
            print(f"   Output: {result}")
            print(f"   Expected: {expected}")

    sol = Solution()

    test(
        sol.maxSlidingWindow,
        ([1,2,1,0,4,2,6], 3),
        [2,2,4,4,6],
        "Test 1 - Example"
    )

    test(
        sol.maxSlidingWindow,
        ([4,3,5,4,3,3,6,7], 1),
        [4,3,5,4,3,3,6,7],
        "Test 2 - k=1"
    )

    test(
        sol.maxSlidingWindow,
        ([2,1,3], 3),
        [3],
        "Test 3 - k=len(nums)"
    )

    test(
        sol.maxSlidingWindow,
        ([1,2,3,4,5], 3),
        [3,4,5],
        "Test 4 - Increasing"
    )

    test(
        sol.maxSlidingWindow,
        ([5,4,3,2,1], 3),
        [5,4,3],
        "Test 5 - Decreasing"
    )

    test(
        sol.maxSlidingWindow,
        ([1,3,3,3,2], 3),
        [3,3,3],
        "Test 6 - Duplicates"
    )

    test(
        sol.maxSlidingWindow,
        ([-4,-2,-5,-1,-3], 2),
        [-2,-2,-1,-1],
        "Test 7 - Negatives"
    )

    test(
        sol.maxSlidingWindow,
        ([1,1,1,10,1,1], 3),
        [1,10,10,10],
        "Test 8 - Peak"
    )