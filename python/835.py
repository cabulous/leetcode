from collections import Counter
from typing import List


class Solution:

    def __init__(self):
        self.dimension = 0

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        self.dimension = len(img1)

        max_overlaps = 0
        for y_shift in range(self.dimension):
            for x_shift in range(self.dimension):
                max_overlaps = max(max_overlaps, self.shift_and_count(x_shift, y_shift, img1, img2))
                max_overlaps = max(max_overlaps, self.shift_and_count(x_shift, y_shift, img2, img1))

        return max_overlaps

    def shift_and_count(self, x_shift, y_shift, matrix, reference):
        left_shift_count = 0
        right_shift_count = 0

        for r_row, m_row in enumerate(range(y_shift, self.dimension)):
            for r_col, m_col in enumerate(range(x_shift, self.dimension)):
                if matrix[m_row][m_col] == reference[r_row][r_col] == 1:
                    left_shift_count += 1
                if matrix[m_row][r_col] == reference[r_row][m_col] == 1:
                    right_shift_count += 1

        return max(left_shift_count, right_shift_count)


class Solution:

    def __init__(self):
        self.dimension = 0

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        self.dimension = len(img1)

        transformation_count = Counter()
        max_overlaps = 0

        img1_ones = self.non_zero_cells(img1)
        img2_ones = self.non_zero_cells(img2)

        for (x_img1, y_img1) in img1_ones:
            for (x_img2, y_img2) in img2_ones:
                vec = (x_img2 - x_img1, y_img2 - y_img1)
                transformation_count[vec] += 1
                max_overlaps = max(max_overlaps, transformation_count[vec])

        return max_overlaps

    def non_zero_cells(self, matrix):
        res = []
        for x in range(self.dimension):
            for y in range(self.dimension):
                if matrix[x][y] == 1:
                    res.append((x, y))
        return res
