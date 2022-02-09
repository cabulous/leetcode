from typing import List


# https://leetcode.com/problems/cherry-pickup/discuss/109909/Python-cleanandcommented-O(N3)-DP
class Solution:

    def __init__(self):
        self.memo = {}
        self.n = 0
        self.grid = []

    def cherryPickup(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == -1:
            return -1

        self.n = len(grid)
        self.grid = grid

        return max(self.dp(0, 0, 0, 0), 0)

    def dp(self, i1, j1, i2, j2):
        if (i1, j1, i2, j2) in self.memo:
            return self.memo[i1, j1, i2, j2]

        if self.n in (i1, j1, i2, j2):
            return -1

        if i1 == j1 == i2 == j2 == self.n - 1:
            return self.grid[-1][-1]

        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1:
            return -1

        comb_max = max(
            self.dp(i1 + 1, j1, i2 + 1, j2),
            self.dp(i1 + 1, j1, i2, j2 + 1),
            self.dp(i1, j1 + 1, i2 + 1, j2),
            self.dp(i1, j1 + 1, i2, j2 + 1),
        )

        if comb_max == -1:
            res = -1
        else:
            res = comb_max + self.grid[i1][j1]
            if i1 != i2 or j1 != j2:
                res += self.grid[i2][j2]

        self.memo[i1, j1, i2, j2] = res

        return res
