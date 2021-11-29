from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            first_start, first_end = firstList[p1]
            second_start, second_end = secondList[p2]

            start = max(first_start, second_start)
            end = min(first_end, second_end)

            if start <= end:
                ans.append([start, end])

            if first_end < second_end:
                p1 += 1
            else:
                p2 += 1

        return ans
