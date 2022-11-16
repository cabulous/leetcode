def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n

        while lo <= hi:
            mi = lo + (hi - lo) // 2
            res = guess(mi)
            if res == 0:
                return mi
            if res < 0:
                hi = mi - 1
            else:
                lo = mi + 1

        return -1
