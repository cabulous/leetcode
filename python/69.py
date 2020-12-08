# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num < x:
                left = mid + 1
            elif num > x:
                right = mid - 1
            else:
                return mid

        return right


# Newton's Method
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)
