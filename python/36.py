def is_valid_sudoku(self, board) -> bool:
    if not board or not board[0]:
        return False

    n = 3
    nn = n * n
    rows = [{} for _ in range(nn)]
    cols = [{} for _ in range(nn)]
    boxes = [{} for _ in range(nn)]
    idx = lambda row, col: (row // n) * n + col // n

    for row in range(nn):
        for col in range(nn):
            if board[row][col] != '.':
                d = int(board[row][col])
                box_index = idx(row, col)
                rows[row][d] = rows[row].get(d, 0) + 1
                cols[col][d] = cols[col].get(d, 0) + 1
                boxes[box_index][d] = boxes[box_index].get(d, 0) + 1
                if rows[row][d] > 1 or cols[col][d] > 1 or boxes[box_index][d] > 1:
                    return False
    return True

