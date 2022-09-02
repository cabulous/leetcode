import copy
from collections import Counter
from typing import List


# copy
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


# in-place
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                live = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live += 1
                if board[r][c] == 1 and (live < 2 or 3 < live):
                    board[r][c] = -1
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1


# infinite
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        live_cells = {
            (r, c)
            for r, row in enumerate(board)
            for c, live in enumerate(row)
            if live
        }

        next_live_cells = self.next_round(live_cells)

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = int((r, c) in next_live_cells)

    def next_round(self, live_cells):
        count = Counter(
            (nr, nc)
            for r, c in live_cells
            for nr in range(r - 1, r + 2)
            for nc in range(c - 1, c + 2)
            if (nr, nc) != (r, c)
        )
        return {
            pair
            for pair in count
            if count[pair] == 3 or count[pair] == 2 and pair in live_cells
        }
