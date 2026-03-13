from collections import deque

def maxSlidingWindow(nums, k):
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