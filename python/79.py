from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for r in range(self.rows):
            for c in range(self.cols):
                if self.backtrack(r, c, word):
                    return True

        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return False

        if self.board[row][col] != suffix[0]:
            return False

        found = False
        self.board[row][col] = '#'

        for dr, dc in self.directions:
            found = self.backtrack(row + dr, col + dc, suffix[1:])
            if found:
                break

        self.board[row][col] = suffix[0]

        return found
