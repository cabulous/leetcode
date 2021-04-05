from typing import List


# linear scan
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - x) for i, x in enumerate(A))


# Remember Minimum
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n = len(A)
        floor = n
        for i in range(n - 1, -1, -1):
            floor = min(floor, A[i])
            if i >= 2 and A[i - 2] > floor:
                return False
        return True
