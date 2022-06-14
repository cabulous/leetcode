# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103246/Python-DP-solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1] + (word1[r - 1] == word2[c - 1]))

        return rows + cols - 2 * dp[-1][-1]
