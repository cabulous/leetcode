# https://leetcode.com/problems/unique-paths/solutions/1581998/c-python-5-simple-solutions-w-explanation-optimization-from-brute-force-to-dp-to-math/?envType=daily-question&envId=2023-09-03
import math


class Solution:

    def __init__(self):
        self.memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if (m, n) in self.memo:
            return self.memo[m, n]
        self.memo[m, n] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return self.memo[m, n]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        return dp[-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)
