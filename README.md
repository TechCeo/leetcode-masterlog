# leetcode-masterlog
Personal DSA + LeetCode solutions with detailed explanations in Python

Welcome to my personal repository of LeetCode solutions — structured, explained, and organized by difficulty and algorithmic pattern. 

---
## Repository Structure
leetcode-masterlog/
├── data-structures-in-python/
│ ├── Stack/
│ └── Queue/
│
├── easy/
├── medium/
├── hard/
│
├── utils/
│ ├── test_utils.py
│ └── binary_tree_utils.py
│
├── notebooks/
├── README.md


- `data-structures-in-python/`: Custom implementations of core data structures like Stack and Queue, using both array and linked list approaches. Each file includes tests and use-case comments.
- easy/, medium/, hard/: Python solutions organized by LeetCode difficulty level with reflection explaining the my thought process and approach.
- notebooks/: Jupyter notebooks with visual explanations or deep dives on selected topics.
- utils/: Shared utilities such as test runners (`test_utils.py`) and tree builders (`binary_tree_utils.py`) used across multiple solutions.
- Each solution includes both the .py implementation and a markdown explanation of the thought process.
---

## Testing Philosophy

Each problem and data structure implementation includes test cases to ensure correctness. The utils module provides reusable testing functions for various problem types eg:

- test(...): Generic test harness for functions with one or more inputs and a single expected output.

- test_unordered_groups(...): Used for problems like group anagrams, where output order may vary.

- binary_tree_utils(...): Specialized tester for binary tree problems — converts between list and tree representations.

---

## Goals

- Build a clear and consistent record of algorithmic problem solving through clean, well-tested Python code.
- Reinforce learning with structured markdown reflections that capture key insights, alternative approaches, and trade-offs for each problem.
- Reconstruct foundational data structures from scratch to internalize their mechanics and strengthen design intuition.
- Maintain a thoughtful, extensible codebase that demonstrates ongoing growth in software craftsmanship and technical fluency.

---

Feel free to explore, fork, or reference this repo as part of your own DSA journey!
