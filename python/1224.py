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
            count[num] += 1

            c = count[num]
            if freq[c] * c == index and index < len(nums):
                res = index + 1

            delta = index - freq[c] * c
            if delta in [c + 1, 1] and freq[delta] == 1:
                res = index

        return res
