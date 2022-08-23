from collections import Counter
from typing import List


# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C%2B%2BPython-Esay-Understand-Solution
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remain = Counter(nums)
        end = Counter()

        for num in nums:
            if remain[num] == 0:
                continue

            remain[num] -= 1

            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif remain[num + 1] > 0 and remain[num + 2] > 0:
                remain[num + 1] -= 1
                remain[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False

        return True
