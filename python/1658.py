class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        curr = sum(nums)
        left = 0
        res = float('inf')

        for right in range(len(nums)):
            curr -= nums[right]
            while curr < x and left <= right:
                curr += nums[left]
                left += 1
            if curr == x:
                res = min(res, len(nums) - (right - left + 1))

        return res if res != float('inf') else -1
