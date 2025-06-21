# 76. Reflection – Minimum Window Substring

---
This problem tested my ability to work with sliding window techniques under tight constraints and is arguably one of the most challenging in this category. The difficulty doesn’t lie in the complexity of the logic itself, but rather in the precision required to track window boundaries, match character frequencies, and determine exactly when the window becomes valid.

I immediately ruled out a brute-force approach — checking all substrings would be too expensive. So, I leaned toward an expand-contract sliding window technique, something I’d previously applied in problems like “Permutation in String.”

The first question I asked was: “How do I know if a window contains all characters from t?” This led me to use a character frequency counter. But I also realized that matching presence alone wasn't enough — I needed to match exact counts. That’s when the have/need counter system came into play.

Once the current window satisfied all required characters (i.e., have == need), I checked if it was the smallest seen so far, then contracted the window from the left to try to find an even smaller valid substring. A key takeaway was that shrinking the window requires meticulous updates to tracking variables to maintain correctness.

From a systems perspective, this problem models how we might track minimum valid states in a live data stream — a useful skill for backend systems dealing with logs, metrics, or event processing pipelines.

---
## Key Insight
The core insight was realizing I needed two frequency maps: one to store the required counts from t (t_count), and another to track counts in the current window (window_count). Combined with the have/need logic, this allowed me to manage character validity efficiently and with precision.

## What I Enjoyed
I found the symmetry of expanding the right boundary to collect necessary characters, then contracting the left boundary to find the minimum window, particularly elegant. That balance between exploration and optimization is what makes this technique so satisfying.

## Challenges
Avoiding off-by-one errors when moving boundaries and ensuring result updates occurred only when all characters were matched took care and clarity in logic. Missing just one condition could easily break the validity checks.

## Broader Lessons
This problem reinforced the value of breaking problems into modular components: character tracking, window control, and result comparison. It also reminded me that readable code and logical flow are just as important as performance.

## Reusable Strategy
This pattern of sliding window with frequency counters and have/need tracking is reusable in various real-world applications like log window monitoring, input validation systems, or real-time substring analytics.
---
## Time Complexity: O(s + t)
We iterate through string s once using a sliding window and build a frequency map for t once. Each character in s is visited at most twice — once when expanding right and once when contracting left — making the total time linear.

## Space Complexity: O(t)
We store frequency counts for both t and the sliding window. Although the number of characters is limited to 52 (uppercase + lowercase English letters), the theoretical upper bound remains O(t).