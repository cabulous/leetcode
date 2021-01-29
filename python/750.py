from typing import List


# https://leetcode.com/problems/number-of-corner-rectangles/discuss/110205/Python-Two-approaches:-one-using-set-with-fast-(~300ms)-run-time-another-has-O(m2*n)-time-but-only-use-O(1)-additional-space/111902
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ans = 0
        prevs = []
        for row in grid:
            ones = {idx for idx, val in enumerate(row) if val}
            for prev in prevs:
                matches = len(ones & prev)
                ans += matches * (matches - 1) // 2
            prevs.append(ones)
        return ans
