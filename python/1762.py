from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_height = 0

        for i in reversed(range(len(heights))):
            if heights[i] > max_height:
                max_height = heights[i]
                ans.append(i)

        ans.reverse()
        return ans


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []

        for i in range(len(heights)):
            while ans and heights[ans[-1]] <= heights[i]:
                ans.pop()
            ans.append(i)

        return ans
