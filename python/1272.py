from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        res = []

        for start, end in intervals:
            if remove_end < start or end < remove_start:
                res.append([start, end])
            else:
                if start < remove_start:
                    res.append([start, remove_start])
                if remove_end < end:
                    res.append([remove_end, end])

        return res
