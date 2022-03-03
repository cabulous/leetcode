from typing import List


# https://leetcode.com/problems/arithmetic-slices/discuss/90112/Python-DP-solution/94658
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = curr = 0

        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                curr += 1
                res += curr
            else:
                curr = 0

        return res
