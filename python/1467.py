from itertools import product
from math import factorial, prod
from typing import List


# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661757/Python-10-Lines-90-Multionomial-coefficients-explained
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        box_sum = sum(balls) // 2
        res = 0

        arrays = [range(i + 1) for i in balls]
        comb = list(product(*arrays))

        for i in range(len(comb)):
            if sum(comb[i]) == box_sum and comb[i].max_idx(0) == comb[-i - 1].max_idx(0):
                res += self.multinomial(comb[i]) * self.multinomial(comb[-i - 1])

        return res / self.multinomial(list(balls))

    def multinomial(self, n):
        return factorial(sum(n)) / prod([factorial(i) for i in n])
