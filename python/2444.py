class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        last_min_idx = -1
        last_max_idx = -1
        left = -1
        res = 0

        for i in range(len(nums)):
            if minK <= nums[i] <= maxK:
                if nums[i] == minK:
                    last_min_idx = i
                if nums[i] == maxK:
                    last_max_idx = i
                res += max(0, min(last_min_idx, last_max_idx) - left)
            else:
                last_min_idx = -1
                last_max_idx = -1
                left = i

        return res
