class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = [0] + [len(s)] * len(s)

        for end in range(1, len(s) + 1):
            dp[end] = dp[end - 1] + 1
            for start in range(end):
                if s[start:end] in dictionary:
                    dp[end] = min(dp[end], dp[start])

        return dp[-1]
