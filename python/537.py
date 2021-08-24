import re


# https://leetcode.com/problems/complex-number-multiplication/discuss/100493/2-lines-Python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, ai, b, bi = map(int, re.findall(r'-?\d+', num1 + num2))
        return '%d+%di' % (a * b - ai * bi, a * bi + ai * b)
