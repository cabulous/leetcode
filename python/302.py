from typing import List


# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/discuss/75130/Clear-binary-search-Python
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        top = self.first(0, x, lambda x: '1' in image[x])
        bottom = self.first(x, len(image), lambda x: '1' not in image[x])
        left = self.first(0, y, lambda y: any('1' in row[y] for row in image))
        right = self.first(y, len(image[0]), lambda y: all('1' not in row[y] for row in image))

        return (bottom - top) * (right - left)

    def first(self, lo, hi, check):
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
