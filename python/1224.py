from collections import Counter
from typing import List


# https://leetcode.com/problems/maximum-equal-frequency/discuss/403743/JavaC%2B%2BPython-Only-2-Cases%3A-Delete-it-or-not
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = Counter()
        freq = [0] * (len(nums) + 1)
        res = 0

        for index, num in enumerate(nums, 1):
            freq[count[num]] -= 1
            freq[count[num] + 1] += 1
            c = count[num] = count[num] + 1

            if freq[c] * c == index and index < len(nums):
                res = index + 1

            d = index - freq[c] * c
            if d in [c + 1, 1] and freq[d] == 1:
                res = index

        return res
