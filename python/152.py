class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        cur_max = cur_min = result = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            cur_max, cur_min = max(n, cur_max * n, cur_min * n), min(n, cur_max * n, cur_min * n)
            result = max(result, cur_max)
        return result
