from collections import Counter
from typing import List


# https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            res += count[prefix_sum - k]
            count[prefix_sum] += 1

        return res
