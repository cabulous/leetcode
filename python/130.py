from typing import List


# https://leetcode.com/problems/surrounded-regions/discuss/1551841/Python-Very-simple-idea-DFS
class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def solve(self, board: List[List[str]]) -> None:
        if not any(board):
            return

        self.rows, self.cols = len(board), len(board[0])
        self.board = board

        for row in [0, self.rows - 1]:
            for col in range(self.cols):
                if board[row][col] == 'O':
                    self.dfs(row, col)

        for col in [0, self.cols - 1]:
            for row in range(self.rows):
                if board[row][col] == 'O':
                    self.dfs(row, col)

        self.flip()

    def dfs(self, row, col):
        self.board[row][col] = 'Z'
        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                continue
            if self.board[nr][nc] != 'O':
                continue
            self.dfs(nr, nc)

    def flip(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 'Z':
                    self.board[row][col] = 'O'
                elif self.board[row][col] == 'O':
                    self.board[row][col] = 'X'


# https://leetcode.com/problems/surrounded-regions/discuss/41630/9-lines-Python-148-ms
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not any(board):
            return

        rows, cols = len(board), len(board[0])
        save = [ij for k in range(rows + cols) for ij in ((0, k), (rows - 1, k), (k, 0), (k, cols - 1))]

        while save:
            i, j = save.pop()
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                board[i][j] = 'Z'
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        board[:] = [['XO'[c == 'Z'] for c in row] for row in board]
