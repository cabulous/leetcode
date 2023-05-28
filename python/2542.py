import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        n1_heap = []
        n1_sum = 0
        res = 0
        for n1, n2 in pairs:
            heapq.heappush(n1_heap, n1)
            n1_sum += n1
            if len(n1_heap) > k:
                n1_sum -= heapq.heappop(n1_heap)
            if len(n1_heap) == k:
                res = max(res, n1_sum * n2)

        return res
