import re
from collections import Counter
from typing import List


# https://leetcode.com/problems/basic-calculator-iv/discuss/113549/Easy-%3A-P
class CustomCounter(Counter):

    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.subtract(other)
        return self

    def __mul__(self, other):
        product = CustomCounter()
        for x in self:
            for y in other:
                xy = tuple(sorted(x + y))
                product[xy] += self[x] * other[y]
        return product


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        vals = dict(zip(evalvars, evalints))

        def f(s):
            s = str(vals.get(s, s))
            return CustomCounter({(s,): 1}) if s.isalpha() else CustomCounter({(): int(s)})

        c = eval(re.sub('(\w+)', r'f("\1")', expression))

        return [
            '*'.join((str(c[x]),) + x)
            for x in sorted(c, key=lambda x: (-len(x), x))
            if c[x]
        ]
