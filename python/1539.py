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
        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
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
