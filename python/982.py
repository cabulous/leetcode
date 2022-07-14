from collections import defaultdict
from typing import List


# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/discuss/1257470/Python3-hash-table
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for x in nums:
            for y in nums:
                freq[x & y] += 1

        res = 0
        for x in nums:
            mask = x = x ^ 0xffff
            while x:
                res += freq[x]
                x = mask & (x - 1)
            res += freq[0]

        return res
