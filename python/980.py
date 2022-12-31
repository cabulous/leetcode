from typing import List


class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited_mark = -2
        self.res = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        start_row, start_col = 0, 0
        empty_cells = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    start_row, start_col = r, c
                if grid[r][c] >= 0:
                    empty_cells += 1

        self.backtrack(start_row, start_col, empty_cells)

        return self.res

    def backtrack(self, row, col, remain):
        if self.grid[row][col] == 2 and remain == 1:
            self.res += 1
            return

        val = self.grid[row][col]
        self.grid[row][col] = self.visited_mark

        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] >= 0:
                self.backtrack(nr, nc, remain - 1)

        self.grid[row][col] = val
