class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        neighbors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        rows, cols = len(board), len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    r = row + n[0]
                    c = col + n[1]
                    if 0 <= r < rows and 0 <= c < cols and copy_board[r][c] == 1:
                        live_neighbors += 1
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
