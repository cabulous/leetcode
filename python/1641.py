# math - Combination
# https://en.wikipedia.org/wiki/Combination
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


# dp top down
# https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC%2B%2BPython-DP-O(1)-Time-and-Space
class Solution:
    def countVowelStrings(self, n: int) -> int:
        seen = {}

        def dp(n, k):
            if n == 1 or k == 1:
                return k
            if (n, k) in seen:
                return seen[n, k]
            seen[n, k] = sum(dp(n - 1, k) for k in range(1, k + 1))
            return seen[n, k]

        return dp(n, 5)


# dp  Bottom up, 1D DP
# https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC%2B%2BPython-DP-O(1)-Time-and-Space
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] + [1] * 5
        for i in range(1, n + 1):
            for k in range(1, 6):
                dp[k] += dp[k - 1]
        return dp[5]
