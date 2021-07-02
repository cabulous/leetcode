from typing import List


# https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]
        return res


# https://leetcode.com/problems/gray-code/discuss/245076/4-lines-Elegant-fast-and-easy-understand-Python-solution
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, 2 ** n):
            res.append(res[-1] ^ (i & -i))
        return res
