# https://leetcode.com/problems/minimum-costs-using-the-train-line/solutions/2604531/python3-5-line-dp-solution-time-o-n-extra-space-o-1-explanation/
class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        dpr = 0
        dpe = expressCost
        res = [0] * len(regular)

        for i in range(1, len(regular) + 1):
            dpr, dpe = min(dpr, dpe) + regular[i - 1], min(dpr + expressCost, dpe) + express[i - 1]
            res[i - 1] = min(dpr, dpe)

        return res
