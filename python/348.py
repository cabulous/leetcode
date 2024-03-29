# https://leetcode.com/problems/design-tic-tac-toe/discuss/343824/Python-O(1)-time-O(n)-space.-Detailed-explanation
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1

        if row + col == self.n - 1:
            self.diag1 += 1 if player == 1 else -1
        if row - col == 0:
            self.diag2 += 1 if player == 1 else -1

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n:
            return 1 if player == 1 else 2
        if abs(self.diag1) == self.n or abs(self.diag2) == self.n:
            return 1 if player == 1 else 2
        return 0
