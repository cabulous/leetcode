from typing import List


# https://leetcode.com/problems/rectangle-overlap/discuss/132340/C%2B%2BJavaPython-1-line-Solution-1D-to-2D
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 1left < 2right, 2left < 1right
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2
        return rec1_x1 < rec2_x2 and rec2_x1 < rec1_x2 and rec1_y1 < rec2_y2 and rec2_y1 < rec1_y2
