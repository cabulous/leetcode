from typing import List
from collections import Counter


# https://leetcode.com/problems/longest-harmonious-subsequence/discuss/103534/Python-Straightforward-with-Explanation
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max([count[x] + count[x + 1] for x in count if x + 1 in count] or [0])
