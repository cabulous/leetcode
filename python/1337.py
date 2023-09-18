class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        res = [(sum(row), i) for i, row in enumerate(mat)]
        res.sort()
        return [i for __, i in res[:k]]
