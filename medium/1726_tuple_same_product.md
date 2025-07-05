# Reflection: 1726. Tuple with Same Product

## 🔗 Problem Link

[1726. Tuple with Same Product – LeetCode](https://leetcode.com/problems/tuple-with-same-product/)

## Problem Summary

Given a list of distinct positive integers, the goal is to count the number of tuples (a, b, c, d) such that a × b = c × d, where a, b, c, and d are all elements from the array and their positions are distinct.

---

## Initial Struggles

This problem initially felt approachable — just check all combinations of products — so I started with a brute-force solution using three nested loops and sets to detect valid products dynamically. It worked on small cases but unsurprisingly exceeded the time limit on larger inputs. That false sense of progress delayed the pivot to a better approach.

---

## Breakthrough Insight

The breakthrough came when I shifted from tracking actual tuple values to simply counting how many unique (a, b) pairs produced the same product. I realized that if a product appeared n times among the (a, b) pairs, we could form n × (n - 1) × 4 valid permutations of (a, b, c, d). The x4 factor accounts for the positional permutations within the tuples.

This combinatorial insight wasn’t immediately obvious — understanding how the count of pairs maps to total tuple permutations was key and required some thought and debugging.

---

## Final Approach

- Use a hashmap to count how many times each product occurs among (a, b) pairs.
- For each product with a count ≥ 2, calculate the number of valid permutations using n × (n - 1) × 4.
- Sum across all such products for the final result.

---

## Insights

- This problem reinforced how brute-force is often deceptively easy to write but rarely scales.
- Preprocessing data and converting the problem into a frequency-mapping exercise can lead to elegant, efficient solutions.
- It’s not just about checking pairs — it’s about understanding the underlying combinatorial structure.

---

## Time and Space Complexity

- Time Complexity: O(n²), where n is the number of elements in the input array (from the nested loop over pairs).
- Space Complexity: O(n²) in the worst case, to store all unique product counts.

---



