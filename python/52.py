class Solution:

    def __init__(self):
        self.queen_count = 0
        self.res = []

    def totalNQueens(self, n: int) -> int:
        self.queen_count = n
        self.dfs([], [], [])

        return len(self.res)

    def dfs(self, queens, xy_sum, xy_diff):
        row = len(queens)

        if row == self.queen_count:
            self.res.append(queens)
            return

        for col in range(self.queen_count):
            if col not in queens and row + col not in xy_sum and row - col not in xy_diff:
                self.dfs(queens + [col], xy_sum + [row + col], xy_diff + [row - col])


class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = (1 << n) - 1

        def backtrack(row=0, next_row=0, xy_sum=0, xy_dif=0, count=0):
            if row == n:
                count += 1
            else:
                free_cols = cols & ~(next_row | xy_sum | xy_dif)
                while free_cols:
                    cur_col = - free_cols & free_cols
                    free_cols ^= cur_col
                    count = backtrack(
                        row + 1,
                        next_row | cur_col,
                        (xy_sum | cur_col) << 1,
                        (xy_dif | cur_col) >> 1,
                        count,
                    )
            return count

        return backtrack()
