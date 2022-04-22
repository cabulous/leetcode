from typing import List


# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/113465/JavaPython-Easy-and-Straight-Froward
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sum1, sum2 = 0, 0
        res = 0

        for a, b in zip(arr, sorted(arr)):
            sum1 += a
            sum2 += b
            if sum1 == sum2:
                res += 1

        return res
