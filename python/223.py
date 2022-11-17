class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        box1 = (ax2 - ax1) * (ay2 - ay1)
        box2 = (bx2 - bx1) * (by2 - by1)
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        overlap_x = right - left

        top = min(ay2, by2)
        bottom = max(ay1, by1)
        overlap_y = top - bottom

        overlap = 0
        if overlap_x > 0 and overlap_y > 0:
            overlap = overlap_x * overlap_y

        return box1 + box2 - overlap
