import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        min_heap = []
        curr_sum = 0
        res = 0
        for n1, n2 in pairs:
            heapq.heappush(min_heap, n1)
            curr_sum += n1
            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                res = max(res, curr_sum * n2)

        return res
