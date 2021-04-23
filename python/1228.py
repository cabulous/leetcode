from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        lo, hi = 0, n
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if arr[mi] == arr[0] + diff * mi:
                lo = mi + 1
            else:
                hi = mi
        return arr[0] + lo * diff
