import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution:

    def __init__(self):
        self.nums = []

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        return self.select(0, len(nums) - 1, len(nums) - k)

    def partition(self, left, right, pivot):
        pivot_val = self.nums[pivot]
        self.nums[right], self.nums[pivot] = self.nums[pivot], self.nums[right]

        res = left

        for i in range(left, right):
            if self.nums[i] < pivot_val:
                self.nums[i], self.nums[res] = self.nums[res], self.nums[i]
                res += 1

        self.nums[right], self.nums[res] = self.nums[res], self.nums[right]

        return res

    def select(self, left, right, k_smallest):
        if left == right:
            return self.nums[left]

        pivot = random.randint(left, right)
        pivot = self.partition(left, right, pivot)

        if pivot == k_smallest:
            return self.nums[pivot]

        if pivot < k_smallest:
            return self.select(pivot + 1, right, k_smallest)

        return self.select(left, pivot - 1, k_smallest)
