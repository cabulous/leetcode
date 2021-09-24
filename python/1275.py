from typing import List


class Solution:
    def __init__(self):
        self.n = 3
        self.row = [0] * self.n
        self.col = [0] * self.n
        self.diag1 = 0
        self.diag2 = 0

    def tictactoe(self, moves: List[List[int]]) -> str:
        sign = 1
        n = self.n

        for r, c in moves:
            self.row[r] += sign
            self.col[c] += sign
            if r + c == n - 1:
                self.diag1 += sign
            if r - c == 0:
                self.diag2 += sign
            if abs(self.row[r]) == n or abs(self.col[c]) == n or abs(self.diag1) == n or abs(self.diag2) == n:
                return 'A' if sign == 1 else 'B'
            sign *= -1

        if len(moves) == n * n:
            return 'Draw'

        return 'Pending'
