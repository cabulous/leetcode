from collections import defaultdict


class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        if not board or not board[0]:
            return None

        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]
        idx = lambda row, col: (row // 3) * 3 + col // 3
        n = len(board)
        sudoku_solved = False

        def could_place(d, row, col):
            return d not in rows[row] and d not in cols[col] and d not in boxes[idx(row, col)]

        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[idx(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[idx(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            if row == n - 1 and col == n - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == n - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        backtrack()
