class BinaryMatrix(object):
    def get(self, row: int, col: int):
        pass

    def dimensions(self):
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        cur_row, cur_col = 0, cols - 1

        while cur_row < rows and cur_col >= 0:
            if binaryMatrix.get(cur_row, cur_col) == 0:
                cur_row += 1
            else:
                cur_col -= 1

        return cur_col + 1 if cur_col != cols - 1 else -1
