from typing import List


# https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/439986/Python-keep-track-of-the-right-most-2-points/886958
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        curr = []
        res = 0

        for start, end in intervals:
            if not curr or curr[1] < start:
                res += 2
                curr = [end - 1, end]
            elif curr[0] < start:
                res += 1
                curr = [curr[1], end]

        return res
