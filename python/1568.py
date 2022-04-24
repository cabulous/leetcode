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

        grid_copy = copy.deepcopy(grid)
        count = self.count_island(grid_copy)
        if count != 1:
            return 0

        for i in range(self.rows):
            for j in range(self.cols):
                grid_copy = copy.deepcopy(grid)
                grid_copy[i][j] = 0
                count = self.count_island(grid_copy)
                if count != 1:
                    return 1

        return 2

    def count_island(self, grid):
        res = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    res += 1
                    self.recursive_disconnect_island(grid, i, j)
        return res

    def recursive_disconnect_island(self, grid, i, j):
        if grid[i][j] == 0:
            return

        grid[i][j] = 0

        if i - 1 >= 0:
            self.recursive_disconnect_island(grid, i - 1, j)
        if i + 1 < self.rows:
            self.recursive_disconnect_island(grid, i + 1, j)
        if j - 1 >= 0:
            self.recursive_disconnect_island(grid, i, j - 1)
        if j + 1 < self.cols:
            self.recursive_disconnect_island(grid, i, j + 1)
