from collections import defaultdict, Counter
from itertools import accumulate
from typing import List


# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/discuss/1507271/Pythoncpp-Explanation-with-pictures.-O(N)
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix_sum = list(accumulate(nums))
        nums_sum = sum(nums)

        pre_sum = defaultdict(int)
        suf_sum = Counter(prefix_sum)
        suf_sum[nums_sum] -= 1

        res = 0

        if nums_sum % 2 == 0:
            res = suf_sum[nums_sum // 2]

        for i in range(len(nums)):
            curr = 0
            if nums[i] != k:
                new_sum = nums_sum + k - nums[i]
                if new_sum % 2 == 0:
                    if i > 0:
                        curr += pre_sum[new_sum // 2]
                    if i < len(nums) - 1:
                        curr += suf_sum[new_sum // 2 + nums[i] - k]
            res = max(res, curr)
            pre_sum[prefix_sum[i]] += 1
            suf_sum[prefix_sum[i]] -= 1

        return res
