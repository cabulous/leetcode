import copy
from collections import Counter
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        live_cells = {(r, c) for r, row in enumerate(board) for c, live in enumerate(row) if live}
        live_cells = self.next_round(live_cells)
        for r, row in enumerate(board):
            for c in range(len(row)):
                row[c] = int((r, c) in live_cells)

    def next_round(self, live):
        count = Counter(
            (nr, nc)
            for r, c in live
            for nr in range(r - 1, r + 2)
            for nc in range(c - 1, c + 2)
            if nr != r or nc != c
        )

        return {
            pair
            for pair in count
            if count[pair] == 3 or (count[pair] == 2 and pair in live)
        }


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows, cols = len(board), len(board[0])
        origin_board = copy.deepcopy(board)

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and origin_board[nr][nc] == 1:
                        live_neighbors += 1
                if origin_board[row][col] == 1 and (live_neighbors < 2 or 3 < live_neighbors):
                    board[row][col] = 0
                elif origin_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or 3 < live_neighbors):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0
