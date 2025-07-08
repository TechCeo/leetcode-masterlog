# Reflection: 1751. Maximum Number of Events That Can Be Attended II

## 🔗 Problem Link

[1751. Maximum Number of Events That Can Be Attended II – LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)

---

## Problem Summary

Given a list of events, each with a start day, end day, and value, and an integer k representing the maximum number of events that can be attended, the goal is to determine the maximum sum of values obtainable by attending at most k non-overlapping events. You must attend the entire duration of an event if you choose to attend it, and events that touch on the same day are considered overlapping.

---

## Initial Struggles

The real insight came from recognizing this problem's similarity to the weighted interval scheduling problem — which is a classic DP use case. Since we’re picking k intervals with maximum total value and ensuring they don’t overlap, we need to:

- Sort the events by start time.

- Use binary search to efficiently find the next valid event after a given one.

- Use memoization to avoid recomputation across different states of (index, k_remaining).

This shifted the problem to a top-down recursive DP with caching, which passed all test cases efficiently.

---

## Breakthrough Moment

The real breakthrough came when I reframed the problem as a variation of the classic DP knapsack problem, with the added constraint of time-based overlap. Instead of picking items by weight, I was selecting events based on whether they overlapped and could still fit within the event schedule.

The second key piece was combining binary search with DP. By sorting the events by end time and using binary search to find the last event that ends before the current event starts, I could efficiently build a DP table where:
- dp[i][j] represents the maximum value using the first i events and attending j of them.

This hybrid of dynamic programming and binary search turned out to be the perfect match for this problem.

---

## Insights

- Don’t underestimate the power of binary search when searching for “next possible non-overlapping event.”
- DP + memoization isn’t always about building bottom-up tables — recursive + caching is often more intuitive and just as effective.
- Getting a TLE early was actually helpful — it forced me to rethink the core approach rather than over-optimize a flawed one.

---

## Complexity Summary

Time Complexity: O(n log n * k)
(n for events, log n for binary search, k for depth of decision tree)

Space Complexity: O(n * k)
due to memoization table and call stack (with lru_cache)

---

