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


class Solution:
    def arrangeCoins(self, n: int) -> int:
        row_count = coin_count = cur_row_coin = 0

        while coin_count < n:
            cur_row_coin += 1
            coin_count += cur_row_coin
            row_count += 1

        return row_count if coin_count == n else row_count - 1
