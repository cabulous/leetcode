from functools import lru_cache

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/solutions/623732/java-c-python-dp-prefixsum-in-matrix-clean-code/?orderBy=most_votes
class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.pre_sum = []

    def ways(self, pizza: list[str], k: int) -> int:
        self.rows = len(pizza)
        self.cols = len(pizza[0])
        self.pre_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        for r in range(self.rows - 1, -1, -1):
            for c in range(self.cols - 1, -1, -1):
                self.pre_sum[r][c] = self.pre_sum[r + 1][c] + self.pre_sum[r][c + 1] - self.pre_sum[r + 1][c + 1] + (
                        pizza[r][c] == 'A')

        return self.dp(0, 0, k - 1)

    @lru_cache(None)
    def dp(self, row, col, cuts):
        if self.pre_sum[row][col] == 0:
            return 0

        if cuts == 0:
            return 1

        res = 0

        for nr in range(row + 1, self.rows):
            if self.pre_sum[row][col] - self.pre_sum[nr][col] > 0:
                res += self.dp(nr, col, cuts - 1)
                res %= MOD

        for nc in range(col + 1, self.cols):
            if self.pre_sum[row][col] - self.pre_sum[row][nc] > 0:
                res += self.dp(row, nc, cuts - 1)
                res %= MOD

        return res
