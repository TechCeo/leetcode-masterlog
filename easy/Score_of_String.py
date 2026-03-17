class Solution:
    def scoreOfString(self, s: str) -> int:

        run_sum = 0
        for i in range(1, len(s)):
                run_sum += abs(ord(s[i]) - ord(s[i - 1]))

        return run_sum