from collections import defaultdict, Counter
from typing import List


class Solution:

    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.lookup = defaultdict(set)
        self.word = ''

    def exist(self, board: List[List[str]], word: str) -> bool:
        char_count = Counter(word)

        for r in range(len(board)):
            for c in range(len(board[0])):
                ch = board[r][c]
                if ch in char_count:
                    self.lookup[ch].add((r, c))

        if len(char_count) != len(self.lookup):
            return False

        for ch, count in char_count.items():
            if len(self.lookup[ch]) < count:
                return False

        self.word = word
        for r, c in self.lookup[word[0]]:
            self.lookup[word[0]].remove((r, c))
            if self.backtrack(r, c, 1):
                return True
            self.lookup[word[0]].add((r, c))

        return False

    def backtrack(self, row, col, word_idx):
        if word_idx == len(self.word):
            return True

        ch = self.word[word_idx]

        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if (nr, nc) in self.lookup[ch]:
                self.lookup[ch].remove((nr, nc))
                if self.backtrack(nr, nc, word_idx + 1):
                    return True
                self.lookup[ch].add((nr, nc))

        return False


class Solution:

    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.board = []
        self.rows = 0
        self.cols = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.backtrack(r, c, word):
                    return True

        return False

    def backtrack(self, row, col, chars):
        if len(chars) == 0:
            return True

        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return False

        if self.board[row][col] != chars[0]:
            return False

        found = False
        self.board[row][col] = '#'

        for dr, dc in self.directions:
            found = self.backtrack(row + dr, col + dc, chars[1:])
            if found:
                break

        self.board[row][col] = chars[0]

        return found
