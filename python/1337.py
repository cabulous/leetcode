from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []

        for col in range(len(mat[0])):
            for row in range(len(mat)):
                if len(res) == k:
                    return res
                if mat[row][col] == 0 and (col == 0 or mat[row][col - 1] == 1):
                    res.append(row)

        for row in range(len(mat)):
            if len(res) == k:
                return res
            if row not in res:
                res.append(row)

        return res


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = [(sum(row), i) for i, row in enumerate(mat)]
        res.sort()
        return [i for _, i in res[:k]]
