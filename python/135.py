from typing import List


# https://leetcode.com/problems/candy/discuss/42881/Python-two-pass-solution-(left-to-right-then-right-to-left).
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in reversed(range(1, n)):
            if ratings[i - 1] > ratings[i]:
                res[i - 1] = max(res[i - 1], res[i] + 1)

        return sum(res)
