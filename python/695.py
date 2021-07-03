from typing import List


# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        assert len(grid) > 0 and len(grid[0]) > 0

        max_row, max_col = len(grid), len(grid[0])
        seen = set()

        def dfs(row, col):
            if row < 0 or row >= max_row or col < 0 or col >= max_col:
                return 0
            if (row, col) in seen:
                return 0
            seen.add((row, col))
            if grid[row][col] == 0:
                return 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        return max(dfs(row, col) for row in range(max_row) for col in range(max_col))
