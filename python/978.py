from typing import List
from functools import lru_cache


# https://leetcode.com/problems/longest-turbulent-subarray/discuss/222146/PythonJavaC%2B%2B-O(n)-time-O(1)-space-Simple-and-Clean-solution
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = cur = 0

        for i in range(len(arr)):
            if i >= 2 and (arr[i - 2] < arr[i - 1] > arr[i] or arr[i - 2] > arr[i - 1] < arr[i]):
                cur += 1
            elif i >= 1 and arr[i - 1] != arr[i]:
                cur = 2
            else:
                cur = 1
            best = max(best, cur)

        return best


# https://leetcode.com/problems/longest-turbulent-subarray/discuss/1464554/Python-4-lines-dp-explained
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i, dr):
            if i == 0 or (arr[i] - arr[i - 1]) * dr >= 0:
                return 1
            return dp(i - 1, -dr) + 1

        return max(dp(i, dr) for i in range(len(arr)) for dr in [-1, 1])
