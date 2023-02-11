from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows_count = len(board)
        cols = list(range(rows_count))
        cells = [None] * (rows_count ** 2 + 1)
        curr_cell = 1

        for r in range(rows_count - 1, -1, -1):
            for c in cols:
                cells[curr_cell] = (r, c)
                curr_cell += 1
            cols.reverse()

        dist = [-1] * (rows_count ** 2 + 1)
        dist[1] = 0
        queue = deque([1])

        while queue:
            curr_cell = queue.popleft()
            for next_cell in range(curr_cell + 1, min(curr_cell + 6, rows_count ** 2) + 1):
                r, c = cells[next_cell]
                destination = board[r][c] if board[r][c] != -1 else next_cell
                if dist[destination] == -1:
                    dist[destination] = dist[curr_cell] + 1
                    queue.append(destination)

        return dist[-1]
