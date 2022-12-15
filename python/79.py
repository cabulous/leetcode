from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.is_matched(r, c, word):
                    return True

        return False

    def is_matched(self, row, col, chars):
        if len(chars) == 0:
            return True

        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return False

        if self.board[row][col] != chars[0]:
            return False

        found = False
        self.board[row][col] = '#'

        for dr, dc in self.directions:
            found = self.is_matched(row + dr, col + dc, chars[1:])
            if found:
                break

        self.board[row][col] = chars[0]

        return found
