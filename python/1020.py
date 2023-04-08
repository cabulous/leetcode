import copy

WATER = 0
LAND = 1


class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0

    def numEnclaves(self, grid: list[list[int]]) -> int:
        self.grid = copy.deepcopy(grid)
        self.rows = len(grid)
        self.cols = len(grid[0])

        for r in range(self.rows):
            for c in range(self.cols):
                on_edge = r in (0, self.rows - 1) or c in (0, self.cols - 1)
                if on_edge and self.grid[r][c] == LAND:
                    self.dfs(r, c)

        return sum(sum(row) for row in self.grid)

    def dfs(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == LAND:
            self.grid[row][col] = WATER
            self.dfs(row + 1, col)
            self.dfs(row, col + 1)
            self.dfs(row - 1, col)
            self.dfs(row, col - 1)
