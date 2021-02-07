import collections


# infinite
class Solution:
    def infinite(self, live):
        ctr = collections.Counter(
            (I, J)
            for i, j in live
            for I in range(i - 1, i + 2)
            for J in range(j - 1, j + 2)
            if J != j or I != i
        )
        return {
            ij
            for ij in ctr
            if ctr[ij] == 3 or (ctr[ij] == 2 and ij in live)
        }

    def gameOfLife(self, board: [[int]]) -> None:
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.infinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)


class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        neighbors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        rows, cols = len(board), len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    r, c = row + n[0], col + n[1]
                    if 0 <= r < rows and 0 <= c < cols and copy_board[r][c] == 1:
                        live_neighbors += 1
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


# in place
class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        neighbors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    r, c = row + n[0], col + n[1]
                    if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                        live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
