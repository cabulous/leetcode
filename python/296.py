from typing import List


# https://leetcode.com/problems/best-meeting-point/discuss/74193/Java-2msPython-40ms-two-pointers-solution-no-median-no-sort-with-explanation
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = list(map(sum, grid))
        cols = list(map(sum, zip(*grid)))
        return self.min_dist_1d(rows) + self.min_dist_1d(cols)

    def min_dist_1d(self, vec: List[int]) -> int:
        left = -1
        right = len(vec)
        dist = left_dist = right_dist = 0

        while left < right:
            if left_dist < right_dist:
                dist += left_dist
                left += 1
                left_dist += vec[left]
            else:
                dist += right_dist
                right -= 1
                right_dist += vec[right]

        return dist
