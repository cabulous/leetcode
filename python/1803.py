from collections import Counter
from typing import List


# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/discuss/1120056/JavaC%2B%2BPython-O(n)-solution-beats-100
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        return self.test(nums, high + 1) - self.test(nums, low)

    def test(self, nums, x):
        count = Counter(nums)
        res = 0
        while x:
            if x & 1 != 0:
                res += sum(count[a] * count[(x - 1) ^ a] for a in count)
            count = Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
            x >>= 1
        return res // 2
