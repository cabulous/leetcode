# stack
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


# divide and conquer
class Solution:
    def calculate_area(self, heights, start, end):
        if start > end:
            return 0
        min_index = start
        for i in range(start, end + 1):
            if heights[min_index] > heights[i]:
                min_index = i
        return max(
            heights[min_index] * (end - start + 1),
            self.calculate_area(heights, start, min_index - 1),
            self.calculate_area(heights, min_index + 1, end)
        )

    def largestRectangleArea(self, heights: [int]) -> int:
        return self.calculate_area(heights, 0, len(heights) - 1)
