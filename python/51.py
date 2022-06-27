from typing import List


class Solution:

    def __init__(self):
        self.queen_count = 0
        self.cols = 0
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.queen_count = n
        self.cols = n

        self.helper([], [], [])

        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in row] for row in self.res]

    def helper(self, queens, xy_sum, xy_diff):
        if len(queens) == self.queen_count:
            self.res.append(queens)
            return

        row = len(queens)
        for col in range(self.cols):
            if col in queens:
                continue
            if row + col in xy_sum:
                continue
            if row - col in xy_diff:
                continue
            self.helper(queens + [col], xy_sum + [row + col], xy_diff + [row - col])
