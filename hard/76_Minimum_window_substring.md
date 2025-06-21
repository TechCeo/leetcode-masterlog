📘 Reflection – Minimum Window Substring

This problem tested my ability to work with sliding window techniques under strict constraints. I knew right away that a brute force approach—checking all substrings—would be computationally expensive. So, I leaned toward a window expansion/contraction approach, something I’d previously applied in substring search problems like “Permutation in String.”

Key Insight:
The key insight was recognizing that while both strings could contain duplicate characters, I needed to maintain frequency counts in real time. I used two hash maps—one to track what was needed (t_count) and another to track what was currently seen in the sliding window (window_count). I also needed a have/need counter system to check whether all characters in t were satisfied in the current window.

What I Enjoyed:
I really appreciated the elegance of expanding the right boundary to gather all required characters, and then contracting the left boundary to find the minimum valid window. That balance between exploration and optimization is what makes this technique particularly satisfying to implement.

Challenges:
Maintaining the frequency counts without allowing any off-by-one errors or logic gaps in boundary movement was tricky. Making sure the result was updated only when all characters were matched—and not before—required careful checks.

Broader Lessons:
This question was a reminder of the importance of breaking problems down into moving parts. Managing the internal state of a sliding window, coupled with clear logic for when to update the result, made the solution both efficient and readable.

Reusable Strategy:
This exact window management logic is something I can reuse in many real-world problems—think log parsing, real-time event processing, or string normalization tools.