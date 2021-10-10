from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        self.rows, self.cols = len(board), len(board[0])
        self.board = board

        for r in range(self.rows):
            for c in range(self.cols):
                if self.backtrack(r, c, word):
                    return True

        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False

        if self.board[row][col] != suffix[0]:
            return False

        resolved = False
        self.board[row][col] = '#'

        for dr, dc in self.directions:
            resolved = self.backtrack(row + dr, col + dc, suffix[1:])
            if resolved:
                break

        self.board[row][col] = suffix[0]

        return resolved
