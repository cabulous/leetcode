from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            start = max(first_start, second_start)
            end = min(first_end, second_end)
            if start <= end:
                ans.append([start, end])
            if first_end < second_end:
                i += 1
            else:
                j += 1

        return ans
