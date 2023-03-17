class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def __init__(self):
        self.grid = [[]]

    def construct(self, grid: list[list[int]]) -> 'Node':
        self.grid = grid
        return self.helper(0, 0, len(grid) - 1, len(grid[0]) - 1)

    def helper(self, row_start, col_start, row_end, col_end):
        if row_start > row_end or col_start > col_end:
            return None

        is_leaf = True
        val = self.grid[row_start][col_start]

        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if self.grid[r][c] != val:
                    is_leaf = False
                    break
            if not is_leaf:
                break

        if is_leaf:
            return Node(val == 1, True, None, None, None, None)

        row_mid = (row_start + row_end) // 2
        col_mid = (col_start + col_end) // 2

        top_left = self.helper(row_start, col_start, row_mid, col_mid)
        top_right = self.helper(row_start, col_mid + 1, row_mid, col_end)
        bottom_left = self.helper(row_mid + 1, col_start, row_end, col_mid)
        bottom_right = self.helper(row_mid + 1, col_mid + 1, row_end, col_end)

        return Node(False, False, top_left, top_right, bottom_left, bottom_right)
