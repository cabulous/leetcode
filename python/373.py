import heapq


# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/solutions/84550/slow-1-liner-to-fast-solutions/
class Solution:

    def __init__(self):
        self.nums1 = []
        self.nums2 = []
        self.queue = []

    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        self.nums1 = nums1
        self.nums2 = nums2

        self.push(0, 0)
        res = []

        while self.queue and len(res) < k:
            __, i, j = heapq.heappop(self.queue)
            res.append([nums1[i], nums2[j]])
            self.push(i, j + 1)
            if j == 0:
                self.push(i + 1, 0)

        return res

    def push(self, i, j):
        if i < len(self.nums1) and j < len(self.nums2):
            heapq.heappush(self.queue, (self.nums1[i] + self.nums2[j], i, j))
