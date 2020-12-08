def total_n_queens_bitmap(n: int) -> int:
    def backtrack(row=0, next_row=0, xy_sum=0, xy_dif=0, count=0):
        if row == n:
            count += 1
        else:
            free_cols = cols & ~(next_row | xy_sum | xy_dif)
            while free_cols:
                cur_col = - free_cols & free_cols
                free_cols ^= cur_col
                count = backtrack(
                    row + 1,
                    next_row | cur_col,
                    (xy_sum | cur_col) << 1,
                    (xy_dif | cur_col) >> 1,
                    count,
                )
        return count

    cols = (1 << n) - 1
    return backtrack()


def total_n_queens_backtrack(n: int) -> int:
    def backtrack(row=0, count=0):
        for col in range(n):
            if could_place(row, col):
                place_queen(row, col)
                if row + 1 == n:
                    count += 1
                else:
                    count = backtrack(row + 1, count)
                remove_queen(row, col)
        return count

    def could_place(row, col):
        return rows[col] + xy_sum[row + col] + xy_dif[row - col] == 0

    def place_queen(row, col):
        rows[col] = 1
        xy_sum[row + col] = 1
        xy_dif[row - col] = 1

    def remove_queen(row, col):
        rows[col] = 0
        xy_sum[row + col] = 0
        xy_dif[row - col] = 0

    rows = [0] * n
    xy_sum = [0] * (2 * n - 1)
    xy_dif = [0] * (2 * n - 1)
    return backtrack()
