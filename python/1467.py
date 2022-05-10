from itertools import product
from math import factorial, prod
from typing import List


# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661757/Python-10-Lines-90-Multionomial-coefficients-explained
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k = len(balls)
        n = sum(balls) // 2
        q = 0

        arrays = [range(0, i + 1) for i in balls]
        t = list(product(*arrays))

        for i in range(len(t)):
            if sum(t[i]) == n and t[i].count(0) == t[-i - 1].count(0):
                q += self.multinomial(t[i]) * self.multinomial(t[-i - 1])

        return q / self.multinomial(list(balls))

    def multinomial(self, n):
        return factorial(sum(n)) / prod([factorial(i) for i in n])
