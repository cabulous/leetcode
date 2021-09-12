from typing import List


# https://leetcode.com/problems/rectangle-area-ii/discuss/137914/JavaC%2B%2BPython-Discretization-and-O(NlogN)
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        xs = sorted(set([x for x1, _, x2, _ in rectangles for x in [x1, x2]]))
        x_i = {x: i for i, x in enumerate(xs)}
        count = [0] * len(x_i)

        lst = []
        for x1, y1, x2, y2 in rectangles:
            lst.append([y1, x1, x2, 1])
            lst.append([y2, x1, x2, -1])
        lst.sort()

        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sign in lst:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sign
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))

        return area % mod
