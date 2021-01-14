from math import inf
from typing import List


# two pointer, indirectly
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = 0
        current = 0

        for right in range(n):
            current += nums[right]
            while current > total - x and left <= right:
                current -= nums[left]
                left += 1
            if current == total - x:
                maxi = max(maxi, right - left + 1)

        return n - maxi if maxi != -1 else -1


# two pointer, directly
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        current = sum(nums)
        n = len(nums)
        mini = inf
        left = 0

        for right in range(n):
            current -= nums[right]
            while current < x and left <= right:
                current += nums[left]
                left += 1
            if current == x:
                mini = min(mini, left + (n - right - 1))

        return mini if mini != inf else -1
