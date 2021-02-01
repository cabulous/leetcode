import math
from typing import List


# https://leetcode.com/problems/squirrel-simulation/discuss/102819/Python-Straightforward-with-Explanation
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def distance(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])

        s = sum(2 * distance(tree, nut) for nut in nuts)
        return min(s + distance(squirrel, nut) - distance(nut, tree) for nut in nuts)
