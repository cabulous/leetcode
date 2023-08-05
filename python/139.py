class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [True] + [False] * len(s)
        max_len = max(map(len, wordDict))

        for end in range(1, len(s) + 1):
            for start in range(end - 1, max(-1, end - 1 - max_len), -1):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
                    break

        return dp[-1]
