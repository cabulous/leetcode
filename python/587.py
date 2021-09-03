from typing import List


# https://leetcode.com/problems/erect-the-fence/discuss/103306/C%2B%2B-and-Python-easy-wiki-solution
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted(trees, key=lambda t: (t[0], t[1]))

        if len(points) <= 1:
            return points

        lower = []
        for p in points:
            while len(lower) >= 2 and self.cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and self.cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        res = lower[:-1] + upper[:-1]
        res = set(tuple(x) for x in res)
        res = [list(x) for x in res]

        return res

    def cross(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
