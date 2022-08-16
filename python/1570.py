from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.non_zeros[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, num in self.non_zeros.items():
            if i in vec.non_zeros:
                res += num * vec.non_zeros[i]
        return res
