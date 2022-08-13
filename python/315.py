from typing import List


# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
class Solution:

    def __init__(self):
        self.res = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.res = [0] * len(nums)
        self.merge_sort(list(enumerate(nums)))
        return self.res

    def merge_sort(self, enum):
        half = len(enum) // 2
        if half == 0:
            return enum

        left = self.merge_sort(enum[:half])
        right = self.merge_sort(enum[half:])

        for i in range(len(enum) - 1, -1, -1):
            if not right or (left and left[-1][1] > right[-1][1]):
                self.res[left[-1][0]] += len(right)
                enum[i] = left.pop()
            else:
                enum[i] = right.pop()

        return enum
