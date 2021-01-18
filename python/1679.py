from typing import List
from collections import defaultdict


# https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/961406/JavaPython-3-Two-HashMapdictionary-O(n)-codes-w-analysis.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        res = 0
        d = defaultdict(int)
        for num in nums:
            if d[k - num] > 0:
                d[k - num] -= 1
                res += 1
            else:
                d[num] += 1
        return res
