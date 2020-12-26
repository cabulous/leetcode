import bisect


# generalization
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        def increasing_k_nums(k: int) -> bool:
            if k == 0:
                return True
            inc = [float('inf')] * (k - 1)
            for n in nums:
                i = bisect.bisect_left(inc, n)
                if i >= k - 1:
                    return True
                inc[i] = n
            return False

        return increasing_k_nums(3)


class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
