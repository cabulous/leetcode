#  Binary Search
class Solution:
    def findKthPositive(self, arr: [int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1
        return left + k


class Solution:
    def findKthPositive(self, arr: [int], k: int) -> int:
        n = len(arr)
        if n * k == 0:
            return 0

        i = 0
        while k > 0:
            i += 1
            if i not in arr:
                k -= 1

        return i
