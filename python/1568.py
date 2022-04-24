import copy
from typing import List


# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/discuss/819303/Python-you-need-at-most-2-days
class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def minDays(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        copy_grid = copy.deepcopy(grid)
        count = self.no_islands(copy_grid)
        if count != 1:
            return 0

        for i in range(self.rows):
            for j in range(self.cols):
                copy_grid = copy.deepcopy(grid)
                copy_grid[i][j] = 0
                count = self.no_islands(copy_grid)
                if count != 1:
                    return 1

        return 2

    def no_islands(self, grid):
        res = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    res += 1
                    self.no_islands_recur(grid, i, j)
        return res

    def no_islands_recur(self, grid, i, j):
        if grid[i][j] == 0:
            return

        grid[i][j] = 0

        if i - 1 >= 0:
            self.no_islands_recur(grid, i - 1, j)
        if i + 1 < self.rows:
            self.no_islands_recur(grid, i + 1, j)
        if j - 1 >= 0:
            self.no_islands_recur(grid, i, j - 1)
        if j + 1 < self.cols:
            self.no_islands_recur(grid, i, j + 1)
