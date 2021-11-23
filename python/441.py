class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2
            if coins == n:
                return mid
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
        return right


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)
