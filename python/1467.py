from itertools import product
from math import factorial, prod
from typing import List


# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661757/Python-10-Lines-90-Multionomial-coefficients-explained
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        box_sum = sum(balls) // 2
        res = 0

        arrays = [range(i + 1) for i in balls]
        t = list(product(*arrays))

        for i in range(len(t)):
            if sum(t[i]) == box_sum and t[i].count(0) == t[-i - 1].count(0):
                res += self.multinomial(t[i]) * self.multinomial(t[-i - 1])

        return res / self.multinomial(list(balls))

    def multinomial(self, n):
        return factorial(sum(n)) / prod([factorial(i) for i in n])
