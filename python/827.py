from typing import List


# https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def move(x, y):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    yield nx, ny

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        index = 2
        areas = {0: 0}
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        res = max(areas.values())
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)

        return res
