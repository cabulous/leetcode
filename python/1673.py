from typing import List


# https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/952786/JavaC%2B%2BPython-One-Pass-Stack-Solution
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + n - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
