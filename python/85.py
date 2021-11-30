from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not any(matrix):
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols
        res = 0

        for i in range(rows):
            for j in range(cols):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, self.get_max_area(dp))

        return res

    def get_max_area(self, heights):
        stack = [-1]
        area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, w * h)
            stack.append(i)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1
            area = max(area, w * h)

        return area
