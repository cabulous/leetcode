import bisect


# generalization
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        k = 3

        if k == 0:
            return True

        inc = [float('inf')] * (k - 1)

        for n in nums:
            i = bisect.bisect_left(inc, n)
            if i >= k - 1:
                return True
            inc[i] = n
        return False

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
