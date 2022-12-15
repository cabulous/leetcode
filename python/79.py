from collections import defaultdict, Counter
from typing import List


class Solution:

    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.lookup = defaultdict(set)
        self.word = ''
        self.word_len = 0

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
        self.word_len = len(word)
        if len(self.lookup[word[-1]]) < len(self.lookup[word[0]]):
            self.word = word[::-1]

        for r, c in list(self.lookup[self.word[0]]):
            self.lookup[self.word[0]].remove((r, c))
            if self.dfs(r, c, 1):
                return True
            self.lookup[self.word[0]].add((r, c))

        return False

    def dfs(self, row, col, word_idx):
        if word_idx == self.word_len:
            return True

        ch = self.word[word_idx]

        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if (nr, nc) in self.lookup[ch]:
                self.lookup[ch].remove((nr, nc))
                if self.dfs(nr, nc, word_idx + 1):
                    return True
                self.lookup[ch].add((nr, nc))

        return False


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
