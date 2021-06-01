from typing import List


# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        seen = set()
        max_row, max_col = len(grid), len(grid[0])

        def dfs(row, col):
            if 0 <= row < max_row and 0 <= col < max_col and (row, col) not in seen and grid[row][col] == 1:
                seen.add((row, col))
                return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
            return 0

        return max(dfs(row, col) for row in range(max_row) for col in range(max_col))
