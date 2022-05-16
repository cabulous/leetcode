from typing import List


class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.visited = set()

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        res = set()
        for row in range(self.rows):
            for col in range(self.cols):
                path = []
                self.dfs(row, col, '0', path)
                if len(path) > 0:
                    res.add(tuple(path))

        return len(res)

    def dfs(self, row, col, direction, out):
        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return
        if (row, col) in self.visited:
            return
        if self.grid[row][col] == 0:
            return

        self.visited.add((row, col))
        out.append(direction)

        self.dfs(row - 1, col, 'U', out)
        self.dfs(row + 1, col, 'D', out)
        self.dfs(row, col - 1, 'L', out)
        self.dfs(row, col + 1, 'R', out)

        out.append('0')
