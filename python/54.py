from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top = left = 0
        right = cols - 1
        bottom = rows - 1
        res = []

        while len(res) < rows * cols:
            for col in range(left, right + 1):
                res.append(matrix[top][col])

            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])

            if top != bottom:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])

            if left != right:
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return res


# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = 101
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        change_dir = 0
        row = col = 0
        res = [matrix[0][0]]
        matrix[0][0] = visited

        while change_dir < 2:
            while True:
                next_row = row + directions[cur_dir][0]
                next_col = col + directions[cur_dir][1]
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    break
                if matrix[next_row][next_col] == visited:
                    break
                change_dir = 0
                row, col = next_row, next_col
                res.append(matrix[row][col])
                matrix[row][col] = visited

            cur_dir = (cur_dir + 1) % 4
            change_dir += 1

        return res
