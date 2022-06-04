from typing import List


class Solution:

    def __init__(self):
        self.queen_count = 0
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.queen_count = n
        self.dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in item] for item in self.res]

    def dfs(self, queens, xy_sum, xy_diff):
        row = len(queens)

        if row == self.queen_count:
            self.res.append(queens)
            return

        for col in range(self.queen_count):
            if col not in queens and row + col not in xy_sum and row - col not in xy_diff:
                self.dfs(queens + [col], xy_sum + [row + col], xy_diff + [row - col])
