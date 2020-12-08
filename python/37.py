from collections import defaultdict


def solve_sudoku(self, board) -> None:
    if not board or not board[0]:
        return None

    def could_place(d, row, col):
        return d not in rows[row] and d not in cols[col] and d not in boxes[idx(row, col)]

    def place_number(d, row, col):
        board[row][col] = str(d)
        rows[row][d] += 1
        cols[col][d] += 1
        boxes[idx(row, col)][d] += 1

    def remove_number(d, row, col):
        board[row][col] = '.'
        del rows[row][d]
        del cols[col][d]
        del boxes[idx(row, col)][d]

    def place_next_numbers(row, col):
        if row == nn - 1 and col == nn - 1:
            nonlocal solved
            solved = True
        else:
            if col == nn - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)

    def backtrack(row=0, col=0):
        if board[row][col] == '.':
            for d in range(1, nn + 1):
                if could_place(d, row, col):
                    place_number(d, row, col)
                    place_next_numbers(row, col)
                    if not solved:
                        remove_number(d, row, col)
        else:
            place_next_numbers(row, col)

    n = 3
    nn = n * n
    rows = [defaultdict(int) for _ in range(nn)]
    cols = [defaultdict(int) for _ in range(nn)]
    boxes = [defaultdict(int) for _ in range(nn)]
    idx = lambda row, col: (row // n) * n + col // n
    solved = False

    for i in range(nn):
        for j in range(nn):
            if board[i][j] != '.':
                d = int(board[i][j])
                place_number(d, i, j)

    backtrack()

# def solve_sudoku(self, board) -> None:
#     if not board or not board[0]:
#         return None
#
#     def could_place(d, row, col):
#         return d not in rows[row] and d not in cols[col] and d not in boxes[box_index(row, col)]
#
#     def place_number(d, row, col):
#         board[row][col] = str(d)
#         rows[row][d] += 1
#         cols[col][d] += 1
#         boxes[box_index(row, col)][d] += 1
#
#     def remove_number(d, row, col):
#         board[row][col] = '.'
#         del rows[row][d]
#         del cols[col][d]
#         del boxes[box_index(row, col)][d]
#
#     def place_next_numbers(row, col):
#         if row == nn - 1 and col == nn - 1:
#             nonlocal solved
#             solved = True
#         else:
#             if col == nn - 1:
#                 backtrack(row + 1, 0)
#             else:
#                 backtrack(row, col + 1)
#
#     def backtrack(row=0, col=0):
#         if board[row][col] == '.':
#             for d in range(1, nn + 1):
#                 if could_place(d, row, col):
#                     place_number(d, row, col)
#                     place_next_numbers(row, col)
#                     if not solved:
#                         remove_number(d, row, col)
#         else:
#             place_next_numbers(row, col)
#
#     n = 3
#     nn = n * n
#     rows = [defaultdict(int) for _ in range(nn)]
#     cols = [defaultdict(int) for _ in range(nn)]
#     boxes = [defaultdict(int) for _ in range(nn)]
#     box_index = lambda row, col: (row // n) * n + col // n
#     solved = False
#
#     for i in range(nn):
#         for j in range(nn):
#             if board[i][j] != '.':
#                 d = int(board[i][j])
#                 place_number(d, i, j)
#
#     backtrack()
