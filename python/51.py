class Solution:
    def __init__(self):
        self.n = 0
        self.output = []

    def dfs(self, queens, xy_sum, xy_dif):
        p = len(queens)
        if p == self.n:
            self.output.append(queens)
            return
        for q in range(self.n):
            if q not in queens and p + q not in xy_sum and p - q not in xy_dif:
                self.dfs(queens + [q], xy_sum + [p + q], xy_dif + [p - q])

    def solveNQueens(self, n: int) -> [[str]]:
        self.n = n
        self.dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in self.output]
