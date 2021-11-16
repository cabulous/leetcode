class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n

        while lo < hi:
            mi = lo + (hi - lo) // 2
            count = 0
            for i in range(1, m + 1):
                count += min(mi // i, n)
            if count >= k:
                hi = mi
            else:
                lo = mi + 1

        return lo
