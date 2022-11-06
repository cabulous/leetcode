from typing import List


class Solution:
    def __init__(self):
        self.WORD_KEY = '$'
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.board = []
        self.rows = 0
        self.cols = 0
        self.res = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node[self.WORD_KEY] = word

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] in trie:
                    self.backtrack(r, c, trie)

        return self.res

    def backtrack(self, row, col, parent):
        letter = self.board[row][col]
        curr_node = parent[letter]

        word_match = curr_node.pop(self.WORD_KEY, False)
        if word_match:
            self.res.append(word_match)

        self.board[row][col] = '#'
        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if nr < 0 or self.rows <= nr or nc < 0 or self.cols <= nc:
                continue
            if not self.board[nr][nc] in curr_node:
                continue
            self.backtrack(nr, nc, curr_node)
        self.board[row][col] = letter

        if not curr_node:
            parent.pop(letter)
