class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        r = 0
        c = cols - 1
        res = 0

        while r < rows and c >= 0:
            if grid[r][c] < 0:
                res += rows - r
                c -= 1
            else:
                r += 1

        return res
