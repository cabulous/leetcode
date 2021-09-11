from collections import defaultdict


class Solution:
    def __init__(self):
        self.board = []
        self.n = 0
        self.rows = [defaultdict(int) for _ in range(9)]
        self.cols = [defaultdict(int) for _ in range(9)]
        self.boxes = [defaultdict(int) for _ in range(9)]
        self.resolved = False

    def solveSudoku(self, board: [[str]]) -> None:
        if not board or not board[0]:
            return None

        self.board = board
        self.n = len(board)

        for r in range(9):
            for c in range(9):
                if self.board[r][c] != '.':
                    digit = int(self.board[r][c])
                    self.place_number(digit, r, c)

        self.backtrack()

    def could_place(self, digit: int, row: int, col: int) -> bool:
        box_index = self.get_box_index(row, col)
        return digit not in self.rows[row] and digit not in self.cols[col] and digit not in self.boxes[box_index]

    def place_number(self, digit: int, row: int, col: int):
        box_index = self.get_box_index(row, col)
        self.boxes[box_index][digit] += 1
        self.rows[row][digit] += 1
        self.cols[col][digit] += 1
        self.board[row][col] = str(digit)

    def remove_number(self, digit: int, row: int, col: int):
        box_index = self.get_box_index(row, col)
        del self.boxes[box_index][digit]
        del self.rows[row][digit]
        del self.cols[col][digit]
        self.board[row][col] = '.'

    def place_next_numbers(self, row: int, col: int):
        if row == self.n - 1 and col == self.n - 1:
            self.resolved = True
        else:
            if col == self.n - 1:
                self.backtrack(row + 1, 0)
            else:
                self.backtrack(row, col + 1)

    def backtrack(self, row=0, col=0):
        if self.board[row][col] == '.':
            for digit in range(1, 10):
                if self.could_place(digit, row, col):
                    self.place_number(digit, row, col)
                    self.place_next_numbers(row, col)
                    if not self.resolved:
                        self.remove_number(digit, row, col)
        else:
            self.place_next_numbers(row, col)

    def get_box_index(self, row: int, col: int) -> int:
        return (row // 3) * 3 + col // 3
