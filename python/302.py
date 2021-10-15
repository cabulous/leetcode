from typing import List


# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/discuss/75130/Clear-binary-search-Python
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def first(lo, hi, check):
            while lo < hi:
                mi = lo + (hi - lo) // 2
                if check(mi):
                    hi = mi
                else:
                    lo = mi + 1
            return lo

        top = first(0, x, lambda x: '1' in image[x])
        bottom = first(x, len(image), lambda x: '1' not in image[x])
        left = first(0, y, lambda y: any(row[y] == '1' for row in image))
        right = first(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))

        return (bottom - top) * (right - left)
