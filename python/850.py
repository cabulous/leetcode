from typing import List


# https://leetcode.com/problems/rectangle-area-ii/discuss/137914/JavaC%2B%2BPython-Discretization-and-O(NlogN)
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {x: i for i, x in enumerate(xs)}
        count = [0] * (len(x_i))
        l = []

        for x1, y1, x2, y2 in rectangles:
            l.append([y1, x1, x2, 1])
            l.append([y2, x1, x2, -1])

        l.sort()

        cur_y = cur_x_sum = area = 0

        for y, x1, x2, sig in l:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))

        return area % (10 ** 9 + 7)


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        n = len(rectangles)
        x_vals, y_vals = set(), set()
        for x1, y1, x2, y2 in rectangles:
            x_vals.add(x1)
            x_vals.add(x2)
            y_vals.add(y1)
            y_vals.add(y2)

        imapx = sorted(x_vals)
        imapy = sorted(y_vals)
        mapx = {x: i for i, x in enumerate(imapx)}
        mapy = {y: i for i, y in enumerate(imapy)}

        grid = [[0] * len(imapy) for _ in imapx]
        for x1, y1, x2, y2 in rectangles:
            for x in range(mapx[x1], mapx[x2]):
                for y in range(mapy[y1], mapy[y2]):
                    grid[x][y] = 1

        ans = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    ans += (imapx[x + 1] - imapx[x]) * (imapy[y + 1] - imapy[y])

        return ans % (10 ** 9 + 7)
