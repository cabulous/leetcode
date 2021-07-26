from functools import lru_cache


class Solution:
    def __init__(self):
        self.modulo = 10 ** 9 + 7

    @lru_cache(2000)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
            return 1
        if maxMove == 0:
            return 0
        return (self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
                + self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
                + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
                + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
                ) % self.modulo


# https://leetcode.com/problems/out-of-boundary-paths/discuss/102993/Python-Straightforward-with-Explanation
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7
        nxt = [[0] * n for _ in range(m)]
        nxt[startRow][startColumn] = 1
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for time in range(maxMove):
            cur = nxt
            nxt = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= modulo
                        else:
                            res += val
                            res %= modulo

        return res
