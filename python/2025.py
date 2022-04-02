from collections import defaultdict, Counter
from itertools import accumulate
from typing import List


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        nums_sum = sum(nums)
        pre_sum = defaultdict(int)
        suf_sum = Counter(pre_sum)
        suf_sum[nums_sum] -= 1

        res = 0

        if nums_sum % 2 == 0:
            res = suf_sum[nums_sum // 2]

        prefix_sum = list(accumulate(nums))

        for i in range(len(nums)):
            curr = 0
            if nums[i] != k:
                new_sum = nums_sum + k - nums[i]
                if new_sum % 2 == 0:
                    if i > 0:
                        curr += prefix_sum[new_sum // 2]
                    if i < len(nums) - 1:
                        curr += suf_sum[new_sum // 2 + nums[i] - k]
            res = max(res, curr)
            suf_sum[prefix_sum[i]] -= 1
            pre_sum[prefix_sum[i]] += 1

        return res
