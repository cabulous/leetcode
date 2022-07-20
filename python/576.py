from functools import lru_cache

MOD = 10 ** 9 + 7


class Solution:
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or m <= startRow or startColumn < 0 or n <= startColumn:
            return 1
        if maxMove == 0:
            return 0
        return sum([
            self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn),
            self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn),
            self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1),
            self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1),
        ]) % MOD


# https://leetcode.com/problems/out-of-boundary-paths/discuss/102993/Python-Straightforward-with-Explanation
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        curr_move = [[0] * n for _ in range(m)]
        curr_move[startRow][startColumn] = 1
        res = 0

        for _ in range(maxMove):
            next_move = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    val = curr_move[r][c]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            next_move[nr][nc] += val % modulo
                        else:
                            res += val % modulo
            curr_move = next_move

        return res % modulo
