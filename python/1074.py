from typing import List
from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                ps[r][c] = ps[r - 1][c] + ps[r][c - 1] - ps[r - 1][c - 1] + matrix[r - 1][c - 1]

        res = 0
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                count = Counter()
                count[0] = 1
                for c in range(1, cols + 1):
                    curr = ps[r2][c] - ps[r1 - 1][c]
                    res += count[curr - target]
                    count[curr] += 1

        return res
