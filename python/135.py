# https://leetcode.com/problems/candy/discuss/42881/Python-two-pass-solution-(left-to-right-then-right-to-left).
class Solution:
    def candy(self, ratings: list[int]) -> int:
        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)
