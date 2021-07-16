from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, 4)

    def two_sum(self, nums, target):
        res = []
        seen = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in seen:
                    res.append([target - nums[i], nums[i]])
            seen.add(nums[i])
        return res

    def k_sum(self, nums, target, k):
        if len(nums) == 0 or target < nums[0] * k or target > nums[-1] * k:
            return []
        if k == 2:
            return self.two_sum(nums, target)
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for nums_set in self.k_sum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + nums_set)
        return res
