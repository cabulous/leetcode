class BinaryMatrix(object):
    def get(self, row: int, col: int):
        pass

    def dimensions(self):
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        curr_row, curr_col = 0, cols - 1

        while curr_row < rows and 0 <= curr_col:
            if binaryMatrix.get(curr_row, curr_col) == 0:
                curr_row += 1
            else:
                curr_col -= 1

        return curr_col + 1 if curr_col != cols - 1 else -1
