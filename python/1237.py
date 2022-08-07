from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y) -> int:
        pass


# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/discuss/414249/JavaC%2B%2BPython-O(X%2BY)
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        y = 1000

        for x in range(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])

        return res
