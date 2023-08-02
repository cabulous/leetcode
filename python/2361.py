# https://leetcode.com/problems/minimum-costs-using-the-train-line/solutions/2604531/python3-5-line-dp-solution-time-o-n-extra-space-o-1-explanation/
class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        dpr = 0
        dpe = expressCost
        res = []

        for i in range(len(regular)):
            dpr, dpe = min(dpr, dpe) + regular[i], min(dpr + expressCost, dpe) + express[i]
            res.append(min(dpr, dpe))

        return res
