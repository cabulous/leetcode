from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, num in enumerate(arr):
            if num == i:
                return num
        return -1


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        res = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == mid:
                res = mid
                right = mid - 1
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return res
