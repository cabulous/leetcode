class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        res = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return res if res != float('inf') else 0
