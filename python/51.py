from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.solution = []

    def dfs(self, queens, xy_sum, xy_dif):
        row = len(queens)
        if row == self.n:
            self.solution.append(queens)
            return
        for col in range(self.n):
            if col not in queens and row + col not in xy_sum and row - col not in xy_dif:
                self.dfs(queens + [col], xy_sum + [row + col], xy_dif + [row - col])

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in self.solution]
