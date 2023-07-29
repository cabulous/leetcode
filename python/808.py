# https://leetcode.com/problems/soup-servings/solutions/3831172/video-100-soup-servings-a-dive-into-dynamic-programming-and-probability/
class Solution:

    def __init__(self):
        self.memo = {}

    def soupServings(self, n: int) -> float:
        if n > 4451:
            return 1.0
        n = (n + 24) // 25
        return self.dp(n, n)

    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[i, j]
        if i <= 0 and j <= 0:
            return 0.5
        if i <= 0:
            return 1.0
        if j <= 0:
            return 0.0
        self.memo[i, j] = 0.25 * (
                self.dp(i - 4, j)
                + self.dp(i - 3, j - 1)
                + self.dp(i - 2, j - 2)
                + self.dp(i - 1, j - 3)
        )
        return self.memo[i, j]
