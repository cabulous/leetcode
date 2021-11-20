from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.grid = []
        self.res = 0
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.VISITED_MARK = -2

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0

        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid

        start_row, start_col = 0, 0
        empty = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] >= 0:
                    empty += 1
                if self.grid[row][col] == 1:
                    start_row, start_col = row, col

        self.backtrack(start_row, start_col, empty)

        return self.res

    def backtrack(self, row, col, remain):
        if self.grid[row][col] == 2 and remain == 1:
            self.res += 1
            return

        temp = self.grid[row][col]
        self.grid[row][col] = self.VISITED_MARK
        remain -= 1

        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                continue
            if self.grid[nr][nc] < 0:
                continue
            self.backtrack(nr, nc, remain)

        self.grid[row][col] = temp
