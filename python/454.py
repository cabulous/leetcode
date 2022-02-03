from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.map = defaultdict(int)

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        return self.k_sum_count([nums1, nums2, nums3, nums4])

    def add_to_hash(self, lists, index, total):
        if index == len(lists) // 2:
            self.map[total] += 1
        else:
            for num in lists[index]:
                self.add_to_hash(lists, index + 1, total + num)

    def count_complements(self, lists, index, complement):
        if index == len(lists):
            return self.map[complement]

        res = 0
        for num in lists[index]:
            res += self.count_complements(lists, index + 1, complement - num)

        return res

    def k_sum_count(self, lists):
        self.add_to_hash(lists, 0, 0)
        return self.count_complements(lists, len(lists) // 2, 0)
