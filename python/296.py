from typing import List


# https://leetcode.com/problems/best-meeting-point/discuss/74193/Java-2msPython-40ms-two-pointers-solution-no-median-no-sort-with-explanation
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row_sum = list(map(sum, grid))
        col_sum = list(map(sum, zip(*grid)))
        return self.min_dist_1d(row_sum) + self.min_dist_1d(col_sum)

    def min_dist_1d(self, vec: List[int]) -> int:
        i, j = -1, len(vec)
        dist = left_dist = right_dist = 0

        while i < j:
            if left_dist < right_dist:
                dist += left_dist
                i += 1
                left_dist += vec[i]
            else:
                dist += right_dist
                j -= 1
                right_dist += vec[j]

        return dist
