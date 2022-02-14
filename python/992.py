from collections import Counter
from typing import List


# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most_k(nums, k) - self.at_most_k(nums, k - 1)

    def at_most_k(self, nums, quota):
        count = Counter()
        start = 0
        res = 0

        for end in range(len(nums)):
            if count[nums[end]] == 0:
                quota -= 1
            count[nums[end]] += 1
            while quota < 0:
                count[nums[start]] -= 1
                if count[nums[start]] == 0:
                    quota += 1
                start += 1
            res += end - start + 1

        return res
