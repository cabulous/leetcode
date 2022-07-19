from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for r in range(numRows):
            col_count = r + 1
            curr = [1] * col_count
            for c in range(1, col_count - 1):
                curr[c] = res[r - 1][c - 1] + res[r - 1][c]
            res.append(curr[:])

        return res
