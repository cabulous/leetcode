from typing import List


# https://leetcode.com/problems/stamping-the-grid/discuss/1675412/JavaC%2B%2BPython-Calulate-the-sub-matrix-sum-twice
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        count = stampHeight * stampWidth

        first = [[0] * (cols + 1) for _ in range(rows + 1)]
        good = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                first[r + 1][c + 1] = first[r + 1][c] + first[r][c + 1] - first[r][c] + (1 - grid[r][c])
                if r + 1 >= stampHeight and c + 1 >= stampWidth:
                    nr = r + 1 - stampHeight
                    nc = c + 1 - stampWidth
                    if first[r + 1][c + 1] - first[nr][c + 1] - first[r + 1][nc] + first[nr][nc] == count:
                        good[r][c] += 1

        second = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                second[r + 1][c + 1] = second[r + 1][c] + second[r][c + 1] - second[r][c] + good[r][c]
        for r in range(rows):
            for c in range(cols):
                nr = min(r + stampHeight, rows)
                nc = min(c + stampWidth, cols)
                if grid[r][c] == 0 and second[nr][nc] - second[r][nc] - second[nr][c] + second[r][c] == 0:
                    return False

        return True
