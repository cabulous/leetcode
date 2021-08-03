from typing import List


# https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space./172501
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = [[]]
        cur = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur

        return res
