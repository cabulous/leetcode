from typing import List


# Hash By Path Signature
class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.visited = set()
        self.path_signature = []

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        res = set()

        for row in range(self.rows):
            for col in range(self.cols):
                self.path_signature = []
                self.dfs(row, col, '0')
                if self.path_signature:
                    res.add(tuple(self.path_signature))

        return len(res)

    def dfs(self, row, col, direction):
        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return
        if (row, col) in self.visited:
            return
        if self.grid[row][col] == 0:
            return

        self.visited.add((row, col))
        self.path_signature.append(direction)

        self.dfs(row + 1, col, 'D')
        self.dfs(row - 1, col, 'U')
        self.dfs(row, col + 1, 'R')
        self.dfs(row, col - 1, 'L')

        self.path_signature.append('0')
