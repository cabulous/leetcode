class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i >> 1] + i % 2)
        return res
