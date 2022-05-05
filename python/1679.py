from typing import List
from collections import Counter


# https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/961406/JavaPython-3-Two-HashMapdictionary-O(n)-codes-w-analysis.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        count = Counter()
        res = 0

        for num in nums:
            if count[k - num] > 0:
                count[k - num] -= 1
                res += 1
            else:
                count[num] += 1

        return res
