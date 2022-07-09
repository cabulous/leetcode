# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103246/Python-DP-solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for p1 in range(1, len1 + 1):
            for p2 in range(1, len2 + 1):
                dp[p1][p2] = max(
                    dp[p1 - 1][p2],
                    dp[p1][p2 - 1],
                    dp[p1 - 1][p2 - 1] + (word1[p1 - 1] == word2[p2 - 1]),
                )

        return len1 + len2 - 2 * dp[-1][-1]
