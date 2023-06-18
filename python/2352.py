from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = Counter()
        for row in grid:
            count[str(row)] += 1

        res = 0
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            res += count[str(col)]

        return res
