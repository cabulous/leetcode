from collections import Counter
from functools import lru_cache
from typing import List

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/solutions/2995054/python-3-sliding-window/
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        freq = Counter(nums[:k])
        curr = 0
        for num, count in freq.items():
            curr = (curr + self.mod_pow(num, count)) % MOD

        res = curr

        for i in range(1, len(nums) - k + 1):
            left_num = nums[i - 1]
            right_num = nums[i + k - 1]
            if left_num == right_num:
                continue

            curr -= self.mod_pow(left_num, freq[left_num])
            if freq[left_num] > 1:
                curr += self.mod_pow(left_num, freq[left_num] - 1)

            if freq[right_num] > 0:
                curr -= self.mod_pow(right_num, freq[right_num])
            curr += self.mod_pow(right_num, freq[right_num] + 1)
            curr %= MOD

            res = max(res, curr)

            freq[left_num] -= 1
            if freq[left_num] == 0:
                del freq[left_num]
            freq[right_num] += 1

        return res

    @lru_cache(None)
    def mod_pow(self, a, b):
        return pow(a, b, MOD)
